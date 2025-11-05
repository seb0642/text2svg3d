"""Graphical User Interface for text2svg3d using tkinter."""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, font as tkfont
from pathlib import Path
from typing import Optional

from .font_manager import FontManager
from .glyph_converter import GlyphConverter
from .svg_builder import SVGBuilder
from .config import (
    DEFAULT_SIZE_MM,
    DEFAULT_THICKNESS_MM,
    DEFAULT_LETTER_SPACING_MM,
    DEFAULT_OUTPUT_FILE,
    DEFAULT_OUTPUT_DIR,
)


class Text2SVG3D_GUI:
    """Main GUI application window."""

    def __init__(self, root: tk.Tk) -> None:
        """
        Initialize the GUI.

        Args:
            root: The tkinter root window
        """
        self.root = root
        self.root.title("text2svg3d - Convertisseur Texte vers SVG pour Impression 3D")
        self.root.geometry("750x700")
        self.root.resizable(True, True)

        # Data
        self.font_manager = FontManager(use_cache=True)
        self.all_fonts = []
        self.filtered_fonts = []
        self.current_font_path: Optional[Path] = None

        # Variables
        self.text_var = tk.StringVar(value="HELLO")
        self.font_var = tk.StringVar()
        self.filter_var = tk.StringVar()
        self.size_var = tk.DoubleVar(value=DEFAULT_SIZE_MM)
        self.spacing_var = tk.DoubleVar(value=DEFAULT_LETTER_SPACING_MM)
        self.enable_outline_var = tk.BooleanVar(value=False)
        self.outline_width_var = tk.DoubleVar(value=0.8)  # Valeur par défaut optimale
        self.separate_letters_var = tk.BooleanVar(value=False)
        self.output_var = tk.StringVar(value="")  # Will be set by _update_output_filename
        self.status_var = tk.StringVar(value="Prêt")
        self.preview_var = tk.StringVar(value="")

        # Ensure output directory exists
        self._ensure_output_directory()

        # Build UI
        self._create_widgets()
        self._load_fonts()

        # Bind events
        self.filter_var.trace('w', self._on_filter_changed)
        self.text_var.trace('w', self._update_preview)
        self.text_var.trace('w', self._update_visual_preview)
        self.text_var.trace('w', self._update_output_filename)
        self.font_var.trace('w', self._update_visual_preview)
        self.size_var.trace('w', self._update_preview)
        self.size_var.trace('w', self._update_visual_preview)
        self.spacing_var.trace('w', self._update_preview)
        self.spacing_var.trace('w', self._update_visual_preview)

        # Initialize output filename with default text
        self._update_output_filename()

    def _create_widgets(self) -> None:
        """Create all GUI widgets."""
        # Main container with padding
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        row = 0

        # Title
        title = ttk.Label(
            main_frame,
            text="Convertisseur Texte vers SVG pour Impression 3D",
            font=('Arial', 16, 'bold')
        )
        title.grid(row=row, column=0, columnspan=3, pady=(0, 10))
        row += 1

        # Text input
        ttk.Label(main_frame, text="Texte à convertir :", font=('Arial', 10, 'bold')).grid(
            row=row, column=0, sticky=tk.W, pady=5
        )
        row += 1
        text_entry = ttk.Entry(main_frame, textvariable=self.text_var, font=('Arial', 14))
        text_entry.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        main_frame.columnconfigure(0, weight=1)
        row += 1

        # Visual preview of text with font
        preview_visual_frame = ttk.LabelFrame(main_frame, text="Aperçu Visuel", padding="5")
        preview_visual_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        row += 1

        self.preview_canvas = tk.Canvas(
            preview_visual_frame,
            height=100,
            bg='white',
            relief=tk.SUNKEN,
            borderwidth=2
        )
        self.preview_canvas.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=5, pady=5)
        preview_visual_frame.columnconfigure(0, weight=1)

        # Font selection frame
        font_frame = ttk.LabelFrame(main_frame, text="Sélection de Police", padding="5")
        font_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        row += 1

        # Font filter
        ttk.Label(font_frame, text="Filtrer :").grid(row=0, column=0, sticky=tk.W, padx=5)
        filter_entry = ttk.Entry(font_frame, textvariable=self.filter_var)
        filter_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5)

        # Refresh button
        refresh_btn = ttk.Button(
            font_frame,
            text="🔄 Rafraîchir",
            command=self._refresh_fonts,
            width=12
        )
        refresh_btn.grid(row=0, column=2, padx=5)

        font_frame.columnconfigure(1, weight=1)

        # Font dropdown
        ttk.Label(font_frame, text="Police :").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.font_combo = ttk.Combobox(
            font_frame,
            textvariable=self.font_var,
            state='readonly',
            width=40
        )
        self.font_combo.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)

        # Parameters frame
        params_frame = ttk.LabelFrame(main_frame, text="Paramètres", padding="5")
        params_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        row += 1

        # Size
        ttk.Label(params_frame, text="Largeur du texte (mm) :").grid(row=0, column=0, sticky=tk.W, padx=5)
        size_scale = ttk.Scale(
            params_frame,
            from_=5,
            to=180,
            variable=self.size_var,
            orient=tk.HORIZONTAL
        )
        size_scale.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5)

        # Spinbox for manual entry
        size_spinbox = ttk.Spinbox(
            params_frame,
            from_=5,
            to=180,
            textvariable=self.size_var,
            width=8,
            format="%.1f"
        )
        size_spinbox.grid(row=0, column=2, padx=5)
        params_frame.columnconfigure(1, weight=1)

        # Letter spacing
        ttk.Label(params_frame, text="Espacement (mm) :").grid(
            row=1, column=0, sticky=tk.W, padx=5, pady=5
        )
        spacing_scale = ttk.Scale(
            params_frame,
            from_=-5,
            to=10,
            variable=self.spacing_var,
            orient=tk.HORIZONTAL
        )
        spacing_scale.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)

        # Spinbox for manual entry
        spacing_spinbox = ttk.Spinbox(
            params_frame,
            from_=-5,
            to=10,
            textvariable=self.spacing_var,
            width=8,
            format="%.1f",
            increment=0.5
        )
        spacing_spinbox.grid(row=1, column=2, padx=5, pady=5)

        # Outline options frame
        outline_frame = ttk.LabelFrame(main_frame, text="Options de Contour", padding="5")
        outline_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        row += 1

        # Enable outline checkbox
        outline_check = ttk.Checkbutton(
            outline_frame,
            text="Générer un fichier de contour séparé",
            variable=self.enable_outline_var,
            command=self._toggle_outline_options
        )
        outline_check.grid(row=0, column=0, columnspan=3, sticky=tk.W, padx=5, pady=5)

        # Outline width
        ttk.Label(outline_frame, text="Épaisseur du contour (mm) :").grid(
            row=1, column=0, sticky=tk.W, padx=5, pady=5
        )
        self.outline_scale = ttk.Scale(
            outline_frame,
            from_=0.3,
            to=2.0,
            variable=self.outline_width_var,
            orient=tk.HORIZONTAL,
            state='disabled'
        )
        self.outline_scale.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)

        # Spinbox for outline width
        self.outline_spinbox = ttk.Spinbox(
            outline_frame,
            from_=0.3,
            to=2.0,
            textvariable=self.outline_width_var,
            width=8,
            format="%.1f",
            increment=0.1,
            state='disabled'
        )
        self.outline_spinbox.grid(row=1, column=2, padx=5, pady=5)
        outline_frame.columnconfigure(1, weight=1)

        # Separate letters checkbox
        separate_check = ttk.Checkbutton(
            outline_frame,
            text="Séparer chaque lettre (un fichier par lettre pour multi-couleur)",
            variable=self.separate_letters_var
        )
        separate_check.grid(row=2, column=0, columnspan=3, sticky=tk.W, padx=5, pady=(10, 5))

        # Output file
        output_frame = ttk.Frame(main_frame)
        output_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        row += 1

        ttk.Label(output_frame, text="Fichier de sortie :").grid(row=0, column=0, sticky=tk.W, padx=5)
        output_entry = ttk.Entry(output_frame, textvariable=self.output_var)
        output_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5)
        output_frame.columnconfigure(1, weight=1)

        browse_btn = ttk.Button(output_frame, text="Parcourir...", command=self._browse_output)
        browse_btn.grid(row=0, column=2, padx=5)

        # Preview frame
        preview_frame = ttk.LabelFrame(main_frame, text="Aperçu Dimensions", padding="5")
        preview_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        row += 1

        preview_label = ttk.Label(
            preview_frame,
            textvariable=self.preview_var,
            font=('Courier', 10),
            justify=tk.LEFT
        )
        preview_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

        # Generate button
        generate_btn = ttk.Button(
            main_frame,
            text="Générer le SVG",
            command=self._generate_svg,
            style='Accent.TButton'
        )
        generate_btn.grid(row=row, column=0, columnspan=3, pady=10, sticky=(tk.W, tk.E))
        row += 1

        # Status bar
        status_frame = ttk.Frame(main_frame, relief=tk.SUNKEN, borderwidth=1)
        status_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(5, 0))
        status_label = ttk.Label(status_frame, textvariable=self.status_var, anchor=tk.W)
        status_label.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=5, pady=2)
        status_frame.columnconfigure(0, weight=1)

    def _toggle_outline_options(self) -> None:
        """Enable or disable outline options based on checkbox."""
        if self.enable_outline_var.get():
            self.outline_scale.config(state='normal')
            self.outline_spinbox.config(state='normal')
        else:
            self.outline_scale.config(state='disabled')
            self.outline_spinbox.config(state='disabled')

    def _ensure_output_directory(self) -> None:
        """Ensure the output directory exists."""
        try:
            DEFAULT_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            # If we can't create the directory, use current directory instead
            import os
            fallback_path = os.path.join(os.getcwd(), "output.svg")
            self.output_var.set(fallback_path)
            print(f"Warning: Could not create output directory {DEFAULT_OUTPUT_DIR}: {e}")
            print(f"Using fallback: {fallback_path}")

    def _load_fonts(self) -> None:
        """Load available fonts into the dropdown."""
        self.status_var.set("Chargement des polices...")
        self.root.update()

        self.all_fonts = self.font_manager.list_fonts()

        if not self.all_fonts:
            messagebox.showwarning(
                "Aucune Police Trouvée",
                "Aucune police trouvée sur votre système.\n\n"
                "Veuillez installer des polices TrueType ou OpenType."
            )
            self.status_var.set("Aucune police trouvée")
            return

        self.filtered_fonts = self.all_fonts
        self._update_font_list()

    def _refresh_fonts(self) -> None:
        """Refresh the font list by clearing cache and rescanning."""
        # Confirm with user
        if not messagebox.askyesno(
            "Rafraîchir les polices",
            "Cela va rescanner toutes les polices installées.\n\n"
            "Utile si vous venez d'installer une nouvelle police.\n\n"
            "Continuer ?"
        ):
            return

        self.status_var.set("Suppression du cache...")
        self.root.update()

        # Clear cache
        self.font_manager.clear_cache()

        self.status_var.set("Rechargement des polices...")
        self.root.update()

        # Reload font manager without cache
        self.font_manager = FontManager(use_cache=False)

        # Reload fonts
        self._load_fonts()

        # Show success message
        messagebox.showinfo(
            "Polices rafraîchies",
            f"✅ {len(self.all_fonts)} polices trouvées !\n\n"
            "Les nouvelles polices installées sont maintenant disponibles."
        )

        self.status_var.set("Polices rafraîchies")

        # Select first font by default
        if self.filtered_fonts:
            self.font_var.set(self.filtered_fonts[0][0])
            self.current_font_path = self.filtered_fonts[0][1]
            # Update visual preview with default font
            self._update_visual_preview()

        self.status_var.set(f"{len(self.all_fonts)} police(s) chargée(s)")

    def _update_font_list(self) -> None:
        """Update the font dropdown with filtered fonts."""
        font_names = [name for name, _ in self.filtered_fonts]
        self.font_combo['values'] = font_names

    def _on_filter_changed(self, *args) -> None:
        """Handle font filter changes."""
        filter_text = self.filter_var.get()

        if filter_text:
            self.filtered_fonts = self.font_manager.list_fonts(filter_regex=filter_text)
        else:
            self.filtered_fonts = self.all_fonts

        self._update_font_list()

        # Update status
        self.status_var.set(f"Affichage de {len(self.filtered_fonts)} police(s)")

    def _calculate_font_size_for_width(self, font_path: Path, text: str, target_width: float, spacing: float) -> tuple[float, float]:
        """
        Calculate the font size needed to achieve a target width.

        Returns:
            Tuple of (font_size_mm, actual_height_mm)
        """
        # Start with an arbitrary size to measure proportions
        test_size = 100.0
        converter = GlyphConverter(font_path, test_size)
        test_width, test_height = converter.get_text_dimensions(text, spacing)

        # Calculate the ratio to achieve target width
        if test_width > 0:
            ratio = target_width / test_width
            final_size = test_size * ratio

            # Recalculate with the adjusted size to get accurate height
            final_converter = GlyphConverter(font_path, final_size)
            final_width, final_height = final_converter.get_text_dimensions(text, spacing)

            return final_size, final_height
        else:
            return test_size, test_height

    def _update_preview(self, *args) -> None:
        """Update the preview information."""
        text = self.text_var.get()
        if not text:
            self.preview_var.set("Entrez du texte pour voir l'aperçu")
            return

        font_name = self.font_var.get()
        if not font_name:
            self.preview_var.set("Sélectionnez une police pour voir l'aperçu")
            return

        # Get font path
        font_path = self.font_manager.get_font_path(font_name)
        if not font_path:
            self.preview_var.set("Police non trouvée")
            return

        try:
            # Calculate dimensions
            try:
                target_width = float(self.size_var.get())
            except (ValueError, TypeError):
                target_width = DEFAULT_SIZE_MM

            try:
                spacing = float(self.spacing_var.get())
            except (ValueError, TypeError):
                spacing = DEFAULT_LETTER_SPACING_MM

            # Calculate font size to achieve target width
            font_size, height = self._calculate_font_size_for_width(font_path, text, target_width, spacing)

            preview_text = (
                f"Texte : \"{text}\"\n"
                f"Police : {font_name}\n"
                f"Largeur finale : {target_width:.1f}mm\n"
                f"Hauteur finale : {height:.2f}mm\n"
                f"Espacement : {spacing:.1f}mm entre les lettres\n"
                f"Caractères : {len(text)}\n"
                f"(Taille de police calculée : {font_size:.1f}mm)"
            )
            self.preview_var.set(preview_text)

        except Exception as e:
            self.preview_var.set(f"Erreur : {str(e)}")

    def _update_output_filename(self, *args) -> None:
        """Update the output filename based on the text input."""
        text = self.text_var.get()

        if not text:
            # If no text, use default name
            filename = "output.svg"
        else:
            # Sanitize the text for use as filename
            # Replace spaces with underscores, remove invalid characters
            safe_text = text.strip()

            # Replace invalid filename characters
            invalid_chars = '<>:"/\\|?*'
            for char in invalid_chars:
                safe_text = safe_text.replace(char, '_')

            # Replace spaces with underscores
            safe_text = safe_text.replace(' ', '_')

            # Limit length to avoid too long filenames
            if len(safe_text) > 50:
                safe_text = safe_text[:50]

            # Ensure it's not empty after sanitization
            if not safe_text:
                safe_text = "output"

            filename = f"{safe_text}.svg"

        # Update the output path with new filename
        output_path = DEFAULT_OUTPUT_DIR / filename
        self.output_var.set(str(output_path))

    def _update_visual_preview(self, *args) -> None:
        """Update the visual preview canvas with the text in selected font."""
        # Clear canvas completely
        self.preview_canvas.delete("all")
        self.preview_canvas.update_idletasks()  # Force refresh to avoid artifacts

        text = self.text_var.get()
        if not text:
            # Display placeholder text
            self.preview_canvas.create_text(
                10, 50,
                text="Entrez du texte pour voir l'aperçu...",
                anchor=tk.W,
                font=('Arial', 12),
                fill='gray'
            )
            return

        font_name = self.font_var.get()
        if not font_name:
            self.preview_canvas.create_text(
                10, 50,
                text="Sélectionnez une police...",
                anchor=tk.W,
                font=('Arial', 12),
                fill='gray'
            )
            return

        try:
            # Get available system fonts for tkinter
            available_tk_fonts = tkfont.families()

            # Try to find a matching font for tkinter
            # Try exact match first
            tk_font_name = None
            if font_name in available_tk_fonts:
                tk_font_name = font_name
            else:
                # Try to find similar font (remove "Regular", "Bold" etc.)
                base_name = font_name.split()[0]
                for tk_font in available_tk_fonts:
                    if base_name.lower() in tk_font.lower():
                        tk_font_name = tk_font
                        break

            # If no match found, use a default but show the font name
            if not tk_font_name:
                tk_font_name = 'TkDefaultFont'

            # Calculate font size for preview based on target width
            # Use target width directly for consistent scaling
            target_width = self.size_var.get()

            # Scale: 5mm → 12pt, 180mm → 90pt
            # Formula: preview = min(90, max(12, target_width * 0.5))
            preview_font_size = max(12, min(90, int(target_width * 0.5)))

            # Create font
            display_font = tkfont.Font(family=tk_font_name, size=preview_font_size)

            # Get canvas dimensions
            canvas_width = self.preview_canvas.winfo_width()
            if canvas_width <= 1:  # Canvas not yet rendered
                canvas_width = 700

            # Calculate spacing in pixels (scale down for preview)
            try:
                spacing_mm = float(self.spacing_var.get())
            except (ValueError, TypeError):
                spacing_mm = 0.0

            spacing_pixels = int(spacing_mm * 2)  # Approximation pour l'aperçu

            # Measure total width with spacing
            char_widths = [display_font.measure(char) for char in text]
            total_width = sum(char_widths) + spacing_pixels * max(0, len(text) - 1)

            # Center the text
            x_start = (canvas_width - total_width) // 2
            y_pos = 50

            # Draw each character with spacing
            current_x = x_start
            for i, char in enumerate(text):
                self.preview_canvas.create_text(
                    current_x, y_pos,
                    text=char,
                    font=display_font,
                    fill='black',
                    anchor=tk.W
                )
                current_x += char_widths[i] + spacing_pixels

                # Draw spacing indicator (small vertical line) if spacing > 0
                if spacing_mm > 0 and i < len(text) - 1:
                    # Petite ligne verticale pour visualiser l'espacement
                    line_x = current_x - spacing_pixels // 2
                    self.preview_canvas.create_line(
                        line_x, y_pos - 5,
                        line_x, y_pos + 5,
                        fill='lightblue',
                        width=1,
                        dash=(2, 2)
                    )

            # Add font name below if using fallback
            if tk_font_name == 'TkDefaultFont':
                self.preview_canvas.create_text(
                    x_pos, 85,
                    text=f"(Aperçu approximatif - police finale: {font_name})",
                    font=('Arial', 8),
                    fill='gray',
                    anchor=tk.CENTER
                )

        except Exception as e:
            # If anything fails, show error message
            self.preview_canvas.create_text(
                10, 50,
                text=f"Erreur d'aperçu: {str(e)}",
                anchor=tk.W,
                font=('Arial', 10),
                fill='red'
            )

    def _browse_output(self) -> None:
        """Open file browser for output file selection."""
        # Get initial directory from current output path or use default
        current_output = Path(self.output_var.get())
        if current_output.parent.exists():
            initial_dir = str(current_output.parent)
            initial_file = current_output.name
        else:
            initial_dir = str(DEFAULT_OUTPUT_DIR)
            initial_file = "output.svg"

        filename = filedialog.asksaveasfilename(
            defaultextension=".svg",
            filetypes=[("SVG files", "*.svg"), ("All files", "*.*")],
            initialdir=initial_dir,
            initialfile=initial_file
        )

        if filename:
            self.output_var.set(filename)

    def _generate_svg(self) -> None:
        """Generate the SVG file."""
        text = self.text_var.get()
        if not text:
            messagebox.showerror("Erreur", "Veuillez entrer du texte à convertir")
            return

        font_name = self.font_var.get()
        if not font_name:
            messagebox.showerror("Erreur", "Veuillez sélectionner une police")
            return

        output_path = Path(self.output_var.get())

        self.status_var.set("Génération du SVG...")
        self.root.update()

        try:
            # Get font path
            font_path = self.font_manager.get_font_path(font_name)
            if not font_path:
                raise ValueError(f"Police '{font_name}' non trouvée")

            # Convert text
            target_width = self.size_var.get()
            spacing = self.spacing_var.get()
            thickness = DEFAULT_THICKNESS_MM  # Valeur par défaut (juste pour métadonnées)

            # Calculate font size to achieve target width
            font_size, height = self._calculate_font_size_for_width(font_path, text, target_width, spacing)

            converter = GlyphConverter(font_path, font_size)
            outlines = converter.convert_text(text, spacing)

            if not outlines:
                raise ValueError("Aucun caractère n'a pu être converti")

            # Get dimensions (should match target_width)
            width, height = converter.get_text_dimensions(text, spacing)

            # Build SVG
            builder = SVGBuilder(
                text=text,
                font_name=font_name,
                size_mm=font_size,
                thickness_mm=thickness
            )

            files_created = []

            # Check if separate letters option is enabled
            if self.separate_letters_var.get():
                # Generate separate file for each letter
                files_created = builder.build_svg_per_letter(outlines, output_path, width, height)

                # Generate outline files for each letter if option is enabled
                if self.enable_outline_var.get():
                    outline_width = self.outline_width_var.get()
                    outline_files = []

                    for file_path in files_created:
                        file_path_obj = Path(file_path)
                        outline_path = file_path_obj.parent / f"{file_path_obj.stem}_contour{file_path_obj.suffix}"

                        # Build outline for this letter
                        # Get the letter index from the filename
                        letter_idx = int(file_path_obj.stem.split('_')[2]) - 1
                        letter_outline = [outlines[letter_idx]]
                        letter_width = outlines[letter_idx].advance_width

                        builder.build_svg_with_outline(letter_outline, outline_path, letter_width, height, outline_width)
                        outline_files.append(str(outline_path))

                    files_created.extend(outline_files)
            else:
                # Generate single file with all text
                builder.build_svg(outlines, output_path, width, height)
                files_created = [str(output_path)]

                # Generate outline file if option is enabled
                if self.enable_outline_var.get():
                    outline_width = self.outline_width_var.get()
                    outline_path = output_path.parent / f"{output_path.stem}_contour{output_path.suffix}"
                    builder.build_svg_with_outline(outlines, outline_path, width, height, outline_width)
                    files_created.append(str(outline_path))

            # Success message
            if self.separate_letters_var.get():
                num_letters = len(outlines)
                if self.enable_outline_var.get():
                    message = (
                        f"Fichiers SVG créés avec succès !\n\n"
                        f"{len(files_created)} fichiers créés :\n"
                        f"- {num_letters} fichiers de lettres\n"
                        f"- {num_letters} fichiers de contour\n\n"
                        f"Texte : \"{text}\"\n"
                        f"Dimensions : {width:.2f}mm × {height:.2f}mm\n"
                        f"Épaisseur contour : {outline_width:.1f}mm\n\n"
                        f"Dans votre slicer 3D :\n"
                        f"1. Importez chaque fichier de lettre avec une couleur différente\n"
                        f"2. Importez les contours si souhaité\n"
                        f"→ Impression multi-couleur ! 🌈"
                    )
                else:
                    message = (
                        f"Fichiers SVG créés avec succès !\n\n"
                        f"{len(files_created)} fichiers de lettres créés\n"
                        f"Texte : \"{text}\"\n"
                        f"Dimensions : {width:.2f}mm × {height:.2f}mm\n\n"
                        f"Dans votre slicer 3D :\n"
                        f"Importez chaque fichier avec une couleur différente\n"
                        f"pour un effet multi-couleur ! 🌈"
                    )
            elif len(files_created) == 1:
                message = (
                    f"Fichier SVG créé avec succès !\n\n"
                    f"Fichier : {files_created[0]}\n"
                    f"Dimensions : {width:.2f}mm × {height:.2f}mm\n\n"
                    f"Vous pouvez maintenant l'importer dans votre slicer 3D."
                )
            else:
                message = (
                    f"Fichiers SVG créés avec succès !\n\n"
                    f"Texte : {files_created[0]}\n"
                    f"Contour : {files_created[1]}\n"
                    f"Dimensions : {width:.2f}mm × {height:.2f}mm\n"
                    f"Épaisseur contour : {outline_width:.1f}mm\n\n"
                    f"Importez les deux fichiers dans votre slicer 3D\n"
                    f"pour un effet multi-couleur !"
                )

            self.status_var.set(f"SVG créé : {output_path}")
            messagebox.showinfo("Succès", message)

        except Exception as e:
            self.status_var.set("Erreur lors de la conversion")
            messagebox.showerror("Erreur", f"Échec de la génération du SVG :\n\n{str(e)}")


def main() -> None:
    """Main entry point for the GUI."""
    root = tk.Tk()

    # Set icon if available (optional)
    try:
        # Try to set a nice icon (will fail gracefully if not available)
        pass
    except:
        pass

    # Create and run the application
    app = Text2SVG3D_GUI(root)

    # Center window on screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

    # Run
    root.mainloop()


if __name__ == "__main__":
    main()
