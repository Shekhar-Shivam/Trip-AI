"""
Prompt templates for Bharat Trip Planner.
"""


PLANNER_PROMPT = """
You are an AI Travel Planner.

The user wants to plan a trip.

Source:
{source}

Destination:
{destination}

Days:
{days}

Travellers:
{travellers}

Preferences:
{preferences}

Your job is to decide what information needs to be collected.

Return ONLY valid JSON.

Example:

{{
    "tasks": [
        {{
            "tool": "search",
            "query": "Top tourist attractions in Goa"
        }},
        {{
            "tool": "search",
            "query": "Best local food in Goa"
        }},
        {{
            "tool": "weather",
            "city": "Goa"
        }},
        {{
            "tool": "travel",
            "source": "Delhi",
            "destination": "Goa"
        }}
    ]
}}
"""


ITINERARY_PROMPT = """
You are an expert India travel planner.

Generate a detailed {days}-day itinerary.

Trip Details

Source:
{source}

Destination:
{destination}

Travellers:
{travellers}

Budget:
₹{budget}

Preferences:
{preferences}

Use the following live information collected from external tools:

{tool_results}

Create a well-structured itinerary in Markdown.

Include:

1. Best way to travel from source to destination
2. Weather summary
3. Day-wise itinerary
4. Tourist attractions
5. Local food recommendations
6. Hotel recommendations
7. Approximate total trip cost
8. Budget-saving tips
"""


REPLAN_PROMPT = """
You are an expert travel planner.

The previously generated itinerary exceeded the user's budget.

Trip Details

Source:
{source}

Destination:
{destination}

Days:
{days}

Travellers:
{travellers}

Preferences:
{preferences}

Estimated Cost:
₹{estimated_cost}

Maximum Budget:
₹{budget}

Below is the information collected from the internet:

{tool_results}

Generate a NEW itinerary that is more budget-friendly.

Rules:

- Prefer trains or buses instead of flights.
- Recommend budget hotels.
- Suggest affordable local restaurants.
- Prioritize free or low-cost attractions.
- Keep the same number of days.
- Keep the trip enjoyable.

Return the itinerary in Markdown.
"""