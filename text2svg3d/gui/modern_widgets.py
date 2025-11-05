"""Modern styled widgets with theming support."""

import tkinter as tk
from tkinter import ttk
from typing import Callable, Optional

from .design_system import ICONS, Theme, get_color, get_font, get_radius, get_spacing


class ModernButton(tk.Canvas):
    """Modern button with hover effects and theming."""

    def __init__(
        self,
        parent,
        text: str,
        command: Callable,
        theme: Theme,
        icon: str = "",
        style: str = "primary",
        width: int = 120,
        height: int = 40,
        **kwargs,
    ):
        """Initialize modern button."""
        super().__init__(
            parent,
            width=width,
            height=height,
            highlightthickness=0,
            **kwargs,
        )

        self.text = text
        self.command = command
        self.theme = theme
        self.icon = icon
        self.style = style
        self.width = width
        self.height = height
        self.is_hovered = False

        # Bind events
        self.bind("<Button-1>", self._on_click)
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)

        # Listen to theme changes
        self.theme.add_listener(lambda mode: self._draw())

        self._draw()

    def _draw(self) -> None:
        """Draw button with current state."""
        self.delete("all")

        # Get colors based on style and state
        if self.style == "primary":
            bg_color = (
                self.theme.get_color("primary_hover")
                if self.is_hovered
                else self.theme.get_color("primary")
            )
            text_color = "#FFFFFF"
        elif self.style == "secondary":
            bg_color = (
                self.theme.get_color("secondary_hover")
                if self.is_hovered
                else self.theme.get_color("secondary")
            )
            text_color = "#FFFFFF"
        else:  # outline
            bg_color = self.theme.get_color("surface")
            text_color = self.theme.get_color("text_primary")

        # Draw rounded rectangle
        radius = get_radius("md")
        self.create_rounded_rect(
            2, 2, self.width - 2, self.height - 2, radius, fill=bg_color, outline=""
        )

        # Draw shadow if not hovered
        if not self.is_hovered:
            shadow_color = self.theme.get_color("shadow")
            self.create_rounded_rect(
                4,
                4,
                self.width,
                self.height,
                radius,
                fill="",
                outline=shadow_color,
                width=1,
            )

        # Draw icon and text
        display_text = f"{self.icon} {self.text}" if self.icon else self.text
        self.create_text(
            self.width // 2,
            self.height // 2,
            text=display_text,
            fill=text_color,
            font=get_font("button"),
        )

    def create_rounded_rect(self, x1, y1, x2, y2, radius, **kwargs):
        """Create rounded rectangle on canvas."""
        points = [
            x1 + radius,
            y1,
            x1 + radius,
            y1,
            x2 - radius,
            y1,
            x2 - radius,
            y1,
            x2,
            y1,
            x2,
            y1 + radius,
            x2,
            y1 + radius,
            x2,
            y2 - radius,
            x2,
            y2 - radius,
            x2,
            y2,
            x2 - radius,
            y2,
            x2 - radius,
            y2,
            x1 + radius,
            y2,
            x1 + radius,
            y2,
            x1,
            y2,
            x1,
            y2 - radius,
            x1,
            y2 - radius,
            x1,
            y1 + radius,
            x1,
            y1 + radius,
            x1,
            y1,
        ]
        return self.create_polygon(points, smooth=True, **kwargs)

    def _on_click(self, event) -> None:
        """Handle click event."""
        if self.command:
            self.command()

    def _on_enter(self, event) -> None:
        """Handle mouse enter."""
        self.is_hovered = True
        self._draw()

    def _on_leave(self, event) -> None:
        """Handle mouse leave."""
        self.is_hovered = False
        self._draw()


class ModernCard(tk.Frame):
    """Modern card container with elevation."""

    def __init__(self, parent, theme: Theme, title: str = "", **kwargs):
        """Initialize modern card."""
        super().__init__(parent, **kwargs)

        self.theme = theme
        self.title = title

        self.configure(
            bg=theme.get_color("surface"),
            highlightbackground=theme.get_color("border"),
            highlightthickness=1,
            relief=tk.FLAT,
        )

        # Title if provided
        if title:
            title_label = tk.Label(
                self,
                text=title,
                font=get_font("heading_small"),
                bg=theme.get_color("surface"),
                fg=theme.get_color("text_primary"),
                anchor=tk.W,
            )
            title_label.pack(fill=tk.X, padx=get_spacing("md"), pady=(get_spacing("md"), 0))

        # Listen to theme changes
        theme.add_listener(self._update_theme)

    def _update_theme(self, mode: str) -> None:
        """Update colors when theme changes."""
        self.configure(
            bg=self.theme.get_color("surface"),
            highlightbackground=self.theme.get_color("border"),
        )


class ThemeToggle(tk.Canvas):
    """Theme toggle switch (dark/light mode)."""

    def __init__(self, parent, theme: Theme, **kwargs):
        """Initialize theme toggle."""
        super().__init__(parent, width=60, height=30, highlightthickness=0, **kwargs)

        self.theme = theme
        self.bind("<Button-1>", self._toggle)

        self._draw()
        theme.add_listener(lambda mode: self._draw())

    def _draw(self) -> None:
        """Draw toggle switch."""
        self.delete("all")

        # Background
        bg_color = self.theme.get_color("primary" if self.theme.mode == "dark" else "border")
        self.create_oval(0, 0, 60, 30, fill=bg_color, outline="")

        # Circle
        x = 35 if self.theme.mode == "dark" else 5
        circle_color = "#FFFFFF"
        self.create_oval(x, 5, x + 20, 25, fill=circle_color, outline="")

        # Icon
        icon = ICONS["moon"] if self.theme.mode == "dark" else ICONS["sun"]
        self.create_text(30, 15, text=icon, font=("Segoe UI", 12))

    def _toggle(self, event) -> None:
        """Toggle theme."""
        self.theme.toggle()


class ModernEntry(tk.Frame):
    """Modern entry with floating label."""

    def __init__(
        self,
        parent,
        theme: Theme,
        label: str,
        variable: Optional[tk.Variable] = None,
        **kwargs,
    ):
        """Initialize modern entry."""
        super().__init__(parent, bg=theme.get_color("surface"))

        self.theme = theme
        self.label_text = label
        self.variable = variable or tk.StringVar()

        # Label
        self.label = tk.Label(
            self,
            text=label,
            font=get_font("body_small"),
            bg=theme.get_color("surface"),
            fg=theme.get_color("text_secondary"),
            anchor=tk.W,
        )
        self.label.pack(fill=tk.X, pady=(0, 4))

        # Entry
        self.entry = tk.Entry(
            self,
            textvariable=self.variable,
            font=get_font("body_large"),
            bg=theme.get_color("surface_elevated"),
            fg=theme.get_color("text_primary"),
            insertbackground=theme.get_color("primary"),
            relief=tk.FLAT,
            highlightthickness=2,
            highlightbackground=theme.get_color("border"),
            highlightcolor=theme.get_color("border_focus"),
        )
        self.entry.pack(fill=tk.X, ipady=8, ipadx=12)

        # Theme updates
        theme.add_listener(self._update_theme)

    def _update_theme(self, mode: str) -> None:
        """Update colors when theme changes."""
        self.configure(bg=self.theme.get_color("surface"))
        self.label.configure(
            bg=self.theme.get_color("surface"), fg=self.theme.get_color("text_secondary")
        )
        self.entry.configure(
            bg=self.theme.get_color("surface_elevated"),
            fg=self.theme.get_color("text_primary"),
            insertbackground=self.theme.get_color("primary"),
            highlightbackground=self.theme.get_color("border"),
            highlightcolor=self.theme.get_color("border_focus"),
        )


class ProgressIndicator(tk.Canvas):
    """Modern circular progress indicator."""

    def __init__(self, parent, theme: Theme, size: int = 40, **kwargs):
        """Initialize progress indicator."""
        super().__init__(parent, width=size, height=size, highlightthickness=0, **kwargs)

        self.theme = theme
        self.size = size
        self.angle = 0
        self.is_running = False

        self.configure(bg=theme.get_color("background"))

    def start(self) -> None:
        """Start animation."""
        self.is_running = True
        self._animate()

    def stop(self) -> None:
        """Stop animation."""
        self.is_running = False
        self.delete("all")

    def _animate(self) -> None:
        """Animate progress."""
        if not self.is_running:
            return

        self.delete("all")

        # Draw arc
        margin = 4
        self.create_arc(
            margin,
            margin,
            self.size - margin,
            self.size - margin,
            start=self.angle,
            extent=270,
            outline=self.theme.get_color("primary"),
            width=3,
            style=tk.ARC,
        )

        self.angle = (self.angle + 10) % 360
        self.after(50, self._animate)
