# Migration Guide: Python 3.12+ and Dependencies Update

This document outlines the changes made to migrate `lark-oapi-compact` to support Python 3.12+ and upgrade all dependencies to their latest versions.

## Overview

- **Migration Date**: December 2025
- **Python Version**: `>=3.7` → `>=3.12`
- **Major Changes**: Dropped support for Python versions below 3.12, upgraded all dependencies to latest versions

## Breaking Changes

### 1. Python Version Support
- **Minimum Python version changed from 3.7 to 3.12**
- Supported Python versions: 3.12, 3.13, 3.14
- Impact: Users must upgrade their Python interpreter to version 3.12 or higher

### 2. Pydantic Major Version Upgrade
- **Pydantic v1.10.18 → v2.12.0+**
- Pydantic v2 introduced breaking changes in API and behavior
- Impact: Code using Pydantic v1 specific features may need updates

## Dependency Updates

### Core Dependencies
| Package | Old Version | New Version | Change Type |
|---------|-------------|-------------|-------------|
| `lark-oapi` | `1.3.4` | `1.4.24` | Feature update |
| `pydantic` | `1.10.18` | `>=2.12.0` | **Major upgrade** |
| `attrs` | `>=23.2.0` | `>=25.4.0` | Feature update |
| `pycryptodome` | `>=3.20.0` | `>=3.23.0` | Feature update |
| `requests` | `>=2.31.0` | `>=2.32.5` | Feature update |
| `typing_extensions` | unversioned | `>=4.15.0` | Version pin |

### Development Dependencies
| Package | Old Version | New Version | Change Type |
|---------|-------------|-------------|-------------|
| `ipython` | `>=7.34.0` | `>=8.37.0` | Feature update |
| `pre-commit` | `>=2.21.0` | `>=4.5.0` | Feature update |
| `pytest-cov` | `>=4.1.0` | `>=7.0.0` | Feature update |
| `pytest` | `>=7.4.4` | `>=9.0.2` | Feature update |
| `ruff` | `>=0.6.8` | `>=0.14.9` | Feature update |

## Configuration Changes

### 1. UV Configuration
- **Before**: Used deprecated `tool.uv.dev-dependencies`
- **After**: Migrated to modern `dependency-groups.dev` format
- **Impact**: Better alignment with latest UV standards

### 2. Ruff Configuration
- **Target Python version**: `py37` → `py312`
- **Impact**: Enables Python 3.12+ specific linting rules and optimizations

### 3. Project Classifiers
Updated Python version classifiers in `pyproject.toml`:
- Added: `Programming Language :: Python :: 3.12`
- Added: `Programming Language :: Python :: 3.13`
- Added: `Programming Language :: Python :: 3.14`
- Removed: `Programming Language :: Python :: 3.7`

## Code Quality Improvements

### Fixed Issues
1. Removed unused `typing.Optional` imports
2. Updated deprecated `typing.Dict`, `typing.List`, `typing.Tuple` to built-in `dict`, `list`, `tuple`
3. All Ruff linting issues resolved

### Benefits
- Better performance with Python 3.12+ optimizations
- Enhanced security with latest dependency versions
- Improved type checking and IDE support
- Access to modern Python features

## Migration Steps for Users

### Prerequisites
```bash
# Ensure you have Python 3.12+ installed
python --version  # Should show 3.12.x or higher
```

### Installation
```bash
# Install the latest version
pip install "lark-oapi-compact>=0.1.3"

# Or upgrade existing installation
pip install --upgrade "lark-oapi-compact>=0.1.3"
```

### Potential Code Changes (Pydantic v2)

If you're using Pydantic v1 specific features, you may need:

1. **Import Changes**:
   ```python
   # Pydantic v1
   from pydantic import BaseModel

   # Pydantic v2 (compatible)
   from pydantic import BaseModel
   ```

2. **Validation Changes**:
   - Pydantic v2 has stricter validation
   - Some validation behaviors have changed
   - Check the [Pydantic migration guide](https://docs.pydantic.dev/latest/migration/) for details

## Testing

- All existing tests pass with Python 3.13.11
- No breaking changes to the public API
- Backward compatibility maintained for core functionality

## Performance Improvements

### Python 3.12+ Benefits
- Faster performance due to Python optimizations
- Better error messages and debugging
- Improved type hinting support
- Enhanced memory management

### Dependency Benefits
- Latest security patches
- Performance optimizations
- Modern Python feature support

## Troubleshooting

### Common Issues

1. **Python Version Error**:
   ```
   ERROR: Package requires a different Python: 3.12.x not in '<3.12'
   ```
   **Solution**: Upgrade your Python interpreter to 3.12 or higher

2. **Pydantic Import Errors**:
   ```
   ImportError: cannot import name 'BaseModel' from 'pydantic'
   ```
   **Solution**: Ensure you have Pydantic v2 installed: `pip install "pydantic>=2.0"`

3. **Dependency Conflicts**:
   **Solution**: Use a fresh virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install "lark-oapi-compact>=0.1.3"
   ```

## Getting Help

- **Issues**: Report on [GitHub Issues](https://github.com/StrayDragon/oapi-sdk-python-compact/issues)
- **Documentation**: [Project README](https://github.com/StrayDragon/oapi-sdk-python-compact/blob/main/README.md)
- **Pydantic Migration**: [Official Pydantic Migration Guide](https://docs.pydantic.dev/latest/migration/)

## Future Considerations

This migration positions the project well for future Python releases and ensures continued access to the latest Python features and security updates.