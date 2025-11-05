"""Font management - scanning and locating system fonts."""

import json
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from fontTools import ttLib

from .config import CACHE_FILE, FONT_DIRECTORIES, FONT_EXTENSIONS


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
                continue

            for ext in FONT_EXTENSIONS:
                for font_path in font_dir.rglob(f"*{ext}"):
                    try:
                        family_name = self._get_font_family_name(font_path)
                        if family_name:
                            # Store first occurrence of each family name
                            if family_name not in self.fonts:
                                self.fonts[family_name] = font_path
                    except Exception:
                        # Skip fonts that can't be read
                        continue

    def _get_font_family_name(self, font_path: Path) -> Optional[str]:
        """
        Extract the family name from a font file.

        Args:
            font_path: Path to the font file

        Returns:
            Family name or None if not found
        """
        try:
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

        except Exception:
            pass

        return None

    def _save_to_cache(self) -> None:
        """Save font list to cache file."""
        try:
            CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
            cache_data = {name: str(path) for name, path in self.fonts.items()}
            with open(CACHE_FILE, "w") as f:
                json.dump(cache_data, f, indent=2)
        except Exception:
            # Cache is optional, ignore errors
            pass

    def _load_from_cache(self) -> None:
        """Load font list from cache file."""
        try:
            with open(CACHE_FILE, "r") as f:
                cache_data = json.load(f)
                self.fonts = {name: Path(path) for name, path in cache_data.items()}
        except Exception:
            # If cache is invalid, scan system
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
        except Exception:
            pass
