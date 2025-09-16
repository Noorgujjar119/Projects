from pydantic import BaseModel

# Follow request
class FollowCreate(BaseModel):
    follower_id: int
    followee_id: int


# Followers response
class FollowersResponse(BaseModel):
    success: bool
    user: str
    followers_count: int
    followers: list


# Following response
class FollowingResponse(BaseModel):
    success: bool
    user: str
    following_count: int
    following: list

