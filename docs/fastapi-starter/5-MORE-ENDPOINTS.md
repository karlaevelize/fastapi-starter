# Expanding our API

We just built a very simple API that runs on http://127.0.0.1:8000 and has one `GET` endpoint registered on the `/` path. Our focus for this next part is to add a few more endpoints and send more complex data. You will also learn a few more concepts:

- Path Parameters
- Query Parameters
- Request Body

If you don't remember, here is the code from `main.py`

```py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```
