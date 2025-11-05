"""Modern design system for text2svg3d GUI."""

from typing import Dict, Tuple

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

    def __init__(self, mode: str = "light"):
        """
        Initialize theme.

        Args:
            mode: "light" or "dark"
        """
        self.mode = mode
        self._listeners = []

    def get_color(self, key: str) -> str:
        """Get color from current theme."""
        return COLORS[self.mode].get(key, "#000000")

    def toggle(self) -> str:
        """Toggle between light and dark mode."""
        self.mode = "dark" if self.mode == "light" else "light"
        self._notify_listeners()
        return self.mode

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
