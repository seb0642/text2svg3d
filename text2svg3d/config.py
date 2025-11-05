"""Configuration and constants for text2svg3d."""

import json
import logging
from pathlib import Path
from typing import List

logger = logging.getLogger(__name__)

# Default values
DEFAULT_SIZE_MM: float = 20.0

# Output directory - use system-appropriate paths
# Try Desktop first (most user-friendly), fallback to Documents
_desktop = Path.home() / "Desktop" / "text2svg3d_output"
_documents = Path.home() / "Documents" / "text2svg3d_output"
_home = Path.home() / "text2svg3d_output"

# Check which directory is most appropriate
if (Path.home() / "Desktop").exists():
    DEFAULT_OUTPUT_DIR: Path = _desktop
elif (Path.home() / "Documents").exists():
    DEFAULT_OUTPUT_DIR: Path = _documents
else:
    DEFAULT_OUTPUT_DIR: Path = _home

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

# User preferences directory
PREFERENCES_DIR: Path = Path.home() / ".config" / "text2svg3d"
THEME_PREF_FILE: Path = PREFERENCES_DIR / "theme.json"
HISTORY_FILE: Path = PREFERENCES_DIR / "history.json"


# Theme preference functions
def save_theme_preference(mode: str) -> None:
    """
    Save theme preference to user config.

    Args:
        mode: Theme mode ("light" or "dark")
    """
    try:
        PREFERENCES_DIR.mkdir(parents=True, exist_ok=True, mode=0o700)
        with open(THEME_PREF_FILE, "w") as f:
            json.dump({"theme": mode, "version": "1.0"}, f, indent=2)
        logger.debug(f"Theme preference saved: {mode}")
    except (OSError, IOError, PermissionError) as e:
        logger.warning(f"Failed to save theme preference: {e}")
    except Exception as e:
        logger.error(f"Unexpected error saving theme preference: {e}")


def load_theme_preference() -> str:
    """
    Load theme preference from user config.

    Returns:
        Theme mode ("light" or "dark"), defaults to "light"
    """
    try:
        if THEME_PREF_FILE.exists():
            with open(THEME_PREF_FILE, "r") as f:
                data = json.load(f)
                theme = data.get("theme", "light")
                if theme in ("light", "dark"):
                    logger.debug(f"Theme preference loaded: {theme}")
                    return theme
    except (OSError, IOError, PermissionError) as e:
        logger.debug(f"Failed to load theme preference: {e}")
    except json.JSONDecodeError as e:
        logger.warning(f"Corrupt theme preference file: {e}")
    except Exception as e:
        logger.error(f"Unexpected error loading theme preference: {e}")

    # Default to light theme
    return "light"


# History functions
def save_generation_history(entry: dict) -> None:
    """
    Save a generation entry to history.

    Args:
        entry: Dictionary with generation parameters and result
    """
    try:
        PREFERENCES_DIR.mkdir(parents=True, exist_ok=True, mode=0o700)

        # Load existing history
        history = []
        if HISTORY_FILE.exists():
            with open(HISTORY_FILE, "r") as f:
                data = json.load(f)
                history = data.get("entries", [])

        # Add new entry (limit to last 50)
        history.insert(0, entry)
        history = history[:50]

        # Save updated history
        with open(HISTORY_FILE, "w") as f:
            json.dump({"version": "1.0", "entries": history}, f, indent=2)

        logger.debug("Generation history entry saved")
    except (OSError, IOError, PermissionError) as e:
        logger.warning(f"Failed to save generation history: {e}")
    except Exception as e:
        logger.error(f"Unexpected error saving generation history: {e}")


def load_generation_history() -> List[dict]:
    """
    Load generation history.

    Returns:
        List of generation history entries
    """
    try:
        if HISTORY_FILE.exists():
            with open(HISTORY_FILE, "r") as f:
                data = json.load(f)
                entries = data.get("entries", [])
                logger.debug(f"Loaded {len(entries)} history entries")
                return entries
    except (OSError, IOError, PermissionError) as e:
        logger.debug(f"Failed to load generation history: {e}")
    except json.JSONDecodeError as e:
        logger.warning(f"Corrupt history file: {e}")
    except Exception as e:
        logger.error(f"Unexpected error loading generation history: {e}")

    return []


# Language preference file
LANGUAGE_PREF_FILE: Path = PREFERENCES_DIR / "language.json"


# Language preference functions
def save_language_preference(language: str) -> None:
    """
    Save user's language preference.

    Args:
        language: Language code (e.g., "en_US", "fr_FR")
    """
    try:
        PREFERENCES_DIR.mkdir(parents=True, exist_ok=True, mode=0o700)

        with open(LANGUAGE_PREF_FILE, "w") as f:
            json.dump({"language": language, "version": "1.0"}, f, indent=2)

        logger.debug(f"Language preference saved: {language}")
    except (OSError, IOError, PermissionError) as e:
        logger.warning(f"Failed to save language preference: {e}")
    except Exception as e:
        logger.error(f"Unexpected error saving language preference: {e}")


def load_language_preference() -> str:
    """
    Load user's language preference.

    Returns:
        Language code (defaults to system locale or "fr_FR")
    """
    try:
        if LANGUAGE_PREF_FILE.exists():
            with open(LANGUAGE_PREF_FILE, "r") as f:
                data = json.load(f)
                language = data.get("language", "fr_FR")
                logger.debug(f"Loaded language preference: {language}")
                return language
    except (OSError, IOError, PermissionError) as e:
        logger.debug(f"Failed to load language preference: {e}")
    except json.JSONDecodeError as e:
        logger.warning(f"Corrupt language preference file: {e}")
    except Exception as e:
        logger.error(f"Unexpected error loading language preference: {e}")

    # Default to French (original language)
    return "fr_FR"
