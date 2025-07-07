from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import movies, actors, directors, genres
from app.models import movie_models
from app.database import engine

movie_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # your frontend's origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(movies.router)
app.include_router(actors.router)
app.include_router(directors.router)
app.include_router(genres.router)
