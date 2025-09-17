
from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database.core import get_db
from .service import create_access_token, authenticate_user
from ..utils.database.user_insert import create_user
from ..utils.validation.user import User as UserModel

router = APIRouter(prefix="/auth", tags=["/auth"])

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(user: UserModel, db: Session = Depends(get_db)):
    try:
        created_user = create_user(email=user.email, password=user.password, db=db)

        if not created_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User could not be created."
            )

        return {"message": "User registered successfully."}
    
    except ValueError as ve:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(ve))

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
    
@router.post("/login")
def login_user(user: UserModel, db: Session = Depends(get_db)):
    
    success, message = authenticate_user(user.email, user.password, db)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=message
        )
    access_token = create_access_token(data={"sub": user.email})
    return {
        "message": message,
        "access_token": access_token,
        "token_type": "bearer"
    }