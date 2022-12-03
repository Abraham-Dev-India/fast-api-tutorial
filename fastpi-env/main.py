from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index():
    return 'hey' 

@app.get('/blog/{id}/fetch')
def fetch(id:int):
    return 'THe blog for ' + id + 'is this'

@app.get('/blog')
def bloglist(published : bool = True , sort : Optional[bool] = False):
    if sort == True:
        return "Both are True"

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(request:Blog):
    #return request
    return {'data':"Blog is created"}