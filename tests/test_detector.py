"""
FasalMitra AI - Detector Unit Tests
"""
import unittest
from pathlib import Path
from PIL import Image
import numpy as np

from config import MODEL_PATH, SAMPLES_DIR, DEFAULT_CONF_THRESHOLD
from core.detector import PestDetector, get_detector

class TestPestDetector(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.detector = get_detector()

    def test_01_model_loading(self):
        """Verify model checkpoint loaded without error and has 102 classes."""
        self.assertTrue(self.detector.is_ready, f"Detector failed to load: {self.detector.load_error}")
        self.assertEqual(self.detector.num_classes, 102, f"Expected 102 classes, got {self.detector.num_classes}")
        self.assertIn(self.detector.device, ["cpu", "cuda"])

    def test_02_class_names_integrity(self):
        """Verify class names are non-empty and contains expected IP102 benchmark species."""
        classes = self.detector.get_supported_classes()
        self.assertEqual(len(classes), 102)
        # Check specific IP102 anchor species
        self.assertIn("rice leaf roller", classes)
        self.assertIn("brown plant hopper", classes)
        self.assertIn("corn borer", classes)
        self.assertIn("aphids", classes)

    def test_03_inference_on_pest_sample(self):
        """Verify inference on a pest sample yields structured bounding boxes and valid confidence."""
        sample_path = SAMPLES_DIR / "sample_pest_1.jpg"
        if not sample_path.exists():
            self.skipTest(f"Sample not found: {sample_path}")

        img = Image.open(sample_path).convert("RGB")
        res = self.detector.predict(img, conf_threshold=0.20)
        
        self.assertTrue(res["success"])
        self.assertGreater(res["num_detections"], 0)
        self.assertGreater(res["inference_time_ms"], 0)
        self.assertIn("boxes", res)

        first_box = res["boxes"][0]
        self.assertIn("class_name", first_box)
        self.assertIn("confidence", first_box)
        self.assertGreaterEqual(first_box["confidence"], 0.20)
        self.assertLessEqual(first_box["confidence"], 1.0)
        self.assertEqual(len(first_box["xyxy"]), 4)

    def test_04_inference_on_clean_negative(self):
        """Verify inference on clean foliage yields 0 false-positive detections at standard threshold."""
        clean_path = SAMPLES_DIR / "healthy_leaf_nodetect.jpg"
        if not clean_path.exists():
            self.skipTest(f"Sample not found: {clean_path}")

        img = Image.open(clean_path).convert("RGB")
        res = self.detector.predict(img, conf_threshold=DEFAULT_CONF_THRESHOLD)
        
        self.assertTrue(res["success"])
        self.assertEqual(res["num_detections"], 0)
        self.assertEqual(len(res["boxes"]), 0)
        self.assertEqual(len(res["class_counts"]), 0)

    def test_05_graceful_error_handling(self):
        """Verify handling when invalid inputs are passed."""
        # Non-existent model path handling
        dummy_detector = PestDetector(model_path=Path("non_existent_model.pt"))
        self.assertFalse(dummy_detector.is_ready)
        res = dummy_detector.predict(Image.new("RGB", (100, 100)))
        self.assertFalse(res["success"])
        self.assertIsNotNone(res["error"])

if __name__ == "__main__":
    unittest.main()
