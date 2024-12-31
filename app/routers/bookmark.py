import logging

from fastapi import APIRouter, HTTPException

from ..db.models import Bookmark
from ..dependencies import AccessTokenDep

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/create/", tags=["bookmarks"])
def create_bookmark(bookmark: Bookmark, session: AccessTokenDep):
    try:
        session.add(bookmark)
        session.commit()
    except Exception as e:
        logging.error("Error during bookmark creation %s", e)
        raise HTTPException(status_code=400, detail="Error during bookmark creation")
    return {"message": "Bookmark created successfully", "data": bookmark}
