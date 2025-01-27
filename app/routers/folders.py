import logging
from uuid import UUID

from fastapi import APIRouter, HTTPException

from ..db import crud
from ..db.models import Folder
from ..dependencies import DBSessionDependency, UserDependency
from ..schemas.folder import FolderContent, FolderCreate, FolderUpdate

logger = logging.getLogger(__name__)

router = APIRouter(tags=["folders"])


@router.get("/folders/")
def get_folders(db: DBSessionDependency, user: UserDependency):
    return crud.get_folders(db, user_id=user.id)


@router.get("/folder/{folder_id}")
def get_folder(
    folder_id: UUID, db: DBSessionDependency, user: UserDependency
) -> FolderContent:
    """Return a folder and its content by id."""
    db_folder = crud.get_folder_by_id(db, folder_id, user_id=user.id)
    if db_folder is None:
        raise HTTPException(status_code=404, detail="Folder not found")
    return db_folder


@router.post("/folder/create/")
def create(folder: FolderCreate, db: DBSessionDependency, user: UserDependency):
    try:
        db.add(Folder(**folder.model_dump(), user_id=user.id))
        db.commit()
    except Exception as e:
        logging.error("Error during folder creation %s", e)
        raise HTTPException(status_code=400, detail="Error during folder creation")
    return {"message": "Folder created successfully", "data": folder}


@router.put("/folder/update/{folder_id}")
def update(
    folder_id: UUID,
    folder_update: FolderUpdate,
    db: DBSessionDependency,
    user: UserDependency,
):
    db_folder = crud.get_folder_by_id(db, folder_id, user_id=user.id)
    updated_folder = crud.update_db_element(
        db=db, original_element=db_folder, element_update=folder_update
    )
    return updated_folder


@router.delete("/folder/delete/{folder_id}")
def delete(folder_id: UUID, db: DBSessionDependency, user: UserDependency):
    db_folder = crud.get_folder_by_id(db, folder_id, user_id=user.id)
    if db_folder is None:
        raise HTTPException(status_code=404, detail="Folder not found")

    crud.delete_db_element(db=db, element=db_folder)
    return {"detail": "Folder and related bookmarks deleted successfully"}
