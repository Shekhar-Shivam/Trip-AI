"""
search_places()
travel_options()
weather()
packing_list()

Planner->search_places()->Tavily API->Planner

run : python backend/mcp_server.py
"""

from fastmcp import FastMCP

from backend.tools.search import search_tool
from backend.tools.weather import weather_tool
from backend.tools.travel import travel_tool


mcp = FastMCP(
    "Trip Planner MCP"
)


@mcp.tool()
def search_places(query: str):

    """
    Search tourist places.
    """

    return search_tool.search(query)


@mcp.tool()
def weather(city: str):

    """
    Get weather.
    """

    return weather_tool.get_weather(city)


@mcp.tool()
def travel_options(
    source: str,
    destination: str
):

    """
    Get travel suggestions.
    """

    return travel_tool.get_transport(
        source,
        destination
    )


if __name__ == "__main__":
    mcp.run()