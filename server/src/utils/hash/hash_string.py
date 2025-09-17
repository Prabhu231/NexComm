from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(data: str):
    hashed_pw = pwd_context.hash(data)
    return hashed_pw

def verify_hash(plain_data: str, hashed_data: str):
    return pwd_context.verify(plain_data, hashed_data)