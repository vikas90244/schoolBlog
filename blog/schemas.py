from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class BlogSchema(BaseModel):
    title: str
    content: str
    author: str
    tags: Optional[List[str]]
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Introduction to FastAPI",
                "content": "FastAPI is a modern web framework...",
                "author": "John Doe",
                "tags": ["fastapi", "python", "web development"],
            }
        }


class UpdateBlogSchema(BaseModel):
    title: Optional[str]=None
    content: Optional[str]=None
    author: Optional[str]=None
    tags: Optional[List[str]]=None

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Advanced FastAPI",
                "content": "This is an advanced tutorial on FastAPI...",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
