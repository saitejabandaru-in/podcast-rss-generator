"""Package installation and distribution guide."""

# Installation

## From PyPI (Recommended)

```bash
pip install podcast-rss-generator
```

## From Source

```bash
git clone https://github.com/saitejabandaru-in/podcast-test.git
cd podcast-test
pip install -e .
```

## Development Installation

```bash
git clone https://github.com/saitejabandaru-in/podcast-test.git
cd podcast-test
pip install -e ".[dev]"
```

# Usage

## Command Line

```bash
podcast-rss-generator --input feed.yaml --output podcast.xml
```

Or using default filenames:

```bash
podcast-rss-generator
```

## Python API

```python
from podcast_rss_generator import generate_rss_feed

# Generate RSS feed from YAML
output_path = generate_rss_feed("feed.yaml", "podcast.xml")
print(f"Feed generated: {output_path}")
```

# Publishing to PyPI

## Build the Package

```bash
pip install build twine
python -m build
```

## Upload to TestPyPI (Optional)

```bash
python -m twine upload --repository testpypi dist/*
```

## Upload to PyPI

```bash
python -m twine upload dist/*
```

## Version Update

Update version in:
- `pyproject.toml`
- `setup.py`
- `podcast_rss_generator/__init__.py`

Then rebuild and upload.
