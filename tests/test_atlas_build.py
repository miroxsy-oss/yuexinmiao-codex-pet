"""Atlas pixel regression without artwork writes / 无素材写入的图集像素回归。"""
import importlib.util
from io import BytesIO
from pathlib import Path
import unittest
import warnings

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]


class AtlasBuildRegression(unittest.TestCase):
    def test_rebuild_and_webp_round_trip(self):
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            spec = importlib.util.spec_from_file_location("atlas_builder", ROOT / "scripts/build.py")
            builder = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(builder)
            atlas = builder.compose()
            with Image.open(ROOT / "dist/yuexinmiao-selected/spritesheet.webp") as published:
                expected = published.convert("RGBA")
            self.assertEqual(atlas.mode, expected.mode)
            self.assertEqual(atlas.size, expected.size)
            self.assertEqual(atlas.tobytes(), expected.tobytes())
            self.assertEqual(atlas.getchannel("A").getextrema(), (0, 255))
            encoded = BytesIO()
            atlas.save(encoded, format="WEBP", lossless=True, quality=100, method=6, exact=True)
            encoded.seek(0)
            with Image.open(encoded) as decoded:
                self.assertEqual(decoded.size, expected.size)
                self.assertEqual(decoded.convert("RGBA").tobytes(), expected.tobytes())


if __name__ == "__main__":
    unittest.main()
