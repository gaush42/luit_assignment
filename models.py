# models.py
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
import datetime

# MongoDB configuration
MONGO_DETAILS = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.school_blog
blog_collection = database.get_collection("blogs")

# Helper function to convert MongoDB documents to Python dict
def blog_helper(blog) -> dict:
    return {
        "id": str(blog["_id"]),
        "title": blog["title"],
        "content": blog["content"],
        "author": blog["author"],
        "created_at": blog["created_at"],
        "updated_at": blog["updated_at"],
    }

# CRUD operations
async def add_blog(blog_data: dict) -> dict:
    blog_data["created_at"] = datetime.datetime.utcnow()
    blog_data["updated_at"] = datetime.datetime.utcnow()
    blog = await blog_collection.insert_one(blog_data)
    return blog_helper(await blog_collection.find_one({"_id": blog.inserted_id}))

async def get_blog(id: str) -> dict:
    blog = await blog_collection.find_one({"_id": ObjectId(id)})
    if blog:
        return blog_helper(blog)

async def get_all_blogs():
    blogs = []
    async for blog in blog_collection.find():
        blogs.append(blog_helper(blog))
    return blogs

async def update_blog(id: str, data: dict):
    data["updated_at"] = datetime.datetime.utcnow()
    blog = await blog_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    if blog:
        return await get_blog(id)

async def delete_blog(id: str):
    blog = await blog_collection.delete_one({"_id": ObjectId(id)})
    return bool(blog.deleted_count)

