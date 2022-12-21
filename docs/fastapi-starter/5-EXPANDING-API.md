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

The one problem we still have to solve is where to get the data to send, since we don't have a database yet. For now, we can simply hardcode it, all we need is a list of programmers so we can send it on the response.

FastAPI and [pydantic](https://docs.pydantic.dev/) work very well together, it's also very helpful to have our data typed, we will make sure to type most of our data from now on.

## Setting up Mock DB

### Part 1 - Programmer Model

Create a new file in the root of your directory called `models.py`, we will use it to define models with pydantic. The first model we want to create is the Programmer one.

1. Install pydantic: `pipenv install pydantic`
2. Import BaseModel from pydantic

```py
# /models.py

from pydantic import BaseModel
```

3. Define a Programmer model with id and name

```py
# /models.py

...
class Programmer(BaseModel):
  id: int
  name: str
```

4. The programmer class is missing a third property `languages`. Languages is a list of strings with some predefined values. Create a new class Languages with some sample data.

```py
# /models.py

from enum import Enum

class Languages(str, Enum):
  c = "c"
  python = "python"
  javascript = "javascript"
```

5. Add a new property languages to the Programmer class.

```py
# /models.py

from typing import List

class Programmer(BaseModel):
  id: int
  name: str
  languages: List[Languages]
```

### Part 2 - Database

---

[Next → Exercises](https://karlaevelize.github.io/fastapi-starter/docs/fastapi-starter/6-EXERCISES)

---
