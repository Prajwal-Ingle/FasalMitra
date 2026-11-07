import sys, os
sys.path.insert(0, os.path.abspath('.'))
from core.detector import get_detector
from core.postprocessing import draw_annotated_image
from PIL import Image
import os

detector = get_detector()
img_path = 'assets/samples/user_test_weevil.jpg'
img = Image.open(img_path)

print(f"Testing image: {img_path} ({img.size})")

for conf in [0.25, 0.15, 0.10, 0.05, 0.01]:
    res = detector.predict(img, conf_threshold=conf)
    print(f"\n--- Confidence Threshold: {conf} ---")
    print(f"Num detections: {res.get('num_detections')}")
    print(f"Inference time: {res.get('inference_time_ms', 0):.1f}ms")
    for box in res.get('boxes', []):
        cname = box.get('class_name')
        cid = box.get('class_id')
        conf_val = box.get('confidence')
        coords = box.get('box')
        print(f"  Class: '{cname}' (id: {cid}), Confidence: {conf_val*100:.2f}%, Box: {coords}")

# Run default inference and save annotated image
default_res = detector.predict(img, conf_threshold=0.10)
annotated = draw_annotated_image(img, default_res)
annotated.save('assets/samples/user_test_annotated.jpg')
print("\nSaved annotated image to assets/samples/user_test_annotated.jpg")
