# Publishing Guide for PyPI

This guide explains how to publish the `podcast-rss-generator` package to PyPI (Python Package Index).

## 📋 Pre-Publication Checklist

- [x] Package structure created
- [x] setup.py and pyproject.toml configured  
- [x] CLI entry point defined
- [x] Dependencies specified (pyyaml)
- [x] README with examples
- [x] License file (MIT)
- [x] Tests added
- [x] Code is on GitHub

## 🔧 Setup for Publishing

### 1. Create PyPI Account

Visit [https://pypi.org/account/register/](https://pypi.org/account/register/) and create an account.

### 2. Create API Token

1. Go to [PyPI Account Settings](https://pypi.org/manage/account/)
2. Click "Add API token"
3. Name it something like "podcast-rss-generator-publish"
4. Select "Entire account"
5. Copy the token (starts with `pypi-`)

### 3. Configure Local Credentials

Create or edit `~/.pypirc`:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = __token__
password = pypi-YOUR_TOKEN_HERE

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-YOUR_TEST_TOKEN_HERE
```

Or use keyring (recommended):

```bash
pip install keyring
keyring set https://upload.pypi.org/legacy/ __token__
# Then enter your PyPI token when prompted
```

## 🚀 Publishing Steps

### Step 1: Install Build Tools

```bash
pip install build twine
```

### Step 2: Update Version

Update version number in three places:

**1. `pyproject.toml`:**
```toml
version = "1.0.1"
```

**2. `setup.py`:**
```python
version="1.0.1",
```

**3. `podcast_rss_generator/__init__.py`:**
```python
__version__ = "1.0.1"
```

### Step 3: Build Distribution

```bash
cd /workspaces/podcast-test
python -m build
```

This creates:
- `dist/podcast-rss-generator-1.0.1.tar.gz` (source distribution)
- `dist/podcast-rss-generator-1.0.1-py3-none-any.whl` (wheel)

### Step 4: Test on TestPyPI (Optional but Recommended)

```bash
python -m twine upload --repository testpypi dist/*
```

Then test installation:

```bash
pip install --index-url https://test.pypi.org/simple/ podcast-rss-generator
```

### Step 5: Upload to PyPI

```bash
python -m twine upload dist/*
```

You'll be prompted for your username and password (or token).

### Step 6: Verify Publication

Visit [https://pypi.org/project/podcast-rss-generator/](https://pypi.org/project/podcast-rss-generator/)

## 📦 After Publication

### Installation Command

Users can now install with:

```bash
pip install podcast-rss-generator
```

### Update Documentation

Update README and docs to show installation:

```markdown
## Installation

```bash
pip install podcast-rss-generator
```
```

### Create GitHub Release

```bash
git tag v1.0.1
git push origin v1.0.1
```

Then create a release on GitHub with release notes.

## 🔄 Publishing Future Updates

For each new version:

1. Update version numbers (as above)
2. Update `CHANGELOG.md` if you have one
3. Commit and push to GitHub
4. Build: `python -m build`
5. Upload: `python -m twine upload dist/*`
6. Create GitHub release/tag

## 📚 Useful Commands

```bash
# Check package metadata
python -m twine check dist/*

# Upload with verbose output
python -m twine upload dist/* -v

# Upload specific file
python -m twine upload dist/podcast-rss-generator-1.0.1.tar.gz

# Check package info
python setup.py --long-description | rst2html.py > output.html
```

## 🐛 Troubleshooting

### "File already exists"
Don't re-upload same version. Increment version and rebuild.

### "Invalid distribution"
Run: `python -m twine check dist/*` to find issues.

### "Unauthorized"
Check token in `~/.pypirc` or run `keyring set` again.

### "403 Forbidden"
Ensure you have permission and correct credentials.

## 📖 Resources

- [PyPI Help](https://pypi.org/help/)
- [Setuptools Documentation](https://setuptools.pypa.io/)
- [Twine Documentation](https://twine.readthedocs.io/)
- [PEP 517 - Build System](https://www.python.org/dev/peps/pep-0517/)

---

**Package Details:**
- Package Name: `podcast-rss-generator`
- PyPI URL: `https://pypi.org/project/podcast-rss-generator/`
- Repository: `https://github.com/saitejabandaru-in/podcast-test`
- License: MIT
- Python: 3.6+
