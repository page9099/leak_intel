# LeakIntel FastAPI backend

## Quick start (local)

```bash
# in repo root
cd backend

# install Poetry & deps
pip install poetry
poetry install

# run dev server
poetry run uvicorn app.main:app --reload
```

Visit http://127.0.0.1:8000/docs for Swagger UI.
