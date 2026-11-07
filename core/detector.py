"""
FasalMitra AI - Pretrained YOLO11s Pest Detection Engine
"""
import time
import torch
from pathlib import Path
from typing import Dict, Any, List, Optional
from PIL import Image
from ultralytics import YOLO
import yaml

from config import MODEL_PATH, YAML_PATH, DEFAULT_CONF_THRESHOLD, DEFAULT_IOU_THRESHOLD, INFERENCE_IMAGE_SIZE


class PestDetector:
    """
    Inference wrapper for the verified YOLO11s IP102 pest detection model.
    """
    def __init__(self, model_path: Path = MODEL_PATH, yaml_path: Path = YAML_PATH):
        self.model_path = Path(model_path)
        self.yaml_path = Path(yaml_path)
        self.model: Optional[YOLO] = None
        self.device: str = "cuda" if torch.cuda.is_available() else "cpu"
        self.class_names: Dict[int, str] = {}
        self.num_classes: int = 0
        self._load_error: Optional[str] = None
        
        self._initialize()

    def _initialize(self):
        """Loads model weights and extracts class mapping."""
        if not self.model_path.exists():
            self._load_error = f"Model checkpoint not found at: {self.model_path}"
            return

        try:
            # Load Ultralytics model
            self.model = YOLO(str(self.model_path))
            # Model class names dictionary {0: 'name', ...}
            if hasattr(self.model, "names") and isinstance(self.model.names, dict):
                self.class_names = self.model.names
            elif self.yaml_path.exists():
                with open(self.yaml_path, "r", encoding="utf-8") as f:
                    yaml_data = yaml.safe_load(f)
                    names_list = yaml_data.get("names", [])
                    self.class_names = {i: name for i, name in enumerate(names_list)}

            self.num_classes = len(self.class_names)
            # Warm up model on selected device
            self._warmup()
        except Exception as e:
            self._load_error = f"Error loading YOLO model checkpoint: {str(e)}"
            self.model = None

    def _warmup(self):
        """Warm up model to initialize PyTorch graphs and memory buffers."""
        if self.model is not None:
            try:
                import numpy as np
                dummy = np.zeros((INFERENCE_IMAGE_SIZE, INFERENCE_IMAGE_SIZE, 3), dtype=np.uint8)
                self.model.predict(dummy, device=self.device, verbose=False, imgsz=INFERENCE_IMAGE_SIZE)
            except Exception:
                pass

    @property
    def is_ready(self) -> bool:
        return self.model is not None and self._load_error is None

    @property
    def load_error(self) -> Optional[str]:
        return self._load_error

    def get_supported_classes(self) -> List[str]:
        """Returns the list of 102 verified pest classes."""
        return [self.class_names[i] for i in sorted(self.class_names.keys())]

    def predict(
        self,
        image: Image.Image,
        conf_threshold: float = DEFAULT_CONF_THRESHOLD,
        iou_threshold: float = DEFAULT_IOU_THRESHOLD,
        imgsz: int = INFERENCE_IMAGE_SIZE
    ) -> Dict[str, Any]:
        """
        Executes pest detection inference on a preprocessed PIL Image.
        Returns detailed bounding boxes, confidence values, class counts, and latency.
        """
        if not self.is_ready:
            return {
                "success": False,
                "error": self._load_error or "Model is not initialized.",
                "num_detections": 0,
                "boxes": [],
                "class_counts": {},
                "inference_time_ms": 0.0
            }

        try:
            start_time = time.perf_counter()
            
            # Run YOLO prediction
            results = self.model.predict(
                source=image,
                conf=conf_threshold,
                iou=iou_threshold,
                imgsz=imgsz,
                device=self.device,
                verbose=False
            )
            
            inference_time_ms = (time.perf_counter() - start_time) * 1000.0
            
            res = results[0]
            boxes_data: List[Dict[str, Any]] = []
            class_counts: Dict[str, int] = {}
            confidences: List[float] = []

            orig_w, orig_h = image.size

            if res.boxes is not None and len(res.boxes) > 0:
                xyxy = res.boxes.xyxy.cpu().numpy()
                confs = res.boxes.conf.cpu().numpy()
                classes = res.boxes.cls.cpu().numpy()

                for i in range(len(confs)):
                    cls_id = int(classes[i])
                    cls_name = self.class_names.get(cls_id, f"Class_{cls_id}")
                    conf = float(confs[i])
                    box = [float(coord) for coord in xyxy[i]]

                    # Normalized box coordinates [x1_norm, y1_norm, x2_norm, y2_norm]
                    box_norm = [
                        max(0.0, box[0] / orig_w),
                        max(0.0, box[1] / orig_h),
                        min(1.0, box[2] / orig_w),
                        min(1.0, box[3] / orig_h)
                    ]

                    boxes_data.append({
                        "box_id": i + 1,
                        "class_id": cls_id,
                        "class_name": cls_name,
                        "confidence": conf,
                        "confidence_pct": round(conf * 100.0, 1),
                        "xyxy": [round(c, 1) for c in box],
                        "xyxy_norm": [round(c, 4) for c in box_norm],
                        "width_px": round(box[2] - box[0], 1),
                        "height_px": round(box[3] - box[1], 1)
                    })

                    class_counts[cls_name] = class_counts.get(cls_name, 0) + 1
                    confidences.append(conf)

            # Sort boxes by confidence descending
            boxes_data.sort(key=lambda x: x["confidence"], reverse=True)

            avg_conf = (sum(confidences) / len(confidences)) if confidences else 0.0
            max_conf = max(confidences) if confidences else 0.0

            return {
                "success": True,
                "error": None,
                "num_detections": len(boxes_data),
                "boxes": boxes_data,
                "class_counts": class_counts,
                "confidences": confidences,
                "avg_confidence": avg_conf,
                "max_confidence": max_conf,
                "inference_time_ms": round(inference_time_ms, 1),
                "device": self.device,
                "image_size": (orig_w, orig_h),
                "conf_threshold_used": conf_threshold,
                "iou_threshold_used": iou_threshold
            }

        except Exception as e:
            return {
                "success": False,
                "error": f"Inference execution failed: {str(e)}",
                "num_detections": 0,
                "boxes": [],
                "class_counts": {},
                "inference_time_ms": 0.0
            }


# Singleton pattern for fast application reuse
_detector_instance: Optional[PestDetector] = None

def get_detector() -> PestDetector:
    """Returns or instantiates the global PestDetector singleton."""
    global _detector_instance
    if _detector_instance is None:
        _detector_instance = PestDetector()
    return _detector_instance
