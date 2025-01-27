import logging

from fastapi import FastAPI

from .routers import auth, bookmark, folders

logger = logging.getLogger(__name__)
logging.info("Starting FastAPI app")

app = FastAPI()

app.include_router(auth.router)
app.include_router(bookmark.router)
app.include_router(folders.router)
