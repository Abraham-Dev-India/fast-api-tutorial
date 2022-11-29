from fastapi import FastAPI
from . import schemas
import json

app = FastAPI()

class Blog(schemas.BaseModel):
    title:str
    body:str

"""
@app.post('/blog')
def create(title, body):
    response =  {'title':title,'body':body}
    result = json.dumps(response)
    with open("sample.json", "w") as outfile:
        outfile.write(result)
"""
@app.post('/blog')
def create(request:Blog):
    return request
