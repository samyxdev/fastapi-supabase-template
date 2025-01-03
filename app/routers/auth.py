import logging
import os

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from ..db.models import User
from ..dependencies import DBSessionDependency, SupabaseDependency
from ..schemas.auth import UserSign

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/token")
async def login_for_swagger(
    supabase: SupabaseDependency, form_data: OAuth2PasswordRequestForm = Depends()
):
    """Swagger specific route to get the JWT token. To be used with
    the "Authorize" button in the Swagger UI."""
    if os.environ.get("DEV_ENV") != "dev":
        raise HTTPException(
            status_code=404, detail="This route is only available in dev."
        )
    try:
        # Use Supabase to authenticate the user
        response = supabase.auth.sign_in_with_password(
            {"email": form_data.username, "password": form_data.password}
        )
        # Return the JWT token
        return {"access_token": response.session.access_token, "token_type": "bearer"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/sign_up/", tags=["users"])
def sign_up(user: UserSign, supabase: SupabaseDependency, db: DBSessionDependency):
    try:
        auth_response = supabase.auth.sign_up(
            {"email": user.email, "password": user.password}
        )
    except Exception as e:
        logger.error("Error during signup %s", e)
        raise HTTPException(status_code=400, detail="Error during signup")

    # Create an User in our database
    db_user = User(id=auth_response.user.id)
    logger.warning("Mail verification is not checked !")
    try:
        db.add(db_user)
        db.commit()
    except Exception as e:
        logger.error("Error during user creation %s", e)
        raise HTTPException(status_code=400, detail="Error during user creation")

    return {"message": "User signed up successfully, waiting for confirmation."}


@router.post("/sign_in/", tags=["users"])
def sign_in(user: UserSign, supabase: SupabaseDependency):
    try:
        _ = supabase.auth.sign_in_with_password(
            {"email": user.email, "password": user.password}
        )
    except Exception as e:
        logger.error("Error during signin %s", e)
        raise HTTPException(status_code=400, detail="Error during signin")
    return {"message": "User signed in successfully"}
