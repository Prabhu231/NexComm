
from fastapi import APIRouter
from .service import create_access_token

router = APIRouter(prefix="/auth", tags=["/auth"])

@router.post("/login")
def login(username: str, password: str):
    token = create_access_token({"sub": username})
    return {"access_token": token, "token_type": "bearer"}
