from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.movie_schemas import GenreOut
from app.crud import genre_crud

router = APIRouter(prefix="/genres", tags=["Genres"])

@router.get("/", response_model=List[GenreOut])
def read_genres(db: Session = Depends(get_db)):
    return genre_crud.get_genres(db)

@router.get("/{genre_id}", response_model=GenreOut)
def read_genre(genre_id: int, db: Session = Depends(get_db)):
    db_genre = genre_crud.get_genre(db, genre_id)
    if db_genre is None:
        raise HTTPException(status_code=404, detail="Genre not found")
    return db_genre
