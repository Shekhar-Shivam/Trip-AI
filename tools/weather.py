"""
from backend.tools.weather import weather_tool

print(
    weather_tool.get_weather("Goa")
)
"""

import requests

class WeatherTool:

    def get_weather(self, city: str):

        geo = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={
                "name": city,
                "count": 1
            }
        ).json()

        if "results" not in geo:
            return "Weather not available."

        lat = geo["results"][0]["latitude"]
        lon = geo["results"][0]["longitude"]

        weather = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": lat,
                "longitude": lon,
                "current": "temperature_2m,weather_code"
            }
        ).json()

        current = weather["current"]

        return f"""
Temperature: {current['temperature_2m']}°C

Weather Code: {current['weather_code']}
"""


weather_tool = WeatherTool()