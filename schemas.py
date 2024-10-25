# schemas.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class BlogPost(BaseModel):
    title: str = Field(..., min_length=5, max_length=100)
    content: str = Field(..., min_length=10)
    author: str = Field(..., min_length=3, max_length=50)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        schema_extra = {
            "example": {
                "title": "My First Blog",
                "content": "This is my first blog post content...",
                "author": "John Doe",
                "created_at": "2023-10-20T14:48:00.000Z",
                "updated_at": "2023-10-21T15:48:00.000Z",
            }
        }
