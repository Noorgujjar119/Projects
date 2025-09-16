from fastapi import HTTPException

users = [
    {"id": 1, "name": "Noor", "followers": [], "following": []},
    {"id": 2, "name": "Neha", "followers": [], "following": []}
]

def follow_user(data):
    follower_id = data.follower_id
    followee_id = data.followee_id

    if follower_id == followee_id:
        raise HTTPException(status_code=400, detail="You cannot follow yourself")

    follower = None
    followee = None

    for u in users:
        if u["id"] == follower_id:
            follower = u
        if u["id"] == followee_id:
            followee = u

    if follower is None or followee is None:
        raise HTTPException(status_code=404, detail="User not found")

    if followee_id in follower["following"]:
        raise HTTPException(status_code=400, detail="Already following this user")

    follower["following"].append(followee_id)
    followee["followers"].append(follower_id)

    return {
        "success": True,
        "msg": f"{follower['name']} is now following {followee['name']}",
        "follower": follower,
        "followee": followee
    }

def get_followers(user_id: int):
    user = None
    for u in users:
        if u["id"] == user_id:
            user = u

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    followers_list = []
    for u in users:
        if u["id"] in user["followers"]:
            followers_list.append(u)

    return {"success": True, "user": user["name"], "followers": followers_list}

def get_following(user_id: int):
    user = None
    for u in users:
        if u["id"] == user_id:
            user = u

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    following_list = []
    for u in users:
        if u["id"] in user["following"]:
            following_list.append(u)

    return {"success": True, "user": user["name"], "following": following_list}
