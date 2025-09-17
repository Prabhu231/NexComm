from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ...database.models.user import User

def find_user(email: str, db: Session) -> User:
    try:
        user = db.query(User).filter_by(email=email).first()
        if not user:
            raise ValueError("Please type a valid email.")
        return user
    except SQLAlchemyError as e:      
        raise e
