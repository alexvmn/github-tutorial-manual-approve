# git-workflow-to-prod

Tiny example app + tests for learning a Git workflow up to prod.

## Run
python -m app.main

## Test (with uv)
uv sync --group dev
uv run pytest -q
