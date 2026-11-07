"""
FasalMitra AI - Pipeline & Agronomic Intelligence Tests
"""
import unittest
from PIL import Image
import numpy as np

from config import SUPPORTED_CROPS
from core.detector import get_detector
from core.preprocessing import load_and_preprocess_image, validate_image_file
from core.postprocessing import (
    draw_annotated_image, calculate_infestation_severity,
    convert_image_to_bytes, build_detection_report
)
from utils.crop_data import get_pest_details, get_crop_pests

class TestPipeline(unittest.TestCase):
    
    def test_01_preprocessing_conversions(self):
        """Test mode conversion (RGBA -> RGB), dimensions, array loading."""
        rgba_img = Image.new("RGBA", (200, 200), (34, 139, 34, 255))
        processed, err = load_and_preprocess_image(rgba_img)
        self.assertIsNone(err)
        self.assertEqual(processed.mode, "RGB")
        self.assertEqual(processed.size, (200, 200))

        # Test numpy array loading
        arr = np.zeros((150, 150, 3), dtype=np.uint8)
        processed_arr, err2 = load_and_preprocess_image(arr)
        self.assertIsNone(err2)
        self.assertEqual(processed_arr.mode, "RGB")

    def test_02_crop_mappings_consistency(self):
        """Verify that all mapped crop pests correspond strictly to verified 102 model classes."""
        detector = get_detector()
        model_classes = set(detector.get_supported_classes())

        for crop, data in SUPPORTED_CROPS.items():
            for p in data["pests"]:
                self.assertIn(
                    p, model_classes, 
                    f"Crop '{crop}' maps pest '{p}' which is not in the model's 102 verified classes!"
                )

    def test_03_agronomic_knowledge_base(self):
        """Verify that pest profiles contain complete IPM guidance."""
        sample_pests = ["rice leaf roller", "brown plant hopper", "aphids", "Dacus dorsalis(Hendel)"]
        for sp in sample_pests:
            details = get_pest_details(sp)
            self.assertIn("scientific_name", details)
            self.assertIn("symptoms", details)
            self.assertIn("ipm", details)
            self.assertIn("cultural", details["ipm"])
            self.assertIn("biological", details["ipm"])
            self.assertIn("chemical", details["ipm"])

    def test_04_postprocessing_drawing(self):
        """Verify annotated image rendering and report generation."""
        img = Image.new("RGB", (300, 300), (255, 255, 255))
        mock_detections = {
            "num_detections": 1,
            "max_confidence": 0.85,
            "inference_time_ms": 120.5,
            "conf_threshold_used": 0.25,
            "boxes": [
                {
                    "box_id": 1,
                    "class_id": 0,
                    "class_name": "rice leaf roller",
                    "confidence": 0.85,
                    "confidence_pct": 85.0,
                    "xyxy": [50, 50, 200, 200],
                    "width_px": 150,
                    "height_px": 150
                }
            ],
            "class_counts": {"rice leaf roller": 1}
        }

        annotated = draw_annotated_image(img, mock_detections)
        self.assertEqual(annotated.size, (300, 300))

        # Check export
        b_bytes = convert_image_to_bytes(annotated)
        self.assertGreater(len(b_bytes), 0)

        # Check report
        report_str = build_detection_report(mock_detections, crop_context="Rice")
        self.assertIn("rice leaf roller", report_str)
        self.assertIn("FasalMitra AI", report_str)

if __name__ == "__main__":
    unittest.main()
