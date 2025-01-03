import logging

from fastapi import APIRouter, HTTPException

from ..db.models import Bookmark
from ..dependencies import DBSessionDependency, UserDependency
from ..schemas.bookmark import BookmarkCreate

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/create/", tags=["bookmarks"])
def create_bookmark(
    bookmark: BookmarkCreate, db: DBSessionDependency, user: UserDependency
):
    print("got user", user)
    try:
        db.add(Bookmark(**bookmark.model_dump(), user_id=user.id))
        db.commit()
    except Exception as e:
        logging.error("Error during bookmark creation %s", e)
        raise HTTPException(status_code=400, detail="Error during bookmark creation")
    return {"message": "Bookmark created successfully", "data": bookmark}
