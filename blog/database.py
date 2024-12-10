import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS ="mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.blogs

blog_collection = database.get_collection("blogs_collection")



def blog_helper(blog) -> dict:
    return {
        "id": str(blog["_id"]),
        "title": blog["title"],
        "content": blog["content"],
        "author": blog["author"],
        "tags": blog["tags"],
        "created_at": blog["created_at"],
    }



async def retrieve_blogs():
    blogs = []
    async for blog in blog_collection.find():
        blogs.append(blog_helper(blog))
    return blogs


async def retrieve_blog(id: str) -> dict:
    blog = await blog_collection.find_one({"_id": ObjectId(id)})
    if blog:
        return blog_helper(blog)


async def add_blog(blog_data: dict) -> dict:
    blog = await blog_collection.insert_one(blog_data)
    new_blog = await blog_collection.find_one({"_id": blog.inserted_id})
    return blog_helper(new_blog)


async def update_blog(id: str, data: dict):
    if len(data) < 1:
        return False
    blog = await blog_collection.find_one({"_id": ObjectId(id)})
    if blog:
        updated_blog = await blog_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_blog:
            return True
        return False


async def delete_blog(id: str):
    blog = await blog_collection.find_one({"_id": ObjectId(id)})
    if blog:
        await blog_collection.delete_one({"_id": ObjectId(id)})
        return True