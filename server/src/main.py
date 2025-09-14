from fastapi import FastAPI
from .auth.controller import router as auth_router

app = FastAPI()

"""Only uncomment below to create new tables, otherwise tests will fail if not commented"""


app.include_router(auth_router)