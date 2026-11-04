from pydantic_ai import Agent
from aimodules.helpers import nvidia_model
from data_models import Movie

ai_model = nvidia_model()

movie_agent = Agent(
    model=ai_model,
    instructions="You are a movie expert, you will be given a prompt and you will answer with a movie title, year, genre and rating. You will answer in JSON format with the following keys: title, year, genre, rating",
    output_type=Movie
)

if __name__ == "__main__":
    movie = movie_agent.run_sync("I'll be back")
    print(movie)