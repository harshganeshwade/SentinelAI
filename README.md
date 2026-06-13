# SentinelAI

SentinelAI is an autonomous security investigation and response platform for Splunk. It provides AI-powered incident summarization, root cause analysis, MITRE ATT&CK mapping, remediation recommendations, and executive reporting.

## Project Structure

- `backend/` — FastAPI backend, AI agent placeholders, Splunk integration helpers
- `frontend/` — React + Tailwind dashboard
- `sample-data/` — sample alerts, logs, and incidents for demo use
- `docs/` — architecture and feature documentation
- `docker-compose.yml` — container orchestration for backend and frontend

## Getting Started

### Backend

1. Create a virtual environment:

```bash
python -m venv .venv
```

2. Activate the environment:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Start the backend:

```bash
uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend

1. From `frontend/` install dependencies:

```bash
cd frontend
npm install
```

2. Start the frontend:

```bash
npm run dev
```

## Environment Variables

Create a `.env` file at the repository root and add your keys there. This file is already ignored by `.gitignore`.

- `OPENAI_API_KEY` — OpenAI API key for AI agent integration
- `SPLUNK_BASE_URL` — Splunk REST endpoint, for example `https://splunk.example.com:8089`
- `SPLUNK_TOKEN` — Splunk API token used for Bearer authentication
- `SPLUNK_VERIFY_SSL` — optional; set to `false` if using a self-signed certificate (default is `true`)

Example `.env`:

```env
OPENAI_API_KEY=your-openai-key
SPLUNK_BASE_URL=https://splunk.example.com:8089
SPLUNK_TOKEN=your-splunk-token
SPLUNK_VERIFY_SSL=true
```

## Available APIs

- `GET /incidents`
- `GET /incident/{id}`
- `POST /investigate`
- `POST /generate-report`
- `POST /recommend-actions`
- `POST /chat`

## Notes

This repository provides a starter scaffolding for SentinelAI. The AI integration and Splunk connectivity are implemented as placeholders and can be extended for production use.

## GitHub Repository

This project is published publicly at:

- https://github.com/harshganeshwade/SentinelAI

## Important

- The `.env` file is intentionally excluded from source control.
- Keep your API keys and Splunk token private.
- Build artifacts in `frontend/dist/` are not tracked in git.
