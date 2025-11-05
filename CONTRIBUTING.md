# Contributing to text2svg3d

Thank you for your interest in contributing to text2svg3d! This document provides guidelines and instructions for contributing.

## Code of Conduct

Please be respectful and constructive in all interactions with the project.

## Development Setup

### Prerequisites

- Python 3.10 or higher
- Git
- Linux system (Ubuntu/Debian recommended)

### Setting up development environment

```bash
# Clone the repository
git clone https://github.com/yourusername/text2svg3d.git
cd text2svg3d

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install in development mode with dev dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

## Development Workflow

### 1. Code Style

We use several tools to maintain code quality:

- **Black**: Code formatting
- **isort**: Import sorting
- **flake8**: Linting
- **mypy**: Type checking

Run all formatters and linters:

```bash
# Format code
black text2svg3d tests
isort text2svg3d tests

# Check linting
flake8 text2svg3d tests

# Type check
mypy text2svg3d
```

Or let pre-commit handle it automatically:

```bash
pre-commit run --all-files
```

### 2. Testing

We aim for 70%+ test coverage. Write tests for all new features and bug fixes.

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=text2svg3d --cov-report=term-missing

# Run specific test file
pytest tests/test_font_manager.py

# Run specific test
pytest tests/test_font_manager.py::TestFontManager::test_list_fonts
```

### 3. Making Changes

1. **Create a branch**:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/issue-description
   ```

2. **Make your changes**:
   - Write clean, readable code
   - Follow PEP 8 style guide
   - Add type hints
   - Write docstrings for public APIs
   - Add unit tests

3. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```

   Good commit messages:
   - Start with a verb (Add, Fix, Update, Remove, etc.)
   - Keep first line under 50 characters
   - Add detailed description if needed

4. **Push and create PR**:
   ```bash
   git push origin feature/your-feature-name
   ```

## Code Guidelines

### Python Style

- **Line length**: 100 characters max
- **Imports**: Grouped and sorted by isort
- **Naming**:
  - `snake_case` for functions and variables
  - `PascalCase` for classes
  - `UPPER_CASE` for constants
- **Type hints**: Use for function signatures
- **Docstrings**: Use Google style

Example:

```python
from pathlib import Path
from typing import List, Optional

def process_font(font_path: Path, size_mm: float) -> Optional[List[str]]:
    """
    Process a font file and extract information.

    Args:
        font_path: Path to the font file
        size_mm: Desired size in millimeters

    Returns:
        List of font information or None if processing fails

    Raises:
        FileNotFoundError: If font file does not exist
        ValueError: If size_mm is out of valid range
    """
    if not font_path.exists():
        raise FileNotFoundError(f"Font not found: {font_path}")

    if not 0.1 <= size_mm <= 1000:
        raise ValueError(f"size_mm must be 0.1-1000, got {size_mm}")

    # Implementation here
    pass
```

### Error Handling

- Use specific exceptions, not generic `Exception`
- Always provide context in error messages
- Use logging for non-critical errors
- Validate inputs early

Bad:
```python
try:
    # some operation
    pass
except Exception:
    pass
```

Good:
```python
import logging

logger = logging.getLogger(__name__)

try:
    # some operation
    pass
except (IOError, OSError) as e:
    logger.warning(f"Failed to read file: {e}")
except ValueError as e:
    logger.error(f"Invalid value: {e}")
    raise
```

### Logging

Use appropriate log levels:

- `DEBUG`: Detailed diagnostic information
- `INFO`: General informational messages
- `WARNING`: Something unexpected but handled
- `ERROR`: Serious problem, operation failed

```python
import logging

logger = logging.getLogger(__name__)

logger.debug(f"Processing font: {font_path}")
logger.info(f"Loaded {len(fonts)} fonts from cache")
logger.warning(f"Font cache is outdated, rescanning")
logger.error(f"Failed to parse font: {e}")
```

### Testing

Write tests that:

- Test one thing at a time
- Have clear, descriptive names
- Use fixtures for setup
- Mock external dependencies
- Cover edge cases and error conditions

Example:

```python
import pytest
from pathlib import Path
from text2svg3d.font_manager import FontManager

class TestFontManager:
    def test_load_fonts_success(self):
        """Test that fonts can be loaded successfully."""
        fm = FontManager(use_cache=False)
        fonts = fm.list_fonts()
        assert isinstance(fonts, list)

    def test_get_font_path_not_found(self):
        """Test that None is returned for non-existent font."""
        fm = FontManager(use_cache=False)
        result = fm.get_font_path("NonExistentFont123")
        assert result is None

    def test_validate_size_mm_out_of_range(self):
        """Test that ValueError is raised for invalid size."""
        with pytest.raises(ValueError, match="size_mm must be"):
            GlyphConverter(Path("/tmp/font.ttf"), -1.0)
```

## Project Structure

```
text2svg3d/
├── text2svg3d/          # Main package
│   ├── __init__.py      # Package initialization
│   ├── __main__.py      # CLI entry point
│   ├── config.py        # Configuration constants
│   ├── font_manager.py  # Font scanning and management
│   ├── glyph_converter.py # Glyph to vector conversion
│   ├── svg_builder.py   # SVG document generation
│   └── gui.py           # GUI application
├── tests/               # Test files
│   ├── test_font_manager.py
│   ├── test_svg_output.py
│   └── ...
├── examples/            # Example scripts
├── .github/workflows/   # CI/CD configuration
├── pyproject.toml       # Project configuration
├── setup.py             # Setup script (legacy)
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

## Reporting Issues

When reporting bugs, please include:

1. **Description**: Clear description of the issue
2. **Steps to reproduce**: Minimal code to reproduce
3. **Expected behavior**: What should happen
4. **Actual behavior**: What actually happens
5. **Environment**:
   - OS and version
   - Python version
   - text2svg3d version
6. **Error messages**: Full traceback if available

## Feature Requests

For feature requests, please describe:

1. **Use case**: What problem does this solve?
2. **Proposed solution**: How should it work?
3. **Alternatives**: Have you considered alternatives?
4. **Examples**: Example usage code

## Pull Request Process

1. **Update tests**: Add tests for new features
2. **Update documentation**: Update README, docstrings, etc.
3. **Run all checks**: Ensure tests, linting, and formatting pass
4. **Keep PRs focused**: One feature/fix per PR
5. **Describe changes**: Clear description of what and why

### PR Checklist

- [ ] Code follows project style guidelines
- [ ] All tests pass
- [ ] New tests added for new features
- [ ] Documentation updated
- [ ] Type hints added
- [ ] Logging added where appropriate
- [ ] No unnecessary dependencies added
- [ ] Commit messages are clear
- [ ] PR description is clear

## Release Process

(For maintainers)

1. Update version in `__init__.py` and `pyproject.toml`
2. Update CHANGELOG.md
3. Create git tag: `git tag v1.x.x`
4. Push tag: `git push --tags`
5. CI will automatically build and publish

## Questions?

If you have questions, feel free to:

- Open an issue with the "question" label
- Check existing issues and discussions
- Read the documentation

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
