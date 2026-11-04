from pydantic import BaseModel, Field
from typing import Literal

class Movie(BaseModel):
    title: str = Field(description="Title of the movie.")
    year: int = Field(description="Year of release.")
    genre: Literal["Action", "Comedy", "Drama", "Horror", "Romance", "Sci-Fi", "Fantasy"] = Field(description="Main genre of the movie.")
    rating: int = Field(description="Rating between 1 and 5. The higher rating the more popular the movie is.", gt=0, lt=6)
    summary: str = Field(description="A brief summary of the movie, max 3 sentences.")