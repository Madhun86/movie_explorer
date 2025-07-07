from sqlalchemy.orm import Session
from app.models.movie_models import Genre

def get_genres(db: Session):
    return db.query(Genre).all()

def get_genre(db: Session, genre_id: int):
    return db.query(Genre).filter(Genre.id == genre_id).first()
