"""Basic tests for font_manager module."""

import unittest
from pathlib import Path

# Note: These tests require the dependencies to be installed
# Run: pip install -e .
# Then: python -m pytest tests/


class TestFontManager(unittest.TestCase):
    """Test FontManager class."""

    def setUp(self):
        """Set up test fixtures."""
        try:
            from text2svg3d.font_manager import FontManager

            self.FontManager = FontManager
            self.can_test = True
        except ImportError:
            self.can_test = False
            self.skipTest("Dependencies not installed. Run: pip install -e .")

    def test_font_manager_initialization(self):
        """Test that FontManager can be initialized."""
        if not self.can_test:
            return

        fm = self.FontManager(use_cache=False)
        self.assertIsNotNone(fm)
        self.assertIsInstance(fm.fonts, dict)

    def test_list_fonts(self):
        """Test that fonts can be listed."""
        if not self.can_test:
            return

        fm = self.FontManager(use_cache=False)
        fonts = fm.list_fonts()

        # Should return a list
        self.assertIsInstance(fonts, list)

        # On most Linux systems, there should be at least some fonts
        # This test might fail on minimal systems
        if len(fonts) > 0:
            # Each entry should be a tuple of (name, path)
            name, path = fonts[0]
            self.assertIsInstance(name, str)
            self.assertIsInstance(path, Path)

    def test_filter_fonts(self):
        """Test font filtering by regex."""
        if not self.can_test:
            return

        fm = self.FontManager(use_cache=False)

        # Get all fonts
        all_fonts = fm.list_fonts()

        if len(all_fonts) == 0:
            self.skipTest("No fonts found on system")

        # Filter by first letter of first font
        first_font_name = all_fonts[0][0]
        first_letter = first_font_name[0]

        filtered = fm.list_fonts(filter_regex=f"^{first_letter}")

        # Should have at least the first font
        self.assertGreater(len(filtered), 0)

        # All filtered fonts should start with the first letter
        for name, _ in filtered:
            self.assertTrue(name.startswith(first_letter) or name.startswith(first_letter.lower()))

    def test_get_font_path(self):
        """Test getting font path by name."""
        if not self.can_test:
            return

        fm = self.FontManager(use_cache=False)
        fonts = fm.list_fonts()

        if len(fonts) == 0:
            self.skipTest("No fonts found on system")

        # Try to get the first available font
        font_name, expected_path = fonts[0]

        result_path = fm.get_font_path(font_name)

        self.assertIsNotNone(result_path)
        self.assertEqual(result_path, expected_path)

        # Test case-insensitive match
        result_path_lower = fm.get_font_path(font_name.lower())
        self.assertEqual(result_path_lower, expected_path)

    def test_find_similar_fonts(self):
        """Test finding similar fonts."""
        if not self.can_test:
            return

        fm = self.FontManager(use_cache=False)
        fonts = fm.list_fonts()

        if len(fonts) == 0:
            self.skipTest("No fonts found on system")

        # Use part of a real font name
        font_name = fonts[0][0]
        partial_name = font_name[:3]  # First 3 characters

        similar = fm.find_similar_fonts(partial_name)

        # Should return a list
        self.assertIsInstance(similar, list)

        # Should contain the original font (or fonts starting with those chars)
        # At least one result should match
        matching = [f for f in similar if partial_name.lower() in f.lower()]
        self.assertGreater(len(matching), 0)


if __name__ == "__main__":
    unittest.main()
