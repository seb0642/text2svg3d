"""Glyph to vector path conversion using FreeType."""

from pathlib import Path
from typing import List, NamedTuple, Optional

import freetype

from .config import DEFAULT_COORDINATE_PRECISION, DPI


class Point(NamedTuple):
    """2D point with x, y coordinates."""
    x: float
    y: float


class GlyphOutline(NamedTuple):
    """Outline data for a single glyph."""
    path_data: str
    advance_width: float
    char: str


class GlyphConverter:
    """Converts font glyphs to SVG path data using FreeType."""

    def __init__(self, font_path: Path, size_mm: float) -> None:
        """
        Initialize the GlyphConverter.

        Args:
            font_path: Path to the TrueType/OpenType font file
            size_mm: Desired text height in millimeters

        Raises:
            FileNotFoundError: If font file does not exist
            ValueError: If size_mm is not in valid range (0.1 to 1000)
            RuntimeError: If font file cannot be loaded
        """
        # Validate font_path
        if not isinstance(font_path, Path):
            font_path = Path(font_path)

        if not font_path.exists():
            raise FileNotFoundError(f"Font file not found: {font_path}")

        if not font_path.is_file():
            raise ValueError(f"Path is not a file: {font_path}")

        # Validate size_mm
        if not isinstance(size_mm, (int, float)):
            raise TypeError(f"size_mm must be numeric, got {type(size_mm).__name__}")

        if not 0.1 <= size_mm <= 1000:
            raise ValueError(f"size_mm must be between 0.1 and 1000, got {size_mm}")

        self.font_path = font_path
        self.size_mm = size_mm

        # Try to load the font
        try:
            self.face = freetype.Face(str(font_path))
        except Exception as e:
            raise RuntimeError(f"Failed to load font file {font_path}: {e}") from e

        # Set character size (width=0 means auto, height in 1/64th points)
        # Convert mm to points: 1mm ≈ 2.83465 points
        points = size_mm * 2.83465
        self.face.set_char_size(0, int(points * 64), DPI, DPI)

        # Calculate font metrics in mm
        ascender_ratio = self.face.ascender / self.face.units_per_EM
        descender_ratio = self.face.descender / self.face.units_per_EM  # Already negative

        self.ascender_mm = ascender_ratio * self.size_mm
        self.descender_mm = descender_ratio * self.size_mm  # Negative value

        # Total height from ascender to descender
        self.total_height_mm = self.ascender_mm - self.descender_mm  # descender is negative

    def convert_text(
        self,
        text: str,
        letter_spacing_mm: float = 0.0
    ) -> List[GlyphOutline]:
        """
        Convert text string to list of glyph outlines.

        Args:
            text: Text string to convert
            letter_spacing_mm: Additional spacing between letters in mm

        Returns:
            List of GlyphOutline objects, one per character
        """
        outlines = []

        for char in text:
            try:
                outline = self._convert_char(char)
                if outline:
                    # Add letter spacing to advance width
                    outline = GlyphOutline(
                        path_data=outline.path_data,
                        advance_width=outline.advance_width + letter_spacing_mm,
                        char=outline.char
                    )
                    outlines.append(outline)
            except Exception:
                # Character not supported by font, skip it
                continue

        return outlines

    def _convert_char(self, char: str) -> Optional[GlyphOutline]:
        """
        Convert a single character to SVG path data.

        Args:
            char: Single character to convert

        Returns:
            GlyphOutline or None if character not supported
        """
        # Load the glyph for this character
        # Load with NO_SCALE to get coordinates in font units (not scaled)
        self.face.load_char(char, freetype.FT_LOAD_NO_BITMAP | freetype.FT_LOAD_NO_SCALE)

        # Get the glyph outline
        outline = self.face.glyph.outline

        if not outline:
            return None

        # Convert outline to SVG path
        path_data = self._outline_to_svg_path(outline)

        # Get advance width in mm (already in font units with NO_SCALE)
        advance_mm = self._font_units_to_mm(self.face.glyph.advance.x)

        return GlyphOutline(
            path_data=path_data,
            advance_width=advance_mm,
            char=char
        )

    def _outline_to_svg_path(self, outline) -> str:
        """
        Convert FreeType outline to SVG path data.

        Args:
            outline: FreeType glyph outline

        Returns:
            SVG path data string
        """
        points = outline.points
        tags = outline.tags
        contours = outline.contours

        path_parts = []
        start = 0

        for contour_end in contours:
            # Process each contour (closed path)
            contour_points = points[start:contour_end + 1]
            contour_tags = tags[start:contour_end + 1]

            path_parts.append(
                self._contour_to_svg_path(contour_points, contour_tags)
            )

            start = contour_end + 1

        return " ".join(path_parts)

    def _contour_to_svg_path(self, points, tags) -> str:
        """
        Convert a single contour to SVG path commands.

        Args:
            points: List of FreeType points
            tags: List of FreeType point tags

        Returns:
            SVG path string for this contour
        """
        if not points:
            return ""

        path_commands = []
        i = 0
        n = len(points)

        # Start point
        start_point = self._point_to_mm(points[0])
        path_commands.append(f"M {start_point.x:.{DEFAULT_COORDINATE_PRECISION}f} {start_point.y:.{DEFAULT_COORDINATE_PRECISION}f}")

        i = 1
        while i < n:
            tag = tags[i]

            if tag & 1:  # On-curve point
                pt = self._point_to_mm(points[i])
                path_commands.append(
                    f"L {pt.x:.{DEFAULT_COORDINATE_PRECISION}f} {pt.y:.{DEFAULT_COORDINATE_PRECISION}f}"
                )
                i += 1
            else:  # Off-curve point (control point)
                if i + 1 < n and not (tags[i + 1] & 1):
                    # Two consecutive off-curve points
                    # Create implied on-curve point between them
                    cp1 = self._point_to_mm(points[i])
                    cp2 = self._point_to_mm(points[i + 1])

                    # Implied point is midpoint
                    mid_x = (cp1.x + cp2.x) / 2
                    mid_y = (cp1.y + cp2.y) / 2

                    path_commands.append(
                        f"Q {cp1.x:.{DEFAULT_COORDINATE_PRECISION}f} {cp1.y:.{DEFAULT_COORDINATE_PRECISION}f} "
                        f"{mid_x:.{DEFAULT_COORDINATE_PRECISION}f} {mid_y:.{DEFAULT_COORDINATE_PRECISION}f}"
                    )
                    i += 1
                elif i + 1 < n:
                    # Normal quadratic curve
                    cp = self._point_to_mm(points[i])
                    end_pt = self._point_to_mm(points[i + 1])

                    path_commands.append(
                        f"Q {cp.x:.{DEFAULT_COORDINATE_PRECISION}f} {cp.y:.{DEFAULT_COORDINATE_PRECISION}f} "
                        f"{end_pt.x:.{DEFAULT_COORDINATE_PRECISION}f} {end_pt.y:.{DEFAULT_COORDINATE_PRECISION}f}"
                    )
                    i += 2
                else:
                    # Last point is control point, curve back to start
                    cp = self._point_to_mm(points[i])
                    path_commands.append(
                        f"Q {cp.x:.{DEFAULT_COORDINATE_PRECISION}f} {cp.y:.{DEFAULT_COORDINATE_PRECISION}f} "
                        f"{start_point.x:.{DEFAULT_COORDINATE_PRECISION}f} {start_point.y:.{DEFAULT_COORDINATE_PRECISION}f}"
                    )
                    i += 1

        # Close the path
        path_commands.append("Z")

        return " ".join(path_commands)

    def _point_to_mm(self, point) -> Point:
        """
        Convert FreeType point to millimeters.

        Args:
            point: FreeType point in font units

        Returns:
            Point in millimeters with Y in SVG coordinate system
        """
        # Convert coordinates
        x_mm = self._font_units_to_mm(point[0])

        # Transform Y coordinate:
        # FreeType: Y+ is up, origin at baseline
        # SVG: Y+ is down, we want ascender at Y=0
        # Formula: y_svg = ascender - y_freetype
        y_mm = self.ascender_mm - self._font_units_to_mm(point[1])

        return Point(x_mm, y_mm)

    def _font_units_to_mm(self, value: float) -> float:
        """
        Convert font units to millimeters.

        Args:
            value: Value in font units

        Returns:
            Value in millimeters
        """
        # Get units per EM (typically 1000 or 2048)
        units_per_em = self.face.units_per_EM

        # Convert to mm using the set size
        # size_mm is the height we want
        # We scale based on the units_per_em
        return (value / units_per_em) * self.size_mm

    def get_text_dimensions(self, text: str, letter_spacing_mm: float = 0.0) -> tuple[float, float]:
        """
        Calculate the dimensions of rendered text.

        Args:
            text: Text string
            letter_spacing_mm: Letter spacing in mm

        Returns:
            Tuple of (width_mm, height_mm)
        """
        outlines = self.convert_text(text, letter_spacing_mm)

        if not outlines:
            return (0.0, 0.0)

        # Width is sum of advance widths (minus last spacing)
        width = sum(o.advance_width for o in outlines) - letter_spacing_mm

        # Height is ascender + descender (total vertical span)
        height = self.total_height_mm

        return (width, height)
