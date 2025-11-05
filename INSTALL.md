# Installation Instructions

## Prerequisites

This application requires Python 3.10+ and pip to be installed on your system.

### Installing pip on Linux

If pip is not installed, you can install it with:

```bash
# On Debian/Ubuntu
sudo apt update
sudo apt install python3-pip

# On Fedora
sudo dnf install python3-pip

# On Arch Linux
sudo pacman -S python-pip
```

### Installing System Dependencies

Some of the Python libraries require system packages:

```bash
# On Debian/Ubuntu
sudo apt install python3-dev libfreetype6-dev

# On Fedora
sudo dnf install python3-devel freetype-devel

# On Arch Linux
sudo pacman -S python freetype2
```

## Installation

### Option 1: Install in development mode (recommended for testing)

```bash
cd text2svg3d
pip install -e .
```

### Option 2: Install dependencies manually

```bash
cd text2svg3d
pip install -r requirements.txt
```

Then run with:
```bash
python -m text2svg3d "Your Text"
```

### Option 3: Install system-wide

```bash
cd text2svg3d
pip install .
```

## Verify Installation

```bash
# Check version
text2svg3d --version

# List available fonts
text2svg3d --list-fonts

# Create a test SVG
text2svg3d -o test.svg "Hello"
```

## Troubleshooting

### ModuleNotFoundError: No module named 'pip'

Install pip using your system package manager (see above).

### Permission denied when installing

Use `--user` flag:
```bash
pip install --user -e .
```

Or use a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

### freetype-py compilation errors

Install libfreetype development files:
```bash
sudo apt install libfreetype6-dev
```
