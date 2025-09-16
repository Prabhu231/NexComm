from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ...database.models.user import User
from ..hash.hash_string import hash

def create_user(db: Session, email: str, password: str) -> User:
    try:
        existing_user = db.query(User).filter_by(email=email).first()
        if existing_user:
            raise ValueError("A user with this email already exists.")
        hashed_password = hash(password)
        user = User(email=email, password=hashed_password)
        db.add(user)
        db.commit()         
        db.refresh(user)   
        return user
    except SQLAlchemyError as e:
        db.rollback()      
        raise e
