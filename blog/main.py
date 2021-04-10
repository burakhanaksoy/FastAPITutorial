from fastapi import FastAPI, Depends, Response
import schemas
import models
import crud
import uvicorn as uvicorn
from database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()

models.Blog.metadata.create_all(bind=engine)

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/blogs/")
def get_blogs(db: Session = Depends(get_db)):
    return crud.get_blogs(db)


@app.post("/blogs/", response_model=schemas.CreateBlog, status_code=201)
def create_blog(request: schemas.CreateBlog, db: Session = Depends(get_db)):
    return crud.create_blog(request, db)


@app.get("/blogs/{id}", status_code=200)
def get_blog_by_id(id: int, response: Response, db: Session = Depends(get_db)):
    return crud.get_blog_by_id(id, response, db)


@app.delete("/blogs/{id}")
def delete_by_id(id: int, response: Response, db: Session = Depends(get_db)):
    return crud.delete_by_id(id, response, db)


@app.put('/blogs/{id}')
def put_blog_post(id: int, request: schemas.CreateBlog, response: Response, db: Session = Depends(get_db)):
    return crud.put_blog_post(id, request, response, db)


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8080)
