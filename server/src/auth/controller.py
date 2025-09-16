
from fastapi import APIRouter, status, HTTPException
from .service import create_access_token
from ..utils.database.user_insert import create_user
from ..utils.validation.user import User as UserModel

router = APIRouter(prefix="/auth", tags=["/auth"])

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user: UserModel):
    try:
        created_user = create_user(username=user.username, password=user.password)

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
def login(username: str, password: str):
    token = create_access_token({"sub": username})
    return {"access_token": token, "token_type": "bearer"}
