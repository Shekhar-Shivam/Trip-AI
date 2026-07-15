"""
MCP Client

Responsible for talking to the MCP Server.

The graph never directly calls tools.
"""

from tools.search import search_tool
from tools.weather import weather_tool
from tools.travel import travel_tool


class MCPClient:

    def execute(self, task):

        tool = task["tool"]

        if tool == "search":

            return search_tool.search(
                task["query"]
            )

        elif tool == "weather":

            return weather_tool.get_weather(
                task["city"]
            )

        elif tool == "travel":

            return travel_tool.get_transport(
                task["source"],
                task["destination"]
            )

        else:

            return "Unknown Tool"


mcp_client = MCPClient()