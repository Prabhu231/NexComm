from sqlalchemy import Column, Integer, String, DateTime, func, CheckConstraint
from ..core import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    __table_args__ = (
        CheckConstraint(
            r"password ~ '^(?=.*[0-9])(?=.*[!@#$%^&*(),.?\":{}|<>])(?=.*[A-Z])(?=.*[a-z]).{8,}$'",
            name="password_complexity_check"
        ),
        CheckConstraint(
            r"email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'",
            name="email_format_check"
        ),
    )

    def __repr__(self):
        return f"<User id={self.id} email={self.email}>"
