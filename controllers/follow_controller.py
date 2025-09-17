from fastapi import HTTPException

user_db = [
    {"id": 1, "name": "Noor"},
    {"id": 2, "name": "Neha"},
    {"id": 3, "name": "Anku"},
    {"id": 4, "name": "Harman"}
]

follow = [{"followed_by": 1, "followed_to": 2}, {"followed_by": 3, "followed_to": 2}]
block = [{"block_by": 2, "block_to": 1}, {"block_by": 2, "block_to": 3}]


def Follow_User(data):
    for i in follow:
        if i["followed_by"] == data.followed_by and i["followed_to"] == data.followed_to:
            return {"success": True, "status": 200, "msg": "You are already following this user."}
    for user in user_db:
        if user["id"] == data.followed_by:
            for u in user_db:
                if u["id"] == data.followed_to:
                    follow.append(data.dict())
                    return {"success": True, "status": 200, "msg": "User FOLLOWED successfully."}
            raise HTTPException(status_code=400, detail="Target user NOT FOUND.")
    raise HTTPException(status_code=400, detail="User not found.")


def Unfollow_User(data):
    for i in follow:
        if i["followed_by"] == data.followed_by and i["followed_to"] == data.followed_to:
            follow.remove(i)
            return {"success": True, "status": 200, "msg": "User UNFOLLOWED successfully."}
    raise HTTPException(status_code=400, detail="You are NOT FOLLOWING this user.")


def Check_Followers(id):
    users = []
    for i in follow:
        if i["followed_to"] == id:
            users.append(i["followed_by"])
    if len(users) > 0:
        for u in block:
            if u["block_to"] == id or u["block_by"] == id:
                if u["block_to"] in users:
                    users.remove(u["block_to"])
                if u["block_by"] in users:
                    users.remove(u["block_by"])
    if len(users) > 0:
        return {
            "success": True,
            "status": 200,
            "msg": "Followers retrieved successfully.",
            "total_followers": len(users),
            "followers": users
        }
    raise HTTPException(status_code=200, detail="You DON'T HAVE any FOLLOWERS yet.")


def Check_Following(id):
    users = []
    for i in follow:
        if i["followed_by"] == id:
            users.append(i["followed_to"])
    if len(users) > 0:
        for u in block:
            if u["block_to"] == id or u["block_by"] == id:
                if u["block_to"] in users:
                    users.remove(u["block_to"])
                if u["block_by"] in users:
                    users.remove(u["block_by"])
    if len(users) > 0:
        return {
            "success": True,
            "status": 200,
            "msg": "Following list retrieved SUCCESSFULLY.",
            "total_following": len(users),
            "following": users
        }
    raise HTTPException(status_code=200, detail="You are NOT FOLLOWED ANYONE yet.")


def Block_User(data):
    for i in block:
        if i["block_by"] == data.block_by and i["block_to"] == data.block_to:
            return {"success": True, "status": 200, "msg": "You have ALREADY BLOCKED this user."}
    for user in user_db:
        if user["id"] == data.block_by:
            for u in user_db:
                if u["id"] == data.block_to:
                    block.append(data.dict())
                    return {"success": True, "status": 200, "msg": "User BLOCKED successfully."}
            raise HTTPException(status_code=400, detail="Target user NOT FOUND.")
    raise HTTPException(status_code=400, detail="User NOT FOUND.")


def Unblock_User(data):
    for i in block:
        if i["block_by"] == data.block_by and i["block_to"] == data.block_to:
            block.remove(i)
            return {"success": True, "status": 200, "msg": "User UNBLOCKED successfully."}
    raise HTTPException(status_code=400, detail="You have NOT BLOCKED this user.")
