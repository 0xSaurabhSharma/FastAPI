from fastapi import Request
from fastapi.responses import JSONResponse

async def custom_validation_exception_handler(request: Request, exc):
    return JSONResponse(
        status_code=422,
        content={"error":"Validation Error", "details": exc.errors()}
    )