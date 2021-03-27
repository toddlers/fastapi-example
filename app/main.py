#!usr/bin/env python3
from fastapi import FastAPI
from blog import database, models

from blog.routers import blog, user, authentication

models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)