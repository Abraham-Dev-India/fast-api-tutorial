from fastapi import FastAPI,Depends,status,Response,HTTPException
from . import schemas
import json
from . import models
from .database import engine,Sessionlocal
from sqlalchemy.orm import Session
app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()
"""
@app.post('/blog')
def create(title, body):
    response =  {'title':title,'body':body}
    result = json.dumps(response)
    with open("sample.json", "w") as outfile:
        outfile.write(result)
"""
@app.post('/blog',status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog,db:Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog')
def all(db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}',status_code=status.HTTP_200_OK,response_model=schemas.ShowBlog)
def getId(id,response: Response,db:Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"Blog with the {id} is not found")
    
    """
    if not blogs:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'Details:' + f"for given {id} is not found"}"""
    return blogs