"""Internationalization (i18n) support for text2svg3d."""

import gettext
import locale
import logging
from pathlib import Path
from typing import Callable

logger = logging.getLogger(__name__)

# Locale directory
LOCALE_DIR = Path(__file__).parent / "locales"

# Current translation function
_translate: Callable[[str], str] = lambda s: s  # Default: no translation


def setup_i18n(language: str = None) -> None:
    """
    Setup internationalization.

    Args:
        language: Language code (e.g., "fr_FR", "en_US", "es_ES", "de_DE")
                  If None, auto-detect from system locale
    """
    global _translate

    try:
        # Auto-detect if not specified
        if language is None:
            try:
                language, _ = locale.getdefaultlocale()
                logger.info(f"Auto-detected system locale: {language}")
            except Exception as e:
                logger.warning(f"Failed to auto-detect locale: {e}, using French")
                language = "fr_FR"

        # Try to load translation
        try:
            # Use GNU gettext with explicit UTF-8 encoding
            translation = gettext.translation(
                "text2svg3d",
                localedir=str(LOCALE_DIR),
                languages=[language],
                fallback=False,
            )
            # Explicitly use UTF-8 strings (Python 3 default)
            _translate = translation.gettext
            logger.info(f"Loaded translation for: {language}")

        except FileNotFoundError:
            # Fallback to French (default)
            logger.warning(f"Translation file not found for {language}, " f"using French (default)")
            # No translation needed, source is French

            def _no_translate(s: str) -> str:
                return s

            _translate = _no_translate

    except Exception as e:
        # Use repr() to avoid encoding issues in error messages
        logger.error(f"Failed to setup i18n: {repr(e)}")
        # Fallback to no translation

        def _fallback_translate(s: str) -> str:
            return s

        _translate = _fallback_translate


def _(message: str) -> str:
    """
    Translate a message.

    Args:
        message: Message to translate (in French)

    Returns:
        Translated message
    """
    return _translate(message)


def get_available_languages() -> list:
    """
    Get list of available language codes.

    Returns:
        List of language codes (e.g., ["fr_FR", "en_US", "es_ES"])
    """
    available = ["fr_FR"]  # French is always available (source language)

    if LOCALE_DIR.exists():
        for lang_dir in LOCALE_DIR.iterdir():
            if lang_dir.is_dir() and (lang_dir / "LC_MESSAGES" / "text2svg3d.mo").exists():
                available.append(lang_dir.name)

    return sorted(available)


def get_language_name(code: str) -> str:
    """
    Get friendly name for language code.

    Args:
        code: Language code

    Returns:
        Friendly name
    """
    names = {
        "fr_FR": "Français",
        "en_US": "English",
        "es_ES": "Español",
        "de_DE": "Deutsch",
    }
    return names.get(code, code)
