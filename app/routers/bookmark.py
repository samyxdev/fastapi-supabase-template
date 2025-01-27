import logging
from uuid import UUID

from fastapi import APIRouter, HTTPException

from ..db.crud import get_bookmark_by_id, update_db_element
from ..db.models import Bookmark
from ..dependencies import DBSessionDependency, UserDependency
from ..schemas.bookmark import BookmarkCreate, BookmarkUpdate

logger = logging.getLogger(__name__)

router = APIRouter(tags=["bookmarks"])


@router.post("/create/")
def create_bookmark(
    bookmark: BookmarkCreate, db: DBSessionDependency, user: UserDependency
):
    try:
        db.add(Bookmark(**bookmark.model_dump(), user_id=user.id))
        db.commit()
    except Exception as e:
        logging.error("Error during bookmark creation %s", e)
        raise HTTPException(status_code=400, detail="Error during bookmark creation")
    return {"message": "Bookmark created successfully", "data": bookmark}


@router.put("/bookmark/{bookmark_id}")
def update_bookmark(
    bookmark_id: UUID,
    bookmark_update: BookmarkUpdate,
    db: DBSessionDependency,
    user: UserDependency,
):
    db_bookmark = get_bookmark_by_id(db=db, bookmark_id=bookmark_id, user_id=user.id)
    return update_db_element(db, db_bookmark, bookmark_update)


@router.delete("/bookmark/{bookmark_id}")
def delete_bookmark(bookmark_id: UUID, db: DBSessionDependency, user: UserDependency):
    db_bookmark = get_bookmark_by_id(db=db, bookmark_id=bookmark_id, user_id=user.id)

    db.delete(db_bookmark)
    db.commit()

    return {"message": "Bookmark deleted successfully", "data": db_bookmark}
