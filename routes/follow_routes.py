from fastapi import APIRouter
from controllers.follow_controller import follow_user, get_followers, get_following
from schemas.follow_schema import FollowCreate

router = APIRouter()

# Follow API
@router.post("/follow")
def follow(data: FollowCreate):
    return follow_user(data)

# Get Followers API
@router.get("/followers/{user_id}")
def followers(user_id: int):
    return get_followers(user_id)

# Get Following API
@router.get("/following/{user_id}")
def following(user_id: int):
    return get_following(user_id)
