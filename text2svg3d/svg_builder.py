"""SVG document builder for 3D printing."""

from pathlib import Path
from typing import List
from xml.dom import minidom

import svgwrite

from .config import SVG_NAMESPACE, SVG_UNITS
from .glyph_converter import GlyphOutline


class SVGBuilder:
    """Builds SVG documents optimized for 3D printing."""

    def __init__(
        self,
        text: str,
        font_name: str,
        size_mm: float,
        thickness_mm: float
    ) -> None:
        """
        Initialize the SVG builder.

        Args:
            text: Original text string
            font_name: Font family name used
            size_mm: Text size in millimeters
            thickness_mm: Suggested extrusion thickness
        """
        self.text = text
        self.font_name = font_name
        self.size_mm = size_mm
        self.thickness_mm = thickness_mm

    def build_svg(
        self,
        outlines: List[GlyphOutline],
        output_path: Path,
        width_mm: float,
        height_mm: float
    ) -> None:
        """
        Build and save SVG document.

        Args:
            outlines: List of glyph outlines
            output_path: Path to save SVG file
            width_mm: Total width in millimeters
            height_mm: Total height in millimeters
        """
        # Create SVG document with proper dimensions
        dwg = svgwrite.Drawing(
            str(output_path),
            size=(f"{width_mm}{SVG_UNITS}", f"{height_mm}{SVG_UNITS}"),
            viewBox=f"0 0 {width_mm} {height_mm}",
            profile='full'
        )

        # Metadata would be added here
        # (svgwrite doesn't support comments directly)

        # Add each glyph as a separate path
        x_offset = 0.0

        for idx, outline in enumerate(outlines):
            # Create path element with proper ID
            char_safe = self._sanitize_char_for_id(outline.char)
            path_id = f"letter_{char_safe}_{idx}"

            # Transform path to include x offset
            transformed_path = self._transform_path(outline.path_data, x_offset)

            # Add path element
            path = dwg.path(
                d=transformed_path,
                id=path_id,
                fill="black",
                stroke="none",
                fill_rule="evenodd"  # Important for letters with holes (O, A, B, etc.)
            )

            dwg.add(path)

            # Move to next letter position
            x_offset += outline.advance_width

        # Save the SVG
        dwg.save(pretty=True)

        # Post-process to ensure compatibility
        self._post_process_svg(output_path)

    def build_svg_with_outline(
        self,
        outlines: List[GlyphOutline],
        output_path: Path,
        width_mm: float,
        height_mm: float,
        outline_width_mm: float
    ) -> None:
        """
        Build and save SVG document with outline/stroke.

        Args:
            outlines: List of glyph outlines
            output_path: Path to save SVG file
            width_mm: Total width in millimeters
            height_mm: Total height in millimeters
            outline_width_mm: Width of the outline/stroke in millimeters
        """
        # Add padding for the outline
        padding = outline_width_mm
        total_width = width_mm + (padding * 2)
        total_height = height_mm + (padding * 2)

        # Create SVG document with proper dimensions including outline
        dwg = svgwrite.Drawing(
            str(output_path),
            size=(f"{total_width}{SVG_UNITS}", f"{total_height}{SVG_UNITS}"),
            viewBox=f"0 0 {total_width} {total_height}",
            profile='full'
        )

        # Metadata would be added here
        # (svgwrite doesn't support comments directly)

        # Add each glyph as a separate path with stroke
        x_offset = padding  # Start with padding offset

        for idx, outline in enumerate(outlines):
            # Create path element with proper ID
            char_safe = self._sanitize_char_for_id(outline.char)
            path_id = f"letter_{char_safe}_{idx}_outline"

            # Transform path to include x offset
            transformed_path = self._transform_path(outline.path_data, x_offset)

            # Add path element with stroke (outline) only, no fill
            path = dwg.path(
                d=transformed_path,
                id=path_id,
                fill="black",  # Fill the letters
                stroke="black",  # Add stroke for outline
                stroke_width=f"{outline_width_mm}{SVG_UNITS}",
                stroke_linejoin="round",  # Round corners for better 3D printing
                stroke_linecap="round",  # Round ends
                fill_rule="evenodd"
            )

            dwg.add(path)

            # Move to next letter position
            x_offset += outline.advance_width

        # Save the SVG
        dwg.save(pretty=True)

        # Post-process to ensure compatibility
        self._post_process_svg(output_path)

    def _sanitize_char_for_id(self, char: str) -> str:
        """
        Sanitize character for use in XML ID attribute.

        Args:
            char: Character to sanitize

        Returns:
            Safe string for ID
        """
        # Convert special characters to readable names
        special_chars = {
            ' ': 'space',
            '!': 'exclamation',
            '?': 'question',
            '.': 'period',
            ',': 'comma',
            ':': 'colon',
            ';': 'semicolon',
            '-': 'hyphen',
            '_': 'underscore',
            '/': 'slash',
            '\\': 'backslash',
            '(': 'lparen',
            ')': 'rparen',
            '[': 'lbracket',
            ']': 'rbracket',
            '{': 'lbrace',
            '}': 'rbrace',
        }

        if char in special_chars:
            return special_chars[char]
        elif char.isalnum():
            return char
        else:
            # Use unicode code point for other characters
            return f"u{ord(char):04x}"

    def _transform_path(self, path_data: str, x_offset: float) -> str:
        """
        Transform path data by applying x offset.

        Args:
            path_data: Original SVG path data
            x_offset: X offset to apply in mm

        Returns:
            Transformed path data
        """
        if x_offset == 0:
            return path_data

        # Split path into commands
        parts = path_data.split()
        transformed_parts = []

        i = 0
        while i < len(parts):
            part = parts[i]

            if part in ['M', 'L', 'Q', 'Z']:
                # Command letter
                transformed_parts.append(part)
                i += 1

                if part == 'Z':
                    continue

                # Process coordinates following the command
                if part == 'M' or part == 'L':
                    # Move or Line: x y
                    if i + 1 < len(parts):
                        x = float(parts[i]) + x_offset
                        y = float(parts[i + 1])
                        transformed_parts.append(f"{x:.2f}")
                        transformed_parts.append(f"{y:.2f}")
                        i += 2
                elif part == 'Q':
                    # Quadratic: cx cy x y
                    if i + 3 < len(parts):
                        cx = float(parts[i]) + x_offset
                        cy = float(parts[i + 1])
                        x = float(parts[i + 2]) + x_offset
                        y = float(parts[i + 3])
                        transformed_parts.append(f"{cx:.2f}")
                        transformed_parts.append(f"{cy:.2f}")
                        transformed_parts.append(f"{x:.2f}")
                        transformed_parts.append(f"{y:.2f}")
                        i += 4
            else:
                # Shouldn't happen with our path format, but just in case
                transformed_parts.append(part)
                i += 1

        return " ".join(transformed_parts)

    def build_svg_per_letter(
        self,
        outlines: List[GlyphOutline],
        output_path: Path,
        width_mm: float,
        height_mm: float
    ) -> List[str]:
        """
        Build and save separate SVG files for each letter.

        Args:
            outlines: List of glyph outlines
            output_path: Base path for output files
            width_mm: Total width in millimeters
            height_mm: Total height in millimeters

        Returns:
            List of created file paths
        """
        created_files = []
        x_offset = 0.0

        for idx, outline in enumerate(outlines):
            # Create filename for this letter
            char_safe = self._sanitize_char_for_id(outline.char)
            letter_path = output_path.parent / f"{output_path.stem}_lettre_{idx+1}_{char_safe}{output_path.suffix}"

            # Calculate width for this letter only
            letter_width = outline.advance_width

            # Create SVG document for this letter
            dwg = svgwrite.Drawing(
                str(letter_path),
                size=(f"{letter_width}{SVG_UNITS}", f"{height_mm}{SVG_UNITS}"),
                viewBox=f"0 0 {letter_width} {height_mm}",
                profile='full'
            )

            # Metadata would be added here
            # (svgwrite doesn't support comments directly)

            # Add the letter path (no x_offset transform needed, starts at 0)
            char_safe_id = self._sanitize_char_for_id(outline.char)
            path_id = f"letter_{char_safe_id}_{idx}"

            path = dwg.path(
                d=outline.path_data,
                id=path_id,
                fill="black",
                stroke="none",
                fill_rule="evenodd"
            )

            dwg.add(path)

            # Save the SVG
            dwg.save(pretty=True)

            # Post-process
            self._post_process_svg(letter_path)

            created_files.append(str(letter_path))

            # Move to next letter position for metadata tracking
            x_offset += outline.advance_width

        return created_files

    def _post_process_svg(self, output_path: Path) -> None:
        """
        Post-process SVG file to ensure proper formatting.

        Args:
            output_path: Path to SVG file
        """
        try:
            # Read and parse the SVG
            with open(output_path, 'r') as f:
                content = f.read()

            # Parse with minidom for pretty printing
            dom = minidom.parseString(content)

            # Write back with proper formatting
            with open(output_path, 'w') as f:
                f.write(dom.toprettyxml(indent="  ", encoding=None))

        except Exception:
            # If post-processing fails, keep original file
            pass
