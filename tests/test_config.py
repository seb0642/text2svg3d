"""Tests for configuration module."""

import unittest
from pathlib import Path


class TestConfig(unittest.TestCase):
    """Test configuration constants."""

    def setUp(self):
        """Set up test fixtures."""
        try:
            from text2svg3d import config

            self.config = config
            self.can_test = True
        except ImportError:
            self.can_test = False
            self.skipTest("Dependencies not installed")

    def test_default_values_exist(self):
        """Test that all default values are defined."""
        if not self.can_test:
            return

        self.assertIsInstance(self.config.DEFAULT_SIZE_MM, float)
        self.assertIsInstance(self.config.DEFAULT_OUTPUT_DIR, Path)
        self.assertIsInstance(self.config.DEFAULT_OUTPUT_FILE, str)
        self.assertIsInstance(self.config.DEFAULT_THICKNESS_MM, float)
        self.assertIsInstance(self.config.DEFAULT_LETTER_SPACING_MM, float)
        self.assertIsInstance(self.config.DEFAULT_COORDINATE_PRECISION, int)

    def test_default_values_valid(self):
        """Test that default values are in valid ranges."""
        if not self.can_test:
            return

        self.assertGreater(self.config.DEFAULT_SIZE_MM, 0)
        self.assertGreater(self.config.DEFAULT_THICKNESS_MM, 0)
        self.assertGreaterEqual(self.config.DEFAULT_LETTER_SPACING_MM, 0)
        self.assertGreater(self.config.DEFAULT_COORDINATE_PRECISION, 0)

    def test_font_directories_are_paths(self):
        """Test that font directories are Path objects."""
        if not self.can_test:
            return

        self.assertIsInstance(self.config.FONT_DIRECTORIES, list)
        for directory in self.config.FONT_DIRECTORIES:
            self.assertIsInstance(directory, Path)

    def test_font_extensions_valid(self):
        """Test that font extensions are valid."""
        if not self.can_test:
            return

        self.assertIsInstance(self.config.FONT_EXTENSIONS, list)
        for ext in self.config.FONT_EXTENSIONS:
            self.assertIsInstance(ext, str)
            self.assertTrue(ext.startswith("."))

    def test_svg_constants(self):
        """Test SVG-related constants."""
        if not self.can_test:
            return

        self.assertEqual(self.config.SVG_UNITS, "mm")
        self.assertIn("svg", self.config.SVG_NAMESPACE.lower())

    def test_dpi_constant(self):
        """Test DPI constant."""
        if not self.can_test:
            return

        self.assertIsInstance(self.config.DPI, int)
        self.assertGreater(self.config.DPI, 0)

    def test_cache_file_path(self):
        """Test cache file path is valid."""
        if not self.can_test:
            return

        self.assertIsInstance(self.config.CACHE_FILE, Path)
        self.assertTrue(str(self.config.CACHE_FILE).endswith(".cache"))

    def test_output_dir_logic(self):
        """Test that output directory selection logic is sound."""
        if not self.can_test:
            return

        # Should be one of the expected directories
        output_dir_str = str(self.config.DEFAULT_OUTPUT_DIR)
        self.assertTrue(
            "Desktop" in output_dir_str
            or "Documents" in output_dir_str
            or output_dir_str.endswith("text2svg3d_output")
        )


if __name__ == "__main__":
    unittest.main()
