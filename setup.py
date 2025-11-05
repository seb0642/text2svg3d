"""Setup script for text2svg3d."""

from setuptools import setup, find_packages
from pathlib import Path

# Read long description from README
readme_file = Path(__file__).parent / "README.md"
long_description = ""
if readme_file.exists():
    long_description = readme_file.read_text(encoding="utf-8")

setup(
    name="text2svg3d",
    version="1.0.0",
    author="text2svg3d",
    description="Convert text to SVG for 3D printing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/text2svg3d",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Manufacturing",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
        "Topic :: Printing",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.10",
    install_requires=[
        "fonttools>=4.38.0",
        "freetype-py>=2.3.0",
        "svgwrite>=1.4.3",
    ],
    entry_points={
        "console_scripts": [
            "text2svg3d=text2svg3d.__main__:main",
            "text2svg3d-gui=text2svg3d.gui:main",
        ],
    },
    keywords="svg 3d-printing font text conversion vector",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/text2svg3d/issues",
        "Source": "https://github.com/yourusername/text2svg3d",
    },
)
