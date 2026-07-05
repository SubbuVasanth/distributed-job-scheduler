from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserRegister
from app.core.security import hash_password


class AuthService:

    @staticmethod
    def create_user(db: Session, user: UserRegister):

        existing_user = (
            db.query(User)
            .filter(User.email == user.email)
            .first()
        )

        if existing_user:
            raise ValueError("Email already registered")

        new_user = User(
            name=user.name,
            email=user.email,
            password_hash=hash_password(user.password),
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user