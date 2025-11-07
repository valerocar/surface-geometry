# Repository Guidelines

## Project Structure & Module Organization
Keep core automation logic under `src/` with each agent in its own module (e.g., `src/planner`, `src/executor`). Shared prompts and fixtures live in `assets/`, configuration defaults go to `config/agents.yml`, and CLI or maintenance helpers belong in `scripts/`. Tests mirror the structure inside `tests/`, so `tests/planner/test_planner.py` exercises `src/planner/`.

## Build, Test, and Development Commands
- `python -m venv .venv && source .venv/bin/activate`: create and enter the project environment before any work.
- `pip install -r requirements.txt -r requirements-dev.txt`: install runtime plus lint/test extras.
- `python -m src.cli --agent planner --dry-run`: run an agent locally with debugging output.
- `pytest -q`: execute the unit test suite; add `--maxfail=1` when iterating quickly.
- `make lint`: run Black and Ruff to enforce formatting and static checks.

## Coding Style & Naming Conventions
Use Black with an 88-character line width and Ruff for linting; `make lint` must pass before committing. Prefer type hints and docstrings describing inputs and outputs. Modules stay snake_case, classes are PascalCase, and agent identifiers such as `planner_agent` stay lowercase with underscores. Keep functions focused on a single responsibility and move shared utilities into `src/common/`.

## Testing Guidelines
Pytest discovers files matching `tests/**/test_*.py`. Mirror production modules and keep fixtures in `tests/conftest.py`. New features require at least one focused unit test plus a scenario test that exercises the end-to-end agent loop. Aim for 85% or higher coverage, verified with `pytest --cov=src --cov-report=term-missing`.

## Commit & Pull Request Guidelines
Follow Conventional Commits (`feat: add planner memory cache`) so release notes can be generated automatically. Commits should be scoped to one concern and include updated docs and tests. Pull requests need a summary, linked issue ID, test evidence (command output or screenshots), and any deployment considerations. Request review from another agent maintainer before merging.
