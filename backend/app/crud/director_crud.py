from sqlalchemy.orm import Session
from app.models.movie_models import Director

def get_directors(db: Session):
    return db.query(Director).all()

def get_director(db: Session, director_id: int):
    return db.query(Director).filter(Director.id == director_id).first()
