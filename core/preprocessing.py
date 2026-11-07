"""
FasalMitra AI - Image Preprocessing and Validation Pipeline
"""
from typing import Tuple, Optional, Union
from PIL import Image, ImageOps
import numpy as np
import io

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "webp", "bmp"}
MAX_FILE_SIZE_BYTES = 25 * 1024 * 1024  # 25 MB max
MIN_DIMENSION = 32
MAX_DIMENSION = 8192

def validate_image_file(file_obj) -> Tuple[bool, str]:
    """
    Validates uploaded file against allowed formats and size limits.
    """
    if file_obj is None:
        return False, "No file uploaded."
    
    # Check size
    if hasattr(file_obj, "size") and file_obj.size > MAX_FILE_SIZE_BYTES:
        return False, f"File exceeds maximum allowed size of {MAX_FILE_SIZE_BYTES / (1024*1024):.0f}MB."
    
    # Check filename extension if available
    if hasattr(file_obj, "name") and file_obj.name:
        ext = file_obj.name.split(".")[-1].lower()
        if ext not in ALLOWED_EXTENSIONS:
            return False, f"Unsupported file type (.{ext}). Allowed: {', '.join(ALLOWED_EXTENSIONS)}."

    return True, "Valid file."


def load_and_preprocess_image(
    source: Union[bytes, io.BytesIO, Image.Image, np.ndarray, str]
) -> Tuple[Optional[Image.Image], Optional[str]]:
    """
    Loads and preprocesses an image into a standard RGB PIL Image.
    Handles EXIF orientation, mode conversion, and dimension sanity checks.
    """
    try:
        if isinstance(source, Image.Image):
            pil_img = source
        elif isinstance(source, (bytes, bytearray)):
            pil_img = Image.open(io.BytesIO(source))
        elif isinstance(source, io.BytesIO):
            source.seek(0)
            pil_img = Image.open(source)
        elif isinstance(source, np.ndarray):
            pil_img = Image.fromarray(source)
        elif isinstance(source, str):
            pil_img = Image.open(source)
        else:
            return None, f"Unsupported image source type: {type(source)}"

        # Correct EXIF rotation (smartphones often store portrait photos rotated)
        try:
            pil_img = ImageOps.exif_transpose(pil_img)
        except Exception:
            pass  # Fall back to unrotated if EXIF is malformed

        # Convert to RGB (handles RGBA, P, L, CMYK)
        if pil_img.mode != "RGB":
            pil_img = pil_img.convert("RGB")

        # Sanity check dimensions
        w, h = pil_img.size
        if w < MIN_DIMENSION or h < MIN_DIMENSION:
            return None, f"Image dimensions too small ({w}x{h}). Minimum {MIN_DIMENSION}x{MIN_DIMENSION} required."
        if w > MAX_DIMENSION or h > MAX_DIMENSION:
            # Rescale proportionally to prevent memory exhaustion
            pil_img.thumbnail((MAX_DIMENSION, MAX_DIMENSION), Image.Resampling.LANCZOS)

        return pil_img, None

    except Exception as e:
        return None, f"Failed to decode image: {str(e)}"
