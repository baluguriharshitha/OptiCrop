from sqlalchemy.orm import Session

from app.models.user import User

from app.auth.password import hash_password


def create_user(db: Session, full_name, email, password):

    user = User(
        full_name=full_name,
        email=email,
        hashed_password=hash_password(password)
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user
