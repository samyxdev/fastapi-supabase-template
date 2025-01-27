from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4

from sqlmodel import Field, Relationship, SQLModel

# SQLModel requires to define a Model for each scheme. As we want
# to reference to the auth.user table in the public scheme
# we define it here.


# Note that the real table holds more columns than expressed here,
# but we only need the id column for the reference.
# This table will also be skipped during alembic autogeneration.
class AuthSchemeModel(SQLModel, table=True):
    __tablename__ = "users"
    __table_args__ = {"schema": "auth"}

    id: UUID = Field(default_factory=uuid4, primary_key=True)


class Bookmark(SQLModel, table=True):
    __tablename__ = "bookmark"

    id: UUID = Field(default_factory=uuid4, primary_key=True)

    url: str
    desc: Optional[str] = None
    is_ticked: bool = False
    content_type: Optional[str] = None

    folder_id: Optional[UUID] = Field(
        default=None, foreign_key="folder.id", nullable=True
    )
    user_id: UUID = Field(foreign_key="user.id", nullable=False)
    created_at: datetime = Field(default_factory=datetime.now)

    user: "User" = Relationship(back_populates="bookmarks")
    folder: "Folder" = Relationship(back_populates="bookmarks")


class Folder(SQLModel, table=True):
    __tablename__ = "folder"

    id: UUID = Field(default_factory=uuid4, primary_key=True)

    name: str
    desc: Optional[str] = None
    color: Optional[str] = None
    parent_folder: Optional[UUID] = Field(foreign_key="folder.id", nullable=True)

    user_id: UUID = Field(default_factory=uuid4, foreign_key="user.id")
    created_at: datetime = Field(default_factory=datetime.now)

    user: "User" = Relationship(back_populates="folders")
    bookmarks: Optional[List[Bookmark]] = Relationship(back_populates="folder")


class User(SQLModel, table=True):
    __tablename__ = "user"

    id: UUID = Field(
        default_factory=uuid4, primary_key=True, foreign_key="auth.users.id"
    )

    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.now)

    bookmarks: Optional[List[Bookmark]] = Relationship(back_populates="user")
    folders: Optional[List[Folder]] = Relationship(back_populates="user")
