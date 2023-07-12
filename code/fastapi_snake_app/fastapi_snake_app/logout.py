from fastapi import HTTPException,Cookie
from fastapi.responses import JSONResponse

from fastapi_snake_app.main import app


@app.post('/logout')
async def logout(username: str = Cookie(default=None)):
    if username is None:
        raise HTTPException(status_code=401, detail="You have not logged in!")
    response = JSONResponse(content={"message": "Logout Successfully"})
    response.delete_cookie(key="username")
    return response
