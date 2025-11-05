"""Modern design system for text2svg3d GUI."""

from typing import Tuple

# Color Palette - Modern & Professional
COLORS = {
    # Light Theme
    "light": {
        "primary": "#2563EB",  # Blue vibrant
        "primary_hover": "#1D4ED8",
        "primary_light": "#DBEAFE",
        "secondary": "#8B5CF6",  # Purple
        "secondary_hover": "#7C3AED",
        "success": "#10B981",  # Green
        "warning": "#F59E0B",  # Orange
        "error": "#EF4444",  # Red
        "background": "#F9FAFB",  # Light gray
        "surface": "#FFFFFF",  # White
        "surface_elevated": "#F3F4F6",
        "text_primary": "#111827",  # Dark gray
        "text_secondary": "#6B7280",  # Medium gray
        "text_disabled": "#9CA3AF",  # Light gray
        "border": "#E5E7EB",
        "border_focus": "#3B82F6",
        "shadow": "rgba(0, 0, 0, 0.1)",
    },
    # Dark Theme
    "dark": {
        "primary": "#3B82F6",  # Blue bright
        "primary_hover": "#2563EB",
        "primary_light": "#1E3A8A",
        "secondary": "#A78BFA",  # Purple light
        "secondary_hover": "#8B5CF6",
        "success": "#34D399",  # Green light
        "warning": "#FBBF24",  # Orange light
        "error": "#F87171",  # Red light
        "background": "#111827",  # Dark
        "surface": "#1F2937",  # Dark gray
        "surface_elevated": "#374151",
        "text_primary": "#F9FAFB",  # Light
        "text_secondary": "#D1D5DB",  # Light gray
        "text_disabled": "#9CA3AF",  # Medium gray
        "border": "#374151",
        "border_focus": "#60A5FA",
        "shadow": "rgba(0, 0, 0, 0.3)",
    },
    # High Contrast Theme (Accessibility)
    "high_contrast": {
        "primary": "#FFFF00",  # Bright yellow
        "primary_hover": "#FFCC00",
        "primary_light": "#FFFFAA",
        "secondary": "#00FFFF",  # Cyan
        "secondary_hover": "#00CCCC",
        "success": "#00FF00",  # Bright green
        "warning": "#FF8800",  # Bright orange
        "error": "#FF0000",  # Bright red
        "background": "#000000",  # Pure black
        "surface": "#000000",  # Pure black
        "surface_elevated": "#1A1A1A",
        "text_primary": "#FFFFFF",  # Pure white
        "text_secondary": "#FFFFFF",  # Pure white
        "text_disabled": "#808080",  # Medium gray
        "border": "#FFFFFF",  # Pure white
        "border_focus": "#FFFF00",  # Bright yellow
        "shadow": "rgba(255, 255, 255, 0.3)",
    },
    # Solarized Dark Theme
    "solarized": {
        "primary": "#268BD2",  # Blue
        "primary_hover": "#2AA198",
        "primary_light": "#073642",
        "secondary": "#6C71C4",  # Violet
        "secondary_hover": "#859900",
        "success": "#859900",  # Green
        "warning": "#B58900",  # Yellow
        "error": "#DC322F",  # Red
        "background": "#002B36",  # Base03
        "surface": "#073642",  # Base02
        "surface_elevated": "#586E75",
        "text_primary": "#839496",  # Base0
        "text_secondary": "#93A1A1",  # Base1
        "text_disabled": "#657B83",  # Base00
        "border": "#586E75",  # Base01
        "border_focus": "#268BD2",
        "shadow": "rgba(0, 0, 0, 0.5)",
    },
    # Solarized Light Theme
    "solarized_light": {
        "primary": "#268BD2",  # Blue
        "primary_hover": "#2AA198",
        "primary_light": "#EEE8D5",
        "secondary": "#6C71C4",  # Violet
        "secondary_hover": "#859900",
        "success": "#859900",  # Green
        "warning": "#B58900",  # Yellow
        "error": "#DC322F",  # Red
        "background": "#FDF6E3",  # Base3
        "surface": "#EEE8D5",  # Base2
        "surface_elevated": "#93A1A1",
        "text_primary": "#657B83",  # Base00
        "text_secondary": "#586E75",  # Base01
        "text_disabled": "#93A1A1",  # Base1
        "border": "#93A1A1",  # Base1
        "border_focus": "#268BD2",
        "shadow": "rgba(0, 0, 0, 0.1)",
    },
}

# Typography
FONTS = {
    "heading_large": ("Segoe UI", 24, "bold"),
    "heading_medium": ("Segoe UI", 18, "bold"),
    "heading_small": ("Segoe UI", 14, "bold"),
    "body_large": ("Segoe UI", 12),
    "body_medium": ("Segoe UI", 11),
    "body_small": ("Segoe UI", 10),
    "code": ("Consolas", 10),
    "button": ("Segoe UI", 11, "bold"),
}

# Spacing System (8px base)
SPACING = {
    "xs": 4,
    "sm": 8,
    "md": 16,
    "lg": 24,
    "xl": 32,
    "2xl": 48,
}

# Border Radius
RADIUS = {
    "sm": 4,
    "md": 8,
    "lg": 12,
    "xl": 16,
    "full": 999,
}

# Shadows
SHADOWS = {
    "sm": "2 2 8",
    "md": "4 4 12",
    "lg": "8 8 24",
}

# Icons (Unicode symbols - works without external dependencies)
ICONS = {
    "text": "📝",
    "font": "🔤",
    "size": "📏",
    "spacing": "↔️",
    "outline": "⬚",
    "color": "🎨",
    "file": "📄",
    "folder": "📁",
    "save": "💾",
    "refresh": "🔄",
    "settings": "⚙️",
    "preview": "👁️",
    "generate": "⚡",
    "success": "✓",
    "error": "✗",
    "info": "ℹ️",
    "warning": "⚠️",
    "search": "🔍",
    "close": "✕",
    "moon": "🌙",
    "sun": "☀️",
    "star": "⭐",
    "heart": "❤️",
    "3d": "🎲",
}

# Animation Durations (ms)
ANIMATIONS = {
    "fast": 150,
    "normal": 250,
    "slow": 400,
}


class Theme:
    """Theme manager for the application."""

    # Available themes in cycle order
    AVAILABLE_THEMES = ["light", "dark", "high_contrast", "solarized", "solarized_light"]

    def __init__(self, mode: str = "light"):
        """
        Initialize theme.

        Args:
            mode: Theme name (light, dark, high_contrast, solarized, solarized_light)
        """
        if mode not in COLORS:
            mode = "light"  # Fallback to light if invalid
        self.mode = mode
        self._listeners = []

    def get_color(self, key: str) -> str:
        """Get color from current theme."""
        return COLORS[self.mode].get(key, "#000000")

    def toggle(self) -> str:
        """Cycle to next theme."""
        try:
            current_index = self.AVAILABLE_THEMES.index(self.mode)
            next_index = (current_index + 1) % len(self.AVAILABLE_THEMES)
            self.mode = self.AVAILABLE_THEMES[next_index]
        except ValueError:
            self.mode = "light"  # Fallback if current mode not in list

        self._notify_listeners()
        return self.mode

    def set_mode(self, mode: str) -> None:
        """
        Set specific theme mode.

        Args:
            mode: Theme name
        """
        if mode in COLORS:
            self.mode = mode
            self._notify_listeners()

    def get_theme_name(self) -> str:
        """Get friendly name for current theme."""
        names = {
            "light": "Clair",
            "dark": "Sombre",
            "high_contrast": "Contraste Élevé",
            "solarized": "Solarized Sombre",
            "solarized_light": "Solarized Clair",
        }
        return names.get(self.mode, self.mode)

    def add_listener(self, callback) -> None:
        """Add theme change listener."""
        self._listeners.append(callback)

    def _notify_listeners(self) -> None:
        """Notify all listeners of theme change."""
        for callback in self._listeners:
            callback(self.mode)


def get_font(key: str) -> Tuple:
    """Get font configuration."""
    return FONTS.get(key, FONTS["body_medium"])


def get_spacing(key: str) -> int:
    """Get spacing value."""
    return SPACING.get(key, SPACING["md"])


def get_radius(key: str) -> int:
    """Get border radius."""
    return RADIUS.get(key, RADIUS["md"])


def get_icon(key: str) -> str:
    """Get icon character."""
    return ICONS.get(key, "")


# Gradient generator
def create_gradient(color1: str, color2: str) -> str:
    """Create CSS-like gradient string (for future use)."""
    return f"linear-gradient({color1}, {color2})"
