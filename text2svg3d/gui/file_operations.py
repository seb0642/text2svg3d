"""File operations for GUI."""

import logging
from pathlib import Path
from typing import List, Optional, Tuple

from ..config import DEFAULT_OUTPUT_DIR, DEFAULT_THICKNESS_MM
from ..font_manager import FontManager
from ..glyph_converter import GlyphConverter
from ..svg_builder import SVGBuilder

logger = logging.getLogger(__name__)


class FileOperations:
    """Handles file operations for the GUI."""

    def __init__(self, font_manager: FontManager):
        """
        Initialize file operations.

        Args:
            font_manager: FontManager instance
        """
        self.font_manager = font_manager

    def calculate_font_size_for_width(
        self, font_path: Path, text: str, target_width: float, spacing: float
    ) -> Tuple[float, float]:
        """
        Calculate font size to achieve target width.

        Args:
            font_path: Path to font file
            text: Text to measure
            target_width: Target width in mm
            spacing: Letter spacing in mm

        Returns:
            Tuple of (font_size_mm, actual_height_mm)
        """
        # Start with arbitrary size to measure proportions
        test_size = 100.0
        converter = GlyphConverter(font_path, test_size)
        test_width, test_height = converter.get_text_dimensions(text, spacing)

        # Calculate ratio to achieve target width
        if test_width > 0:
            ratio = target_width / test_width
            final_size = test_size * ratio

            # Recalculate with adjusted size
            final_converter = GlyphConverter(font_path, final_size)
            final_width, final_height = final_converter.get_text_dimensions(text, spacing)

            return final_size, final_height
        else:
            return test_size, test_height

    def generate_svg(
        self,
        text: str,
        font_name: str,
        target_width: float,
        spacing: float,
        output_path: Path,
        enable_outline: bool = False,
        outline_width: float = 0.8,
        separate_letters: bool = False,
    ) -> Tuple[bool, List[str], str]:
        """
        Generate SVG file(s).

        Args:
            text: Text to convert
            font_name: Font family name
            target_width: Target width in mm
            spacing: Letter spacing in mm
            output_path: Output file path
            enable_outline: Whether to generate outline
            outline_width: Outline width in mm
            separate_letters: Whether to separate letters

        Returns:
            Tuple of (success, files_created, error_message)
        """
        try:
            # Get font path
            font_path = self.font_manager.get_font_path(font_name)
            if not font_path:
                return False, [], f"Police '{font_name}' non trouvée"

            # Calculate font size
            font_size, height = self.calculate_font_size_for_width(
                font_path, text, target_width, spacing
            )

            # Convert text
            converter = GlyphConverter(font_path, font_size)
            outlines = converter.convert_text(text, spacing)

            if not outlines:
                return False, [], "Aucun caractère n'a pu être converti"

            # Get final dimensions
            width, height = converter.get_text_dimensions(text, spacing)

            # Build SVG
            builder = SVGBuilder(
                text=text,
                font_name=font_name,
                size_mm=font_size,
                thickness_mm=DEFAULT_THICKNESS_MM,
            )

            files_created = []

            # Generate files based on options
            if separate_letters:
                files_created = builder.build_svg_per_letter(outlines, output_path, width, height)

                # Generate outline for each letter if enabled
                if enable_outline:
                    outline_files = self._generate_letter_outlines(
                        builder, outlines, files_created, width, height, outline_width
                    )
                    files_created.extend(outline_files)
            else:
                # Single file
                builder.build_svg(outlines, output_path, width, height)
                files_created = [str(output_path)]

                # Generate outline if enabled
                if enable_outline:
                    outline_path = (
                        output_path.parent / f"{output_path.stem}_contour{output_path.suffix}"
                    )
                    builder.build_svg_with_outline(
                        outlines, outline_path, width, height, outline_width
                    )
                    files_created.append(str(outline_path))

            logger.info(f"Generated {len(files_created)} SVG file(s)")
            return True, files_created, ""

        except Exception as e:
            logger.error(f"Failed to generate SVG: {e}")
            return False, [], str(e)

    def _generate_letter_outlines(
        self,
        builder: SVGBuilder,
        outlines: List,
        letter_files: List[str],
        width: float,
        height: float,
        outline_width: float,
    ) -> List[str]:
        """Generate outline files for individual letters."""
        outline_files = []

        for file_path in letter_files:
            file_path_obj = Path(file_path)
            outline_path = (
                file_path_obj.parent / f"{file_path_obj.stem}_contour{file_path_obj.suffix}"
            )

            # Get letter index from filename
            try:
                letter_idx = int(file_path_obj.stem.split("_")[2]) - 1
                letter_outline = [outlines[letter_idx]]
                letter_width = outlines[letter_idx].advance_width

                builder.build_svg_with_outline(
                    letter_outline, outline_path, letter_width, height, outline_width
                )
                outline_files.append(str(outline_path))
            except (IndexError, ValueError) as e:
                logger.warning(f"Failed to generate outline for {file_path}: {e}")
                continue

        return outline_files

    def format_success_message(
        self,
        text: str,
        files_created: List[str],
        width: float,
        height: float,
        separate_letters: bool,
        enable_outline: bool,
        outline_width: float,
    ) -> str:
        """
        Format success message for user.

        Args:
            text: Original text
            files_created: List of created files
            width: Width in mm
            height: Height in mm
            separate_letters: Whether letters were separated
            enable_outline: Whether outline was generated
            outline_width: Outline width in mm

        Returns:
            Formatted success message
        """
        if separate_letters:
            num_letters = len(files_created) // (2 if enable_outline else 1)

            if enable_outline:
                return (
                    f"Fichiers SVG créés avec succès !\n\n"
                    f"{len(files_created)} fichiers créés :\n"
                    f"- {num_letters} fichiers de lettres\n"
                    f"- {num_letters} fichiers de contour\n\n"
                    f'Texte : "{text}"\n'
                    f"Dimensions : {width:.2f}mm × {height:.2f}mm\n"
                    f"Épaisseur contour : {outline_width:.1f}mm\n\n"
                    f"Dans votre slicer 3D :\n"
                    f"1. Importez chaque fichier de lettre avec une couleur différente\n"
                    f"2. Importez les contours si souhaité\n"
                    f"→ Impression multi-couleur ! 🌈"
                )
            else:
                return (
                    f"Fichiers SVG créés avec succès !\n\n"
                    f"{len(files_created)} fichiers de lettres créés\n"
                    f'Texte : "{text}"\n'
                    f"Dimensions : {width:.2f}mm × {height:.2f}mm\n\n"
                    f"Dans votre slicer 3D :\n"
                    f"Importez chaque fichier avec une couleur différente\n"
                    f"pour un effet multi-couleur ! 🌈"
                )
        elif len(files_created) == 1:
            return (
                f"Fichier SVG créé avec succès !\n\n"
                f"Fichier : {files_created[0]}\n"
                f"Dimensions : {width:.2f}mm × {height:.2f}mm\n\n"
                f"Vous pouvez maintenant l'importer dans votre slicer 3D."
            )
        else:
            return (
                f"Fichiers SVG créés avec succès !\n\n"
                f"Texte : {files_created[0]}\n"
                f"Contour : {files_created[1]}\n"
                f"Dimensions : {width:.2f}mm × {height:.2f}mm\n"
                f"Épaisseur contour : {outline_width:.1f}mm\n\n"
                f"Importez les deux fichiers dans votre slicer 3D\n"
                f"pour un effet multi-couleur !"
            )

    def sanitize_filename(self, text: str, max_length: int = 50) -> str:
        """
        Sanitize text for use as filename.

        Args:
            text: Text to sanitize
            max_length: Maximum length

        Returns:
            Sanitized filename (without extension)
        """
        safe_text = text.strip()

        # Replace invalid characters
        invalid_chars = '<>:"/\\|?*'
        for char in invalid_chars:
            safe_text = safe_text.replace(char, "_")

        # Replace spaces
        safe_text = safe_text.replace(" ", "_")

        # Limit length
        if len(safe_text) > max_length:
            safe_text = safe_text[:max_length]

        # Ensure not empty
        if not safe_text:
            safe_text = "output"

        return safe_text

    def get_output_path(self, text: str) -> Path:
        """
        Get output path for text.

        Args:
            text: Text being converted

        Returns:
            Path object for output file
        """
        filename = self.sanitize_filename(text)
        return DEFAULT_OUTPUT_DIR / f"{filename}.svg"

    def ensure_output_directory(self) -> bool:
        """
        Ensure output directory exists.

        Returns:
            True if directory exists or was created
        """
        try:
            DEFAULT_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
            return True
        except Exception as e:
            logger.error(f"Failed to create output directory: {e}")
            return False
