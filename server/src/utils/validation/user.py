from pydantic import BaseModel, EmailStr, field_validator
import re

class User(BaseModel):
    email: EmailStr
    password: str

    @field_validator("password")
    @classmethod
    def validate_password(cls, v: str) -> str:
        pattern = re.compile(
            r'^(?=.*[0-9])(?=.*[!@#$%^&*(),.?":{}|<>])(?=.*[A-Z])(?=.*[a-z]).{8,}$'
        )
        if not pattern.match(v):
            raise ValueError(
                "Password must be at least 8 characters long, include one uppercase, "
                "one lowercase, one digit, and one special character."
            )
        return v
