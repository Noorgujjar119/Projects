from fastapi import FastAPI
from routes import user_routes, post_routes, follow_routes

app = FastAPI()

app.include_router(user_routes.router)
app.include_router(post_routes.router)
app.include_router(follow_routes.router)
