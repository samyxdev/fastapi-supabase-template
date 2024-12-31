import logging
import os
from typing import Annotated

from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session, create_engine
from supabase import Client, create_client

from .schemas.auth import UserIn

logger = logging.getLogger(__name__)

load_dotenv()

# Direct Postgres connection
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
engine_url = os.environ.get("SUPABASE_DB_STRING")
engine = create_engine(engine_url)


def get_supabase_client() -> Client:
    logging.info("Initializing Supabase client")
    return create_client(url, key)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="token")
AccessTokenDep = Annotated[str, Depends(reusable_oauth2)]


async def get_current_user(
    access_token: AccessTokenDep, supabase_client: Client = Depends(get_supabase_client)
) -> UserIn:
    """Get current user from access_token and validate at the same time"""
    response = supabase_client.auth.api.get_user(access_token)
    if response.get("error"):
        raise HTTPException(status_code=401, detail="Invalid token")
    return UserIn(**response["user"])
