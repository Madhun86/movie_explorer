from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database import get_db
from app.schemas.movie_schemas import ActorOut
from app.crud import actor_crud

router = APIRouter(prefix="/actors", tags=["Actors"])

@router.get("/", response_model=List[ActorOut])
def read_actors(
    movie: Optional[str] = None,
    genre: Optional[str] = None,
    db: Session = Depends(get_db)
):
    return actor_crud.get_actors(db, movie, genre)

@router.get("/{actor_id}", response_model=ActorOut)
def read_actor(actor_id: int, db: Session = Depends(get_db)):
    db_actor = actor_crud.get_actor(db, actor_id)
    if db_actor is None:
        raise HTTPException(status_code=404, detail="Actor not found")
    return db_actor
