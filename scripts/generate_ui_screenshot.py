import sys, os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import shutil

# Dimensions
w, h = 1200, 1100
canvas = Image.new('RGB', (w, h), '#FFFDF7')
draw = ImageDraw.Draw(canvas)

# Fonts
try:
    f_title = ImageFont.truetype('arialbd.ttf', 30)
    f_h2 = ImageFont.truetype('arialbd.ttf', 20)
    f_bold = ImageFont.truetype('arialbd.ttf', 14)
    f_reg = ImageFont.truetype('arial.ttf', 13)
    f_sm = ImageFont.truetype('arial.ttf', 11)
    f_lg = ImageFont.truetype('arialbd.ttf', 16)
except Exception:
    f_title = f_h2 = f_bold = f_reg = f_sm = f_lg = ImageFont.load_default()

def draw_neo_card(x1, y1, x2, y2, bg='#FFFFFF', border='#1E293B', shadow_offset=6, radius=16):
    # shadow
    draw.rounded_rectangle([x1 + shadow_offset, y1 + shadow_offset, x2 + shadow_offset, y2 + shadow_offset], radius=radius, fill=border)
    # card
    draw.rounded_rectangle([x1, y1, x2, y2], radius=radius, fill=bg, outline=border, width=3)

# 1. Top Navbar
nav_x1, nav_y1, nav_x2, nav_y2 = 60, 24, 1140, 76
draw_neo_card(nav_x1, nav_y1, nav_x2, nav_y2, bg='#FFFFFF', radius=26, shadow_offset=4)
# Brand
draw.rounded_rectangle([nav_x1 + 12, nav_y1 + 8, nav_x1 + 48, nav_y1 + 44], radius=10, fill='#FCE7F3', outline='#1E293B', width=2)
draw.text((nav_x1 + 22, nav_y1 + 14), "🌾", font=f_h2)
draw.text((nav_x1 + 58, nav_y1 + 14), "FasalMitra AI", fill='#0F172A', font=f_h2)
draw.text((nav_x1 + 200, nav_y1 + 18), "(फसल मित्र)", fill='#059669', font=f_bold)

# Nav links
links = [("Home", False), ("Pest Detection", True), ("Pest Knowledge", False), ("My Detections", False), ("About", False)]
lx = nav_x1 + 350
for name, active in links:
    if active:
        draw.rounded_rectangle([lx - 10, nav_y1 + 12, lx + 110, nav_y1 + 40], radius=14, fill='#D1FAE5', outline='#1E293B', width=2)
        draw.text((lx + 4, nav_y1 + 17), name, fill='#065F46', font=f_bold)
        lx += 135
    else:
        draw.text((lx, nav_y1 + 18), name, fill='#475569', font=f_bold)
        lx += 110

# Scan button
draw.rounded_rectangle([nav_x2 - 170, nav_y1 + 10, nav_x2 - 14, nav_y1 + 42], radius=16, fill='#22C55E', outline='#1E293B', width=2)
draw.text((nav_x2 - 146, nav_y1 + 17), "📷 Scan Crop Leaf", fill='#FFFFFF', font=f_bold)

# 2. Main Title
draw.rounded_rectangle([60, 105, 260, 133], radius=14, fill='#D1FAE5', outline='#1E293B', width=2)
draw.text((75, 111), "⚡ Live Pest Vision Scanner", fill='#065F46', font=f_bold)

draw.text((60, 142), "Inspect Crop Foliage & Stored Grain", fill='#0F172A', font=f_title)
draw.text((60, 184), "Point your camera at a crop leaf or upload an image to identify pests and get immediate organic field remedies.", fill='#64748B', font=f_reg)

# 3. Mode Switcher
modes = [("📷 Take Photo with Camera", False), ("📁 Upload Leaf Photo", True), ("🌾 Curated Test Samples", False)]
mx = 60
for m_text, m_active in modes:
    m_w = 210 if "Upload" in m_text else 240
    if m_active:
        draw.rounded_rectangle([mx, 215, mx + m_w, 255], radius=14, fill='#34D399', outline='#1E293B', width=2)
        draw.text((mx + 20, 226), m_text, fill='#0F172A', font=f_bold)
    else:
        draw.rounded_rectangle([mx, 215, mx + m_w, 255], radius=14, fill='#FFFFFF', outline='#CBD5E1', width=1)
        draw.text((mx + 20, 226), m_text, fill='#475569', font=f_reg)
    mx += m_w + 14

# 4. Result Container
res_x1, res_y1, res_x2, res_y2 = 60, 280, 1140, 1050
draw_neo_card(res_x1, res_y1, res_x2, res_y2, bg='#FFFFFF', radius=24, shadow_offset=8)

# Verdict Banner (Image 1 style)
v_x1, v_y1, v_x2, v_y2 = res_x1 + 24, res_y1 + 24, res_x2 - 24, res_y1 + 115
draw.rounded_rectangle([v_x1, v_y1, v_x2, v_y2], radius=16, fill='#FFE4E6', outline='#1E293B', width=2)
# Badge
draw.rounded_rectangle([v_x1 + 16, v_y1 + 14, v_x1 + 180, v_y1 + 38], radius=12, fill='#FFFFFF', outline='#1E293B', width=2)
draw.text((v_x1 + 26, v_y1 + 18), "⚠️ Mild / Isolated Pest", fill='#BE123C', font=f_bold)
draw.text((v_x1 + 16, v_y1 + 46), "1 Pest Specimen Located", fill='#0F172A', font=f_h2)
draw.text((v_x1 + 16, v_y1 + 72), "An isolated weevil was identified on grain kernels. Inspect nearby stock to stop spread.", fill='#475569', font=f_reg)

# Certainty display right side
draw.text((v_x2 - 160, v_y1 + 20), "Match Certainty", fill='#64748B', font=f_bold)
draw.text((v_x2 - 160, v_y1 + 42), "82.6%", fill='#059669', font=f_title)
draw.text((v_x2 - 160, v_y1 + 76), "Latency: 125ms", fill='#64748B', font=f_sm)

# Image Tabs
draw.rounded_rectangle([res_x1 + 24, res_y1 + 130, res_x1 + 220, res_y1 + 162], radius=12, fill='#6EE7B7', outline='#1E293B', width=2)
draw.text((res_x1 + 36, res_y1 + 138), "🎯 Marked Pests (Bounding Box)", fill='#0F172A', font=f_bold)
draw.rounded_rectangle([res_x1 + 230, res_y1 + 130, res_x1 + 370, res_y1 + 162], radius=12, fill='#F8FAFC', outline='#CBD5E1', width=1)
draw.text((res_x1 + 244, res_y1 + 138), "🖼️ Original Photo", fill='#64748B', font=f_bold)

# Paste Annotated Image in middle container
ann_img = Image.open('assets/samples/user_test_annotated.jpg').convert('RGB')
ann_scale = 1.95
disp_w, disp_h = int(ann_img.width * ann_scale), int(ann_img.height * ann_scale)
ann_resized = ann_img.resize((disp_w, disp_h), Image.Resampling.LANCZOS)

img_box_x = (w - disp_w) // 2
img_box_y = res_y1 + 175
draw.rounded_rectangle([img_box_x - 3, img_box_y - 3, img_box_x + disp_w + 3, img_box_y + disp_h + 3], radius=16, fill='#0F172A', outline='#1E293B', width=3)
canvas.paste(ann_resized, (img_box_x, img_box_y))

# 3 Practical Remedies Cards
rem_y = img_box_y + disp_h + 20
draw.text((res_x1 + 24, rem_y), "🌾 Practical Field Remedies & Protection Protocol", fill='#0F172A', font=f_h2)

c_w = (res_x2 - res_x1 - 48 - 32) // 3
c1_x = res_x1 + 24
c2_x = c1_x + c_w + 16
c3_x = c2_x + c_w + 16
c_y = rem_y + 30
c_h = 135

# Card 1: Organic Care
draw.rounded_rectangle([c1_x, c_y, c1_x + c_w, c_y + c_h], radius=14, fill='#ECFDF5', outline='#1E293B', width=2)
draw.rounded_rectangle([c1_x + 12, c_y + 10, c1_x + 38, c_y + 36], radius=8, fill='#A7F3D0', outline='#1E293B', width=1)
draw.text((c1_x + 18, c_y + 13), "🌿", font=f_bold)
draw.text((c1_x + 48, c_y + 16), "Organic Storage Care", fill='#065F46', font=f_bold)
draw.text((c1_x + 12, c_y + 44), "• Sun-dry wheat seeds to < 10% moisture.\n• Mix dried neem leaf powder or edible oils\n  (5ml/kg) to repel grain weevils.\n• Store in airtight hermetic PICS bags.", fill='#0F172A', font=f_sm)

# Card 2: Natural Allies
draw.rounded_rectangle([c2_x, c_y, c2_x + c_w, c_y + c_h], radius=14, fill='#FEF3C7', outline='#1E293B', width=2)
draw.rounded_rectangle([c2_x + 12, c_y + 10, c2_x + 38, c_y + 36], radius=8, fill='#FDE68A', outline='#1E293B', width=1)
draw.text((c2_x + 18, c_y + 13), "🐞", font=f_bold)
draw.text((c2_x + 48, c_y + 16), "Natural Biological Allies", fill='#92400E', font=f_bold)
draw.text((c2_x + 12, c_y + 44), "• Parasitoid wasps (Anisopteromalus\n  calandrae) attack weevil larvae.\n• Predatory mites (Cheyletus eruditus)\n  naturally suppress early colonies.", fill='#0F172A', font=f_sm)

# Card 3: Safe Field Treatment
draw.rounded_rectangle([c3_x, c_y, c3_x + c_w, c_y + c_h], radius=14, fill='#E0F2FE', outline='#1E293B', width=2)
draw.rounded_rectangle([c3_x + 12, c_y + 10, c3_x + 38, c_y + 36], radius=8, fill='#BAE6FD', outline='#1E293B', width=1)
draw.text((c3_x + 18, c_y + 13), "🧪", font=f_bold)
draw.text((c3_x + 48, c_y + 16), "Sanitation & Treatment", fill='#0369A1', font=f_bold)
draw.text((c3_x + 12, c_y + 44), "• Clean bin walls before new harvest.\n• Dust with Diatomaceous Earth (DE) or\n  Pyrethrin dust.\n• Consult local KVK officer before fumigation.", fill='#0F172A', font=f_sm)

# Save screenshot image
out_file = Path('assets/screenshots/detection_workspace_screenshot.png')
canvas.save(out_file)
print("Saved UI screenshot to", out_file)

# Copy to artifacts directory
art_dir = Path(r'C:\Users\RDP\.gemini\antigravity\brain\c7017b9a-851b-4e38-94cf-e5048981aca2')
shutil.copy(out_file, art_dir / 'detection_workspace_screenshot.png')
print("Copied UI screenshot to artifact dir:", (art_dir / 'detection_workspace_screenshot.png').exists())
