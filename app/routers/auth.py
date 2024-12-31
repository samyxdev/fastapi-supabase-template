import logging

from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_supabase_client
from ..schemas.auth import UserSign

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/sign_up/", tags=["users"])
def sign_up(user: UserSign, supabase=Depends(get_supabase_client)):
    try:
        _ = supabase.auth.sign_up({"email": user.email, "password": user.password})
    except Exception as e:
        logging.error("Error during signup %s", e)
        raise HTTPException(status_code=400, detail="Error during signup")
    return {"message": "User signed up successfully, waiting for confirmation."}


@router.post("/sign_in/", tags=["users"])
def sign_in(user: UserSign, supabase=Depends(get_supabase_client)):
    try:
        _ = supabase.auth.sign_in_with_password(
            {"email": user.email, "password": user.password}
        )
    except Exception as e:
        logging.error("Error during signin %s", e)
        raise HTTPException(status_code=400, detail="Error during signin")
    return {"message": "User signed in successfully"}
