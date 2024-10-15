from pydantic import BaseModel, Field
from datetime import time

class CreateMovie(BaseModel):
    id: int
    title: str = Field(max_length=100)
    year: int = Field(ge=1900, le=2100)
    director: str = Field(max_length=100)
    length: time
    rating: int = Field(ge=0, le=10)

class UpdateMovie(BaseModel):
    title: str = None
    year: int = None
    director: str = None
    length: time = None
    rating: int = None

class GetMovie(BaseModel):
    id: int
    title: str
    year: int
    director: str
    length: time
    rating: int