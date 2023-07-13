from fastapi import HTTPException, Cookie
from fastapi.responses import JSONResponse

from fastapi_snake_app.main import app


@app.post('/logout', tags=['用户基本操作'])
async def logout(username: str = Cookie(default=None)):
    """
      用于用户执行登出操作
      - param username:  用户名,默认使用cookie中的数据，无需用户传参
      """
    if username is None:
        raise HTTPException(status_code=401, detail="You have not logged in!")
    response = JSONResponse(content={"message": "Logout Successfully"})
    response.delete_cookie(key="username")
    return response
