
from datetime import datetime, timedelta
from jose import jwt
from ..constants import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..utils.database.user_find import find_user
from ..utils.hash.hash_string import verify_hash

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now() + (expires_delta or timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES)))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def authenticate_user(email: str, password: str, db: Session) -> tuple[bool, str]:
    try:
        user = find_user(email, db)
    except ValueError:
        return False, "No user found with that email/username."
    except SQLAlchemyError:
        return False, "A database error occurred. Please try again later."

    if not verify_hash(password, user.password):
        return False, "Incorrect password."

    return True, "Authenticated successfully."