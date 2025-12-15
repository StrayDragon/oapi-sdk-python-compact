# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is `lark-oapi-compact`, a Python SDK for Lark (Feishu) OpenAPI that provides enhanced functionality and convenience shortcuts on top of the official SDK. It merges code from multiple branches of the upstream repository and adds user-friendly shortcut functions.

### Key Architecture

- **Main Package**: `src/lark_oapi_compact/` - The main SDK package
- **Shortcut Modules**: `src/lark_oapi_compact/shortcut/` - High-level convenience APIs
  - `compact/` - Core settings and configuration (51 lines)
  - `driver/` - File system and drive operations (341 lines)
  - `group_robot/` - Group robot messaging (87 lines)
  - `message/` - Message handling (42 lines)
  - `sheets/` - Spreadsheet operations with rich data models (695 lines)
  - `utils/` - Utility functions (34 lines)
- **Legacy Code**: `src/lark_oapi_compact/remaintain/` - Backward compatibility code from older SDK versions

The shortcut modules provide simplified APIs for common operations like:
- Spreadsheet manipulation with cell ranges and data type support
- File/folder operations in Lark Drive
- Group robot messaging with webhook support
- Message handling and utilities

## Development Setup

### Environment Setup
```bash
# Install dependencies
uv sync --all-extras --dev

# Activate virtual environment
uv venv
source .venv/bin/activate  # On Linux/Mac
```

### Pre-commit Hooks
```bash
pre-commit install
```

### Testing Configuration

Tests require real Feishu API credentials. Copy `.env.example` to `.env` and configure:

```bash
cp .env.example .env
source .env
```

Required environment variables:
- `FEISHU_APP_ID` - Feishu application ID
- `FEISHU_APP_SECRET` - Feishu application secret
- `FEISHU_GROUP_ROBOT_WEBHOOK_URL` - (Optional) Group robot webhook URL
- `FEISHU_GROUP_ROBOT_SIGN_SECRET` - (Optional) Group robot signature secret

## Common Commands

### Development
```bash
# Install dependencies
uv sync --all-extras --dev

# Linting (auto-fix enabled)
uv run ruff check src/lark_oapi_compact/shortcut/
uv run ruff format src/lark_oapi_compact/shortcut/

# Check formatting without fixing
uv run ruff format --check src/lark_oapi_compact/shortcut/
```

### Testing
```bash
# Run all tests with coverage
uv run pytest tests/ --cov=src/lark_oapi_compact/shortcut --cov-report=xml

# Run specific test files
uv run pytest tests/test_utils.py -v
uv run pytest tests/test_sheets.py -v
uv run pytest tests/test_driver.py -v
uv run pytest tests/test_group_robot.py -v

# Run tests without live API calls
FEISHU_SKIP_LIVE_TESTS=true uv run pytest tests/ -v
```

### Python Version
- **Target**: Python 3.12+
- **Supported**: 3.12, 3.13, 3.14
- Uses modern `dependency-groups.dev` format for uv

## Code Quality Tools

- **Ruff**: Linting and formatting (configured in `pyproject.toml`)
- **Pre-commit**: Hooks for code quality (configured in `.pre-commit-config.yaml`)
- **pytest**: Testing with fixtures in `tests/conftest.py`
- **Coverage**: Tracked for shortcut modules only

## Important Notes

- The `remaintain/extra/` directory is excluded from pre-commit hooks
- Line length limit: 120 characters
- Code formatting uses double quotes and space indentation
- Tests use session-scoped fixtures for efficient API client reuse
- Migration to Python 3.12+ completed in December 2025 (see `MIGRATE.md`)