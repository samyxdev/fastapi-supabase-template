from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class BookmarkCreate(BaseModel):
    url: str
    desc: Optional[str] = None
    is_ticked: bool = False
    content_type: Optional[str] = None
    folder_id: Optional[UUID] = None


class BookmarkUpdate(BaseModel):
    id: UUID

    url: Optional[str] = None
    desc: Optional[str] = None
    is_ticked: Optional[bool] = None
    content_type: Optional[str] = None
    folder_id: Optional[UUID] = None
