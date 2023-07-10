from typing import NoReturn

from fastapi import WebSocket

from fastapi_snake_app.main import app


@app.get('/echo')
async def echo(text: str) -> str:
    return text


@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket) -> NoReturn:
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f'Message text was: {data}')
