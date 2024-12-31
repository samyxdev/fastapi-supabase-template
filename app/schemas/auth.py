# schemas/auth.py
from pydantic import BaseModel, EmailStr


class UserIn(BaseModel):
    id: str
    email: EmailStr


class UserSign(BaseModel):
    email: EmailStr
    password: str
