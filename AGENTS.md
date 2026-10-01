# Base44 Dev Environment

## Project Overview
Python book generator using AI (OpenAI API or local Ollama) to create educational/technical books in PDF and EPUB.

A Flask web UI (`app.py`) was added so the app is visible in the browser preview on port 3000. The original CLI (`main.py`) still works.

## Architecture
- `app.py` — Flask web server (port 3000, debug mode) with a form UI for book generation
- `main.py` — Original CLI entry point
- `generators/` — AI handlers: `openai_handler.py` (OpenAI API), `local_handler.py` (Ollama)
- `formatters/` — `pdf_formatter.py` (reportlab), `epub_formatter.py` (ebooklib)
- `config.py` — Loads env vars via python-dotenv; creates `output/` and `templates/` dirs
- `output/` — Generated books (created at runtime, downloadable via web UI)

## Running
```bash
docker compose -f docker-compose.base44.yml up -d --build
```

## Key Notes
- `openai_handler.py` was updated for the openai 1.x API (`client.chat.completions.create` instead of the removed `openai.ChatCompletion.create`)
- `OPENAI_API_KEY` is needed for AI generation; without a real key the UI loads but generation returns an auth error
- Ollama (local model) path requires a running Ollama service with a pulled model — not included in compose
- Flask runs in debug mode for auto-reload during development
- Dependencies install on container startup via pip (bind-mounted source, no rebuild needed for code edits)
