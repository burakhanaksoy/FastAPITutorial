from fastapi import FastAPI
# from typing import Optional
from constants import constants
from pydantic import BaseModel

app = FastAPI()


class Blog(BaseModel):
    title: str
    body: str
    published: bool


class BlogPost:
    def __init__(self, post_id: int, user: str, comments: list):
        self.post_id = post_id
        self.user = user
        self.comments = comments


@app.get('/blog')
def blog():
    blog_list = []
    for i in range(5):
        data = BlogPost(constants.blog_id[i % 5], constants.user[i % 4], constants.comments[i % 4])
        blog_list.append(data)
    print(blog_list)
    return {'data': {'blog_post': blog_list}}


# @app.get('/blog')
# def blog(limit: int = 10, published: bool = False):
#     if published:
#         return {'data': f'{limit} published blogs from the db'}
#     else:
#         return {'data': f'{limit} blogs from the db'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id: int):
    # fetch comments with blog id = id
    return {
        'data': {'blog_post': [{'id': id, 'user': 'theBMan', 'likes': 123812,
                                'comments': ['wow! This post was what I just needed!'
                                    , 'You earned my upvote pal!'
                                    , 'Keep up with the good work'
                                    , '++']},
                               {'id': id, 'user': 'theBMan', 'likes': 123812,
                                'comments': ['wow! This post was what I just needed!'
                                    , 'You earned my upvote pal!'
                                    , 'Keep up with the good work'
                                    , '++']}
            ,
                               {'id': id, 'user': 'theBMan', 'likes': 123812,
                                'comments': ['wow! This post was what I just needed!'
                                    , 'You earned my upvote pal!'
                                    , 'Keep up with the good work'
                                    , '++']}
            ,
                               {'id': id, 'user': 'theBMan', 'likes': 123812,
                                'comments': ['wow! This post was what I just needed!'
                                    , 'You earned my upvote pal!'
                                    , 'Keep up with the good work'
                                    , '++']}
            ,
                               {'id': id, 'user': 'theBMan', 'likes': 123812,
                                'comments': ['wow! This post was what I just needed!'
                                    , 'You earned my upvote pal!'
                                    , 'Keep up with the good work'
                                    , '++']}
                               ]}}


@app.post('/blog', status_code=201)
def create_blog(blog: Blog):
    return {'data': f'Blog is created with title \'{blog.title}\''}
