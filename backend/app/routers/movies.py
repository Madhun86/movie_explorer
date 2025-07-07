from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database import get_db
from app.schemas.movie_schemas import MovieOut, MovieCreate
from app.crud import movie_crud

router = APIRouter(prefix="/movies", tags=["Movies"])

@router.get("/", response_model=List[MovieOut])
def read_movies(
    genre: Optional[str] = None,
    actor: Optional[str] = None,
    director: Optional[str] = None,
    year: Optional[int] = None,
    db: Session = Depends(get_db)
):
    return movie_crud.get_movies(db, genre, actor, director, year)

@router.get("/{movie_id}", response_model=MovieOut)
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = movie_crud.get_movie(db, movie_id)
    print(db_movie)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie

@router.post("/", response_model=MovieOut)
def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    return movie_crud.create_movie(db, movie)
