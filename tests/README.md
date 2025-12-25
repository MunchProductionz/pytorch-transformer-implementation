# Tests

This directory contains test suites for the project.

## Structure

- `unit/` - Unit tests for individual components
- `integration/` - Integration tests for component interactions
- `conftest.py` - Shared pytest fixtures and configuration

## Usage

Run tests using pytest:
```bash
uv run pytest tests/
```

Run specific test categories:
```bash
uv run pytest tests/unit/
uv run pytest tests/integration/
```
