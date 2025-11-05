"""Preview components for GUI."""

import logging
import tkinter as tk
from tkinter import font as tkfont
from typing import Optional

logger = logging.getLogger(__name__)


class VisualPreview:
    """Manages visual preview canvas."""

    def __init__(self, parent: tk.Widget, width: int = 700, height: int = 100):
        """Initialize visual preview."""
        self.canvas = tk.Canvas(parent, height=height, bg="white", relief=tk.SUNKEN, borderwidth=2)
        self.canvas.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=5, pady=5)
        self.width = width
        self.height = height

    def clear(self) -> None:
        """Clear the canvas."""
        self.canvas.delete("all")
        self.canvas.update_idletasks()

    def show_placeholder(self, text: str = "Entrez du texte pour voir l'aperçu...") -> None:
        """Show placeholder text."""
        self.clear()
        self.canvas.create_text(
            10, self.height // 2, text=text, anchor=tk.W, font=("Arial", 12), fill="gray"
        )

    def render_text(
        self,
        text: str,
        font_name: str,
        target_width: float,
        spacing_mm: float = 0.0,
    ) -> None:
        """
        Render text preview with font.

        Args:
            text: Text to render
            font_name: Font name to use
            target_width: Target width in mm
            spacing_mm: Letter spacing in mm
        """
        try:
            self.clear()

            if not text:
                self.show_placeholder()
                return

            # Get available tkinter fonts
            available_tk_fonts = tkfont.families()

            # Try to find matching font
            tk_font_name = self._find_matching_font(font_name, available_tk_fonts)

            # Calculate font size for preview
            preview_font_size = self._calculate_preview_size(target_width)

            # Create font
            display_font = tkfont.Font(family=tk_font_name, size=preview_font_size)

            # Get canvas dimensions
            canvas_width = self.canvas.winfo_width()
            if canvas_width <= 1:
                canvas_width = self.width

            # Calculate spacing in pixels
            spacing_pixels = int(spacing_mm * 2)

            # Measure character widths
            char_widths = [display_font.measure(char) for char in text]
            total_width = sum(char_widths) + spacing_pixels * max(0, len(text) - 1)

            # Center the text
            x_start = (canvas_width - total_width) // 2
            y_pos = self.height // 2

            # Draw each character with spacing
            current_x = x_start
            for i, char in enumerate(text):
                self.canvas.create_text(
                    current_x, y_pos, text=char, font=display_font, fill="black", anchor=tk.W
                )
                current_x += char_widths[i] + spacing_pixels

                # Draw spacing indicator if spacing > 0
                if spacing_mm > 0 and i < len(text) - 1:
                    line_x = current_x - spacing_pixels // 2
                    self.canvas.create_line(
                        line_x,
                        y_pos - 5,
                        line_x,
                        y_pos + 5,
                        fill="lightblue",
                        width=1,
                        dash=(2, 2),
                    )

            # Add font name if using fallback
            if tk_font_name == "TkDefaultFont":
                self.canvas.create_text(
                    canvas_width // 2,
                    self.height - 15,
                    text=f"(Aperçu approximatif - police finale: {font_name})",
                    font=("Arial", 8),
                    fill="gray",
                    anchor=tk.CENTER,
                )

        except Exception as e:
            logger.error(f"Failed to render preview: {e}")
            self.clear()
            self.canvas.create_text(
                10,
                self.height // 2,
                text=f"Erreur d'aperçu: {str(e)}",
                anchor=tk.W,
                font=("Arial", 10),
                fill="red",
            )

    def _find_matching_font(self, font_name: str, available_fonts: tuple) -> str:
        """Find matching tkinter font."""
        # Try exact match
        if font_name in available_fonts:
            return font_name

        # Try base name (remove Bold, Regular, etc.)
        base_name = font_name.split()[0]
        for tk_font in available_fonts:
            if base_name.lower() in tk_font.lower():
                return tk_font

        # Fallback to default
        return "TkDefaultFont"

    def _calculate_preview_size(self, target_width: float) -> int:
        """Calculate preview font size from target width."""
        # Scale: 5mm → 12pt, 180mm → 90pt
        return max(12, min(90, int(target_width * 0.5)))


class DimensionsPreview:
    """Manages dimensions preview text."""

    def __init__(self, parent: tk.Widget):
        """Initialize dimensions preview."""
        self.preview_var = tk.StringVar(value="")
        self.label = tk.Label(
            parent, textvariable=self.preview_var, font=("Courier", 10), justify=tk.LEFT
        )
        self.label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

    def update_dimensions(
        self,
        text: str,
        font_name: str,
        width: float,
        height: float,
        spacing: float,
        font_size: float,
    ) -> None:
        """Update dimensions preview."""
        preview_text = (
            f'Texte : "{text}"\n'
            f"Police : {font_name}\n"
            f"Largeur finale : {width:.1f}mm\n"
            f"Hauteur finale : {height:.2f}mm\n"
            f"Espacement : {spacing:.1f}mm entre les lettres\n"
            f"Caractères : {len(text)}\n"
            f"(Taille de police calculée : {font_size:.1f}mm)"
        )
        self.preview_var.set(preview_text)

    def show_error(self, message: str) -> None:
        """Show error message."""
        self.preview_var.set(f"Erreur : {message}")

    def show_placeholder(self, message: str = "Entrez du texte pour voir l'aperçu") -> None:
        """Show placeholder message."""
        self.preview_var.set(message)
