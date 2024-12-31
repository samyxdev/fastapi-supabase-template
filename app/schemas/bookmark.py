from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class BookmarkCreate(BaseModel):
    url: str
    desc: Optional[str] = None
    is_ticked: bool = False
    content_type: Optional[str] = None
    folder_id: UUID
    user_id: UUID


class BookmarkUpdate(BaseModel):
    url: Optional[str] = None
    desc: Optional[str] = None
    is_ticked: Optional[bool] = None
    content_type: Optional[str] = None
    folder_id: Optional[UUID] = None
