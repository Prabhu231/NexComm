from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(data: str):
    hashed_pw = pwd_context.hash(data)
    return hashed_pw