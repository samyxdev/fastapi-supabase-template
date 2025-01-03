from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class FolderCreate(BaseModel):
    name: str
    desc: Optional[str] = None
    color: Optional[str] = None
    parent_folder: Optional[UUID] = None


class FolderUpdate(BaseModel):
    id: UUID

    name: Optional[str] = None
    desc: Optional[str] = None
    color: Optional[str] = None
    parent_folder: Optional[UUID] = None
