from pydantic_ai import Agent, FunctionToolset
from aimodules.helpers import nvidia_model
from tools import get_weather, geocode, WeatherDeps
from pydantic_ai.toolsets import FunctionToolset

weather_agent = Agent(
    nvidia_model(),
    instructions=(
        "You are a weather agent that can provide the current temperature for a given city."
        "Use the provided tools to get the latitude and longitude of the city, and then fetch the current weather information."
    ),
    toolsets=[FunctionToolset([get_weather, geocode])],
    deps_type=WeatherDeps)
