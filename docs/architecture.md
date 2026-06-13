# SentinelAI Architecture

## Overview

SentinelAI is a layered security investigation platform integrating a React frontend, Python FastAPI backend, AI reasoning layer, and Splunk connectivity.

## Architecture Components

- Frontend
  - React + Tailwind UI
  - Dashboard, Incident Center, Investigation Chat, Reports, Settings
- Backend
  - FastAPI service for REST APIs
  - AI agent placeholders for summarization, root cause analysis, MITRE mapping, response recommendations, and report generation
- AI Layer
  - Uses OpenAI GPT API when `OPENAI_API_KEY` is provided
  - Provides natural language investigation, incident summarization, and response advising
- Splunk Integration
  - Placeholder Splunk client for fetching alerts and log search
  - Can be extended to call Splunk REST and SPL Search APIs
- Data
  - `sample-data/` contains sample logs, alerts, and incidents for demo mode

## Deployment

- `docker-compose.yml` defines backend and frontend services
- Backend exposes port `8000`
- Frontend exposes port `5173`

## Data Flow

1. User interacts with the React dashboard
2. Frontend calls backend APIs
3. Backend queries Splunk or sample data
4. AI layer analyzes alert data and returns summaries
5. Reports and remediation suggestions are generated
