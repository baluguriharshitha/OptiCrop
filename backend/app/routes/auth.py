from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.user import (
    UserRegister,
    UserLogin,
    UserResponse,
    Token
)

from app.services.user_service import (
    create_user,
    authenticate_user
)

from app.auth.jwt_handler import create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
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
            detail="Email already exists."
        )

    return user


@router.post(
    "/login",
    response_model=Token
)
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
            detail="Invalid email or password."
        )

    token = create_access_token(
        {
            "sub": user.email,
            "role": user.role
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
