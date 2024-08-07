"""
FastAPI Tutorial
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """
    Create a new item.

    Returns:
        Item: The created item.
    """
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
