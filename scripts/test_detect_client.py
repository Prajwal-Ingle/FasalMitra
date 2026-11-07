import requests
import json

url = "http://localhost:5000/api/detect"
with open("assets/samples/sample_pest_1.jpg", "rb") as f:
    files = {"file": ("sample.jpg", f, "image/jpeg")}
    data = {"confidence": 0.25}
    res = requests.post(url, files=files, data=data)
    print("Status:", res.status_code)
    payload = res.json()
    print("Success:", payload.get("success"))
    print("Total detected:", payload.get("total_count"))
    for d in payload.get("detections", []):
        print(f" - {d['pest_name']} ({d['confidence']*100:.1f}%)")
    print("Remedy keys:", list(payload.get("remedies", {}).keys()))
