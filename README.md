# 🇮🇳 Bharat Trip Planner

AI-powered multi-agent travel planner for India.

---

## Features

- Multi-Agent Workflow using LangGraph
- FastAPI Backend
- Streamlit Frontend
- Gemini LLM
- Tavily Internet Search
- Weather Information
- Travel Suggestions
- Budget Validation
- Conditional Replanning

---

## Architecture

Streamlit

↓

FastAPI

↓

LangGraph

↓

Planner Agent

↓

Tool Executor

↓

Internet APIs

↓

Itinerary Generator

↓

Budget Agent

↓

Conditional Replan

---

## Installation

### Clone

```bash
git clone <repo-url>

cd bharat-trip-planner
```

### Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

Install

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create

```
.env
```

Example

```
GEMINI_API_KEY=xxxxxxxxxxxxxxxx

TAVILY_API_KEY=xxxxxxxxxxxxxxxx

MODEL_NAME=gemini-2.5-flash

TEMPERATURE=0.3
```

---

## Run Backend

```bash
uvicorn backend.main:app --reload
```

Backend

```
http://localhost:8000
```

Swagger

```
http://localhost:8000/docs
```

---

## Run Frontend

```bash
streamlit run frontend/streamlit.py
```

Open

```
http://localhost:8501
```

---

## Docker

```bash
docker compose up --build
```

---

## Inputs

- Source
- Destination
- Days
- Travellers
- Budget
- Preferences

---

## Outputs

- Day-wise itinerary
- Places to visit
- Weather
- Travel suggestions
- Estimated cost