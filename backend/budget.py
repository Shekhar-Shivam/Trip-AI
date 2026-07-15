"""
Simple Budget Estimator

Uses fixed assumptions to estimate the overall trip cost.
This is sufficient for the demo.
"""

from backend.state import TripState


def estimate_trip_cost(state: TripState) -> int:
    """
    Estimate total trip cost.

    Assumptions (per traveller):
    - Hotel: ₹2000/night
    - Food: ₹800/day
    - Local Transport: ₹500/day
    - Intercity Travel: ₹2000/person
    """

    hotel_cost = 2000 * state["days"] * state["travellers"]

    food_cost = 800 * state["days"] * state["travellers"]

    local_transport = 500 * state["days"] * state["travellers"]

    intercity_travel = 2000 * state["travellers"]

    total_cost = (
        hotel_cost
        + food_cost
        + local_transport
        + intercity_travel
    )

    return total_cost