from fastapi import FastAPI
from .auth.controller import router as auth_router
from  .database.core import Base, engine

app = FastAPI()

"""Only uncomment below to create new tables, otherwise tests will fail if not commented"""
Base.metadata.create_all(bind=engine)

app.include_router(auth_router)