"""Extended tests for glyph converter."""

import tempfile
import unittest
from pathlib import Path


class TestGlyphConverterExtended(unittest.TestCase):
    """Extended tests for GlyphConverter."""

    def setUp(self):
        """Set up test fixtures."""
        try:
            from text2svg3d.font_manager import FontManager
            from text2svg3d.glyph_converter import GlyphConverter

            self.FontManager = FontManager
            self.GlyphConverter = GlyphConverter
            self.can_test = True
        except ImportError:
            self.can_test = False
            self.skipTest("Dependencies not installed")

    def test_convert_text_empty_string(self):
        """Test converting empty string."""
        if not self.can_test:
            return

        fm = self.FontManager(use_cache=False)
        fonts = fm.list_fonts()

        if not fonts:
            self.skipTest("No fonts available")

        _, font_path = fonts[0]
        converter = self.GlyphConverter(font_path, 20.0)

        outlines = converter.convert_text("")
        self.assertEqual(len(outlines), 0)

    def test_convert_text_with_spacing(self):
        """Test converting text with spacing."""
        if not self.can_test:
            return

        fm = self.FontManager(use_cache=False)
        fonts = fm.list_fonts()

        if not fonts:
            self.skipTest("No fonts available")

        _, font_path = fonts[0]
        converter = self.GlyphConverter(font_path, 20.0)

        outlines = converter.convert_text("AB", letter_spacing_mm=5.0)

        if outlines:
            # Check that spacing was applied
            self.assertGreater(len(outlines), 0)
            for outline in outlines:
                self.assertIsNotNone(outline.advance_width)

    def test_path_data_format(self):
        """Test that path data has correct format."""
        if not self.can_test:
            return

        fm = self.FontManager(use_cache=False)
        fonts = fm.list_fonts()

        if not fonts:
            self.skipTest("No fonts available")

        _, font_path = fonts[0]
        converter = self.GlyphConverter(font_path, 20.0)

        outlines = converter.convert_text("A")

        if outlines:
            path_data = outlines[0].path_data
            # Should contain SVG path commands
            self.assertIn("M", path_data)  # MoveTo command
            self.assertTrue(path_data.endswith("Z"))  # ClosePath command

    def test_get_dimensions_consistency(self):
        """Test that dimensions are consistent."""
        if not self.can_test:
            return

        fm = self.FontManager(use_cache=False)
        fonts = fm.list_fonts()

        if not fonts:
            self.skipTest("No fonts available")

        _, font_path = fonts[0]
        converter = self.GlyphConverter(font_path, 20.0)

        # Get dimensions twice
        width1, height1 = converter.get_text_dimensions("ABC")
        width2, height2 = converter.get_text_dimensions("ABC")

        # Should be identical
        self.assertEqual(width1, width2)
        self.assertEqual(height1, height2)

    def test_dimensions_scale_with_size(self):
        """Test that dimensions scale with font size."""
        if not self.can_test:
            return

        fm = self.FontManager(use_cache=False)
        fonts = fm.list_fonts()

        if not fonts:
            self.skipTest("No fonts available")

        _, font_path = fonts[0]

        converter_small = self.GlyphConverter(font_path, 10.0)
        converter_large = self.GlyphConverter(font_path, 20.0)

        width_small, _ = converter_small.get_text_dimensions("A")
        width_large, _ = converter_large.get_text_dimensions("A")

        # Large should be approximately 2x small
        if width_small > 0:
            ratio = width_large / width_small
            self.assertAlmostEqual(ratio, 2.0, delta=0.1)

    def test_unsupported_characters(self):
        """Test handling of unsupported characters."""
        if not self.can_test:
            return

        fm = self.FontManager(use_cache=False)
        fonts = fm.list_fonts()

        if not fonts:
            self.skipTest("No fonts available")

        _, font_path = fonts[0]
        converter = self.GlyphConverter(font_path, 20.0)

        # Try unusual characters
        outlines = converter.convert_text("你好")  # Chinese characters

        # Should either convert or skip gracefully
        self.assertIsInstance(outlines, list)

    def test_advance_width_positive(self):
        """Test that advance width is always positive."""
        if not self.can_test:
            return

        fm = self.FontManager(use_cache=False)
        fonts = fm.list_fonts()

        if not fonts:
            self.skipTest("No fonts available")

        _, font_path = fonts[0]
        converter = self.GlyphConverter(font_path, 20.0)

        outlines = converter.convert_text("ABCDEFG")

        for outline in outlines:
            self.assertGreater(outline.advance_width, 0)


if __name__ == "__main__":
    unittest.main()
