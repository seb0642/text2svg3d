"""Export SVG to other formats (PDF, DXF, PNG)."""

import logging
from pathlib import Path
from typing import Optional, Tuple

logger = logging.getLogger(__name__)


def export_to_pdf(svg_path: Path, pdf_path: Optional[Path] = None) -> Tuple[bool, str]:
    """
    Export SVG file to PDF.

    Args:
        svg_path: Path to input SVG file
        pdf_path: Path to output PDF file (default: same name with .pdf extension)

    Returns:
        Tuple of (success: bool, message: str)
    """
    if pdf_path is None:
        pdf_path = svg_path.with_suffix(".pdf")

    try:
        # Try cairosvg first (best quality)
        try:
            import cairosvg

            cairosvg.svg2pdf(url=str(svg_path), write_to=str(pdf_path))
            logger.info(f"PDF exported successfully using cairosvg: {pdf_path}")
            return True, f"PDF créé : {pdf_path.name}"

        except ImportError:
            pass

        # Fallback to svglib + reportlab
        try:
            from reportlab.graphics import renderPDF
            from svglib.svglib import svg2rlg

            drawing = svg2rlg(str(svg_path))
            if drawing:
                renderPDF.drawToFile(drawing, str(pdf_path))
                logger.info(f"PDF exported successfully using svglib: {pdf_path}")
                return True, f"PDF créé : {pdf_path.name}"
            else:
                return False, "Impossible de convertir le SVG"

        except ImportError:
            return (
                False,
                "Export PDF non disponible. Installez: pip install cairosvg ou pip install svglib reportlab",
            )

    except Exception as e:
        logger.error(f"PDF export failed: {e}")
        return False, f"Erreur lors de l'export PDF : {e}"


def export_to_png(
    svg_path: Path, png_path: Optional[Path] = None, dpi: int = 300
) -> Tuple[bool, str]:
    """
    Export SVG file to PNG (rasterized).

    Args:
        svg_path: Path to input SVG file
        png_path: Path to output PNG file (default: same name with .png extension)
        dpi: Resolution in DPI (default: 300 for print quality)

    Returns:
        Tuple of (success: bool, message: str)
    """
    if png_path is None:
        png_path = svg_path.with_suffix(".png")

    try:
        # Try cairosvg (best quality)
        try:
            import cairosvg

            cairosvg.svg2png(url=str(svg_path), write_to=str(png_path), dpi=dpi)
            logger.info(f"PNG exported successfully using cairosvg at {dpi} DPI: {png_path}")
            return True, f"PNG créé : {png_path.name} ({dpi} DPI)"

        except ImportError:
            pass

        # Fallback to Pillow + svglib
        try:
            from PIL import Image
            from reportlab.graphics import renderPM
            from svglib.svglib import svg2rlg

            drawing = svg2rlg(str(svg_path))
            if drawing:
                renderPM.drawToFile(drawing, str(png_path), fmt="PNG", dpi=dpi)
                logger.info(f"PNG exported successfully using svglib+Pillow: {png_path}")
                return True, f"PNG créé : {png_path.name} ({dpi} DPI)"
            else:
                return False, "Impossible de convertir le SVG"

        except ImportError:
            return (
                False,
                "Export PNG non disponible. Installez: pip install cairosvg ou pip install svglib reportlab pillow",
            )

    except Exception as e:
        logger.error(f"PNG export failed: {e}")
        return False, f"Erreur lors de l'export PNG : {e}"


def export_to_dxf(svg_path: Path, dxf_path: Optional[Path] = None) -> Tuple[bool, str]:
    """
    Export SVG file to DXF (CAD format).

    Note: This is a basic implementation that converts SVG paths to DXF polylines.
    Complex SVG features may not be fully supported.

    Args:
        svg_path: Path to input SVG file
        dxf_path: Path to output DXF file (default: same name with .dxf extension)

    Returns:
        Tuple of (success: bool, message: str)
    """
    if dxf_path is None:
        dxf_path = svg_path.with_suffix(".dxf")

    try:
        import ezdxf
        from xml.etree import ElementTree as ET

        # Parse SVG
        tree = ET.parse(str(svg_path))
        root = tree.getroot()

        # Create DXF document
        doc = ezdxf.new("R2010")
        msp = doc.modelspace()

        # SVG namespace
        ns = {"svg": "http://www.w3.org/2000/svg"}

        # Extract paths from SVG
        paths_converted = 0
        for path_elem in root.findall(".//svg:path", ns):
            d_attr = path_elem.get("d")
            if d_attr:
                # Parse path data (simplified - handles M, L, Z commands)
                points = []
                commands = d_attr.replace(",", " ").split()
                i = 0
                current_x, current_y = 0.0, 0.0

                while i < len(commands):
                    cmd = commands[i]

                    if cmd == "M" and i + 2 < len(commands):
                        # MoveTo
                        try:
                            current_x = float(commands[i + 1])
                            current_y = float(commands[i + 2])
                            points = [(current_x, current_y)]
                            i += 3
                        except ValueError:
                            i += 1

                    elif cmd == "L" and i + 2 < len(commands):
                        # LineTo
                        try:
                            current_x = float(commands[i + 1])
                            current_y = float(commands[i + 2])
                            points.append((current_x, current_y))
                            i += 3
                        except ValueError:
                            i += 1

                    elif cmd == "Z" or cmd == "z":
                        # ClosePath
                        if points and len(points) > 1:
                            points.append(points[0])  # Close the path
                            # Create polyline in DXF
                            msp.add_lwpolyline(points, close=True)
                            paths_converted += 1
                        points = []
                        i += 1

                    else:
                        # Skip unsupported commands (Q, C, etc.)
                        i += 1

                # Add final polyline if not closed
                if points and len(points) > 1:
                    msp.add_lwpolyline(points, close=False)
                    paths_converted += 1

        # Save DXF
        doc.saveas(str(dxf_path))
        logger.info(f"DXF exported successfully: {dxf_path} ({paths_converted} paths converted)")
        return True, f"DXF créé : {dxf_path.name} ({paths_converted} tracés)"

    except ImportError:
        return False, "Export DXF non disponible. Installez: pip install ezdxf"

    except Exception as e:
        logger.error(f"DXF export failed: {e}")
        return False, f"Erreur lors de l'export DXF : {e}"


def get_available_exporters() -> dict:
    """
    Check which exporters are available based on installed dependencies.

    Returns:
        Dictionary with format names and their availability status
    """
    available = {
        "pdf": False,
        "png": False,
        "dxf": False,
    }

    # Check PDF
    try:
        import cairosvg

        available["pdf"] = True
    except ImportError:
        try:
            from svglib.svglib import svg2rlg
            from reportlab.graphics import renderPDF

            available["pdf"] = True
        except ImportError:
            pass

    # Check PNG
    try:
        import cairosvg

        available["png"] = True
    except ImportError:
        try:
            from svglib.svglib import svg2rlg
            from reportlab.graphics import renderPM
            from PIL import Image

            available["png"] = True
        except ImportError:
            pass

    # Check DXF
    try:
        import ezdxf

        available["dxf"] = True
    except ImportError:
        pass

    return available
