from fastapi import FastAPI
from routes import blog
app = FastAPI()

app.include_router(blog.router, tags=["blog"], prefix="/blog")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the School Blog API "}


