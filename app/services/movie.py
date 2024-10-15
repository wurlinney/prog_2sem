from app.models.movies import Movie
from app.schemas.movies import CreateMovie, UpdateMovie
from sqlalchemy.orm import Session
from fastapi import HTTPException



def get_all_movies(db: Session):
    return db.query(Movie).all()

def get_movie(movie_id: int, db: Session):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

def post_movie(movie: CreateMovie, db: Session):
    try:
        created_movie = Movie(
            id = movie.id,
            title = movie.title,
            year = movie.year,
            director = movie.director,
            length = movie.length,
            rating = movie.rating
        )
        db.add(created_movie)
        db.commit()
        db.refresh(created_movie),
        return created_movie
    except  HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail={"status": 500, "reason": str(e)})

def update_movie(movie_id: int, movie: UpdateMovie, db: Session):
    try:
        movie_to_change = get_movie(movie_id, db)
        if movie.title is not None:
            movie_to_change.title = movie.title
        if movie.year is not None:
            movie_to_change.year = movie.year
        if movie.director is not None:
            movie_to_change.director = movie.director
        if movie.length is not None:
            movie_to_change.length = movie.length
        if movie.rating is not None:
            movie_to_change.rating = movie.rating
        db.commit()
        db.refresh(movie_to_change)
        return movie_to_change
    except  HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail={"status": 500, "reason": str(e)})


def delete_movie(movie_id: int, db: Session):
    try:
        movie_to_delete = get_movie(movie_id, db)
        db.delete(movie_to_delete)
        db.commit()
    except  HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail={"status": 500, "reason": str(e)})