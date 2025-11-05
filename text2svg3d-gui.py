#!/usr/bin/env python3
"""
Launcher script for text2svg3d GUI.

This script can be run directly without installation:
    python3 text2svg3d-gui.py

Or make it executable:
    chmod +x text2svg3d-gui.py
    ./text2svg3d-gui.py
"""

import sys
from pathlib import Path

# Add the text2svg3d package to path
sys.path.insert(0, str(Path(__file__).parent))

# Import and run the GUI
from text2svg3d.gui import main

if __name__ == "__main__":
    main()
