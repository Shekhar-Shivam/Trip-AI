from typing import TypedDict, List, Dict, Any


class TripState(TypedDict):

    # -------------------------
    # User Input
    # -------------------------

    source: str
    destination: str
    days: int
    travellers: int
    budget: int
    preferences: str

    # -------------------------
    # Planner Output
    # -------------------------

    tasks: List[Dict[str, Any]]

    # -------------------------
    # Tool Outputs
    # -------------------------

    tool_results: Dict[str, Any]

    # -------------------------
    # Final Output
    # -------------------------

    itinerary: str

    estimated_cost: int

    budget_ok: bool

    budget_mode: bool

    # -------------------------
    # Workflow
    # -------------------------

    retry_count: int