"""Configuration and constants for text2svg3d."""

from pathlib import Path
from typing import List

# Default values
DEFAULT_SIZE_MM: float = 20.0
DEFAULT_OUTPUT_DIR: Path = Path.home() / "Bureau" / "ready to blender"
DEFAULT_OUTPUT_FILE: str = str(DEFAULT_OUTPUT_DIR / "output.svg")
DEFAULT_THICKNESS_MM: float = 2.0
DEFAULT_LETTER_SPACING_MM: float = 0.0
DEFAULT_COORDINATE_PRECISION: int = 2

# Font directories to scan (Linux standard locations)
FONT_DIRECTORIES: List[Path] = [
    Path("/usr/share/fonts/"),
    Path("/usr/local/share/fonts/"),
    Path.home() / ".local" / "share" / "fonts",
    Path.home() / ".fonts",
]

# Supported font extensions
FONT_EXTENSIONS: List[str] = [".ttf", ".otf"]

# SVG constants
SVG_UNITS: str = "mm"
SVG_NAMESPACE: str = "http://www.w3.org/2000/svg"

# FreeType constants (convert from font units to mm)
# Standard DPI for conversion
DPI: int = 72

# Cache file for font list (optional, for performance)
CACHE_FILE: Path = Path.home() / ".cache" / "text2svg3d" / "fonts.cache"
