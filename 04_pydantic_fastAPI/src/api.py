from agents import movie_agent
from fastapi import FastAPI
from aimodules.helpers import nvidia_model

app = FastAPI()

@app.get("/movie")
async def read_movies():
    return "movies here"

@app.post("/movies")
async def create_movie(query):
    result = await movie_agent.run(query)
    movie = result.output

    return movie