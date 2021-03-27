from blog import schemas, database
from blog.repository import user
from typing import List
from sqlalchemy.orm import Session
from fastapi import (
    Depends,
    APIRouter
)
router = APIRouter(
    prefix='/user',
    tags=['User']
)

@router.get('/', status_code=200, response_model=List[schemas.ShowUser])
def show(db: Session = Depends(database.get_db)):
    return user.get_all(db)

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create(request, db)


@router.get('/{username}', status_code=200, response_model=schemas.ShowUser)
def show(username: str, db: Session = Depends(database.get_db)):
    return user.show(username, db)

@router.delete('/{username}')
def delete_username(username: str, db: Session = Depends(database.get_db)):
    return user.delete(username, db)