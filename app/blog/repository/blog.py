from sqlalchemy.orm import Session
from blog import models, schemas
import json
from fastapi import (
    HTTPException,
    status
)


def get_all(db: Session):
    return db.query(models.Blog).all()


def create(request: schemas.Blog, db: Session):
    blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

def delete(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog:
        blog.delete(synchronize_session=False)
        db.commit()
        db.refresh
        return f'Blog with id : {id} deleted'

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail = f'Blog with id : {id} not found'
    )
   
def update(id: int, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if blog:
        print(f'original blog : {json.dumps(blog.__serialize__())}')
        db.query(models.Blog).filter(models.Blog.id == id).update(
            {
                models.Blog.id: id,
                models.Blog.title: request.title,
                models.Blog.body: request.body
            },
            synchronize_session=False
        )
        db.commit()
        db.refresh
        return blog
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail = f'Blog with id : {request.id} not found'
    )

def get(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        message = f'Blog with id: {id} not found'
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=message
            )
    return blog