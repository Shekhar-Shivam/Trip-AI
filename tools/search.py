"""
from backend.tools.search import search_tool

print(
    search_tool.search(
        "Top tourist attractions in Jaipur"
    )
)
"""

from tavily import TavilyClient
from backend.config import settings


class SearchTool:
    """
    Internet Search Tool
    Uses Tavily Search API
    """

    def __init__(self):
        self.client = TavilyClient(
            api_key=settings.TAVILY_API_KEY
        )

    def search(self, query: str) -> str:
        """
        Search the internet and return summarized results.
        """

        response = self.client.search(
            query=query,
            search_depth="advanced",
            max_results=5
        )

        results = []

        for item in response["results"]:

            results.append(
                f"""
Title:
{item["title"]}

Content:
{item["content"]}

URL:
{item["url"]}
"""
            )

        return "\n\n".join(results)


search_tool = SearchTool()