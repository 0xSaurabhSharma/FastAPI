from fastapi import FastAPI
from app.routers import items
# from config.settings import settings
from app.utils.error_handlers import custom_validation_exception_handler
from fastapi.exceptions import ResponseValidationError

TITLE = "My FastAPI App"
VERSION = "1.0.0"

app = FastAPI(title=TITLE, version = VERSION)

app.add_exception_handler(ResponseValidationError, custom_validation_exception_handler)
app.include_router(items.router)

@app.get("/")
async def root():
    return{"message":"Hello, FastAPI"}

@app.get("/hello/{name}")
async def check_hello (name: str):
    return {"message": f"Hello, {name}"}

@app.get("/check_health/")
def check_health():
    print('Server Is Running...')
    return {"message":"Server Is Running"}