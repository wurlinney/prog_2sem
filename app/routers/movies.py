from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.schemas import movies as schemas
from app.schemas.movies import CreateMovie, UpdateMovie
from app.services.movie import get_all_movies, get_movie, post_movie, update_movie, delete_movie
from app.backend.db_depends import get_db
from sqlalchemy.exc import NoResultFound


router = APIRouter(prefix='/movies', tags=['movie'])

@router.get("/", response_model = dict[str, list[schemas.GetMovie]], status_code=status.HTTP_200_OK)
def all_movies_get(db: Session = Depends(get_db)):
    all_movies = get_all_movies(db)
    return {"list": all_movies}

@router.get("/{movie_id}", response_model = dict[str, schemas.GetMovie], status_code=status.HTTP_200_OK)
def movie_get(movie_id: int, db: Session = Depends(get_db)):
    movie = get_movie(movie_id, db)
    return {'movie': movie}

@router.post("/", response_model = dict[str, schemas.GetMovie], status_code = status.HTTP_200_OK)
def movie_create(movie: CreateMovie, db: Session = Depends(get_db)):
    created_movie = post_movie(movie, db)
    return {"movie": created_movie}

@router.patch("/{movie_id}", response_model = dict[str, schemas.GetMovie], status_code=status.HTTP_200_OK)
def movie_update(movie_id: int, movie: UpdateMovie, db: Session = Depends(get_db)):
    movie_to_change = update_movie(movie_id, movie, db)
    return {"movie": movie_to_change}

@router.delete("/{movie_id}", status_code=status.HTTP_202_ACCEPTED)
def movie_delete(movie_id : int, db: Session = Depends(get_db)):
    movie_to_delete = delete_movie(movie_id, db)
    return {"status": status.HTTP_202_ACCEPTED}
