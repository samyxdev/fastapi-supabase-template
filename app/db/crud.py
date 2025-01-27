from typing import List
from uuid import UUID

from fastapi import HTTPException
from pydantic import BaseModel
from sqlmodel import Session, SQLModel, select

from ..schemas.folder import FolderContent
from .models import Bookmark, Folder

######################################################
# Generic CRUD operations
######################################################


def update_db_element(
    db: Session, original_element: SQLModel, element_update: BaseModel
) -> BaseModel:
    """Updates an element in database.
    Note that it doesn't take care of user ownership.
    """
    update_data = element_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(original_element, key, value)

    db.add(original_element)
    db.commit()
    db.refresh(original_element)

    return original_element


def delete_db_element(db: Session, element: SQLModel):
    """Deletes an element from database."""
    db.delete(element)
    db.commit()


######################################################
# Specific CRUD operations
######################################################


def get_bookmark_by_id(db: Session, bookmark_id: UUID, user_id: UUID) -> Bookmark:
    """Returns a bookmark by id and user id."""
    db_bookmark = db.exec(
        select(Bookmark).where(Bookmark.id == bookmark_id, Bookmark.user_id == user_id)
    ).first()
    if not db_bookmark:
        raise HTTPException(status_code=404, detail="Bookmark not found")

    return db_bookmark


def get_folder_by_id(db: Session, folder_id: UUID, user_id: UUID) -> FolderContent:
    """Returns a folder and its content by id."""
    db_folder = db.exec(
        select(Folder).where(Folder.id == folder_id, Folder.user_id == user_id)
    ).first()
    if not db_folder:
        raise HTTPException(status_code=404, detail="Folder not found")

    return FolderContent(folder=db_folder, bookmarks=db_folder.bookmarks)


def get_folders(db: Session, user_id: UUID) -> List[Folder]:
    """Returns all folders for a user."""
    folders = db.exec(select(Folder).where(Folder.user_id == user_id)).all()
    return folders
