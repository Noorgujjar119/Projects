from fastapi import APIRouter
from controllers import user_controller
from schemas.user_schema import UserSignup, UserLogin, ResetPassword

router = APIRouter()

@router.post("/signup")
def signup(user: UserSignup):
    return user_controller.signup(user)

@router.post("/login")
def login(data: UserLogin):
    return user_controller.login(data)

@router.put("/reset-password")
def reset_password(data: ResetPassword):
    return user_controller.reset_password(data)
