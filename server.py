"""
FasalMitra AI - FastAPI Backend Server for Agricultural Vision
Serves real-time YOLO11s pest detection, crop intelligence, and static assets.
"""
import os
import io
import base64
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, FileResponse
from PIL import Image

from config import SAMPLES_DIR, SUPPORTED_CROPS, DEFAULT_CONF_THRESHOLD, DEFAULT_IOU_THRESHOLD
from core.detector import get_detector
from core.preprocessing import load_and_preprocess_image
from core.postprocessing import (
    draw_annotated_image, calculate_infestation_severity, convert_image_to_bytes
)
from utils.crop_data import PEST_INTELLIGENCE, get_pest_details

app = FastAPI(
    title="FasalMitra AI API",
    description="Intelligent Agricultural Pest Detection & Crop Protection API",
    version="2.0.0"
)

# Enable CORS for frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize detector
detector = get_detector()


@app.get("/api/health")
def health_check():
    """Returns system operational status and model readiness."""
    return {
        "status": "ready" if detector.is_ready else "error",
        "model": "YOLO11s",
        "dataset": "IP102 (102 Classes)",
        "classes_count": detector.num_classes,
        "device": detector.device
    }


@app.get("/api/crops")
def get_crops():
    """Returns the list of 8 primary crops and their mapped pests."""
    return {
        "crops": [
            {
                "name": name,
                "scientific_name": data["scientific_name"],
                "icon": data["icon"],
                "description": data["description"],
                "pests_count": len(data["pests"]),
                "pests": data["pests"]
            }
            for name, data in SUPPORTED_CROPS.items()
        ]
    }


@app.get("/api/pests")
def get_pests(query: Optional[str] = None, crop: Optional[str] = None):
    """Returns the verified agronomic pest library with filter support."""
    results = []
    for pest_key, info in PEST_INTELLIGENCE.items():
        # Filter by search query
        if query:
            q = query.lower()
            if not (
                q in pest_key.lower() or 
                q in info.get("common_name", "").lower() or 
                q in info.get("hindi_name", "").lower() or 
                q in info.get("how_to_spot", "").lower()
            ):
                continue

        # Filter by crop
        if crop and crop != "All Crops":
            if crop not in info.get("crops", []):
                continue

        results.append({
            "key": pest_key,
            "common_name": info.get("common_name", pest_key.title()),
            "hindi_name": info.get("hindi_name", ""),
            "scientific_name": info.get("scientific_name", ""),
            "crops": info.get("crops", []),
            "how_to_spot": info.get("how_to_spot", ""),
            "damage_risk": info.get("damage_risk", ""),
            "prevention_organic": info.get("prevention_organic", ""),
            "natural_predators": info.get("natural_predators", ""),
            "recommended_treatment": info.get("recommended_treatment", "")
        })

    return {"pests": results, "total": len(results)}


@app.get("/api/samples")
def get_samples():
    """Returns curated agricultural test images with preview base64."""
    samples = []
    if SAMPLES_DIR.exists():
        for f in os.listdir(SAMPLES_DIR):
            if f.lower().endswith((".jpg", ".jpeg", ".png")):
                f_path = SAMPLES_DIR / f
                try:
                    with open(f_path, "rb") as img_f:
                        b64_data = base64.b64encode(img_f.read()).decode("utf-8")
                        samples.append({
                            "filename": f,
                            "title": f.replace("_", " ").replace(".jpg", "").title(),
                            "preview_url": f"data:image/jpeg;base64,{b64_data}"
                        })
                except Exception:
                    pass
    return {"samples": samples}


@app.post("/api/detect")
async def detect_pest(
    file: Optional[UploadFile] = File(None),
    image_base64: Optional[str] = Form(None),
    crop: str = Form("General Field Crop"),
    conf: float = Form(DEFAULT_CONF_THRESHOLD)
):
    """
    Executes real-time YOLO11s pest detection.
    Accepts either a multipart file upload or a base64 encoded image string (from camera).
    """
    if not detector.is_ready:
        raise HTTPException(status_code=500, detail="AI Vision model is not initialized.")

    image_bytes = None

    if file is not None:
        image_bytes = await file.read()
    elif image_base64:
        # Strip header if present e.g. "data:image/jpeg;base64,..."
        if "," in image_base64:
            image_base64 = image_base64.split(",")[1]
        try:
            image_bytes = base64.b64decode(image_base64)
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Invalid base64 image data: {str(e)}")
    else:
        raise HTTPException(status_code=400, detail="No image provided. Upload a file or capture via camera.")

    # Preprocess image
    pil_image, err = load_and_preprocess_image(image_bytes)
    if err or pil_image is None:
        raise HTTPException(status_code=400, detail=err or "Failed to decode image.")

    # Run real YOLO inference
    detection_res = detector.predict(
        image=pil_image,
        conf_threshold=conf,
        iou_threshold=DEFAULT_IOU_THRESHOLD
    )

    if not detection_res.get("success"):
        raise HTTPException(status_code=500, detail=detection_res.get("error", "Inference failed."))

    # Generate annotated image with bounding boxes
    annotated_img = draw_annotated_image(pil_image, detection_res)

    # Encode images to base64
    annotated_bytes = convert_image_to_bytes(annotated_img, format="JPEG")
    orig_bytes = convert_image_to_bytes(pil_image, format="JPEG")

    annotated_b64 = "data:image/jpeg;base64," + base64.b64encode(annotated_bytes).decode("utf-8")
    original_b64 = "data:image/jpeg;base64," + base64.b64encode(orig_bytes).decode("utf-8")

    # Severity analysis
    num_detections = detection_res.get("num_detections", 0)
    max_conf = detection_res.get("max_confidence", 0.0)
    severity = calculate_infestation_severity(num_detections, max_conf)

    # Gather actionable remedies for all detected classes
    class_counts = detection_res.get("class_counts", {})
    remedies = {}
    for pest_name in class_counts.keys():
        details = get_pest_details(pest_name)
        remedies[pest_name] = {
            "common_name": details.get("common_name", pest_name.title()),
            "hindi_name": details.get("hindi_name", ""),
            "how_to_spot": details.get("how_to_spot", ""),
            "damage_risk": details.get("damage_risk", ""),
            "prevention_organic": details.get("prevention_organic", ""),
            "natural_predators": details.get("natural_predators", ""),
            "recommended_treatment": details.get("recommended_treatment", "")
        }

    return {
        "success": True,
        "num_detections": num_detections,
        "max_confidence_pct": round(max_conf * 100.0, 1),
        "inference_time_ms": detection_res.get("inference_time_ms", 0.0),
        "severity": severity,
        "boxes": detection_res.get("boxes", []),
        "class_counts": class_counts,
        "remedies": remedies,
        "crop_context": crop,
        "annotated_image": annotated_b64,
        "original_image": original_b64
    }


# Mount built React frontend if dist exists
dist_dir = Path(__file__).resolve().parent / "frontend" / "dist"
if dist_dir.exists():
    app.mount("/", StaticFiles(directory=str(dist_dir), html=True), name="frontend")


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 5000))
    uvicorn.run("server.py:app", host="0.0.0.0", port=port, reload=True)
