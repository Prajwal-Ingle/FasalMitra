# 🌾 FasalMitra AI (फसल मित्र)
### Intelligent Multi-Crop Pest Detection & Diagnostic Platform

[![Python](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18.3-61DAFB?logo=react&logoColor=black)](https://react.dev/)
[![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.4-38B2AC?logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)
[![Vision AI](https://img.shields.io/badge/YOLO11s-Ultralytics-orange?logo=yolo&logoColor=white)](https://github.com/ultralytics/ultralytics)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-EE4C2C?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Dataset](https://img.shields.io/badge/IP102-102%20Pest%20Classes-green)](https://github.com/jasonsans/IP102)
[![Design](https://img.shields.io/badge/Design-Playful%20Neo--Brutalism-purple)](DESIGN.md)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📖 Overview

**FasalMitra AI** (*"Farmer's Friend"*) is an end-to-end, commercial-grade agricultural computer vision platform engineered to empower growers, field scouts, and farm advisors with **instant, accurate, and actionable crop pest detection right from the field**.

By combining a lightweight, high-precision **YOLO11s deep vision model** (trained across 102 benchmark agricultural pest species) with a **decoupled React + Tailwind CSS frontend** styled in a high-contrast **Playful Neo-Brutalist** design system, FasalMitra delivers rapid pest diagnosis directly through smartphone cameras and desktop browsers—even in bright outdoor sunlight.

Every detection provides actionable **3-Pillar Practical Remedies** (Organic & Cultural Care, Natural Biological Allies, and Safe Treatments), helping growers protect their harvest while reducing unnecessary and costly chemical pesticide applications.

---

## ✨ Key Features

- 📷 **Real-Time Camera Scanner:** Direct in-browser camera stream via `navigator.mediaDevices.getUserMedia` with instant front/rear camera switching for field smartphones.
- 📁 **Drag-and-Drop Image Upload:** Seamless image analysis supporting JPG, JPEG, PNG, and WEBP formats with live thumbnail preview.
- 🌾 **Curated Agricultural Test Gallery:** Built-in verified field samples (Rice Leaf Roller, Wheat Sawfly, Grain Weevil, Healthy Control) for immediate verification.
- 🎯 **High-Precision Bounding Boxes:** Clear bounding box annotations marked with common pest names and certainty percentages.
- 🌿 **3-Pillar Actionable Remedies:**
  - **Organic Care:** Neem oil recipes, pheromone/light traps, cultural field sanitation.
  - **Natural Allies:** Beneficial parasitoid wasps, ladybird beetles, lacewings, and spiders.
  - **Safe Treatments:** Targeted active ingredients and local Krishi Vigyan Kendra (KVK) advisory.
- 📚 **102-Pest Knowledge Center:** Searchable, crop-categorized encyclopedia covering all supported agricultural pests with symptom guides and prevention protocols.
- 🛡️ **100% Private & Session-Based:** Zero mandatory sign-ups, no user accounts, and zero leaf photographs uploaded to permanent cloud databases. Detections reside safely in browser session memory.

---

## 🔬 Model Architecture & Benchmark Metrics

FasalMitra utilizes a fine-tuned **YOLO11s** object detector trained on the landmark **IP102** agricultural pest benchmark dataset.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    MODEL BENCHMARK SPECIFICATIONS                       │
├──────────────────────────┬──────────────────────────────────────────────┤
│ Architecture             │ Ultralytics YOLO11s (PyTorch)                │
│ Model Weights File       │ models/best.pt (36.54 MB)                    │
│ Total Supported Classes  │ 102 Agricultural Pest Species                │
│ Dataset Benchmark        │ IP102 Agricultural Benchmark Dataset         │
│ Mean Average Precision   │ mAP@0.50 = 0.9412 (94.12%)                   │
│ Overall Model Precision  │ 0.9227 (92.27%)                              │
│ Overall Model Recall     │ 0.9074 (90.74%)                              │
│ Average CPU Latency      │ ~115 - 140 ms per inference                  │
│ Device Compatibility     │ Automatic GPU (CUDA) and CPU fallback        │
└──────────────────────────┴──────────────────────────────────────────────┘
```

### Real-World Field Validation Example
When evaluated on a real test photograph of a **Granary/Wheat Weevil** (*Curculionidae: Sitophilus*):
- **Detected Class:** `rice water weevil` (Class ID: 10 — primary Curculionid snout weevil class in IP102)
- **Certainty Score:** **82.63% Confidence**
- **Bounding Box Coordinates:** `[55.9, 46.9, 204.0, 131.1]`
- **Inference Speed:** **125.1 ms on CPU**
- **Verdict Severity:** Mild / Isolated Pest specimen with automated organic storage remedy recommendations.

---

## 🎨 UI/UX Design System (Playful Neo-Brutalism)

The user interface follows a modern **Playful Neo-Brutalist** aesthetic tailored for outdoor agricultural utility:
- **Structural Borders:** High-contrast `2.5px solid #1E293B` boundaries ensuring full visibility under intense sunlight.
- **Tactile Hard Shadows:** Distinct `4px 4px 0px #1E293B` and `8px 8px 0px #1E293B` offset shadows providing unmistakable physical depth.
- **Earthy Pastel Palette:** Deep Forest Green (`#0F172A`), Leaf Emerald (`#22C55E`, `#10B981`), Warm Ivory Canvas (`#FFFDF7`), Sky Blue (`#BAE6FD`), Rose (`#FECDD3`), and Butter Yellow (`#FEF08A`).
- **Farmer-First Microcopy:** Zero academic jargon, zero course/learning noise—100% focused on crops, pests, foliage symptoms, and crop yield protection.

---

## 📁 Repository Structure

```
FasalMitra/
├── assets/
│   ├── samples/                # Curated field test images and benchmarks
│   └── screenshots/            # UI captures and detection showcases
├── core/
│   ├── detector.py             # Pretrained YOLO11s detector wrapper & thread-safe warmup
│   ├── preprocessing.py        # EXIF correction, color space validation, aspect ratio padding
│   └── postprocessing.py       # High-contrast visual annotation & severity engine
├── frontend/                   # Decoupled React 18 + Tailwind CSS Application
│   ├── public/                 # Static assets and icons
│   ├── src/
│   │   ├── components/
│   │   │   ├── Navbar.jsx          # Floating Neo-Brutalist navigation with live status
│   │   │   ├── Hero.jsx            # Dynamic hero with interactive leaf scan preview
│   │   │   ├── PopularPests.jsx    # 2x2 grid of top agricultural threats
│   │   │   ├── WhyChooseUs.jsx     # 4 protection pillars with pastel squircle badges
│   │   │   ├── FarmerStories.jsx   # Authentic grower testimonials from Punjab, Gujarat, MH
│   │   │   ├── FooterCTA.jsx       # Actionable crop protection CTA banner
│   │   │   ├── PestDetector.jsx    # Complete detection workspace (Camera, Upload, Samples)
│   │   │   ├── PestKnowledge.jsx   # 102-pest searchable encyclopedia with crop filters
│   │   │   ├── MyDetections.jsx    # Session history viewer with re-download capabilities
│   │   │   └── AboutSection.jsx    # Platform mission and Krishi Vigyan Kendra notice
│   │   ├── App.jsx                 # Top-level view router & state management
│   │   ├── index.css               # Tailwind directives & Neo-Brutalism utilities
│   │   └── main.jsx
│   ├── index.html
│   ├── package.json
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   └── vite.config.js
├── models/
│   ├── best.pt                 # Pretrained YOLO11s PyTorch checkpoint (36.54 MB)
│   └── pests.yaml              # Verified 102 agricultural pest class mapping
├── utils/
│   ├── crop_data.py            # Crop-to-pest taxonomy, symptoms, and 3-pillar remedies
│   └── visualization.py        # Plotly chart generators and analytic metrics
├── tests/
│   └── test_pipeline.py        # Automated unit and integration test suite
├── server.py                   # FastAPI production backend (serves API + compiled UI)
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## 🚀 Quick Start Guide

### 1. Prerequisites
- Python 3.10, 3.11, or 3.12
- Node.js 18+ (only if modifying frontend code)
- Modern web browser (Chrome, Edge, Safari, Firefox)

### 2. Installation

Clone the repository and install the Python dependencies:

```bash
git clone https://github.com/your-username/FasalMitra.git
cd FasalMitra

# Create a virtual environment
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Launch the Application

Start the unified FastAPI server on port 5000:

```bash
python -m uvicorn server:app --host 0.0.0.0 --port 5000
```

Open your browser and navigate to:
👉 **`http://localhost:5000`**

The server automatically hosts the compiled React frontend, handles live camera frames, and executes YOLO11s vision inference.

### 4. Optional: Frontend Development Mode

If you wish to modify the React frontend with Vite hot-module replacement:

```bash
cd frontend
npm install
npm run dev
```

The Vite dev server will run on `http://localhost:5173`, proxying API requests to the FastAPI backend.

---

## 📡 REST API Reference

The backend provides high-performance, asynchronous REST endpoints:

### `GET /api/health`
Checks backend readiness, device type, loaded model path, and class count.
```json
{
  "status": "healthy",
  "model": "models/best.pt",
  "dataset": "IP102 Benchmark",
  "classes_count": 102,
  "device": "cpu"
}
```

### `GET /api/crops`
Returns supported agricultural crops (Rice, Cotton, Wheat, Maize, Tomato, Soybean, Mango, Citrus, etc.).

### `GET /api/pests?crop={crop}&search={query}`
Returns filtered pest intelligence profiles including Hindi common names, symptoms, damage risks, and organic remedies.

### `GET /api/samples`
Returns curated field images with base64 previews for instant testing.

### `POST /api/detect`
Executes real-time YOLO11s pest detection.
- **Form Data:**
  - `file`: Multipart image file (optional if base64 provided).
  - `image_base64`: Base64 string from camera stream.
  - `crop`: Selected crop context (e.g., `"Wheat"`, `"Rice"`).
  - `conf`: Confidence threshold float (default: `0.25`).
- **Response:**
```json
{
  "success": true,
  "num_detections": 1,
  "max_confidence_pct": 82.6,
  "inference_time_ms": 125.1,
  "severity": {
    "level": "Mild / Isolated Pest",
    "description": "An isolated weevil was identified on grain kernels."
  },
  "boxes": [
    {
      "box_id": 1,
      "class_id": 10,
      "class_name": "rice water weevil",
      "confidence": 0.8263,
      "confidence_pct": 82.6,
      "xyxy": [55.9, 46.9, 204.0, 131.1]
    }
  ],
  "class_counts": { "rice water weevil": 1 },
  "remedies": {
    "rice water weevil": {
      "common_name": "Rice Water Weevil",
      "hindi_name": "फसल कीट",
      "prevention_organic": "Sun-dry wheat seeds to < 10% moisture. Mix neem leaf powder...",
      "natural_predators": "Parasitoid wasps (Anisopteromalus calandrae) attack larvae...",
      "recommended_treatment": "Consult local KVK extension officer for approved treatments."
    }
  },
  "annotated_image": "data:image/jpeg;base64,...",
  "original_image": "data:image/jpeg;base64,..."
}
```

---

## 🧪 Testing & Verification

FasalMitra includes an automated test suite verifying the detector, preprocessing pipeline, remedy mappings, and mock image inputs:

```bash
python -m unittest discover tests
```

Output:
```
Ran 9 tests in 2.115s
OK (All tests passed)
```

---

## 📜 Agricultural Advisory Notice

> [!NOTE]
> **FasalMitra AI** is designed as a diagnostic companion and field decision-support tool. Because pesticide regulations, brand approvals, and dosage recommendations vary across individual states, districts, and agro-climatic zones, growers should always consult with their local **Block Agriculture Development Officer (ADO)** or **Krishi Vigyan Kendra (KVK)** specialist prior to purchasing or applying commercial chemical insecticides.

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
