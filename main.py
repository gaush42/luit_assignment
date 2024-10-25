# main.py
from fastapi import FastAPI, HTTPException, status
from schemas import BlogPost
from models import add_blog, get_blog, get_all_blogs, update_blog, delete_blog

app = FastAPI()

@app.post("/blogs/", response_description="Add new blog post", response_model=BlogPost)
async def create_blog(blog: BlogPost):
    blog = await add_blog(blog.dict())
    return blog

@app.get("/blogs/", response_description="List all blog posts")
async def list_blogs():
    blogs = await get_all_blogs()
    return {"blogs": blogs}

@app.get("/blogs/{id}", response_description="Get a single blog post", response_model=BlogPost)
async def get_single_blog(id: str):
    blog = await get_blog(id)
    if blog:
        return blog
    raise HTTPException(status_code=404, detail="Blog not found")

@app.put("/blogs/{id}", response_description="Update a blog post", response_model=BlogPost)
async def update_blog_post(id: str, blog: BlogPost):
    updated_blog = await update_blog(id, blog.dict(exclude_unset=True))
    if updated_blog:
        return updated_blog
    raise HTTPException(status_code=404, detail="Blog not found")

@app.delete("/blogs/{id}", response_description="Delete a blog post")
async def delete_blog_post(id: str):
    deleted = await delete_blog(id)
    if deleted:
        return {"message": "Blog deleted successfully"}
    raise HTTPException(status_code=404, detail="Blog not found")
