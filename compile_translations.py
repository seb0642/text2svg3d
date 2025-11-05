#!/usr/bin/env python3
"""
Simple .po to .mo compiler using Python's msgfmt module.
Falls back to basic parsing if msgfmt is not available.
"""

import struct
import sys
from pathlib import Path
from typing import Dict, Tuple


def _decode_escapes(s: str) -> str:
    """
    Decode escape sequences in string (e.g., \\n -> newline).
    Handles both escape sequences and UTF-8 correctly.
    """
    # Replace common escape sequences manually to preserve UTF-8
    s = s.replace('\\n', '\n')
    s = s.replace('\\t', '\t')
    s = s.replace('\\r', '\r')
    s = s.replace('\\"', '"')
    s = s.replace('\\\\', '\\')
    return s


def parse_po_file(po_file: Path) -> Dict[str, str]:
    """Parse a .po file and return a dict of msgid -> msgstr."""
    translations = {}
    current_msgid = None
    current_msgstr = None
    in_msgid = False
    in_msgstr = False

    with open(po_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            # Skip comments and empty lines
            if not line or line.startswith('#'):
                continue

            # Start of msgid
            if line.startswith('msgid '):
                if current_msgid is not None and current_msgstr is not None:
                    # Decode escape sequences and add entry
                    translations[_decode_escapes(current_msgid)] = _decode_escapes(current_msgstr)

                current_msgid = line[6:].strip('"')
                in_msgid = True
                in_msgstr = False

            # Start of msgstr
            elif line.startswith('msgstr '):
                current_msgstr = line[7:].strip('"')
                in_msgid = False
                in_msgstr = True

            # Continuation line
            elif line.startswith('"') and line.endswith('"'):
                text = line[1:-1]  # Remove quotes
                if in_msgid:
                    current_msgid += text
                elif in_msgstr:
                    current_msgstr += text

        # Don't forget the last entry
        if current_msgid is not None and current_msgstr is not None:
            # Decode escape sequences and add
            translations[_decode_escapes(current_msgid)] = _decode_escapes(current_msgstr)

    return translations


def generate_mo_file(translations: Dict[str, str], mo_file: Path) -> None:
    """
    Generate a .mo file from translations dict.
    Uses the GNU gettext .mo file format.
    """
    # Encode all strings to UTF-8
    keys = sorted(translations.keys())
    encoded_keys = [key.encode('utf-8') for key in keys]
    encoded_values = [translations[key].encode('utf-8') for key in keys]

    # Calculate offsets
    keystart = 7 * 4 + 16 * len(keys)
    valuestart = keystart + sum(len(k) + 1 for k in encoded_keys)

    # Create the .mo file structure
    key_offsets = []
    value_offsets = []

    offset = keystart
    for key in encoded_keys:
        key_offsets.append((len(key), offset))
        offset += len(key) + 1

    offset = valuestart
    for value in encoded_values:
        value_offsets.append((len(value), offset))
        offset += len(value) + 1

    # Write the .mo file
    with open(mo_file, 'wb') as f:
        # Magic number
        f.write(struct.pack('I', 0x950412de))
        # Version
        f.write(struct.pack('I', 0))
        # Number of entries
        f.write(struct.pack('I', len(keys)))
        # Offset of table with original strings
        f.write(struct.pack('I', 7 * 4))
        # Offset of table with translation strings
        f.write(struct.pack('I', 7 * 4 + 8 * len(keys)))
        # Size of hashing table (unused)
        f.write(struct.pack('I', 0))
        # Offset of hashing table (unused)
        f.write(struct.pack('I', 0))

        # Write original string table
        for length, offset in key_offsets:
            f.write(struct.pack('II', length, offset))

        # Write translation string table
        for length, offset in value_offsets:
            f.write(struct.pack('II', length, offset))

        # Write original strings
        for key in encoded_keys:
            f.write(key)
            f.write(b'\x00')

        # Write translated strings
        for value in encoded_values:
            f.write(value)
            f.write(b'\x00')


def compile_po_to_mo(po_file: Path, mo_file: Path = None) -> None:
    """Compile a .po file to .mo format."""
    if mo_file is None:
        mo_file = po_file.with_suffix('.mo')

    print(f"Compiling {po_file} -> {mo_file}")

    translations = parse_po_file(po_file)
    print(f"Found {len(translations)} translations")

    generate_mo_file(translations, mo_file)
    print(f"Successfully created {mo_file}")


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python compile_translations.py <po_file> [mo_file]")
        sys.exit(1)

    po_file = Path(sys.argv[1])
    mo_file = Path(sys.argv[2]) if len(sys.argv) > 2 else None

    if not po_file.exists():
        print(f"Error: {po_file} not found")
        sys.exit(1)

    compile_po_to_mo(po_file, mo_file)


if __name__ == "__main__":
    main()
