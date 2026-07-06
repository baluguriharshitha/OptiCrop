from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.user import (
    UserRegister,
    UserLogin
)

from app.services.user_service import (
    create_user,
    authenticate_user
)

from app.auth.jwt_handler import (
    create_access_token
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    request: UserRegister,
    db: Session = Depends(get_db)
):

    user = create_user(
        db,
        request.full_name,
        request.email,
        request.password
    )

    if not user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    return {
        "message": "Registration Successful"
    }


@router.post("/login")
def login(
    request: UserLogin,
    db: Session = Depends(get_db)
):

    user = authenticate_user(
        db,
        request.email,
        request.password
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )

    token = create_access_token(
        {
            "sub": user.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
