#!/usr/bin/env python3
"""Debug script to check ascender value."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from text2svg3d.font_manager import FontManager
from text2svg3d.glyph_converter import GlyphConverter

# Find font
font_manager = FontManager()
font_name = "DejaVu Sans"
font_path = font_manager.get_font_path(font_name)

print(f"Police : {font_name}")
print(f"Chemin : {font_path}\n")

# Create converter
size_mm = 30.0
converter = GlyphConverter(font_path, size_mm)

print(f"Taille demandée : {size_mm} mm")
print(f"Ascender (unités police) : {converter.face.ascender}")
print(f"Descender (unités police) : {converter.face.descender}")
print(f"Height (unités police) : {converter.face.height}")
print(f"Units per EM : {converter.face.units_per_EM}")
print()
print(f"Ascender (mm) : {converter.ascender_mm:.2f} mm")
print()

# Get raw FreeType coordinates
import freetype
converter.face.load_char('T', freetype.FT_LOAD_NO_BITMAP | freetype.FT_LOAD_NO_SCALE)
outline = converter.face.glyph.outline

if outline:
    print(f"Points bruts de 'T' (FreeType) :")
    print(f"  Nombre de points : {len(outline.points)}")

    # Calculate bbox manually
    y_values = [p[1] for p in outline.points]
    print(f"  Y min : {min(y_values)}")
    print(f"  Y max : {max(y_values)}")
    print(f"  (Ascender attendu : 1901)")
    print()

    for i, point in enumerate(outline.points[:5]):  # First 5 points
        print(f"  Point {i}: x={point[0]}, y={point[1]}")
    print()

# Convert a simple letter to see coordinates
outlines = converter.convert_text("T", 0)
if outlines:
    print(f"Chemin de 'T' (après transformation) :")
    print(f"{outlines[0].path_data[:200]}...")
