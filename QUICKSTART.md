# Quick Start Guide

Get started with text2svg3d in 5 minutes!

## 1. Install Dependencies

```bash
# Install system packages (Ubuntu/Debian)
sudo apt update
sudo apt install python3-pip python3-dev libfreetype6-dev

# Navigate to project directory
cd text2svg3d
```

## 2. Install the Application

```bash
# Install in development mode
pip install -e .
```

Or if you prefer a virtual environment:

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install
pip install -e .
```

## 3. Check Installation

```bash
# Verify it works
text2svg3d --version

# List available fonts
text2svg3d --list-fonts
```

## 4. Create Your First SVG

```bash
# Simple example
text2svg3d "HELLO"

# This creates output.svg with default settings
```

## 5. Customize Your Output

```bash
# Larger text with specific font
text2svg3d -f "Arial" -s 40 -o mytext.svg "3D PRINT"

# With letter spacing
text2svg3d -f "DejaVu Sans Bold" -s 30 -l 2 -o spaced.svg "LOGO"

# See dimensions before creating
text2svg3d -s 25 --preview "TEST"
```

## 6. Import to Your 3D Slicer

1. Open your slicer (PrusaSlicer, Cura, etc.)
2. Import the SVG file
3. Set extrusion depth (2-3mm recommended)
4. Slice and print!

## Common Commands Cheat Sheet

```bash
# List all fonts
text2svg3d --list-fonts

# Find specific font
text2svg3d --list-fonts --filter-fonts "Arial"

# Create with all options
text2svg3d -f "FONT_NAME" -s SIZE -l SPACING -t THICKNESS -o OUTPUT.svg "TEXT"

# Examples:
text2svg3d -f "Liberation Sans" -s 30 "ABC"
text2svg3d -f "DejaVu Sans Bold" -s 25 -l 1.5 -o logo.svg "LOGO"
text2svg3d --preview -s 20 "Preview Me"
```

## Troubleshooting

**Font not found?**
```bash
# List all available fonts
text2svg3d --list-fonts

# Use exact name from list
text2svg3d -f "DejaVu Sans" "TEXT"
```

**Module errors?**
```bash
# Make sure you installed dependencies
pip install -r requirements.txt
```

**Permission errors?**
```bash
# Install for user only
pip install --user -e .
```

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check [INSTALL.md](INSTALL.md) for installation troubleshooting
- See [examples/example_usage.py](examples/example_usage.py) for programmatic usage
- Experiment with different fonts and sizes!

## Tips for Best Results

1. **Font Choice**: Sans-serif fonts (Arial, DejaVu Sans) work best for 3D printing
2. **Size**: 20-40mm height works well for most applications
3. **Thickness**: 2-3mm extrusion is a good starting point
4. **Letter Spacing**: Add 1-2mm spacing for better separation
5. **Preview First**: Use `--preview` to check dimensions before creating

Happy 3D printing! 🎨
