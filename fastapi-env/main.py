from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index(): 
    return {"message": "Hello, World!"}


@app.get('/blog')
def index(limit=10, published: bool = True,sort: Optional[str] =None):
    if published:
        return {'data': f'{limit} publishedblogs'}
    else:
        return {'data': f'{limit} blogs'}


@app.get('/about')
def about():
    return {"message": "This is the about page!"}


@app.get('/blog/{id}')
def show(id : int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id):
    return {'data':{1,2}}


class Blog(BaseModel):
    title : str
    content : str
    published : Optional[str] = None
    number : int

@app.post('/blog', status_code=201)
def create_blog(blog : Blog):
    return {'data': f'Blog is. created with title as {blog.title} and content : {blog.content}'}
