import pytest
from app.models.movie_models import Movie, Director, Actor, Genre

def test_get_all_movies(client, db_session):
    # Create director first
    director = Director(name="Christopher Nolan")
    db_session.add(director)
    db_session.commit()
    
    # Create movie with proper relationships
    movie = Movie(
        title="Inception", 
        director_id=director.id, 
        release_year=2010
    )
    db_session.add(movie)
    db_session.commit()
    
    response = client.get("/movies/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1

def test_filter_movies_by_director(client, db_session):
    # Create director first
    director = Director(name="Christopher Nolan")
    db_session.add(director)
    db_session.commit()
    
    # Create movie with proper relationships
    movie = Movie(
        title="Inception", 
        director_id=director.id,
        release_year=2010
    )
    db_session.add(movie)
    db_session.commit()
    
    response = client.get("/movies/?director=nolan")
    assert response.status_code == 200
    data = response.json()
    assert any("Inception" in movie["title"] for movie in data)

def test_get_movie_by_id(client, db_session):
    # Create director first
    director = Director(name="Christopher Nolan")
    db_session.add(director)
    db_session.commit()
    
    # Create movie with proper relationships
    movie = Movie(
        id=1,
        title="Inception", 
        director_id=director.id,
        release_year=2010
    )
    db_session.add(movie)
    db_session.commit()
    
    response = client.get("/movies/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Inception"

def test_create_movie_with_genres_and_actors(client, db_session):
    # Create related entities
    director = Director(name="Christopher Nolan")
    actor1 = Actor(name="Leonardo DiCaprio")
    actor2 = Actor(name="Marion Cotillard")
    genre1 = Genre(name="Sci-Fi")
    genre2 = Genre(name="Thriller")
    
    db_session.add_all([director, actor1, actor2, genre1, genre2])
    db_session.commit()
    
    # Create movie with all relationships
    movie = Movie(
        title="Inception",
        director_id=director.id,
        release_year=2010
    )
    # Add many-to-many relationships
    movie.actors = [actor1, actor2]
    movie.genres = [genre1, genre2]
    
    db_session.add(movie)
    db_session.commit()
    
    response = client.get("/movies/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1