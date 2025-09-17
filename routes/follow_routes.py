from fastapi import APIRouter
from controllers.follow_controller import Follow_User, Unblock_User, Check_Followers, Check_Following, Block_User, Unblock_User
from schemas.follow_schema import FollowSchema, BlockSchema

router = APIRouter()

@router.post("/follow")
def follow_user(followdata: FollowSchema):
    return Follow_User(followdata)

@router.patch("/unfollow")
def unfollow_user(followdata: FollowSchema):
    return unfollow_user(followdata)

@router.get("/followers/{id}")
def followers(id: int):
    return Check_Followers(id)

@router.get("/following/{id}")
def following(id: int):
    return Check_Following(id)

@router.post("/blockuser")
def block_user(blockdata: BlockSchema):
    return Block_User(blockdata)

@router.patch("/unblockuser")
def unblock_user(blockdata: BlockSchema):
    return Unblock_User(blockdata)
