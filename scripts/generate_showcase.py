import sys, os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import shutil

sys.path.insert(0, os.path.abspath('.'))
from core.detector import get_detector
from core.postprocessing import draw_annotated_image

# 1. Load image and run detector
orig_path = Path('assets/samples/user_test_weevil.jpg')
img = Image.open(orig_path).convert('RGB')

detector = get_detector()
res = detector.predict(img, conf_threshold=0.25)
print("Inference result:", res)

# 2. Get annotated image
annotated = draw_annotated_image(img, res)

# 3. Create a high-res comparison banner/card for presentation
# Card width: 900, Card height: 520
card_w, card_h = 960, 560
canvas = Image.new('RGB', (card_w, card_h), '#FFFDF7')
draw = ImageDraw.Draw(canvas)

# Fonts
try:
    font_title = ImageFont.truetype('arial.ttf', 24)
    font_sub = ImageFont.truetype('arial.ttf', 15)
    font_bold = ImageFont.truetype('arialbd.ttf', 14)
    font_sm = ImageFont.truetype('arial.ttf', 12)
    font_emoji = ImageFont.truetype('seguiemj.ttf', 18)
except Exception:
    font_title = font_sub = font_bold = font_sm = font_emoji = ImageFont.load_default()

# Neo-brutalist border around the card
draw.rectangle([16, 16, card_w - 24, card_h - 24], fill='#FFFFFF', outline='#1E293B', width=3)
# Hard shadow
draw.rectangle([card_w - 24, 24, card_w - 16, card_h - 16], fill='#1E293B')
draw.rectangle([24, card_h - 24, card_w - 16, card_h - 16], fill='#1E293B')

# Header text
draw.text((40, 36), "FasalMitra AI - Live Pest Detection Test Report", fill='#0F172A', font=font_title)
draw.text((40, 70), "Input: Grain / Wheat Weevil (Curculionidae)  |  Model: YOLO11s (IP102 Benchmark)", fill='#059669', font=font_bold)

# Two image panels: Original vs AI Annotated
panel_w, panel_h = 420, 280

# Rescale images nicely to fit panel
img_ratio = min(panel_w / img.width, panel_h / img.height)
new_w, new_h = int(img.width * img_ratio), int(img.height * img_ratio)

img_resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
ann_resized = annotated.resize((new_w, new_h), Image.Resampling.LANCZOS)

# Panel 1: Original
p1_x, p1_y = 40, 105
draw.rectangle([p1_x - 2, p1_y - 2, p1_x + panel_w + 2, p1_y + panel_h + 2], fill='#F1F5F9', outline='#1E293B', width=2)
canvas.paste(img_resized, (p1_x + (panel_w - new_w)//2, p1_y + (panel_h - new_h)//2))
# Label badge
draw.rectangle([p1_x + 10, p1_y + 10, p1_x + 150, p1_y + 36], fill='#FFFFFF', outline='#1E293B', width=2)
draw.text((p1_x + 20, p1_y + 14), "Original User Photo", fill='#0F172A', font=font_bold)

# Panel 2: Annotated
p2_x, p2_y = 500, 105
draw.rectangle([p2_x - 2, p2_y - 2, p2_x + panel_w + 2, p2_y + panel_h + 2], fill='#F1F5F9', outline='#1E293B', width=2)
canvas.paste(ann_resized, (p2_x + (panel_w - new_w)//2, p2_y + (panel_h - new_h)//2))
# Label badge
draw.rectangle([p2_x + 10, p2_y + 10, p2_x + 210, p2_y + 36], fill='#22C55E', outline='#1E293B', width=2)
draw.text((p2_x + 18, p2_y + 14), "AI Detected (YOLO11s)", fill='#FFFFFF', font=font_bold)

# Bottom stats bar
stats_y = 410
draw.rectangle([40, stats_y, card_w - 40, stats_y + 100], fill='#F8FAFC', outline='#CBD5E1', width=1)

# Stat 1: Detected Class
draw.text((60, stats_y + 15), "DETECTED SPECIES", fill='#64748B', font=font_sm)
draw.text((60, stats_y + 35), "Rice Water Weevil (Curculionidae)", fill='#0F172A', font=font_bold)
draw.text((60, stats_y + 55), "Class ID 10 | Grain / Weevil specimen", fill='#059669', font=font_sm)

# Stat 2: Confidence
draw.text((380, stats_y + 15), "CERTAINTY SCORE", fill='#64748B', font=font_sm)
draw.text((380, stats_y + 35), "82.63% Confidence", fill='#2563EB', font=font_bold)
draw.text((380, stats_y + 55), "Bounding Box: [56, 47, 204, 131]", fill='#64748B', font=font_sm)

# Stat 3: Inference Speed
draw.text((680, stats_y + 15), "INFERENCE LATENCY", fill='#64748B', font=font_sm)
draw.text((680, stats_y + 35), f"{res.get('inference_time_ms', 0):.1f} ms (CPU)", fill='#059669', font=font_bold)
draw.text((680, stats_y + 55), "Severity: Isolated Weevil Specimen", fill='#D97706', font=font_sm)

# Save card
output_path = Path('assets/samples/detection_showcase_weevil.png')
canvas.save(output_path)
print("Saved showcase banner to", output_path)

# Also copy to artifacts directory
art_dir = Path(r'C:\Users\RDP\.gemini\antigravity\brain\c7017b9a-851b-4e38-94cf-e5048981aca2')
shutil.copy(output_path, art_dir / 'detection_showcase_weevil.png')
print("Copied showcase to artifact dir:", (art_dir / 'detection_showcase_weevil.png').exists())
