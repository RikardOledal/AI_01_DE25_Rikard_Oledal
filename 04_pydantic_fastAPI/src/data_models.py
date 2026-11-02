from pydantic import BaseModel, Field

class Movie(BaseModel):
    title: str
    year: int
    gener: str
    rating: int = Field(gt=0, lt=6)

class Prompt(BaseModel):
    prompt: str