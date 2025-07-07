from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.movie_schemas import DirectorOut
from app.crud import director_crud

router = APIRouter(prefix="/directors", tags=["Directors"])

@router.get("/", response_model=List[DirectorOut])
def read_directors(db: Session = Depends(get_db)):
    return director_crud.get_directors(db)

@router.get("/{director_id}", response_model=DirectorOut)
def read_director(director_id: int, db: Session = Depends(get_db)):
    db_director = director_crud.get_director(db, director_id)
    if db_director is None:
        raise HTTPException(status_code=404, detail="Director not found")
    return db_director
