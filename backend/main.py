"""
uvicorn backend.main:app --reload
http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.schemas import (
    TripRequest,
    TripResponse
)

from backend.graph import graph


app = FastAPI(
    title="Bharat Trip Planner",
    version="1.0"
)


# Allow Streamlit frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Bharat Trip Planner API is running"
    }


@app.post(
    "/plan-trip",
    response_model=TripResponse
)
def plan_trip(request: TripRequest):

    initial_state = {

        "source": request.source,

        "destination": request.destination,

        "days": request.days,

        "travellers": request.travellers,

        "budget": request.budget,

        "preferences": request.preferences,

        "tasks": [],

        "tool_results": {},

        "itinerary": "",

        "estimated_cost": 0,

        "budget_ok": False,

        "retry_count": 0
    }

    result = graph.invoke(initial_state)

    return TripResponse(

        itinerary=result["itinerary"],

        estimated_cost=result["estimated_cost"]

    )