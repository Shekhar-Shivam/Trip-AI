"""
travel_tool.get_transport(
    "Delhi",
    "Jaipur"
)
"""

from tools.search import search_tool


class TravelTool:

    def get_transport(
        self,
        source: str,
        destination: str
    ):

        query = f"""
Best travel options from
{source}
to
{destination}

Mention

Train

Bus

Flight

Road

Approximate travel time.
"""

        return search_tool.search(query)


travel_tool = TravelTool()