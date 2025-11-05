#!/usr/bin/env python3
"""Script pour générer LOGO avec différentes épaisseurs de contour."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from text2svg3d.font_manager import FontManager
from text2svg3d.glyph_converter import GlyphConverter
from text2svg3d.svg_builder import SVGBuilder


def generate_logo_examples():
    """Génère LOGO avec différentes épaisseurs de contour."""

    # Configuration
    text = "LOGO"
    size_mm = 40.0  # Plus grand pour mieux voir les trous
    spacing_mm = 2.0
    thickness_mm = 3.0
    output_dir = Path.home() / "Bureau" / "ready to blender" / "exemples_logo"

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"🎨 Génération de '{text}' en {size_mm}mm")
    print(f"   (avec des trous dans les 'O' pour tester les contours)\n")
    print(f"📁 Dossier de sortie : {output_dir}\n")

    # Find font
    font_manager = FontManager()
    font_name = "DejaVu Sans"
    font_path = font_manager.get_font_path(font_name)

    if not font_path:
        print(f"❌ Police '{font_name}' non trouvée")
        return

    print(f"✅ Police : {font_name}")
    print(f"   Chemin : {font_path}\n")

    # Convert text to outlines
    converter = GlyphConverter(font_path, size_mm)
    outlines = converter.convert_text(text, spacing_mm)

    if not outlines:
        print("❌ Erreur : Aucun caractère converti")
        return

    # Get dimensions
    width, height = converter.get_text_dimensions(text, spacing_mm)
    print(f"📐 Dimensions : {width:.2f}mm × {height:.2f}mm\n")

    # Create builder
    builder = SVGBuilder(
        text=text,
        font_name=font_name,
        size_mm=size_mm,
        thickness_mm=thickness_mm
    )

    # 1. Generate without outline (reference)
    print("1️⃣  Génération SANS contour (référence)...")
    output_path = output_dir / f"{text}_reference.svg"
    builder.build_svg(outlines, output_path, width, height)
    print(f"   ✅ {output_path.name}")
    print(f"   → Vous verrez les trous dans les 'O' !\n")

    # 2. Generate with different outline widths
    outline_widths = [1.0, 2.0, 3.0]

    for idx, outline_width in enumerate(outline_widths, start=2):
        print(f"{idx}️⃣  Génération avec contour {outline_width}mm...")

        padding = outline_width
        total_width = width + (padding * 2)
        total_height = height + (padding * 2)

        output_path = output_dir / f"{text}_contour_{outline_width:.1f}mm.svg"
        builder.build_svg_with_outline(outlines, output_path, width, height, outline_width)

        print(f"   ✅ {output_path.name}")
        print(f"   📐 Dimensions : {total_width:.2f}mm × {total_height:.2f}mm")
        print(f"   → Les contours apparaissent AUSSI à l'intérieur des trous ! 🎯\n")

    # Summary
    print("=" * 70)
    print("🎉 GÉNÉRATION TERMINÉE !\n")
    print(f"📁 Fichiers dans : {output_dir}\n")
    print("📋 Fichiers créés :")
    print(f"   1. {text}_reference.svg           (SANS contour)")
    print(f"   2. {text}_contour_1.0mm.svg       (contour fin)")
    print(f"   3. {text}_contour_2.0mm.svg       (contour moyen) ⭐")
    print(f"   4. {text}_contour_3.0mm.svg       (contour épais)")
    print("\n" + "=" * 70)
    print("\n🔍 CE QU'IL FAUT OBSERVER :")
    print("   Dans les fichiers avec contour, regardez les deux 'O' :")
    print("   - Le CONTOUR EXTÉRIEUR autour de la lettre")
    print("   - Le CONTOUR INTÉRIEUR autour du trou !")
    print("\n   Les deux 'O' ont un trou au milieu, et le contour")
    print("   s'applique des DEUX côtés (extérieur ET intérieur) ! 🎨")
    print("\n💡 ASTUCE :")
    print("   Ouvrez les fichiers dans votre navigateur ou slicer")
    print("   pour voir l'effet en détail !")
    print()


if __name__ == "__main__":
    try:
        generate_logo_examples()
    except Exception as e:
        print(f"\n❌ ERREUR : {e}")
        import traceback
        traceback.print_exc()
