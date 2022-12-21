# Expanding our API

We just built a very simple API that runs on http://127.0.0.1:8000 and has one `GET` endpoint registered on the `/` path. Our focus for this next part is to add a few more endpoints and send more complex data. You will also learn a few more concepts:

- Path Parameters
- Query Parameters
- Request Body

If you don't remember, here is the code from `main.py`. We will keep working on this file and expand it.

```py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

When it comes to endpoints, we can return way more than a single string, let's add a few more that return different types of data. We also want to make our app somewhat more meaningful, than it's better if we define proper objectives.

## What are we building?

Let's build an application about famous programmers, we want to have at least 2 different sets of data: programmers and programming languages. When it comes to the endpoints, we can write at least 4:

- `/programmers:` responds with a list of programmers
- `/languages:` responds with a list of programming languages
- `/programmers/id:` responds with a specific programmer
- `/languages/id:` responds with a specific programming language

For the last two, we will need to use something called **path parameters**, we will get to that later in this lesson.
