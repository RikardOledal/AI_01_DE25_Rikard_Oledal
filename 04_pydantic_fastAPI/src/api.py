from agents import movie_agent
from fastapi import FastAPI
from aimodules.helpers import nvidia_model
from setup_db import query_duckdb
from data_models import Prompt

app = FastAPI()

@app.get("/movie")
async def read_movies(genere: str = None):
    if genere:
        sql = "SELECT * FROM movies WHERE genre = ?;"
        params = [genere]
    else:
        sql = "SELECT * FROM movies"
        params = None

    movies = query_duckdb(sql, parameters=params)
    return movies.to_dict(orient="records")

@app.post("/movies")
async def create_movie(query: Prompt):
    result = await movie_agent.run(query.prompt)
    movie = result.output

    query_duckdb("""
        INSERT INTO movies (title, year, genre, rating, summary)
        VALUES (?, ?, ?, ?, ?)""", 
        parameters=[movie.title, movie.year, movie.genre, movie.rating, movie.summary])

    return movie