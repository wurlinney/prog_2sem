from fastapi import FastAPI, Request, HTTPException
from app.routers import movies
import uvicorn
from app.backend.db import engine
from app.models.movies import Base
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI(debug=True)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    first_error = exc.errors()[0]
    loc = first_error['loc'][-1]
    message = first_error['msg']
    return JSONResponse(
        status_code=400,
        content={"status": 400, "reason": f"Field '{loc}' - {message}"}
    )

app.include_router(movies.router)

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
