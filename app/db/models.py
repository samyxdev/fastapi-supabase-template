from datetime import datetime
from typing import List, Optional
from uuid import UUID

from sqlmodel import Field, Relationship, SQLModel


class Bookmark(SQLModel, table=True):
    __tablename__ = "bookmark"

    id: UUID = Field(default=None, primary_key=True)

    url: str
    desc: Optional[str] = None
    is_ticked: bool = False
    content_type: Optional[str] = None

    folder_id: UUID = Field(default=None, foreign_key="folder.id")
    user_id: UUID = Field(foreign_key="user.id", nullable=False)
    created_at: datetime = Field(default=datetime.now)

    user: "User" = Relationship(back_populates="bookmarks")
    folder: "Folder" = Relationship(back_populates="bookmarks")


class Folder(SQLModel, table=True):
    __tablename__ = "folder"

    id: UUID = Field(default=None, primary_key=True)

    name: str
    desc: Optional[str] = None
    color: Optional[str] = None

    user_id: UUID = Field(default=None, foreign_key="user.id")
    created_at: datetime = Field(default=datetime.now)

    user: "User" = Relationship(back_populates="folders")
    bookmarks: Optional[List[Bookmark]] = Relationship(back_populates="folder")


class User(SQLModel, table=True):
    __tablename__ = "user"

    id: UUID = Field(default=None, primary_key=True)

    is_active: bool = True
    created_at: datetime = Field(default=datetime.now)

    bookmarks: Optional[List[Bookmark]] = Relationship(back_populates="user")
    folders: Optional[List[Folder]] = Relationship(back_populates="user")
