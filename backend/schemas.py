from pydantic import BaseModel


class TripRequest(BaseModel):
    source: str
    destination: str
    days: int
    travellers: int
    budget: int
    preferences: str


class TripResponse(BaseModel):
    itinerary: str
    estimated_cost: int