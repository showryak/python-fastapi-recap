from fastapi import FastAPI
from typing import Optional
from dataclasses import dataclass

# To run the server, use the following command:
# uvicorn main:app --reload

# Sample list of blogs with id, blog content, and publication status

# Dataclass representing a Blog object with id, content, and publication status
@dataclass
class Blog:
    id: int
    blog: str
    status: str

# Sample list of Blog dictionaries used as an in-memory data store
listOfBlogs: list[Blog] =  [ {'id': 1, 'blog': 'sample blog', 'status': 'unPublished'}, 
                 {'id': 2, 'blog': 'sample blog', 'status': 'published'}, 
                 {'id': 3, 'blog': 'sample blog', 'status': 'published'},
                 {'id': 4, 'blog': 'sample blog', 'status': 'unPublished'},
                 {'id': 5, 'blog': 'sample blog', 'status': 'unPublished'},
                 {'id': 6, 'blog': 'sample blog', 'status': 'published'},
                 {'id': 7, 'blog': 'sample blog', 'status': 'unPublished'},
                 {'id': 8, 'blog': 'sample blog', 'status': 'unPublished'},
                 {'id': 9, 'blog': 'sample blog', 'status': 'unPublished'},
                 {'id': 10, 'blog': 'sample blog', 'status': 'published'},
                 {'id': 11, 'blog': 'sample blog', 'status': 'unPublished'},
                 {'id': 12, 'blog': 'sample blog', 'status': 'published'},
                 {'id': 13, 'blog': 'sample blog', 'status': 'unPublished'} ]
# Initialize the FastAPI application
app = FastAPI()

# Helper function: Filters a list of blogs by a given key and matching value
async def filter_blogs(keyTofilter: str, blogs, matchValue: str):
    return list(filter(lambda blog: blog[keyTofilter] == matchValue, blogs))

# Root endpoint: Returns a welcome message describing the API
@app.get("/")
async def root_blog():
    return {'data': 'This api gives you list of blogs'}

# GET /blog - Returns a list of blogs with optional query parameters:
# - limit (int): Number of blogs to return. Defaults to 0 (returns all).
# - published (bool): If True, returns only published blogs. Defaults to False.
# - sort (str): Sort order for the results ('asc' or 'desc'). Defaults to 'asc'.
@app.get('/blog')
async def get_blogs_by_params(limit: int = 0, published: bool = False, sort: Optional[str] = 'asc'):
    if limit > 0 and published == False:
        return  { 'data': listOfBlogs[0: limit]  }
    if limit > 0 and published:
        return  { 'data': await filter_blogs('status', listOfBlogs[0: limit], 'published')  }
    if limit == 0 and published:
        return  { 'data': await filter_blogs('status', listOfBlogs, 'published')  }
    else:
        return  { 'data': listOfBlogs  }    

# GET /blog/{id} - Returns details of a specific blog post by its ID
# Path parameter:
# - id (int): The unique identifier of the blog post
@app.get("/blog/{id}")
async def get_blogs_details_by_id(id: int):
    return {'data': {'id': f'{id}', 'blog': f'You are tyring to get blog details for id:{id}'}}

# GET /blog/{id}/comments - Returns details of a specific blog post along with its comments
# Path parameter:
# - id (int): The unique identifier of the blog post
@app.get('/blog/{id}/comments')
async def get_comments_by_id(id: int):
    return {'data': {'id': f'{id}', 'blog': f'You are tyring to get blog details for id:{id} with comments', 'comments': f'Comments for blog with id: {id}'}} 

# POST /blogs - Accepts a list of Blog objects and appends them to the in-memory store
# Request body:
# - blogs (list[Blog]): A list of Blog objects to be added
# Returns the updated list of blogs along with a success message and status code
@app.post('/blogs')
async def create_blogs(blogs: list[Blog]):
    listOfBlogs.extend(blogs)
    return {'data': listOfBlogs, 'message': 'Blogs added successfully', 'status': 200}