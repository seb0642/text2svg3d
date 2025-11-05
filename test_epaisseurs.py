#!/usr/bin/env python3
"""Script de test pour générer des exemples avec différentes épaisseurs de contour."""

import sys
from pathlib import Path

# Add the module to path
sys.path.insert(0, str(Path(__file__).parent))

from text2svg3d.font_manager import FontManager
from text2svg3d.glyph_converter import GlyphConverter
from text2svg3d.svg_builder import SVGBuilder


def generate_examples():
    """Génère des exemples avec différentes épaisseurs de contour."""

    # Configuration
    text = "TEST"
    size_mm = 30.0
    spacing_mm = 2.0
    thickness_mm = 3.0
    output_dir = Path.home() / "Bureau" / "ready to blender" / "exemples_epaisseurs"

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"🎨 Génération d'exemples pour '{text}' en {size_mm}mm\n")
    print(f"📁 Dossier de sortie : {output_dir}\n")

    # Find font
    font_manager = FontManager()
    font_name = "DejaVu Sans"  # Police par défaut
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
    print(f"📐 Dimensions du texte : {width:.2f}mm × {height:.2f}mm\n")

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
    print(f"   ✅ Créé : {output_path.name}")
    print(f"   📐 Dimensions : {width:.2f}mm × {height:.2f}mm\n")

    # 2. Generate with different outline widths
    outline_widths = [0.5, 1.0, 1.5, 2.0, 3.0, 5.0]

    for idx, outline_width in enumerate(outline_widths, start=2):
        print(f"{idx}️⃣  Génération avec contour {outline_width}mm...")

        # Calculate padded dimensions
        padding = outline_width
        total_width = width + (padding * 2)
        total_height = height + (padding * 2)

        output_path = output_dir / f"{text}_contour_{outline_width:.1f}mm.svg"
        builder.build_svg_with_outline(outlines, output_path, width, height, outline_width)

        print(f"   ✅ Créé : {output_path.name}")
        print(f"   📐 Dimensions : {total_width:.2f}mm × {total_height:.2f}mm")
        print(f"   📏 Padding : +{padding * 2:.2f}mm\n")

    # Summary
    print("=" * 60)
    print("🎉 GÉNÉRATION TERMINÉE !\n")
    print(f"📁 Tous les fichiers sont dans :")
    print(f"   {output_dir}\n")
    print("📋 Fichiers créés :")
    print(f"   1. {text}_reference.svg              (SANS contour)")
    print(f"   2. {text}_contour_0.5mm.svg          (contour fin)")
    print(f"   3. {text}_contour_1.0mm.svg          (contour léger)")
    print(f"   4. {text}_contour_1.5mm.svg          (contour moyen) ⭐")
    print(f"   5. {text}_contour_2.0mm.svg          (contour visible)")
    print(f"   6. {text}_contour_3.0mm.svg          (contour épais)")
    print(f"   7. {text}_contour_5.0mm.svg          (contour très épais)")
    print("\n" + "=" * 60)
    print("\n🔍 POUR COMPARER :")
    print("   1. Ouvrez votre slicer 3D")
    print("   2. Importez chaque fichier un par un")
    print("   3. Comparez l'épaisseur des contours")
    print("   4. Choisissez votre préféré !")
    print("\n💡 ASTUCE :")
    print("   Importez-les tous et affichez-les côte à côte")
    print("   pour voir la progression ! 🌈")
    print()


if __name__ == "__main__":
    try:
        generate_examples()
    except Exception as e:
        print(f"\n❌ ERREUR : {e}")
        import traceback
        traceback.print_exc()
