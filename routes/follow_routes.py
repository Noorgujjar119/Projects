from fastapi import APIRouter
from controllers.follow_controller import followUser, unFollowUser, checkFollowers, checkFollowing, blockUser, unBlockUser
from schemas.follow_schema import FollowSchema, BlockSchema

router = APIRouter()

@router.post("/follow")
def follow_user(followdata: FollowSchema):
    return followUser(followdata)

@router.patch("/unfollow")
def unfollow_user(followdata: FollowSchema):
    return unFollowUser(followdata)

@router.get("/followers/{id}")
def followers(id: int):
    return checkFollowers(id)

@router.get("/following/{id}")
def following(id: int):
    return checkFollowing(id)

@router.post("/blockuser")
def block_user(blockdata: BlockSchema):
    return blockUser(blockdata)

@router.patch("/unblockuser")
def unblock_user(blockdata: BlockSchema):
    return unBlockUser(blockdata)
