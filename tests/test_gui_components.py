"""Tests for GUI components (without tkinter dependency)."""

import unittest
from pathlib import Path


class TestFileOperations(unittest.TestCase):
    """Test FileOperations class."""

    def setUp(self):
        """Set up test fixtures."""
        try:
            from text2svg3d.font_manager import FontManager
            from text2svg3d.gui.file_operations import FileOperations

            self.FontManager = FontManager
            self.FileOperations = FileOperations
            self.can_test = True
        except ImportError:
            self.can_test = False
            self.skipTest("Dependencies not installed")

    def test_sanitize_filename_basic(self):
        """Test basic filename sanitization."""
        if not self.can_test:
            return

        fm = self.FontManager(use_cache=False)
        file_ops = self.FileOperations(fm)

        result = file_ops.sanitize_filename("Hello World")
        self.assertEqual(result, "Hello_World")

    def test_sanitize_filename_invalid_chars(self):
        """Test removal of invalid filename characters."""
        if not self.can_test:
            return

        fm = self.FontManager(use_cache=False)
        file_ops = self.FileOperations(fm)

        result = file_ops.sanitize_filename('Test<>:"/\\|?*File')
        self.assertNotIn("<", result)
        self.assertNotIn(">", result)
        self.assertNotIn(":", result)
        self.assertNotIn('"', result)
        self.assertNotIn("/", result)
        self.assertNotIn("\\", result)
        self.assertNotIn("|", result)
        self.assertNotIn("?", result)
        self.assertNotIn("*", result)

    def test_sanitize_filename_max_length(self):
        """Test filename length limitation."""
        if not self.can_test:
            return

        fm = self.FontManager(use_cache=False)
        file_ops = self.FileOperations(fm)

        long_text = "A" * 100
        result = file_ops.sanitize_filename(long_text, max_length=50)
        self.assertLessEqual(len(result), 50)

    def test_sanitize_filename_empty(self):
        """Test handling of empty filename."""
        if not self.can_test:
            return

        fm = self.FontManager(use_cache=False)
        file_ops = self.FileOperations(fm)

        result = file_ops.sanitize_filename("")
        self.assertEqual(result, "output")

    def test_sanitize_filename_only_spaces(self):
        """Test handling of filename with only spaces."""
        if not self.can_test:
            return

        fm = self.FontManager(use_cache=False)
        file_ops = self.FileOperations(fm)

        result = file_ops.sanitize_filename("   ")
        self.assertEqual(result, "output")

    def test_get_output_path(self):
        """Test output path generation."""
        if not self.can_test:
            return

        fm = self.FontManager(use_cache=False)
        file_ops = self.FileOperations(fm)

        path = file_ops.get_output_path("Test")
        self.assertIsInstance(path, Path)
        self.assertTrue(str(path).endswith(".svg"))
        self.assertIn("Test", str(path))

    def test_format_success_message_simple(self):
        """Test success message formatting for simple case."""
        if not self.can_test:
            return

        fm = self.FontManager(use_cache=False)
        file_ops = self.FileOperations(fm)

        message = file_ops.format_success_message(
            text="Test",
            files_created=["/tmp/test.svg"],
            width=100.0,
            height=20.0,
            separate_letters=False,
            enable_outline=False,
            outline_width=0.8,
        )

        self.assertIn("succès", message.lower())
        self.assertIn("100", message)
        self.assertIn("20", message)

    def test_format_success_message_with_outline(self):
        """Test success message with outline."""
        if not self.can_test:
            return

        fm = self.FontManager(use_cache=False)
        file_ops = self.FileOperations(fm)

        message = file_ops.format_success_message(
            text="Test",
            files_created=["/tmp/test.svg", "/tmp/test_contour.svg"],
            width=100.0,
            height=20.0,
            separate_letters=False,
            enable_outline=True,
            outline_width=0.8,
        )

        self.assertIn("contour", message.lower())
        self.assertIn("0.8", message)

    def test_format_success_message_separate_letters(self):
        """Test success message with separate letters."""
        if not self.can_test:
            return

        fm = self.FontManager(use_cache=False)
        file_ops = self.FileOperations(fm)

        files = [f"/tmp/letter_{i}.svg" for i in range(4)]
        message = file_ops.format_success_message(
            text="TEST",
            files_created=files,
            width=100.0,
            height=20.0,
            separate_letters=True,
            enable_outline=False,
            outline_width=0.8,
        )

        self.assertIn("lettre", message.lower())
        self.assertIn("4", message)


class TestWidgetHelpers(unittest.TestCase):
    """Test widget helper functions."""

    def setUp(self):
        """Set up test fixtures."""
        try:
            from text2svg3d.gui import widgets

            self.widgets = widgets
            self.can_test = True
        except ImportError:
            self.can_test = False
            self.skipTest("Dependencies not installed")

    def test_module_imports(self):
        """Test that module imports correctly."""
        if not self.can_test:
            return

        # Just check that functions exist
        self.assertTrue(hasattr(self.widgets, "show_error"))
        self.assertTrue(hasattr(self.widgets, "show_info"))
        self.assertTrue(hasattr(self.widgets, "show_warning"))
        self.assertTrue(hasattr(self.widgets, "ask_yes_no"))


if __name__ == "__main__":
    unittest.main()
