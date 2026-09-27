"""In-memory pixel regression / 内存像素回归；不修改素材。"""
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest
import warnings
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]

class OutlineRegression(unittest.TestCase):
    def test_all_source_frames(self):
        baseline = json.loads(Path(__file__).with_name("outline-baseline.json").read_text())
        expected = {row["path"]: row for row in baseline["frames"]}
        paths = sorted((ROOT / "source/frames").rglob("*.png"))
        self.assertEqual(len(paths), 57)
        self.assertEqual({p.relative_to(ROOT).as_posix() for p in paths}, set(expected))
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            spec = importlib.util.spec_from_file_location("cleaner", ROOT / "scripts/clean_light_outline.py")
            cleaner = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(cleaner)
            for path in paths:
                key = path.relative_to(ROOT).as_posix()
                with self.subTest(frame=key), Image.open(path) as image:
                    original = image.tobytes()
                    result, count = cleaner.clean(image)
                    self.assertEqual(image.tobytes(), original)
                    self.assertEqual(result.mode, "RGBA")
                    self.assertEqual(list(result.size), expected[key]["size"])
                    self.assertEqual(count, expected[key]["changed_pixels"])
                    self.assertEqual(hashlib.sha256(result.tobytes()).hexdigest(), expected[key]["pixels_sha256"])

if __name__ == "__main__":
    unittest.main()
