# Examples Directory

This directory contains example scripts and generated SVG files.

## Example Scripts

### example_usage.py

Demonstrates programmatic usage of text2svg3d:

```bash
# Run the example script
python examples/example_usage.py
```

This will create several example SVG files:
- `example_hello.svg` - "HELLO" in 30mm
- `example_abc.svg` - "ABC" in 40mm
- `example_numbers.svg` - "123" in 25mm
- `example_logo.svg` - "LOGO" in 35mm

## Using the Examples

### From CLI

```bash
# Simple examples
text2svg3d "HELLO"
text2svg3d -f "Arial" -s 30 "3D PRINT"

# With custom spacing
text2svg3d -f "DejaVu Sans Bold" -s 25 -l 2 -o examples/logo.svg "LOGO"

# Preview mode
text2svg3d -s 40 --preview -o examples/preview.svg "PREVIEW"
```

### From Python Code

```python
from pathlib import Path
from text2svg3d.font_manager import FontManager
from text2svg3d.glyph_converter import GlyphConverter
from text2svg3d.svg_builder import SVGBuilder

# Find a font
fm = FontManager()
font_path = fm.get_font_path("DejaVu Sans")

# Convert text
converter = GlyphConverter(font_path, size_mm=30.0)
outlines = converter.convert_text("HELLO", letter_spacing_mm=2.0)

# Get dimensions
width, height = converter.get_text_dimensions("HELLO", letter_spacing_mm=2.0)

# Build SVG
builder = SVGBuilder(
    text="HELLO",
    font_name="DejaVu Sans",
    size_mm=30.0,
    thickness_mm=2.0
)
builder.build_svg(outlines, Path("output.svg"), width, height)
```

## Generated SVG Files

SVG files generated in this directory will be in the `.gitignore` file,
so they won't be committed to version control.

After running the examples, you can:

1. Open the SVG files in a web browser to preview
2. Import them into Inkscape for editing
3. Import them into your 3D slicer for printing

## Tips for Creating Good Examples

### Font Choice
- **Sans-serif fonts** (Arial, DejaVu Sans, Liberation Sans) work best
- **Bold variants** create thicker, stronger letters
- Avoid very thin or decorative fonts for 3D printing

### Size Guidelines
- **Small text** (10-15mm): For labels, fine details
- **Medium text** (20-30mm): General purpose
- **Large text** (40-60mm): Logos, signs

### Letter Spacing
- **0mm**: Normal, letters touching
- **1-2mm**: Good separation for individual letters
- **3-5mm**: Spaced out, artistic effect

### Thickness
- **1-2mm**: Thin, lightweight
- **2-3mm**: Standard, good strength
- **3-5mm**: Thick, very strong

## Example Workflows

### Creating a Name Tag
```bash
text2svg3d -f "Arial Bold" -s 25 -t 3 -o nametag.svg "JOHN"
```

### Creating Logo Letters
```bash
text2svg3d -f "Liberation Sans Bold" -s 40 -l 3 -t 4 -o logo.svg "ABC"
```

### Creating Numbers for Address
```bash
text2svg3d -f "DejaVu Sans Bold" -s 60 -t 5 -o house_number.svg "123"
```

### Creating Small Labels
```bash
text2svg3d -f "Arial" -s 15 -t 2 -o label.svg "ON/OFF"
```

## Testing Your SVG Files

### In Browser
Simply open the `.svg` file in any web browser to see the vector outline.

### In Inkscape
```bash
inkscape example_hello.svg
```

### In 3D Slicer (PrusaSlicer example)
1. Open PrusaSlicer
2. File → Import → Import SVG
3. Select your SVG file
4. Set the extrusion height (use the thickness value)
5. Position on build plate
6. Slice and export to printer

### Command Line SVG Viewer
If you have `eog` (Eye of GNOME) or similar:
```bash
eog example_hello.svg
```

## Troubleshooting Examples

### "No module named 'text2svg3d'"
Make sure you've installed the package:
```bash
pip install -e .
```

### "Font not found"
List available fonts and use exact name:
```bash
text2svg3d --list-fonts
```

### "Character not supported"
The font doesn't have that character. Try a different font:
```bash
text2svg3d -f "DejaVu Sans" "Your Text"
```
