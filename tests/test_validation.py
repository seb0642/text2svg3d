"""Tests for input validation."""

import tempfile
import unittest
from pathlib import Path

import pytest


class TestInputValidation(unittest.TestCase):
    """Test input validation across modules."""

    def setUp(self):
        """Set up test fixtures."""
        try:
            from text2svg3d.glyph_converter import GlyphConverter

            self.GlyphConverter = GlyphConverter
            self.can_test = True
        except ImportError:
            self.can_test = False
            self.skipTest("Dependencies not installed")

    def test_glyph_converter_nonexistent_font(self):
        """Test that FileNotFoundError is raised for nonexistent font."""
        if not self.can_test:
            return

        fake_path = Path("/tmp/nonexistent_font_12345.ttf")

        with self.assertRaises(FileNotFoundError) as cm:
            self.GlyphConverter(fake_path, 20.0)

        self.assertIn("not found", str(cm.exception).lower())

    def test_glyph_converter_invalid_size_negative(self):
        """Test that ValueError is raised for negative size."""
        if not self.can_test:
            return

        with tempfile.NamedTemporaryFile(suffix=".ttf") as f:
            fake_path = Path(f.name)

            with self.assertRaises(ValueError) as cm:
                self.GlyphConverter(fake_path, -5.0)

            self.assertIn("size_mm", str(cm.exception).lower())

    def test_glyph_converter_invalid_size_zero(self):
        """Test that ValueError is raised for size = 0."""
        if not self.can_test:
            return

        with tempfile.NamedTemporaryFile(suffix=".ttf") as f:
            fake_path = Path(f.name)

            with self.assertRaises(ValueError) as cm:
                self.GlyphConverter(fake_path, 0.0)

            self.assertIn("size_mm", str(cm.exception).lower())

    def test_glyph_converter_invalid_size_too_small(self):
        """Test that ValueError is raised for size < 0.1."""
        if not self.can_test:
            return

        with tempfile.NamedTemporaryFile(suffix=".ttf") as f:
            fake_path = Path(f.name)

            with self.assertRaises(ValueError) as cm:
                self.GlyphConverter(fake_path, 0.05)

            self.assertIn("size_mm", str(cm.exception).lower())

    def test_glyph_converter_invalid_size_too_large(self):
        """Test that ValueError is raised for size > 1000."""
        if not self.can_test:
            return

        with tempfile.NamedTemporaryFile(suffix=".ttf") as f:
            fake_path = Path(f.name)

            with self.assertRaises(ValueError) as cm:
                self.GlyphConverter(fake_path, 2000.0)

            self.assertIn("size_mm", str(cm.exception).lower())

    def test_glyph_converter_invalid_type(self):
        """Test that TypeError is raised for non-numeric size."""
        if not self.can_test:
            return

        with tempfile.NamedTemporaryFile(suffix=".ttf") as f:
            fake_path = Path(f.name)

            with self.assertRaises(TypeError) as cm:
                self.GlyphConverter(fake_path, "not a number")

            self.assertIn("numeric", str(cm.exception).lower())

    def test_glyph_converter_directory_path(self):
        """Test that ValueError is raised when path is directory."""
        if not self.can_test:
            return

        with tempfile.TemporaryDirectory() as tmpdir:
            dir_path = Path(tmpdir)

            with self.assertRaises(ValueError) as cm:
                self.GlyphConverter(dir_path, 20.0)

            self.assertIn("not a file", str(cm.exception).lower())


if __name__ == "__main__":
    unittest.main()
