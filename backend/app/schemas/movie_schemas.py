from typing import List, Optional
from pydantic import BaseModel, ConfigDict

class GenreBase(BaseModel):
    name: str

class GenreOut(GenreBase):
    name: str

class ActorBase(BaseModel):
    name: str

class ActorOut(ActorBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class DirectorBase(BaseModel):
    name: str

class DirectorOut(DirectorBase):
    name: str

class MovieBase(BaseModel):
    title: str
    release_year: int
    director_id: int
    rating: float
    duration: int

class MovieCreate(MovieBase):
    genre_ids: List[int]
    actor_ids: List[int]

class MovieOut(BaseModel):
    id: int
    title: str
    release_year: int
    rating: float
    duration: int
    director: DirectorOut
    actors: List[ActorOut]
    genres: List[GenreOut]
    
    model_config = ConfigDict(from_attributes=True)
        
        
        

