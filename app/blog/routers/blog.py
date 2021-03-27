from typing import List
from blog import schemas, database, oauth2
from sqlalchemy.orm import Session
from fastapi import (
    Response,
    status,
    Depends,
    APIRouter
)

from blog.repository import blog

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)
@router.get('/', response_model=List[schemas.ShowBlog])
def get_blogs(
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.post('/', response_model=schemas.ShowBlog)
def create(request: schemas.Blog, db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)

@router.delete('/{id}', tags=['blogs'])
def delete_blog(id: int, db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ShowBlog)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id: int, response: Response, db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get(id, db)