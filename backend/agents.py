import json

from backend.state import TripState
from backend.llm import llm_service
from backend.budget import estimate_trip_cost

from backend.prompts import (
    PLANNER_PROMPT,
    ITINERARY_PROMPT,
    REPLAN_PROMPT,
)


# ----------------------------------------------------------
# Planner Agent
# ----------------------------------------------------------

def planner_node(state: TripState) -> TripState:
    """
    Decide which tools should be executed.
    """

    prompt = PLANNER_PROMPT.format(
        source=state["source"],
        destination=state["destination"],
        days=state["days"],
        travellers=state["travellers"],
        preferences=state["preferences"],
    )

    response = llm_service.invoke(prompt)

    try:
        state["tasks"] = json.loads(response)["tasks"]

    except Exception:

        # Fallback if LLM doesn't return valid JSON
        state["tasks"] = [

            {
                "tool": "search",
                "query": f"Top tourist attractions in {state['destination']}"
            },

            {
                "tool": "search",
                "query": f"Best food in {state['destination']}"
            },

            {
                "tool": "weather",
                "city": state["destination"]
            },

            {
                "tool": "travel",
                "source": state["source"],
                "destination": state["destination"]
            }

        ]

    return state


# ----------------------------------------------------------
# Itinerary Generator
# ----------------------------------------------------------

def itinerary_node(state: TripState) -> TripState:
    """
    Generate the final itinerary using tool results.
    """

    prompt = ITINERARY_PROMPT.format(
        source=state["source"],
        destination=state["destination"],
        days=state["days"],
        travellers=state["travellers"],
        budget=state["budget"],
        preferences=state["preferences"],
        tool_results=json.dumps(
            state["tool_results"],
            indent=2
        )
    )

    itinerary = llm_service.invoke(prompt)

    state["itinerary"] = itinerary

    return state


# ----------------------------------------------------------
# Budget Agent
# ----------------------------------------------------------

def budget_node(state: TripState) -> TripState:
    """
    Estimate trip cost.
    """

    state["estimated_cost"] = estimate_trip_cost(state)

    state["budget_ok"] = (

        state["estimated_cost"]

        <=

        state["budget"]

    )

    return state


# ----------------------------------------------------------
# Replan Agent
# ----------------------------------------------------------

def replan_node(state: TripState) -> TripState:
    """
    Generate a cheaper itinerary.
    """
    prompt = REPLAN_PROMPT.format(
        source=state["source"],
        destination=state["destination"],
        days=state["days"],
        travellers=state["travellers"],
        preferences=state["preferences"],
        estimated_cost=state["estimated_cost"],
        budget=state["budget"],
        tool_results=json.dumps(
            state["tool_results"],
            indent=2
        )
    )
    itinerary = llm_service.invoke(prompt)

    state["itinerary"] = itinerary

    return state