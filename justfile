# justfile for lark-oapi-compact

# Default recipe - lists all available recipes
default:
    @just --list

# Run tests with pytest
test:
    uv run pytest
