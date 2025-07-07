from sqlalchemy.orm import Session
from app.models.movie_models import Actor

def get_actors(db: Session, movie: str = None, genre: str = None):
    query = db.query(Actor)

    if movie:
        query = query.join(Actor.movies).filter(Movie.title.ilike(f"%{movie}%"))
    if genre:
        query = query.join(Actor.movies).join(Movie.genres).filter(Genre.name.ilike(f"%{genre}%"))

    return query.all()

def get_actor(db: Session, actor_id: int):
    return db.query(Actor).filter(Actor.id == actor_id).first()
