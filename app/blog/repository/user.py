from sqlalchemy.orm import Session
from typing import List
from blog import models, schemas, hashing
import json
from fastapi import (
    HTTPException,
    status
)


def get_all(db: Session)-> List[schemas.User]:
    return db.query(models.User).all()

def create(request: schemas.User, db: Session) -> schemas.User:
    new_user = models.User(
    name=request.name,
    email=request.email,
    password=hashing.Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(username: str, db: Session) -> schemas.User:
    user = db.query(models.User).filter(models.User.name == username).first()
    if not user:
        message = f'User with name: {username} not found'
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=message
            )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return message
    return user

def delete(username: str, db: Session) -> str:
    user = db.query(models.User).filter(models.User.name == username).first()
    if user:
        user.delete(synchronize_session=False)
        db.commit()
        db.refresh
        return f'User with name : {username} deleted'

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail = f'Username with name : {username} not found'
    ) 