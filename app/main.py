from fastapi import FastAPI
from app.routers.items import router
from config.settings import settings

TITLE = "My FastAPI App"
VERSION = "1.0.0"

app = FastAPI(title=TITLE, version = VERSION)

@app.get("/")
async def root():
    return{"message":"Hello, FastAPI"}

@app.get("/hello/{name}")
async def checkHello (name: str):
    return {"message": f"Hello, {name}"}

app.include_router(router)