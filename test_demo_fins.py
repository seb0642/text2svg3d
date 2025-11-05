#!/usr/bin/env python3
"""Script pour générer des exemples avec contours FINS."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from text2svg3d.font_manager import FontManager
from text2svg3d.glyph_converter import GlyphConverter
import svgwrite


def generate_demo_with_thin_strokes():
    """Génère des exemples avec contours FINS et visibles."""

    text = "LOGO"
    size_mm = 40.0
    spacing_mm = 2.0
    output_dir = Path.home() / "Bureau" / "ready to blender" / "demo_contours_fins"

    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"🎨 Génération de DÉMOS avec contours FINS pour '{text}'\n")
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

    # Configurations à tester - CONTOURS BEAUCOUP PLUS FINS
    configs = [
        {
            "name": "demo_reference",
            "desc": "RÉFÉRENCE : Texte noir SANS contour",
            "fill": "black",
            "stroke": "none",
            "stroke_width": 0
        },
        {
            "name": "demo_contour_rouge_0.3mm",
            "desc": "Contour rouge TRÈS FIN (0.3mm)",
            "fill": "black",
            "stroke": "red",
            "stroke_width": 0.3
        },
        {
            "name": "demo_contour_rouge_0.5mm",
            "desc": "Contour rouge FIN (0.5mm)",
            "fill": "black",
            "stroke": "red",
            "stroke_width": 0.5
        },
        {
            "name": "demo_contour_rouge_0.8mm",
            "desc": "Contour rouge MOYEN (0.8mm) ⭐",
            "fill": "black",
            "stroke": "red",
            "stroke_width": 0.8
        },
        {
            "name": "demo_contour_rouge_1.0mm",
            "desc": "Contour rouge VISIBLE (1.0mm)",
            "fill": "black",
            "stroke": "red",
            "stroke_width": 1.0
        },
        {
            "name": "demo_juste_contour_0.5mm",
            "desc": "JUSTE le contour fin (0.5mm, sans remplissage)",
            "fill": "none",
            "stroke": "red",
            "stroke_width": 0.5
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
        print(f"   ✅ {config['name']}.svg\n")

    print("=" * 70)
    print("🎉 DÉMOS CRÉÉES !\n")
    print(f"📁 Fichiers dans : {output_dir}\n")
    print("🔍 OUVREZ LES FICHIERS pour comparer :")
    print("   1. demo_reference.svg")
    print("      → Texte noir simple (sans contour)\n")
    print("   2. demo_contour_rouge_0.3mm.svg")
    print("      → Contour rouge TRÈS fin (subtil)\n")
    print("   3. demo_contour_rouge_0.5mm.svg")
    print("      → Contour rouge FIN (discret mais visible)\n")
    print("   4. demo_contour_rouge_0.8mm.svg ⭐ RECOMMANDÉ")
    print("      → Contour rouge MOYEN (bon équilibre)")
    print("      → On voit BIEN le noir ET le rouge !\n")
    print("   5. demo_contour_rouge_1.0mm.svg")
    print("      → Contour rouge VISIBLE (plus marqué)\n")
    print("   6. demo_juste_contour_0.5mm.svg")
    print("      → JUSTE le contour (effet fil de fer)\n")
    print("=" * 70)
    print("\n💡 RECOMMANDATION :")
    print("   Pour LOGO en 40mm, utilisez un contour de :")
    print("   - 0.5mm à 0.8mm pour un effet subtil ✅")
    print("   - 1.0mm maximum pour rester lisible")
    print("   - PAS 2mm ou plus (trop épais) ❌")
    print("\n📏 RÈGLE GÉNÉRALE :")
    print("   Épaisseur contour ≈ Taille texte ÷ 50")
    print("   - 40mm → 0.8mm de contour")
    print("   - 50mm → 1.0mm de contour")
    print("   - 30mm → 0.6mm de contour")
    print()


if __name__ == "__main__":
    try:
        generate_demo_with_thin_strokes()
    except Exception as e:
        print(f"\n❌ ERREUR : {e}")
        import traceback
        traceback.print_exc()
