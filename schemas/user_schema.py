from pydantic import BaseModel

class UserSignup(BaseModel):
    username: str
    email: str
    password: str
    gender: str

class UserLogin(BaseModel):
    email: str
    password: str

class ResetPassword(BaseModel):
    email: str
    new_password: str

