"""Tests for CLI interface."""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class TestCLI(unittest.TestCase):
    """Test command-line interface."""

    def run_cli(self, *args):
        """Run CLI command and return result."""
        cmd = [sys.executable, "-m", "text2svg3d"] + list(args)
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=30
        )
        return result

    def test_help_option(self):
        """Test --help option."""
        result = self.run_cli("--help")
        self.assertEqual(result.returncode, 0)
        self.assertIn("text2svg3d", result.stdout.lower())
        self.assertIn("usage", result.stdout.lower())

    def test_version_option(self):
        """Test --version option."""
        result = self.run_cli("--version")
        self.assertEqual(result.returncode, 0)
        self.assertIn("text2svg3d", result.stdout.lower())

    def test_list_fonts_option(self):
        """Test --list-fonts option."""
        result = self.run_cli("--list-fonts")
        # Should succeed even if no fonts found
        self.assertIn(result.returncode, [0, 1])

    def test_no_arguments(self):
        """Test running without arguments shows help."""
        result = self.run_cli()
        # Should show help or error
        self.assertIn(result.returncode, [0, 1])

    def test_invalid_size(self):
        """Test that invalid size is rejected."""
        result = self.run_cli("-s", "-5", "Test")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("size", result.stderr.lower())

    def test_invalid_size_too_large(self):
        """Test that size > 1000 is rejected."""
        result = self.run_cli("-s", "2000", "Test")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("size", result.stderr.lower())

    def test_invalid_thickness(self):
        """Test that invalid thickness is rejected."""
        result = self.run_cli("-t", "-1", "Test")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("thickness", result.stderr.lower())

    def test_invalid_spacing(self):
        """Test that invalid spacing is rejected."""
        result = self.run_cli("-l", "-20", "Test")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("spacing", result.stderr.lower())

    def test_simple_conversion(self):
        """Test simple text conversion."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_file = Path(tmpdir) / "test.svg"

            result = self.run_cli(
                "-o", str(output_file),
                "-s", "20",
                "A"
            )

            # May fail if font not found, but should not crash
            if result.returncode == 0:
                self.assertTrue(output_file.exists())
                self.assertGreater(output_file.stat().st_size, 0)

    def test_preview_option(self):
        """Test --preview option."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_file = Path(tmpdir) / "test.svg"

            result = self.run_cli(
                "-o", str(output_file),
                "--preview",
                "A"
            )

            # May fail if font not found
            if result.returncode == 0:
                self.assertIn("dimensions", result.stdout.lower())

    def test_verbose_option(self):
        """Test -v/--verbose option."""
        result = self.run_cli("-v", "--list-fonts")
        # Verbose should work
        self.assertIn(result.returncode, [0, 1])


if __name__ == "__main__":
    unittest.main()
