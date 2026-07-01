from fastapi import FastAPI
from typing import Optional

# Initializing the app
#  uvicorn main:app --reload
listOfBlogs =  [ {'id': '1', 'blog': 'sample blog', 'status': 'unPublished'}, 
                 {'id': '2', 'blog': 'sample blog', 'status': 'published'}, 
                 {'id': '3', 'blog': 'sample blog', 'status': 'published'},
                 {'id': '4', 'blog': 'sample blog', 'status': 'unPublished'},
                 {'id': '5', 'blog': 'sample blog', 'status': 'unPublished'},
                 {'id': '6', 'blog': 'sample blog', 'status': 'published'},
                 {'id': '7', 'blog': 'sample blog', 'status': 'unPublished'},
                 {'id': '8', 'blog': 'sample blog', 'status': 'unPublished'},
                 {'id': '9', 'blog': 'sample blog', 'status': 'unPublished'},
                 {'id': '10', 'blog': 'sample blog', 'status': 'published'},
                 {'id': '11', 'blog': 'sample blog', 'status': 'unPublished'},
                 {'id': '12', 'blog': 'sample blog', 'status': 'published'},
                 {'id': '13', 'blog': 'sample blog', 'status': 'unPublished'} ]
app = FastAPI()
# helper
async def filter_blogs(keyTofilter: str, blogs, matchValue: str):
    return list(filter(lambda blog: blog[keyTofilter] == matchValue, blogs))
@app.get("/")
async def root_blog():
    return {'data': 'This api gives you list of blogs'}
# path matching starts from /blog
@app.get('/blog')
async def get_blogs_params(limit: int = 0, published: bool = False, sort: Optional[str] = 'asc'):
    if limit > 0 and published == False:
        return  { 'data': listOfBlogs[0: limit]  }
    if limit > 0 and published:
        return  { 'data': await filter_blogs('status', listOfBlogs[0: limit], 'published')  }
    if limit == 0 and published:
        return  { 'data': await filter_blogs('status', listOfBlogs, 'published')  }
    else:
        return  { 'data': listOfBlogs  }    

# /showrya is the path and get is the operation
# get_showrya_details is call path operation function
@app.get("/blog/{id}")
async def get_blogs_details_by_id(id: int):
    return {'data': {'id': f'{id}', 'blog': f'You are tyring to get blog details for id:{id}'}}

@app.get('/blog/{id}/comments')
async def get_comments_by_id(id: int):
    return {'data': {'id': f'{id}', 'blog': f'You are tyring to get blog details for id:{id} with comments', 'comments': f'Comments for blog with id: {id}'}} 

