"""Main entry point for text2svg3d CLI."""

import argparse
import sys
from pathlib import Path

from . import __version__
from .config import (
    DEFAULT_LETTER_SPACING_MM,
    DEFAULT_OUTPUT_FILE,
    DEFAULT_SIZE_MM,
    DEFAULT_THICKNESS_MM,
)
from .font_manager import FontManager
from .glyph_converter import GlyphConverter
from .svg_builder import SVGBuilder


def list_fonts_command(args: argparse.Namespace) -> int:
    """
    Handle --list-fonts command.

    Args:
        args: Command line arguments

    Returns:
        Exit code
    """
    if args.verbose:
        print("Scanning system fonts...")

    font_manager = FontManager(use_cache=True)
    fonts = font_manager.list_fonts(filter_regex=args.filter_fonts)

    if not fonts:
        if args.filter_fonts:
            print(f"No fonts found matching pattern: {args.filter_fonts}")
        else:
            print("No fonts found on system.")
        return 1

    print(f"Found {len(fonts)} font(s):\n")
    for name, path in fonts:
        if args.verbose:
            print(f"  {name}")
            print(f"    Path: {path}")
        else:
            print(f"  {name}")

    return 0


def convert_text_command(args: argparse.Namespace) -> int:
    """
    Handle text conversion command.

    Args:
        args: Command line arguments

    Returns:
        Exit code
    """
    text = args.text
    if not text:
        print("Error: Text cannot be empty.")
        return 1

    if args.verbose:
        print(f'Converting text: "{text}"')
        print(f"Font: {args.font}")
        print(f"Size: {args.size}mm")
        print(f"Output: {args.output}")

    # Load font manager
    font_manager = FontManager(use_cache=True)

    # Find font
    font_path = font_manager.get_font_path(args.font)

    if not font_path:
        print(f"Error: Font '{args.font}' not found.")
        similar = font_manager.find_similar_fonts(args.font)
        if similar:
            print("\nDid you mean one of these?")
            for font_name in similar:
                print(f"  - {font_name}")
        else:
            print("\nUse --list-fonts to see available fonts.")
        return 1

    if args.verbose:
        print(f"Font path: {font_path}")

    # Convert glyphs
    try:
        converter = GlyphConverter(font_path, args.size)
        outlines = converter.convert_text(text, args.letter_spacing)

        if not outlines:
            print(
                "Error: No characters could be converted. Font may not support these characters."
            )
            return 1

        if len(outlines) < len(text):
            print(f"Warning: {len(text) - len(outlines)} character(s) not supported by font.")

        # Get dimensions
        width, height = converter.get_text_dimensions(text, args.letter_spacing)

        if args.preview:
            print("\nSVG Dimensions:")
            print(f"  Width:  {width:.2f}mm")
            print(f"  Height: {height:.2f}mm")
            print(f"  Suggested thickness: {args.thickness}mm")

        # Build SVG
        builder = SVGBuilder(
            text=text, font_name=args.font, size_mm=args.size, thickness_mm=args.thickness
        )

        output_path = Path(args.output)
        builder.build_svg(outlines, output_path, width, height)

        print(f"\nSVG file created: {output_path}")

        if args.preview:
            print(f"Characters converted: {len(outlines)}")

        return 0

    except Exception as e:
        print(f"Error during conversion: {e}")
        if args.verbose:
            import traceback

            traceback.print_exc()
        return 1


def main() -> int:
    """
    Main entry point for CLI.

    Returns:
        Exit code
    """

    # Validation functions for arguments
    def validate_size(value: str) -> float:
        """Validate size argument."""
        try:
            fvalue = float(value)
            if not 0.1 <= fvalue <= 1000:
                raise argparse.ArgumentTypeError(f"size must be between 0.1 and 1000, got {fvalue}")
            return fvalue
        except ValueError:
            raise argparse.ArgumentTypeError(f"size must be a number, got '{value}'")

    def validate_thickness(value: str) -> float:
        """Validate thickness argument."""
        try:
            fvalue = float(value)
            if not 0.1 <= fvalue <= 100:
                raise argparse.ArgumentTypeError(
                    f"thickness must be between 0.1 and 100, got {fvalue}"
                )
            return fvalue
        except ValueError:
            raise argparse.ArgumentTypeError(f"thickness must be a number, got '{value}'")

    def validate_spacing(value: str) -> float:
        """Validate letter spacing argument."""
        try:
            fvalue = float(value)
            if not -10 <= fvalue <= 100:
                raise argparse.ArgumentTypeError(
                    f"letter-spacing must be between -10 and 100, got {fvalue}"
                )
            return fvalue
        except ValueError:
            raise argparse.ArgumentTypeError(f"letter-spacing must be a number, got '{value}'")

    parser = argparse.ArgumentParser(
        description="Convert text to SVG for 3D printing", prog="text2svg3d"
    )

    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")

    parser.add_argument("text", nargs="?", help="Text to convert to SVG")

    parser.add_argument(
        "-f", "--font", default="DejaVu Sans", help="Font family name (default: DejaVu Sans)"
    )

    parser.add_argument(
        "-s",
        "--size",
        type=validate_size,
        default=DEFAULT_SIZE_MM,
        help=f"Text height in mm (default: {DEFAULT_SIZE_MM}, range: 0.1-1000)",
    )

    parser.add_argument(
        "-o",
        "--output",
        default=DEFAULT_OUTPUT_FILE,
        help=f"Output SVG file (default: {DEFAULT_OUTPUT_FILE})",
    )

    parser.add_argument(
        "-t",
        "--thickness",
        type=validate_thickness,
        default=DEFAULT_THICKNESS_MM,
        help=f"Suggested extrusion thickness in mm (default: {DEFAULT_THICKNESS_MM}, range: 0.1-100)",
    )

    parser.add_argument(
        "-l",
        "--letter-spacing",
        type=validate_spacing,
        default=DEFAULT_LETTER_SPACING_MM,
        help=f"Letter spacing in mm (default: {DEFAULT_LETTER_SPACING_MM}, range: -10 to 100)",
    )

    parser.add_argument("--list-fonts", action="store_true", help="List all available system fonts")

    parser.add_argument(
        "--filter-fonts", help="Filter fonts by regex pattern (use with --list-fonts)"
    )

    parser.add_argument("--preview", action="store_true", help="Display SVG dimensions and info")

    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output for debugging")

    args = parser.parse_args()

    # Handle --list-fonts command
    if args.list_fonts:
        return list_fonts_command(args)

    # Handle text conversion
    if not args.text:
        parser.print_help()
        return 1

    return convert_text_command(args)


if __name__ == "__main__":
    sys.exit(main())
