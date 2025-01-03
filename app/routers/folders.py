import logging
from uuid import UUID

from fastapi import APIRouter, HTTPException

from ..db.crud import delete_db_element, get_folder_by_id, update_db_element
from ..db.models import Folder
from ..dependencies import DBSessionDependency, UserDependency
from ..schemas.folder import FolderCreate, FolderUpdate

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/create/")
def create(folder: FolderCreate, db: DBSessionDependency, user: UserDependency):
    try:
        db.add(Folder(**folder.model_dump(), user_id=user.id))
        db.commit()
    except Exception as e:
        logging.error("Error during folder creation %s", e)
        raise HTTPException(status_code=400, detail="Error during folder creation")
    return {"message": "Folder created successfully", "data": folder}


@router.put("/update/{folder_id}")
def update(
    folder_id: UUID,
    folder_update: FolderUpdate,
    db: DBSessionDependency,
    user: UserDependency,
):
    db_folder = get_folder_by_id(db, folder_id, user_id=user.id)
    updated_folder = update_db_element(
        db=db, original_element=db_folder, element_update=folder_update
    )
    return updated_folder


@router.delete("/delete/{folder_id}")
def delete(folder_id: UUID, db: DBSessionDependency, user: UserDependency):
    db_folder = get_folder_by_id(db, folder_id, user_id=user.id)
    if db_folder is None:
        raise HTTPException(status_code=404, detail="Folder not found")

    delete_db_element(db=db, element=db_folder)
    return {"detail": "Folder and related bookmarks deleted successfully"}
