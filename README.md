# text2svg3d

Convert text to SVG files optimized for 3D printing using system fonts.

## 🖥️ Interface Graphique Disponible !

**Nouveau !** Une interface graphique facile à utiliser est maintenant disponible.

### Lancement Rapide (Sans Installation)

```bash
# Installer les dépendances
pip3 install --user fonttools freetype-py svgwrite

# Lancer l'interface graphique
./LANCER-GUI.sh
# ou directement :
python3 text2svg3d-gui.py
```

📖 **[Guide Complet de l'Interface Graphique](GUI_GUIDE.md)**

### 🎨 Impression 3D Multi-Couleur

**Générez des fichiers de contour** pour créer des impressions 3D en deux couleurs !
📖 **[Guide du Contour](CONTOUR-3D.md)**

**Séparez chaque lettre** pour des impressions arc-en-ciel ! 🌈
📖 **[Guide Lettres Séparées](LETTRES-SEPAREES.md)**

---

## Features

- Uses TrueType/OpenType fonts installed on your system
- Generates vector outlines (no font references)
- Optimized for 3D printing with closed paths
- **Graphical user interface (GUI) with tkinter** ✨
- **Outline generation for multi-color 3D printing** ✨
- **Separate letters (one file per letter for rainbow printing)** ✨ NEW!
- Command-line interface with intuitive options
- Supports custom font sizes, letter spacing, and thickness
- Preview dimensions before exporting
- Manual parameter entry via keyboard
- Automatic filename generation based on text

## Installation

### Quick Install

```bash
cd text2svg3d
pip install -e .
```

### Manual Install

```bash
cd text2svg3d
pip install -r requirements.txt
```

Then run with:
```bash
python -m text2svg3d "Your Text"
```

## Requirements

- Python 3.10 or higher
- Linux system (tested on Ubuntu/Debian)
- System fonts (TrueType or OpenType)

## Usage

### Basic Usage

```bash
# Convert text using default font (DejaVu Sans)
text2svg3d "Hello"

# Specify a font
text2svg3d -f "Arial" "ABC"

# Set custom size (in millimeters)
text2svg3d -f "Liberation Sans" -s 30 "LOGO"
```

### Advanced Options

```bash
# Full example with all options
text2svg3d -f "DejaVu Sans Bold" -s 25 -l 2 -t 3 -o logo.svg --preview "LOGO"
```

### List Available Fonts

```bash
# List all fonts
text2svg3d --list-fonts

# Filter fonts by pattern
text2svg3d --list-fonts --filter-fonts "Arial"
text2svg3d --list-fonts --filter-fonts "Liberation.*Bold"
```

### Command-Line Options

```
text2svg3d [OPTIONS] "TEXT"

Positional Arguments:
  text                  Text to convert to SVG

Options:
  -f, --font FONT       Font family name (default: DejaVu Sans)
  -s, --size SIZE       Text height in mm (default: 20)
  -o, --output FILE     Output SVG file (default: output.svg)
  -t, --thickness NUM   Suggested extrusion thickness in mm (default: 2)
  -l, --letter-spacing N Letter spacing in mm (default: 0)
  --list-fonts          List all available system fonts
  --filter-fonts REGEX  Filter fonts by regex pattern
  --preview             Display SVG dimensions and info
  -v, --verbose         Verbose output for debugging
  --version             Show version and exit
  -h, --help            Show help message and exit
```

## Examples

### Create Text for 3D Printing

```bash
# Create "ABC" in Arial, 30mm tall
text2svg3d -f "Arial" -s 30 -o abc.svg "ABC"

# Create logo with custom spacing
text2svg3d -f "Liberation Sans Bold" -s 25 -l 2 -o logo.svg "LOGO"

# Preview dimensions before saving
text2svg3d -f "DejaVu Sans" -s 20 --preview -o test.svg "Test"
```

### Find the Right Font

```bash
# List all fonts
text2svg3d --list-fonts

# Find Arial variants
text2svg3d --list-fonts --filter-fonts "Arial"

# Find bold fonts
text2svg3d --list-fonts --filter-fonts "Bold"
```

## Workflow: SVG to 3D Print

1. **Generate SVG**: Use text2svg3d to create your text
   ```bash
   text2svg3d -f "Arial" -s 30 -t 2 -o mytext.svg "HELLO"
   ```

2. **Import to Slicer**: Open the SVG in your 3D slicer software
   - PrusaSlicer: File → Import → Import SVG
   - Cura: Plugins → SVG Import
   - Other slicers: Check documentation

3. **Extrude**: Set the extrusion depth (use the `-t` value as reference)

4. **Slice and Print**: Configure your print settings and slice

5. **Print**: Send to your 3D printer

## SVG Output Format

The generated SVG files are optimized for 3D printing:

- **Closed paths**: All paths end with 'Z' command
- **Absolute coordinates**: No relative positioning
- **Real units**: Dimensions in millimeters
- **No transformations**: All transformations applied directly
- **Proper fill-rule**: Uses `fill-rule="evenodd"` for letters with holes (O, A, B, etc.)
- **Metadata**: Includes font name, size, and text in comments

## Known Limitations

- Only supports characters available in the selected font
- Complex fonts with many control points may be slow
- No support for font ligatures or advanced typography
- No automatic emoji support (depends on font)
- Text is always rendered horizontally (no vertical text)

## Troubleshooting

### Font Not Found

```bash
# List available fonts
text2svg3d --list-fonts

# Use exact font name from the list
text2svg3d -f "DejaVu Sans" "Text"
```

### Characters Not Appearing

The font may not support those characters. Try a different font:
```bash
text2svg3d -f "DejaVu Sans" "Text"  # Good Unicode support
```

### SVG Not Importing in Slicer

- Make sure your slicer supports SVG import
- Check that the SVG file is not empty
- Try a different font or simpler text
- Use `--verbose` flag to see detailed error messages

## Development

### Project Structure

```
text2svg3d/
├── text2svg3d/
│   ├── __init__.py
│   ├── __main__.py        # CLI entry point
│   ├── config.py          # Configuration constants
│   ├── font_manager.py    # Font scanning and management
│   ├── glyph_converter.py # Glyph to vector conversion
│   └── svg_builder.py     # SVG document generation
├── tests/
├── setup.py
├── requirements.txt
└── README.md
```

### Running Tests

```bash
# Install in development mode
pip install -e .

# Run basic tests
text2svg3d --list-fonts
text2svg3d -v -o test.svg "Test"
```

## License

MIT License - feel free to use this for any purpose.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Credits

Built with:
- [fontTools](https://github.com/fonttools/fonttools) - Font file parsing
- [freetype-py](https://github.com/rougier/freetype-py) - Glyph rendering
- [svgwrite](https://github.com/mozman/svgwrite) - SVG generation

## Support

For issues, questions, or feature requests, please open an issue on GitHub.
