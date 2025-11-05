# Project Structure

This document describes the organization of the text2svg3d project.

## Directory Layout

```
text2svg3d/
├── text2svg3d/              # Main package directory
│   ├── __init__.py          # Package initialization
│   ├── __main__.py          # CLI entry point
│   ├── config.py            # Configuration constants
│   ├── font_manager.py      # Font scanning and management
│   ├── glyph_converter.py   # Glyph to vector conversion
│   └── svg_builder.py       # SVG document generation
│
├── tests/                   # Test suite
│   ├── __init__.py
│   ├── test_font_manager.py # Font manager tests
│   └── test_svg_output.py   # SVG generation tests
│
├── examples/                # Example scripts and outputs
│   └── example_usage.py     # Programmatic usage example
│
├── setup.py                 # Package installation configuration
├── requirements.txt         # Python dependencies
├── README.md               # Main documentation
├── INSTALL.md              # Installation instructions
├── QUICKSTART.md           # Quick start guide
├── LICENSE                 # MIT License
└── .gitignore              # Git ignore rules
```

## Module Descriptions

### text2svg3d/config.py
- Defines default values for all parameters
- Lists standard font directories to scan
- Configures SVG output settings
- Sets precision for coordinate output

### text2svg3d/font_manager.py
Contains the `FontManager` class which:
- Scans system directories for TrueType/OpenType fonts
- Extracts font family names using fontTools
- Provides font search and filtering capabilities
- Implements caching for improved performance
- Offers case-insensitive font matching

### text2svg3d/glyph_converter.py
Contains the `GlyphConverter` class which:
- Loads fonts using FreeType
- Converts individual characters to glyph outlines
- Transforms FreeType contours to SVG path commands
- Handles quadratic Bézier curves
- Manages coordinate system transformations
- Calculates text dimensions and advance widths
- Implements letter spacing

### text2svg3d/svg_builder.py
Contains the `SVGBuilder` class which:
- Creates SVG documents using svgwrite
- Positions glyphs with proper spacing
- Adds metadata and comments to SVG
- Ensures paths are closed (end with 'Z')
- Sets fill-rule for letters with holes
- Formats coordinates with configurable precision
- Outputs properly formatted XML

### text2svg3d/__main__.py
- Implements the command-line interface using argparse
- Handles all CLI arguments and options
- Provides --list-fonts functionality
- Manages error messages and user feedback
- Coordinates between font_manager, glyph_converter, and svg_builder
- Implements verbose and preview modes

## Data Flow

```
User Input (CLI)
      ↓
   __main__.py
      ↓
   FontManager → Find font file
      ↓
   GlyphConverter → Convert text to glyph outlines
      ↓
   SVGBuilder → Generate SVG file
      ↓
   Output SVG file
```

## Key Design Decisions

### 1. Separation of Concerns
Each module has a single responsibility:
- Font management is isolated from conversion
- Conversion is separate from SVG generation
- CLI logic doesn't mix with core functionality

### 2. Type Hints
All functions use Python type hints for better IDE support and documentation.

### 3. Named Tuples
Used for structured data (Point, GlyphOutline) for clarity and immutability.

### 4. Error Handling
- Graceful handling of missing fonts
- Clear error messages for users
- Skips unsupported characters with warnings
- Optional verbose mode for debugging

### 5. Configurability
All default values are in config.py for easy modification.

### 6. Caching
Optional font cache to improve startup time on subsequent runs.

### 7. SVG Optimization for 3D Printing
- Absolute coordinates only
- All paths closed with 'Z'
- Proper fill-rule for compound paths
- Real-world units (millimeters)
- Metadata for traceability

## Testing Strategy

### Unit Tests
- `test_font_manager.py`: Tests font discovery and filtering
- `test_svg_output.py`: Tests SVG generation and validation

### Integration Tests
Manual testing workflow:
1. Install dependencies
2. List fonts
3. Generate test SVG
4. Import to 3D slicer
5. Verify printability

## Dependencies

### Core Dependencies
- **fonttools**: Reading TrueType/OpenType font files
- **freetype-py**: Rendering glyphs and extracting outlines
- **svgwrite**: Creating SVG documents

### System Dependencies
- libfreetype6-dev: FreeType development files
- Python 3.10+: Modern Python features

## Extension Points

The architecture allows for easy extensions:

1. **New output formats**: Add modules similar to svg_builder.py
2. **Font preprocessing**: Hook into font_manager before conversion
3. **Path optimization**: Enhance glyph_converter path generation
4. **GUI interface**: Import core modules into GUI application
5. **Web service**: Wrap in Flask/FastAPI for web access

## Performance Considerations

- Font caching reduces repeated filesystem scans
- Lazy loading of fonts (only load when needed)
- Coordinate precision configurable for file size vs. accuracy tradeoff
- Minimal dependencies for fast installation

## Security Notes

- No user input is executed as code
- File paths are validated using Path objects
- No network access required
- Only reads font files (no modifications to system)
- Output files respect user permissions

## Future Improvements

Potential enhancements not in current scope:
- Vertical text support
- Advanced kerning using font metrics
- Support for font ligatures
- Direct STL export
- Batch processing mode
- Configuration file support
- Font subsetting for specific character sets
- Cubic Bézier curve support
- Multi-line text support
