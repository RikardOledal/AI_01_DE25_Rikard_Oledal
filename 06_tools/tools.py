import httpx
from dataclasses import dataclass
from numpy import place
from numpy import place
from pydantic_ai import RunContext

@dataclass
class WeatherDeps:
    city: str

def get_weather(ctx: RunContext[WeatherDeps], lat: float, lon: float) -> str:
    """Get the current wheather for latitude and longitude"""
    weather_response = httpx.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": lat,
                "longitude": lon,
                "current_weather": True
                })

    current_weather = weather_response.json().get("current")
    temperature = current_weather.get("temperature_2m")

    return f"The current temperature in {ctx.deps.city} is {temperature}°C."

def geocode(city: str) -> dict:
    response = httpx.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": city, "count": 1}
    )
    
    place = response.json().get("results")[0]

    return {"latitude": place.get("latitude"), "longitude": place.get("longitude")}