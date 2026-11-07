"""
FasalMitra AI - Detection Postprocessing & Visual Annotation Engine
"""
from typing import Dict, Any, List, Tuple
from PIL import Image, ImageDraw, ImageFont
import io
import json

from config import COLORS

def get_class_color(class_id: int) -> str:
    """Returns a deterministic high-contrast hex color for each class."""
    colors = COLORS["box_colors"]
    return colors[class_id % len(colors)]


def hex_to_rgb(hex_code: str) -> Tuple[int, int, int]:
    """Converts hex color string to RGB tuple."""
    hex_code = hex_code.lstrip("#")
    return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))


def draw_annotated_image(
    image: Image.Image,
    detections: Dict[str, Any],
    box_width: int = 3,
    show_labels: bool = True,
    show_conf: bool = True
) -> Image.Image:
    """
    Renders clean, high-contrast bounding boxes and farmer-friendly label tags.
    Presents clean pill badges with common names and certainty percentages.
    """
    annotated = image.copy()
    boxes = detections.get("boxes", [])
    if not boxes:
        return annotated

    draw = ImageDraw.Draw(annotated)
    w, h = image.size

    # Dynamic line width based on image resolution
    dynamic_line_width = max(3, int(min(w, h) / 220))
    line_w = max(box_width, dynamic_line_width)

    # Dynamic font sizing
    font_size = max(14, int(min(w, h) / 34))
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except Exception:
        try:
            font = ImageFont.truetype("DejaVuSans.ttf", font_size)
        except Exception:
            font = ImageFont.load_default()

    for box in boxes:
        cls_id = box["class_id"]
        cls_name = box["class_name"].title()
        conf_pct = box["confidence_pct"]
        coords = box["xyxy"]  # [x1, y1, x2, y2]
        
        hex_color = get_class_color(cls_id)
        rgb_color = hex_to_rgb(hex_color)

        x1, y1, x2, y2 = coords
        # Draw bounding rectangle
        draw.rectangle([x1, y1, x2, y2], outline=rgb_color, width=line_w)

        if show_labels:
            label_text = f"{cls_name}"
            if show_conf:
                label_text += f" ({conf_pct:.0f}%)"

            # Compute label box dimensions
            try:
                bbox_text = draw.textbbox((0, 0), label_text, font=font)
                text_w = bbox_text[2] - bbox_text[0]
                text_h = bbox_text[3] - bbox_text[1]
            except Exception:
                text_w = len(label_text) * (font_size * 0.6)
                text_h = font_size * 1.2

            padding = 6
            # Position pill above box, or inside if near image top boundary
            if y1 - text_h - padding * 2 >= 0:
                badge_y1 = y1 - text_h - padding * 2
                badge_y2 = y1
            else:
                badge_y1 = y1
                badge_y2 = y1 + text_h + padding * 2

            badge_x1 = max(0, x1)
            badge_x2 = min(w, x1 + text_w + padding * 2)

            # Draw solid background pill
            draw.rectangle([badge_x1, badge_y1, badge_x2, badge_y2], fill=rgb_color)
            
            # Text contrast: white on dark colors, dark on light colors
            luminance = (0.299 * rgb_color[0] + 0.587 * rgb_color[1] + 0.114 * rgb_color[2]) / 255.0
            text_color = (17, 42, 26) if luminance > 0.65 else (255, 255, 255)

            draw.text((badge_x1 + padding, badge_y1 + padding / 2), label_text, fill=text_color, font=font)

    return annotated


def calculate_infestation_severity(num_detections: int, max_confidence: float) -> Dict[str, Any]:
    """
    Computes a farmer-friendly infestation status and recommendation badge.
    """
    if num_detections == 0:
        return {
            "level": "Healthy / No Pests Detected",
            "color": COLORS["alert_emerald"],
            "badge": "Crop Clear",
            "css_class": "badge-healthy",
            "description": "Your crop foliage appears healthy and free of common recognized pests."
        }
    elif num_detections == 1:
        return {
            "level": "Mild / Isolated Pest",
            "color": "#0284C7",
            "badge": "Single Pest",
            "css_class": "badge-warning",
            "description": "An isolated pest was spotted. Check nearby plants to stop early spread."
        }
    elif 2 <= num_detections <= 4:
        return {
            "level": "Moderate Attention Needed",
            "color": COLORS["alert_amber"],
            "badge": "Moderate Spread",
            "css_class": "badge-warning",
            "description": "Multiple pests detected on this plant. Organic or cultural treatment recommended."
        }
    else:
        return {
            "level": "Action Recommended (High Pest Count)",
            "color": COLORS["alert_crimson"],
            "badge": "High Infestation",
            "css_class": "badge-severe",
            "description": "High number of pests found. Timely crop protection advised to avoid yield loss."
        }


def convert_image_to_bytes(img: Image.Image, format: str = "JPEG", quality: int = 95) -> bytes:
    """Encodes PIL Image to byte buffer for download."""
    buf = io.BytesIO()
    if format.upper() == "JPEG" and img.mode != "RGB":
        img = img.convert("RGB")
    img.save(buf, format=format, quality=quality)
    return buf.getvalue()


def build_detection_report(
    detections: Dict[str, Any],
    crop_context: str = "General Crop",
    notes: str = ""
) -> str:
    """Builds a structured diagnostic summary for recordkeeping."""
    severity = calculate_infestation_severity(
        detections.get("num_detections", 0),
        detections.get("max_confidence", 0.0)
    )
    
    report = {
        "platform": "FasalMitra AI",
        "crop": crop_context,
        "total_pests_found": detections.get("num_detections", 0),
        "diagnosis": severity["level"],
        "class_breakdown": detections.get("class_counts", {}),
        "pests_detected": [
            {
                "pest_name": b["class_name"].title(),
                "class_name": b["class_name"],
                "certainty": f"{b['confidence_pct']}%"
            }
            for b in detections.get("boxes", [])
        ],
        "advice_summary": severity["description"],
        "field_notes": notes
    }
    return json.dumps(report, indent=2)
