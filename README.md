# FastAPI

A small FastAPI learning project with a health-check endpoint and foundational API examples.

## Requirements

- Python 3.10+

Install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run the API

```powershell
uvicorn main:app --reload
```

The API is available at `http://127.0.0.1:8000`. Interactive API documentation is available at `/docs`.

The `01-fastapi-foundations.py` file contains additional foundational examples.
