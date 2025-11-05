"""Main GUI window for text2svg3d."""

import logging
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, ttk
from typing import Optional

from ..config import DEFAULT_LETTER_SPACING_MM, DEFAULT_OUTPUT_DIR, DEFAULT_SIZE_MM
from ..font_manager import FontManager
from .file_operations import FileOperations
from .preview import DimensionsPreview, VisualPreview
from .widgets import LabeledScale, StatusBar, ask_yes_no, show_error, show_info, show_warning

logger = logging.getLogger(__name__)


class Text2SVG3DWindow:
    """Main application window."""

    def __init__(self, root: tk.Tk) -> None:
        """Initialize the GUI window."""
        self.root = root
        self.root.title("text2svg3d - Convertisseur Texte vers SVG pour Impression 3D")
        self.root.geometry("750x700")
        self.root.resizable(True, True)

        # Initialize managers
        self.font_manager = FontManager(use_cache=True)
        self.file_ops = FileOperations(self.font_manager)

        # Data
        self.all_fonts = []
        self.filtered_fonts = []
        self.current_font_path: Optional[Path] = None

        # Variables
        self._init_variables()

        # Components
        self.visual_preview: Optional[VisualPreview] = None
        self.dimensions_preview: Optional[DimensionsPreview] = None
        self.status_bar: Optional[StatusBar] = None

        # Ensure output directory
        self.file_ops.ensure_output_directory()

        # Build UI
        self._create_widgets()
        self._load_fonts()
        self._bind_events()
        self._update_output_filename()

    def _init_variables(self) -> None:
        """Initialize all tkinter variables."""
        self.text_var = tk.StringVar(value="HELLO")
        self.font_var = tk.StringVar()
        self.filter_var = tk.StringVar()
        self.size_var = tk.DoubleVar(value=DEFAULT_SIZE_MM)
        self.spacing_var = tk.DoubleVar(value=DEFAULT_LETTER_SPACING_MM)
        self.enable_outline_var = tk.BooleanVar(value=False)
        self.outline_width_var = tk.DoubleVar(value=0.8)
        self.separate_letters_var = tk.BooleanVar(value=False)
        self.output_var = tk.StringVar(value="")

    def _create_widgets(self) -> None:
        """Create all GUI widgets."""
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        row = 0

        # Title
        title = ttk.Label(
            main_frame,
            text="Convertisseur Texte vers SVG pour Impression 3D",
            font=("Arial", 16, "bold"),
        )
        title.grid(row=row, column=0, columnspan=3, pady=(0, 10))
        row += 1

        # Text input section
        row = self._create_text_input_section(main_frame, row)

        # Visual preview section
        row = self._create_visual_preview_section(main_frame, row)

        # Font selection section
        row = self._create_font_selection_section(main_frame, row)

        # Parameters section
        row = self._create_parameters_section(main_frame, row)

        # Outline options section
        row = self._create_outline_section(main_frame, row)

        # Output file section
        row = self._create_output_section(main_frame, row)

        # Dimensions preview section
        row = self._create_dimensions_preview_section(main_frame, row)

        # Generate button
        generate_btn = ttk.Button(main_frame, text="Générer le SVG", command=self._generate_svg)
        generate_btn.grid(row=row, column=0, columnspan=3, pady=10, sticky=(tk.W, tk.E))
        row += 1

        # Status bar
        self.status_bar = StatusBar(main_frame)
        self.status_bar.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(5, 0))

    def _create_text_input_section(self, parent: ttk.Frame, row: int) -> int:
        """Create text input section."""
        ttk.Label(parent, text="Texte à convertir :", font=("Arial", 10, "bold")).grid(
            row=row, column=0, sticky=tk.W, pady=5
        )
        row += 1

        text_entry = ttk.Entry(parent, textvariable=self.text_var, font=("Arial", 14))
        text_entry.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        parent.columnconfigure(0, weight=1)
        row += 1

        return row

    def _create_visual_preview_section(self, parent: ttk.Frame, row: int) -> int:
        """Create visual preview section."""
        preview_frame = ttk.LabelFrame(parent, text="Aperçu Visuel", padding="5")
        preview_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        row += 1

        self.visual_preview = VisualPreview(preview_frame)
        preview_frame.columnconfigure(0, weight=1)

        return row

    def _create_font_selection_section(self, parent: ttk.Frame, row: int) -> int:
        """Create font selection section."""
        font_frame = ttk.LabelFrame(parent, text="Sélection de Police", padding="5")
        font_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        row += 1

        # Filter
        ttk.Label(font_frame, text="Filtrer :").grid(row=0, column=0, sticky=tk.W, padx=5)
        filter_entry = ttk.Entry(font_frame, textvariable=self.filter_var)
        filter_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5)

        # Refresh button
        refresh_btn = ttk.Button(
            font_frame, text="🔄 Rafraîchir", command=self._refresh_fonts, width=12
        )
        refresh_btn.grid(row=0, column=2, padx=5)
        font_frame.columnconfigure(1, weight=1)

        # Font dropdown
        ttk.Label(font_frame, text="Police :").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.font_combo = ttk.Combobox(font_frame, textvariable=self.font_var, state="readonly")
        self.font_combo.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)

        return row

    def _create_parameters_section(self, parent: ttk.Frame, row: int) -> int:
        """Create parameters section."""
        params_frame = ttk.LabelFrame(parent, text="Paramètres", padding="5")
        params_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        row += 1

        # Size scale
        size_scale = LabeledScale(
            params_frame, "Largeur du texte (mm) :", self.size_var, from_=5, to=180
        )
        size_scale.grid(row=0, column=0, columnspan=3, sticky=(tk.W, tk.E), padx=5)

        # Spacing scale
        spacing_scale = LabeledScale(
            params_frame,
            "Espacement (mm) :",
            self.spacing_var,
            from_=-5,
            to=10,
            increment=0.5,
        )
        spacing_scale.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), padx=5, pady=5)

        params_frame.columnconfigure(0, weight=1)
        return row

    def _create_outline_section(self, parent: ttk.Frame, row: int) -> int:
        """Create outline options section."""
        outline_frame = ttk.LabelFrame(parent, text="Options de Contour", padding="5")
        outline_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        row += 1

        # Enable outline checkbox
        outline_check = ttk.Checkbutton(
            outline_frame,
            text="Générer un fichier de contour séparé",
            variable=self.enable_outline_var,
            command=self._toggle_outline_options,
        )
        outline_check.grid(row=0, column=0, columnspan=3, sticky=tk.W, padx=5, pady=5)

        # Outline width scale
        self.outline_scale = LabeledScale(
            outline_frame,
            "Épaisseur du contour (mm) :",
            self.outline_width_var,
            from_=0.3,
            to=2.0,
            increment=0.1,
        )
        self.outline_scale.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), padx=5)
        self.outline_scale.children["!scale"].config(state="disabled")
        self.outline_scale.children["!spinbox"].config(state="disabled")

        # Separate letters checkbox
        separate_check = ttk.Checkbutton(
            outline_frame,
            text="Séparer chaque lettre (un fichier par lettre pour multi-couleur)",
            variable=self.separate_letters_var,
        )
        separate_check.grid(row=2, column=0, columnspan=3, sticky=tk.W, padx=5, pady=(10, 5))

        outline_frame.columnconfigure(0, weight=1)
        return row

    def _create_output_section(self, parent: ttk.Frame, row: int) -> int:
        """Create output file section."""
        output_frame = ttk.Frame(parent)
        output_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        row += 1

        ttk.Label(output_frame, text="Fichier de sortie :").grid(
            row=0, column=0, sticky=tk.W, padx=5
        )
        output_entry = ttk.Entry(output_frame, textvariable=self.output_var)
        output_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5)
        output_frame.columnconfigure(1, weight=1)

        browse_btn = ttk.Button(output_frame, text="Parcourir...", command=self._browse_output)
        browse_btn.grid(row=0, column=2, padx=5)

        return row

    def _create_dimensions_preview_section(self, parent: ttk.Frame, row: int) -> int:
        """Create dimensions preview section."""
        preview_frame = ttk.LabelFrame(parent, text="Aperçu Dimensions", padding="5")
        preview_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        row += 1

        self.dimensions_preview = DimensionsPreview(preview_frame)
        return row

    def _bind_events(self) -> None:
        """Bind all event handlers."""
        self.filter_var.trace("w", self._on_filter_changed)
        self.text_var.trace("w", self._update_preview)
        self.text_var.trace("w", self._update_visual_preview)
        self.text_var.trace("w", self._update_output_filename)
        self.font_var.trace("w", self._update_visual_preview)
        self.size_var.trace("w", self._update_preview)
        self.size_var.trace("w", self._update_visual_preview)
        self.spacing_var.trace("w", self._update_preview)
        self.spacing_var.trace("w", self._update_visual_preview)

    def _load_fonts(self) -> None:
        """Load available fonts."""
        if self.status_bar:
            self.status_bar.set_status("Chargement des polices...")

        self.all_fonts = self.font_manager.list_fonts()

        if not self.all_fonts:
            show_warning(
                "Aucune Police Trouvée",
                "Aucune police trouvée sur votre système.\n\n"
                "Veuillez installer des polices TrueType ou OpenType.",
            )
            if self.status_bar:
                self.status_bar.set_status("Aucune police trouvée")
            return

        self.filtered_fonts = self.all_fonts
        self._update_font_list()

        if self.status_bar:
            self.status_bar.set_status(f"{len(self.all_fonts)} police(s) chargée(s)")

    def _refresh_fonts(self) -> None:
        """Refresh font list."""
        if not ask_yes_no(
            "Rafraîchir les polices",
            "Cela va rescanner toutes les polices installées.\n\n"
            "Utile si vous venez d'installer une nouvelle police.\n\n"
            "Continuer ?",
        ):
            return

        if self.status_bar:
            self.status_bar.set_status("Suppression du cache...")

        self.font_manager.clear_cache()

        if self.status_bar:
            self.status_bar.set_status("Rechargement des polices...")

        self.font_manager = FontManager(use_cache=False)
        self._load_fonts()

        show_info(
            "Polices rafraîchies",
            f"✅ {len(self.all_fonts)} polices trouvées !\n\n"
            "Les nouvelles polices installées sont maintenant disponibles.",
        )

        if self.filtered_fonts:
            self.font_var.set(self.filtered_fonts[0][0])
            self.current_font_path = self.filtered_fonts[0][1]
            self._update_visual_preview()

    def _update_font_list(self) -> None:
        """Update font dropdown."""
        font_names = [name for name, _ in self.filtered_fonts]
        self.font_combo["values"] = font_names

    def _on_filter_changed(self, *args) -> None:
        """Handle font filter changes."""
        filter_text = self.filter_var.get()

        if filter_text:
            self.filtered_fonts = self.font_manager.list_fonts(filter_regex=filter_text)
        else:
            self.filtered_fonts = self.all_fonts

        self._update_font_list()

        if self.status_bar:
            self.status_bar.set_status(f"Affichage de {len(self.filtered_fonts)} police(s)")

    def _toggle_outline_options(self) -> None:
        """Enable/disable outline options."""
        state = "normal" if self.enable_outline_var.get() else "disabled"
        self.outline_scale.children["!scale"].config(state=state)
        self.outline_scale.children["!spinbox"].config(state=state)

    def _update_preview(self, *args) -> None:
        """Update dimensions preview."""
        text = self.text_var.get()
        if not text or not self.dimensions_preview:
            if self.dimensions_preview:
                self.dimensions_preview.show_placeholder()
            return

        font_name = self.font_var.get()
        if not font_name:
            self.dimensions_preview.show_placeholder("Sélectionnez une police")
            return

        font_path = self.font_manager.get_font_path(font_name)
        if not font_path:
            self.dimensions_preview.show_error("Police non trouvée")
            return

        try:
            target_width = float(self.size_var.get())
            spacing = float(self.spacing_var.get())

            font_size, height = self.file_ops.calculate_font_size_for_width(
                font_path, text, target_width, spacing
            )

            self.dimensions_preview.update_dimensions(
                text, font_name, target_width, height, spacing, font_size
            )
        except Exception as e:
            logger.error(f"Failed to update preview: {e}")
            self.dimensions_preview.show_error(str(e))

    def _update_visual_preview(self, *args) -> None:
        """Update visual preview."""
        if not self.visual_preview:
            return

        text = self.text_var.get()
        if not text:
            self.visual_preview.show_placeholder()
            return

        font_name = self.font_var.get()
        if not font_name:
            self.visual_preview.show_placeholder("Sélectionnez une police...")
            return

        try:
            target_width = self.size_var.get()
            spacing_mm = self.spacing_var.get()

            self.visual_preview.render_text(text, font_name, target_width, spacing_mm)
        except Exception as e:
            logger.error(f"Failed to render visual preview: {e}")

    def _update_output_filename(self, *args) -> None:
        """Update output filename based on text."""
        text = self.text_var.get()
        output_path = self.file_ops.get_output_path(text)
        self.output_var.set(str(output_path))

    def _browse_output(self) -> None:
        """Browse for output file."""
        current_output = Path(self.output_var.get())
        initial_dir = (
            str(current_output.parent)
            if current_output.parent.exists()
            else str(DEFAULT_OUTPUT_DIR)
        )

        filename = filedialog.asksaveasfilename(
            defaultextension=".svg",
            filetypes=[("SVG files", "*.svg"), ("All files", "*.*")],
            initialdir=initial_dir,
            initialfile=current_output.name,
        )

        if filename:
            self.output_var.set(filename)

    def _generate_svg(self) -> None:
        """Generate SVG file(s)."""
        text = self.text_var.get()
        if not text:
            show_error("Erreur", "Veuillez entrer du texte à convertir")
            return

        font_name = self.font_var.get()
        if not font_name:
            show_error("Erreur", "Veuillez sélectionner une police")
            return

        output_path = Path(self.output_var.get())

        if self.status_bar:
            self.status_bar.set_status("Génération du SVG...")

        try:
            target_width = self.size_var.get()
            spacing = self.spacing_var.get()
            enable_outline = self.enable_outline_var.get()
            outline_width = self.outline_width_var.get()
            separate_letters = self.separate_letters_var.get()

            success, files_created, error = self.file_ops.generate_svg(
                text=text,
                font_name=font_name,
                target_width=target_width,
                spacing=spacing,
                output_path=output_path,
                enable_outline=enable_outline,
                outline_width=outline_width,
                separate_letters=separate_letters,
            )

            if success:
                # Get dimensions for message
                font_path = self.font_manager.get_font_path(font_name)
                if font_path:
                    _, height = self.file_ops.calculate_font_size_for_width(
                        font_path, text, target_width, spacing
                    )

                    message = self.file_ops.format_success_message(
                        text,
                        files_created,
                        target_width,
                        height,
                        separate_letters,
                        enable_outline,
                        outline_width,
                    )

                    if self.status_bar:
                        self.status_bar.set_status(f"SVG créé : {output_path}")

                    show_info("Succès", message)
            else:
                if self.status_bar:
                    self.status_bar.set_status("Erreur lors de la conversion")
                show_error("Erreur", f"Échec de la génération du SVG :\n\n{error}")

        except Exception as e:
            logger.error(f"Failed to generate SVG: {e}")
            if self.status_bar:
                self.status_bar.set_status("Erreur lors de la conversion")
            show_error("Erreur", f"Échec de la génération du SVG :\n\n{str(e)}")


def main() -> None:
    """Main entry point for GUI."""
    root = tk.Tk()

    # Create application
    _app = Text2SVG3DWindow(root)  # noqa: F841

    # Center window
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")

    # Run
    root.mainloop()


if __name__ == "__main__":
    main()
