from fastapi import FastAPI
from starlette import status
from src.app.router import search_router
from src.config import get_settings


def start_application():
    app = FastAPI(title=get_settings().APP_TITLE)
    app.include_router(search_router)
    return app


app = start_application()


@app.get("/", status_code=status.HTTP_200_OK)
def root() -> dict:
    return {"message": "personik", "docs": "/docs"}