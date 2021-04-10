from sqlalchemy.orm import Session
import models
import schemas
from fastapi import Response
import pydantic


def get_blogs(db: Session):
    return db.query(models.Blog).all()


def create_blog(request: schemas.CreateBlog, db: Session):
    new_blog = models.Blog(title=request.title, user=request.user,
                           likes=request.likes, published=request.published)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return request


def get_blog_by_id(id: int, response: Response, db: Session):
    check = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not check == None:
        return db.query(models.Blog).filter(models.Blog.id == id).first()
    else:
        response.status_code = 204
        return response


def delete_by_id(id: int, response: Response, db: Session):
    check = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not check == None:
        db.delete(check)
        db.commit()
    else:
        response.status_code = 204
        return response


def put_blog_post(id: int, request: schemas.CreateBlog, response: Response, db: Session):
    check = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not check == None:
        db.query(models.Blog).filter(models.Blog.id == id).update({'title': request.title, 'user': request.user,
                                                                   'likes': request.likes, 'published': request.published})
        db.commit()
        response.status_code = 200
    else:
        new_blog = models.Blog(title=request.title, user=request.user,
                               likes=request.likes, published=request.published)
        db.add(new_blog)
        db.commit()
        db.refresh(new_blog)
        response.status_code = 201
