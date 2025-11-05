"""Font management - scanning and locating system fonts."""

import json
import logging
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from fontTools import ttLib
from fontTools.ttLib import TTLibError

from .config import CACHE_FILE, FONT_DIRECTORIES, FONT_EXTENSIONS

# Setup logging
logger = logging.getLogger(__name__)


class FontManager:
    """Manages system font discovery and access."""

    def __init__(self, use_cache: bool = True) -> None:
        """
        Initialize the FontManager.

        Args:
            use_cache: Whether to use cached font list for performance
        """
        self.use_cache = use_cache
        self.fonts: Dict[str, Path] = {}
        self._load_fonts()

    def _load_fonts(self) -> None:
        """Load available fonts from system or cache."""
        if self.use_cache and CACHE_FILE.exists():
            self._load_from_cache()
        else:
            self._scan_system_fonts()
            if self.use_cache:
                self._save_to_cache()

    def _scan_system_fonts(self) -> None:
        """Scan system directories for TrueType and OpenType fonts."""
        for font_dir in FONT_DIRECTORIES:
            if not font_dir.exists():
                logger.debug(f"Font directory does not exist: {font_dir}")
                continue

            for ext in FONT_EXTENSIONS:
                for font_path in font_dir.rglob(f"*{ext}"):
                    try:
                        family_name = self._get_font_family_name(font_path)
                        if family_name:
                            # Store first occurrence of each family name
                            if family_name not in self.fonts:
                                self.fonts[family_name] = font_path
                                logger.debug(f"Found font: {family_name} at {font_path}")
                    except (TTLibError, OSError, PermissionError) as e:
                        # Skip fonts that can't be read (corrupt, no permission, etc.)
                        logger.debug(f"Failed to read font {font_path}: {e}")
                        continue
                    except Exception as e:
                        # Unexpected error - log as warning
                        logger.warning(f"Unexpected error reading font {font_path}: {e}")

    def _get_font_family_name(self, font_path: Path) -> Optional[str]:
        """
        Extract the family name from a font file.

        Args:
            font_path: Path to the font file

        Returns:
            Family name or None if not found

        Raises:
            TTLibError: If font file is corrupt or invalid
            OSError: If file cannot be accessed
        """
        font = ttLib.TTFont(str(font_path))
        name_table = font["name"]

        # Try to get the family name (nameID 1)
        # Prefer English (platformID 3, platEncID 1, langID 0x409)
        for record in name_table.names:
            if record.nameID == 1:  # Font Family name
                if record.platformID == 3 and record.langID == 0x409:
                    return record.toUnicode()

        # Fallback to any family name
        for record in name_table.names:
            if record.nameID == 1:
                return record.toUnicode()

        return None

    def _save_to_cache(self) -> None:
        """Save font list to cache file."""
        try:
            CACHE_FILE.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
            cache_data = {
                "version": "1.0",
                "fonts": {name: str(path) for name, path in self.fonts.items()},
            }
            with open(CACHE_FILE, "w") as f:
                json.dump(cache_data, f, indent=2)
            logger.debug(f"Font cache saved to {CACHE_FILE}")
        except (OSError, IOError, PermissionError) as e:
            # Cache is optional, log but don't fail
            logger.warning(f"Failed to save font cache: {e}")
        except Exception as e:
            logger.error(f"Unexpected error saving font cache: {e}")

    def _load_from_cache(self) -> None:
        """Load font list from cache file."""
        try:
            with open(CACHE_FILE, "r") as f:
                cache_data = json.load(f)

            # Validate cache format
            if isinstance(cache_data, dict):
                # New format with version
                if "version" in cache_data and "fonts" in cache_data:
                    if cache_data["version"] == "1.0":
                        self.fonts = {
                            name: Path(path) for name, path in cache_data["fonts"].items()
                        }
                        logger.debug(f"Loaded {len(self.fonts)} fonts from cache")
                        return
                    else:
                        logger.warning(f"Unsupported cache version: {cache_data['version']}")
                # Old format (direct dict)
                elif all(isinstance(v, str) for v in cache_data.values()):
                    logger.info("Upgrading old cache format")
                    self.fonts = {name: Path(path) for name, path in cache_data.items()}
                    # Save in new format
                    self._save_to_cache()
                    return

            # Invalid format
            logger.warning("Invalid cache format, rescanning fonts")
            self._scan_system_fonts()

        except (OSError, IOError, PermissionError) as e:
            logger.warning(f"Failed to load font cache: {e}, rescanning fonts")
            self._scan_system_fonts()
        except json.JSONDecodeError as e:
            logger.warning(f"Corrupt font cache: {e}, rescanning fonts")
            self._scan_system_fonts()
        except Exception as e:
            logger.error(f"Unexpected error loading cache: {e}, rescanning fonts")
            self._scan_system_fonts()

    def list_fonts(self, filter_regex: Optional[str] = None) -> List[Tuple[str, Path]]:
        """
        List all available fonts, optionally filtered by regex.

        Args:
            filter_regex: Optional regex pattern to filter font names

        Returns:
            List of (font_name, font_path) tuples, sorted by name
        """
        fonts = list(self.fonts.items())

        if filter_regex:
            try:
                pattern = re.compile(filter_regex, re.IGNORECASE)
                fonts = [(name, path) for name, path in fonts if pattern.search(name)]
            except re.error:
                # Invalid regex, return all fonts
                pass

        return sorted(fonts, key=lambda x: x[0].lower())

    def get_font_path(self, font_name: str) -> Optional[Path]:
        """
        Get the path to a font file by family name.

        Args:
            font_name: Font family name (case-insensitive)

        Returns:
            Path to font file or None if not found
        """
        # Try exact match first
        for name, path in self.fonts.items():
            if name.lower() == font_name.lower():
                return path

        return None

    def find_similar_fonts(self, font_name: str, limit: int = 5) -> List[str]:
        """
        Find fonts with similar names.

        Args:
            font_name: Font name to search for
            limit: Maximum number of suggestions

        Returns:
            List of similar font names
        """
        font_name_lower = font_name.lower()
        similar = []

        for name in self.fonts.keys():
            if font_name_lower in name.lower():
                similar.append(name)

        return sorted(similar, key=lambda x: len(x))[:limit]

    def clear_cache(self) -> None:
        """Clear the font cache file."""
        try:
            if CACHE_FILE.exists():
                CACHE_FILE.unlink()
                logger.info("Font cache cleared")
        except (OSError, PermissionError) as e:
            logger.error(f"Failed to clear font cache: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error clearing cache: {e}")
            raise
