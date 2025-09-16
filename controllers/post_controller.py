from fastapi import HTTPException
from schemas.post_schema import PostCreate

# Dummy posts store
posts = []
post_counter = {"id": 1}


# Create Post
def create_post(post: PostCreate):
    new_post = {
        "postId": post_counter["id"],
        "userId": post.userId,
        "title": post.title,
        "content": post.content
    }
    posts.append(new_post)
    post_counter["id"] += 1
    return {"success": True,"status":200,"msg": "Post created", "post": new_post}


# Get Post by ID
def get_post_by_id(pid: int):
    for p in posts:
        if p["postId"] == pid:
            return {"success": True,"status":200,"title":p}
    raise HTTPException(status_code=404,detail="Post not found")


# Get Posts by User ID
def get_posts_by_user(uid: int):
    user_posts = []
    for p in posts:
        if p["userId"] == uid:
            user_posts.append(p)
    if not user_posts:
        raise HTTPException(status_code=404,detail="No posts found for this user")
    return {"success": True,"status":200,"userId": uid, "count": len(user_posts), "posts": user_posts}


# Get Post by Title
def get_post_by_title(title: str):
    for p in posts:
        if p["title"].lower() == title.lower():
            return {"success": True,"status":200,"title":p}
    raise HTTPException(status_code=404,detail="Post not found")


# Get Post Count (by User ID)
def get_post_count(uid: int):
    count = 0
    for p in posts:
        if p["userId"] == uid:
            count += 1
    if count == 0:
        raise HTTPException(status_code=404,detail="No posts found for this user")
    return {"success": True,"status":200,"userId": uid, "count": count}
