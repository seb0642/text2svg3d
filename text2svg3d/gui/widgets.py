"""Reusable widgets and UI components."""

import tkinter as tk
from tkinter import ttk
from typing import Callable


class LabeledEntry(ttk.Frame):
    """A labeled entry widget."""

    def __init__(
        self,
        parent: tk.Widget,
        label: str,
        variable: tk.Variable,
        width: int = 20,
        **kwargs,
    ):
        """Initialize labeled entry."""
        super().__init__(parent, **kwargs)

        ttk.Label(self, text=label).grid(row=0, column=0, sticky=tk.W, padx=5)
        entry = ttk.Entry(self, textvariable=variable, width=width)
        entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5)
        self.columnconfigure(1, weight=1)


class LabeledScale(ttk.Frame):
    """A labeled scale widget with spinbox."""

    def __init__(
        self,
        parent: tk.Widget,
        label: str,
        variable: tk.Variable,
        from_: float,
        to: float,
        format_str: str = "%.1f",
        increment: float = 1.0,
        **kwargs,
    ):
        """Initialize labeled scale."""
        super().__init__(parent, **kwargs)

        ttk.Label(self, text=label).grid(row=0, column=0, sticky=tk.W, padx=5)

        scale = ttk.Scale(self, from_=from_, to=to, variable=variable, orient=tk.HORIZONTAL)
        scale.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5)

        spinbox = ttk.Spinbox(
            self,
            from_=from_,
            to=to,
            textvariable=variable,
            width=8,
            format=format_str,
            increment=increment,
        )
        spinbox.grid(row=0, column=2, padx=5)

        self.columnconfigure(1, weight=1)


class StatusBar(ttk.Frame):
    """A status bar widget."""

    def __init__(self, parent: tk.Widget, **kwargs):
        """Initialize status bar."""
        super().__init__(parent, relief=tk.SUNKEN, borderwidth=1, **kwargs)

        self.status_var = tk.StringVar(value="Prêt")
        self.label = ttk.Label(self, textvariable=self.status_var, anchor=tk.W)
        self.label.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=5, pady=2)
        self.columnconfigure(0, weight=1)

    def set_status(self, message: str) -> None:
        """Set status message."""
        self.status_var.set(message)
        self.update_idletasks()


def create_button_with_icon(
    parent: tk.Widget, text: str, command: Callable, width: int = 15, **kwargs
) -> ttk.Button:
    """Create a button with optional icon."""
    return ttk.Button(parent, text=text, command=command, width=width, **kwargs)


def show_error(title: str, message: str) -> None:
    """Show error message dialog."""
    from tkinter import messagebox

    messagebox.showerror(title, message)


def show_info(title: str, message: str) -> None:
    """Show info message dialog."""
    from tkinter import messagebox

    messagebox.showinfo(title, message)


def show_warning(title: str, message: str) -> None:
    """Show warning message dialog."""
    from tkinter import messagebox

    messagebox.showwarning(title, message)


def ask_yes_no(title: str, message: str) -> bool:
    """Ask yes/no question."""
    from tkinter import messagebox

    return messagebox.askyesno(title, message)
