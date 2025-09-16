from fastapi import HTTPException

from schemas.user_schema import UserSignup, UserLogin, ResetPassword

users = []

def signup(user: UserSignup):
    users.append(user.dict())
    return {"success": True,"status":200,"msg": "User signed up", "user": user}

def login(data: UserLogin):
    for u in users:
        if u["email"] == data.email and u["password"] == data.password:
            return {"success": True,"status":200,"msg": "Login success"}
    raise HTTPException(status_code=404,detail= "Invalid email or password")

def reset_password(data: ResetPassword):
    for u in users:
        if u["email"] == data.email:
            u["password"] = data.new_password
            return {"success": True,"status":200,"msg": "Password reset successful"}
    raise HTTPException(status_code=404,detail= "msg :" "User not found")
