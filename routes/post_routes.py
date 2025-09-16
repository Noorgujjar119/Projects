#post_routes
from fastapi import APIRouter
from controllers import post_controller
from schemas.post_schema import PostCreate

router = APIRouter()

@router.post("/create-post")
def create_post(post: PostCreate):
    return post_controller.create_post(post)

@router.get("/post/{post_id}")
def get_post_by_id(post_id: int):
    return post_controller.get_post_by_id(post_id)

@router.get("/posts/user/{user_id}")
def get_posts_by_user(user_id: int):
    return post_controller.get_posts_by_user(user_id)

@router.get("/posts/title/{title}")
def get_post_by_title(title: str):
    return post_controller.get_post_by_title(title)

@router.get("/posts/count/{user_id}")
def get_post_count(user_id: int):
    return post_controller.get_post_count(user_id)
