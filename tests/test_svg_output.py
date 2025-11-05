"""Tests for SVG output generation."""

import tempfile
import unittest
from pathlib import Path
from xml.etree import ElementTree as ET


class TestSVGOutput(unittest.TestCase):
    """Test SVG output generation."""

    def setUp(self):
        """Set up test fixtures."""
        try:
            from text2svg3d.font_manager import FontManager
            from text2svg3d.glyph_converter import GlyphConverter
            from text2svg3d.svg_builder import SVGBuilder

            self.FontManager = FontManager
            self.GlyphConverter = GlyphConverter
            self.SVGBuilder = SVGBuilder
            self.can_test = True
        except ImportError:
            self.can_test = False
            self.skipTest("Dependencies not installed. Run: pip install -e .")

    def test_svg_generation(self):
        """Test basic SVG file generation."""
        if not self.can_test:
            return

        # Find a font to use
        fm = self.FontManager(use_cache=False)
        fonts = fm.list_fonts()

        if len(fonts) == 0:
            self.skipTest("No fonts found on system")

        font_name, font_path = fonts[0]

        # Convert simple text
        converter = self.GlyphConverter(font_path, 20.0)
        outlines = converter.convert_text("A")

        if len(outlines) == 0:
            self.skipTest(f"Font {font_name} doesn't support character 'A'")

        # Get dimensions
        width, height = converter.get_text_dimensions("A")

        # Build SVG
        with tempfile.NamedTemporaryFile(mode="w", suffix=".svg", delete=False) as f:
            temp_path = Path(f.name)

        try:
            builder = self.SVGBuilder(text="A", font_name=font_name, size_mm=20.0, thickness_mm=2.0)

            builder.build_svg(outlines, temp_path, width, height)

            # Verify file exists
            self.assertTrue(temp_path.exists())

            # Verify file is not empty
            self.assertGreater(temp_path.stat().st_size, 0)

            # Parse as XML
            tree = ET.parse(str(temp_path))
            root = tree.getroot()

            # Check it's an SVG
            self.assertIn("svg", root.tag.lower())

            # Should have at least one path element
            # Note: namespace might be present
            paths = list(root.iter())
            path_elements = [p for p in paths if "path" in p.tag.lower()]
            self.assertGreater(len(path_elements), 0)

        finally:
            # Clean up
            if temp_path.exists():
                temp_path.unlink()

    def test_svg_has_closed_paths(self):
        """Test that all paths are closed (end with Z)."""
        if not self.can_test:
            return

        # Find a font to use
        fm = self.FontManager(use_cache=False)
        fonts = fm.list_fonts()

        if len(fonts) == 0:
            self.skipTest("No fonts found on system")

        font_name, font_path = fonts[0]

        # Convert simple text
        converter = self.GlyphConverter(font_path, 20.0)
        outlines = converter.convert_text("O")  # O should have inner and outer paths

        if len(outlines) == 0:
            self.skipTest(f"Font {font_name} doesn't support character 'O'")

        # Check that path data ends with Z
        for outline in outlines:
            path_data = outline.path_data.strip()
            # Should end with 'Z'
            self.assertTrue(path_data.endswith("Z"), f"Path should end with 'Z': {path_data[-20:]}")

    def test_multiple_characters(self):
        """Test conversion of multiple characters."""
        if not self.can_test:
            return

        # Find a font to use
        fm = self.FontManager(use_cache=False)
        fonts = fm.list_fonts()

        if len(fonts) == 0:
            self.skipTest("No fonts found on system")

        font_name, font_path = fonts[0]

        # Convert multiple characters
        converter = self.GlyphConverter(font_path, 20.0)
        outlines = converter.convert_text("ABC")

        # Should have up to 3 glyphs (depends on font support)
        self.assertGreater(len(outlines), 0)
        self.assertLessEqual(len(outlines), 3)

        # Each outline should have proper structure
        for outline in outlines:
            self.assertIsInstance(outline.path_data, str)
            self.assertGreater(len(outline.path_data), 0)
            self.assertGreater(outline.advance_width, 0)
            self.assertIsInstance(outline.char, str)

    def test_letter_spacing(self):
        """Test letter spacing functionality."""
        if not self.can_test:
            return

        # Find a font to use
        fm = self.FontManager(use_cache=False)
        fonts = fm.list_fonts()

        if len(fonts) == 0:
            self.skipTest("No fonts found on system")

        font_name, font_path = fonts[0]

        # Convert with and without spacing
        converter = self.GlyphConverter(font_path, 20.0)

        width_normal, _ = converter.get_text_dimensions("AB", letter_spacing_mm=0.0)
        width_spaced, _ = converter.get_text_dimensions("AB", letter_spacing_mm=5.0)

        # With spacing should be wider
        self.assertGreater(width_spaced, width_normal)

        # Difference should be approximately the spacing amount (5mm for one space)
        # Note: Last letter doesn't add spacing, so 1 space for "AB"
        expected_diff = 5.0
        actual_diff = width_spaced - width_normal
        self.assertAlmostEqual(actual_diff, expected_diff, delta=0.1)


if __name__ == "__main__":
    unittest.main()
