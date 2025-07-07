from sqlalchemy.orm import Session
from app.models.movie_models import Movie, Actor, Genre, Director
from app.schemas.movie_schemas import MovieCreate

def get_movies(db: Session, genre: str = None, actor: str = None, director: str = None, year: int = None, rating: float = None, duration: float = None):
    query = db.query(Movie)

    if genre:
        query = query.join(Movie.genres).filter(Genre.name.ilike(f"%{genre}%"))
    if actor:
        query = query.join(Movie.actors).filter(Actor.name.ilike(f"%{actor}%"))
    if director:
        query = query.join(Movie.director).filter(Director.name.ilike(f"%{director}%"))
    if year:
        query = query.filter(Movie.release_year == year)
    if rating:
        query = query.filter(Movie.rating == rating)
    if duration:
        query = query.filter(Movie.duration == duration)

    return query.all()

def get_movie(db: Session, movie_id: int):
    return db.query(Movie).filter(Movie.id == movie_id).first()

def create_movie(db: Session, movie: MovieCreate):
    db_movie = Movie(
        title=movie.title,
        release_year=movie.release_year,
        director_id=movie.director_id,
        rating=movie.rating,
        duration=movie.duration
    )
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)

    # Add actors and genres
    db_movie.actors = db.query(Actor).filter(Actor.id.in_(movie.actor_ids)).all()
    db_movie.genres = db.query(Genre).filter(Genre.id.in_(movie.genre_ids)).all()
    db.commit()
    return db_movie
