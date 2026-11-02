from fastapi import FastAPI
from pydantic_ai import Agent
from utils import query_duckdb
from aimodules.helpers import nvidia_model
from data_models import Movie, Prompt

ai_model = nvidia_model()

movie_agent = Agent(model=ai_model, output_type=Movie)

app = FastAPI()

@app.get("/movies")
async def read_movies():
    movies = query_duckdb("FROM movies;")
    return movies.to_dict(orient="records")

@app.post("/movies")
async def create_movie(query: Prompt):
    result = await movie_agent.run(query.prompt)
    movie = result.output

    query_duckdb(
        "INSERT INTO movies VALUES (?,?,?,?)",
        parameters=(movie.title,movie.year,movie.gener,movie.rating)
    )

    return movie