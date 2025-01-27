import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import auth, bookmark, folders

logger = logging.getLogger(__name__)
logging.info("Starting FastAPI app")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8081"],  # Allow only this origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

app.include_router(auth.router)
app.include_router(bookmark.router)
app.include_router(folders.router)
