#!/usr/bin/env python3
"""
Example script showing programmatic usage of text2svg3d.

This script demonstrates how to use the text2svg3d library
directly from Python code instead of the CLI.
"""

from pathlib import Path

# Import the modules
from text2svg3d.font_manager import FontManager
from text2svg3d.glyph_converter import GlyphConverter
from text2svg3d.svg_builder import SVGBuilder


def main():
    """Main example function."""

    # 1. Find available fonts
    print("Step 1: Finding available fonts...")
    font_manager = FontManager(use_cache=True)

    # List all fonts
    all_fonts = font_manager.list_fonts()
    print(f"Found {len(all_fonts)} fonts on system")

    # Find a specific font (e.g., DejaVu Sans)
    font_path = font_manager.get_font_path("DejaVu Sans")

    if not font_path:
        # Use first available font as fallback
        if all_fonts:
            font_name, font_path = all_fonts[0]
            print(f"Using fallback font: {font_name}")
        else:
            print("No fonts found!")
            return

    font_name = "DejaVu Sans"
    print(f"Using font: {font_name}")
    print(f"Font path: {font_path}")

    # 2. Convert text to glyph outlines
    print("\nStep 2: Converting text to glyphs...")
    text = "HELLO"
    size_mm = 30.0
    letter_spacing_mm = 2.0

    converter = GlyphConverter(font_path, size_mm)
    outlines = converter.convert_text(text, letter_spacing_mm)

    print(f"Converted {len(outlines)} characters")

    # Show some info about the glyphs
    for i, outline in enumerate(outlines):
        print(f"  Char '{outline.char}': advance={outline.advance_width:.2f}mm")

    # 3. Get text dimensions
    print("\nStep 3: Calculating dimensions...")
    width, height = converter.get_text_dimensions(text, letter_spacing_mm)
    print(f"Text dimensions: {width:.2f}mm x {height:.2f}mm")

    # 4. Build SVG file
    print("\nStep 4: Building SVG...")
    output_path = Path("example_hello.svg")
    thickness_mm = 2.0

    builder = SVGBuilder(
        text=text,
        font_name=font_name,
        size_mm=size_mm,
        thickness_mm=thickness_mm
    )

    builder.build_svg(outlines, output_path, width, height)

    print(f"SVG file created: {output_path}")
    print(f"Size: {output_path.stat().st_size} bytes")

    # 5. Create multiple examples
    print("\nStep 5: Creating additional examples...")

    examples = [
        ("ABC", 40.0, 1.0, "example_abc.svg"),
        ("123", 25.0, 0.5, "example_numbers.svg"),
        ("LOGO", 35.0, 3.0, "example_logo.svg"),
    ]

    for example_text, example_size, example_spacing, example_file in examples:
        try:
            converter = GlyphConverter(font_path, example_size)
            outlines = converter.convert_text(example_text, example_spacing)

            if outlines:
                width, height = converter.get_text_dimensions(example_text, example_spacing)

                builder = SVGBuilder(
                    text=example_text,
                    font_name=font_name,
                    size_mm=example_size,
                    thickness_mm=2.0
                )

                output_path = Path(example_file)
                builder.build_svg(outlines, output_path, width, height)

                print(f"  Created: {example_file}")
        except Exception as e:
            print(f"  Error creating {example_file}: {e}")

    print("\nDone! Check the generated SVG files.")
    print("You can import these into your 3D slicer software.")


if __name__ == "__main__":
    main()
