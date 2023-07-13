from typing import List

import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, status

from fastapi.responses import HTMLResponse

from fastapi_snake_app.main import app

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <h2>Your ID: <span id="ws-id"></span></h2>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var client_id = Date.now()
            document.querySelector("#ws-id").textContent = client_id;
            var ws = new WebSocket(`ws://101.132.165.23:8000/ws/${client_id}`);
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


# 返回一段 HTML 代码给前端
@app.get("/")
async def get():
    return HTMLResponse(html)


# 处理和广播消息到多个 WebSocket 连接
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(client_id: str, websocket: WebSocket):
    # 1、客户端、服务端建立 ws 连接
    await manager.connect(websocket)
    # 2、广播某个客户端进入聊天室
    await manager.broadcast(f"{client_id} 进入了聊天室")
    try:
        while True:
            # 3、服务端接收客户端发送的内容
            data = await websocket.receive_text()
            # 4、广播某个客户端发送的消息
            await manager.broadcast(f"{client_id} 发送消息：{data}")
            # 5、服务端回复客户端
            await manager.send_personal_message(f"服务端回复{client_id}：你发送的信息是：{data}", websocket)
    except WebSocketDisconnect:
        # 6、若有客户端断开连接，广播某个客户端离开了
        manager.disconnect(websocket)
        await manager.broadcast(f"{client_id} 离开了聊天室")
