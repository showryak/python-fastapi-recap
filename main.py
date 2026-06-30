from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/showrya")
async def read_showrya():
    return {'data': {'name': 'Showrya', 'age': 16, 'city': 'Allen'}}

@app.get('/about')
async def about():
    return {'data': {'field': 'About', 'value': 'This api is my first fast api'}}  