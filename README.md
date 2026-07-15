# 🇮🇳 Bharat Trip Planner
AI-powered multi-agent travel planner for India.

---
## Demo Scenario
Suppose I want to travel:

Delhi → Manali

3 Days
2 Travellers
Budget ₹25,000

Instead of opening multiple websites, I simply enter these details, and the AI generates a personalized itinerary automatically.

## Output Sceenshots 

in /screenshots folder

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
                    USER

                      │
                      ▼

               Streamlit UI

                      │
                      ▼

                 FastAPI API

                      │
                      ▼

                 LangGraph

               ┌─────────────┐
               │             │
               ▼             │
          Planner Agent ◄────┘
               │
               ▼
         Tool Executor

      ┌────────┼────────┐
      ▼        ▼        ▼

   Search   Weather   Travel

      │        │        │
      └────────┼────────┘
               ▼

         Tool Results

               ▼

         Budget Agent

               ▼

       Budget Validation
          |           | 
  (under budget)   (over budget) ─────   REPLAN ──────────────► Planner Agent
          |         
          │         
          ▼         
      Itinerary 
      Generator  (LLM)    
          |           
          |  
          ▼

         END     
                    
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