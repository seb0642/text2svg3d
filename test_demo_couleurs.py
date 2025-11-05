#!/usr/bin/env python3
"""Script pour générer des exemples VISUELS avec contours colorés."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from text2svg3d.font_manager import FontManager
from text2svg3d.glyph_converter import GlyphConverter
import svgwrite


def generate_demo_with_colors():
    """Génère des exemples avec contours COLORÉS pour visualisation."""

    text = "LOGO"
    size_mm = 40.0
    spacing_mm = 2.0
    output_dir = Path.home() / "Bureau" / "ready to blender" / "demo_couleurs"

    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"🎨 Génération de DÉMOS VISUELLES pour '{text}'\n")
    print(f"📁 Dossier : {output_dir}\n")

    # Find font
    font_manager = FontManager()
    font_name = "DejaVu Sans"
    font_path = font_manager.get_font_path(font_name)

    if not font_path:
        print(f"❌ Police '{font_name}' non trouvée")
        return

    # Convert text
    converter = GlyphConverter(font_path, size_mm)
    outlines = converter.convert_text(text, spacing_mm)
    width, height = converter.get_text_dimensions(text, spacing_mm)

    print(f"📐 Dimensions : {width:.2f}mm × {height:.2f}mm\n")

    # Configurations à tester
    configs = [
        {
            "name": "demo_sans_contour",
            "desc": "SANS contour (texte noir simple)",
            "fill": "black",
            "stroke": "none",
            "stroke_width": 0
        },
        {
            "name": "demo_contour_rouge_1mm",
            "desc": "Texte noir + contour ROUGE 1mm",
            "fill": "black",
            "stroke": "red",
            "stroke_width": 1.0
        },
        {
            "name": "demo_contour_rouge_2mm",
            "desc": "Texte noir + contour ROUGE 2mm",
            "fill": "black",
            "stroke": "red",
            "stroke_width": 2.0
        },
        {
            "name": "demo_contour_bleu_2mm",
            "desc": "Texte blanc + contour BLEU 2mm",
            "fill": "white",
            "stroke": "blue",
            "stroke_width": 2.0
        },
        {
            "name": "demo_juste_contour_rouge_2mm",
            "desc": "JUSTE le contour ROUGE (pas de remplissage)",
            "fill": "none",
            "stroke": "red",
            "stroke_width": 2.0
        }
    ]

    for idx, config in enumerate(configs, start=1):
        print(f"{idx}️⃣  {config['desc']}...")

        # Calculate dimensions with padding if stroke
        if config['stroke_width'] > 0:
            padding = config['stroke_width']
            total_width = width + (padding * 2)
            total_height = height + (padding * 2)
            x_offset = padding
        else:
            total_width = width
            total_height = height
            x_offset = 0

        # Create SVG
        output_path = output_dir / f"{config['name']}.svg"
        dwg = svgwrite.Drawing(
            str(output_path),
            size=(f"{total_width}mm", f"{total_height}mm"),
            viewBox=f"0 0 {total_width} {total_height}",
            profile='full'
        )

        # Add white background for visibility
        if config['fill'] == "white":
            dwg.add(dwg.rect(
                insert=(0, 0),
                size=(f"{total_width}mm", f"{total_height}mm"),
                fill="lightgray"
            ))

        # Add each glyph
        current_x = x_offset
        for glyph_idx, outline in enumerate(outlines):
            # Transform path
            parts = outline.path_data.split()
            transformed_parts = []
            i = 0
            while i < len(parts):
                part = parts[i]
                if part in ['M', 'L', 'Q', 'Z']:
                    transformed_parts.append(part)
                    i += 1
                    if part == 'Z':
                        continue
                    if part in ['M', 'L'] and i + 1 < len(parts):
                        x = float(parts[i]) + current_x
                        y = float(parts[i + 1])
                        transformed_parts.append(f"{x:.2f}")
                        transformed_parts.append(f"{y:.2f}")
                        i += 2
                    elif part == 'Q' and i + 3 < len(parts):
                        cx = float(parts[i]) + current_x
                        cy = float(parts[i + 1])
                        x = float(parts[i + 2]) + current_x
                        y = float(parts[i + 3])
                        transformed_parts.append(f"{cx:.2f}")
                        transformed_parts.append(f"{cy:.2f}")
                        transformed_parts.append(f"{x:.2f}")
                        transformed_parts.append(f"{y:.2f}")
                        i += 4
                else:
                    transformed_parts.append(part)
                    i += 1

            transformed_path = " ".join(transformed_parts)

            # Add path with colors
            path = dwg.path(
                d=transformed_path,
                fill=config['fill'],
                stroke=config['stroke'],
                fill_rule="evenodd"
            )

            if config['stroke_width'] > 0:
                path['stroke-width'] = f"{config['stroke_width']}mm"
                path['stroke-linejoin'] = "round"
                path['stroke-linecap'] = "round"

            dwg.add(path)
            current_x += outline.advance_width

        dwg.save(pretty=True)
        print(f"   ✅ {config['name']}.svg")
        print(f"   → {config['desc']}\n")

    print("=" * 70)
    print("🎉 DÉMOS CRÉÉES !\n")
    print(f"📁 Fichiers dans : {output_dir}\n")
    print("🔍 OUVREZ LES FICHIERS pour voir :")
    print("   1. demo_sans_contour.svg")
    print("      → Texte noir simple (référence)\n")
    print("   2. demo_contour_rouge_1mm.svg")
    print("      → Texte noir + contour rouge fin\n")
    print("   3. demo_contour_rouge_2mm.svg ⭐")
    print("      → Texte noir + contour rouge visible")
    print("      → REGARDEZ les O : contour extérieur ET intérieur !\n")
    print("   4. demo_contour_bleu_2mm.svg")
    print("      → Texte blanc + contour bleu (sur fond gris)\n")
    print("   5. demo_juste_contour_rouge_2mm.svg")
    print("      → SEULEMENT le contour rouge (pas de remplissage)")
    print("      → On voit juste les bordures !\n")
    print("=" * 70)
    print("\n💡 POUR L'IMPRESSION 3D :")
    print("   Dans votre slicer, vous importerez :")
    print("   - Un fichier pour le TEXTE (couleur 1)")
    print("   - Un fichier pour le CONTOUR (couleur 2)")
    print("   Et vous assignerez les couleurs que vous voulez !")
    print()


if __name__ == "__main__":
    try:
        generate_demo_with_colors()
    except Exception as e:
        print(f"\n❌ ERREUR : {e}")
        import traceback
        traceback.print_exc()
