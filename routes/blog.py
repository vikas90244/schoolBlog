from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from blog.database import (
    add_blog,
    delete_blog,
    retrieve_blogs,
    retrieve_blog,
    update_blog,
)
from blog.schemas import ErrorResponseModel, ResponseModel, BlogSchema, UpdateBlogSchema

router = APIRouter()


@router.post("/", response_description="Blog added into the database")
async def add_blog_data(blog: BlogSchema):
    blog = jsonable_encoder(blog)
    new_blog = await add_blog(blog)
    return ResponseModel(new_blog, "Blog added successfully")


@router.get("/", response_description="Blogs retrieved")
async def get_blogs():
    blogs = await retrieve_blogs()
    if blogs:
        return ResponseModel(blogs, "Blogs data retrieved successfully")
    return ResponseModel(blogs, "No blogs found")


@router.get("/{id}", response_description="Blog data retrieved")
async def get_blog_data(id: str):
    blog = await retrieve_blog(id)
    if blog:
        return ResponseModel(blog, "Blog data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Blog doesn't exist.")


@router.put("/{id}")
async def update_blog_data(id: str, req: UpdateBlogSchema = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_blog = await update_blog(id, req)
    if updated_blog:
        return ResponseModel(
            f"Blog with ID: {id} update is successful",
            "Blog updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred", 404, "There was an error updating the blog data."
    )


@router.delete("/{id}", response_description="Blog deleted from the database")
async def delete_blog_data(id: str):
    deleted_blog = await delete_blog(id)
    if deleted_blog:
        return ResponseModel(
            f"Blog with ID: {id} removed", "Blog deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, f"Blog with ID: {id} doesn't exist"
    )
