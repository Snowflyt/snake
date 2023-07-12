from fastapi import HTTPException,Cookie
from fastapi.responses import JSONResponse

from fastapi_snake_app.main import app


@app.post('/logout')
async def logout(response: JSONResponse, username: str = Cookie(default=None)):
    if username is None:
        raise HTTPException(status_code=401, detail="You have not logged in!")
    response.delete_cookie(key="username")
    return {"message": "Logout successful"}
