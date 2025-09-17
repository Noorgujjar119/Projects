from pydantic import BaseModel

class FollowSchema(BaseModel):
    followed_by: int
    followed_to: int

class BlockSchema(BaseModel):
    block_by: int
    block_to: int
