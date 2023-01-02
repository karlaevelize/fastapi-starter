from fastapi import FastAPI
from models import Programmer, Languages
from typing import List

app = FastAPI()

db: List[Programmer] = [
    Programmer(id= 1, name="Dennis Ritchie", languages=[Languages.b, Languages.c]),
    Programmer(id= 2, name="Brian Wilson Kernighan", languages=[Languages.c]),
    Programmer(id= 3, name="James Gosling", languages=[Languages.java]),
    Programmer(id= 4, name="Guido van Rossum", languages=[Languages.python]),
    Programmer(id= 4, name="Brendan Eich", languages=[Languages.javascript])
]

@app.get("/")
async def root():
    return {"message": "Hello World"}

