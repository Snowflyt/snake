from typing import NoReturn

from fastapi import WebSocket

from fastapi_snake_app.main import app

games = {}
##颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class Point:  # 使用Point类来接受row横坐标 col纵坐标
    def __init__(self, row=0, col=0):
        self.row = row
        self.col = col

    def copy(self):
        return Point(self.row, self.col)


class Snake:  ##定义贪吃蛇类
    def __init__(self, length, color, row, col, height=400, width=400):
        self.length = length  ##设置蛇身长度
        self.color = color
        self.playground_height = height  ##设置场地高度
        self.plauground_width = width  ##设置场地宽度
        self.head = Point(row, col)  ##设置初始蛇头坐标
        self.snake_body = []  ##一个数组 用于保存蛇的身体坐标
        for i in range(length):  ##根据长度初始化蛇身体
            body_part = Point(row, col + i)  ##初始蛇身横向排列
            self.snake_body.append(body_part)
        self.direction = "left"  ##默认初始移动方向为向左

    def move(self, direction_next="left"):  ##默认未来移动方向为向左
        head = self.head.copy()
        ##注意移动方向不能与当前前进方向相反，并且在获取未来移动方向后更新head坐标
        if direction_next == "up":
            if self.direction == "left" or self.direction == "right":
                self.direction = "up"
                head.row -= 1
                self.head.row -= 1  ##更新头位置
        elif direction_next == "down":
            if self.direction == "left" or self.direction == "right":
                self.direction = "down"
                head.row += 1
                self.head.row += 1
        elif direction_next == "left":
            if self.direction == "up" or self.direction == "down":
                self.direction == "left"
                head.col -= 1
                self.head.col -= 1
        elif direction_next == "right":
            if self.direction == "up" or self.direction == "down":
                self.direction == "right"
                head.col += 1
                self.head.col += 1
        ##在更新完毕蛇头位置之后，需要更新蛇体位置,把蛇头插入最新位置，即可更新所有点的位置，然后把最后一个点pop即可
        self.snake_body.insert(0, head)
        self.snake_body.pop()

    def hit_wall_check(self):  ##检测是否撞到墙
        dead = False
        head = self.head.copy()
        if head.col < 0 or head.row < 0 or head.row > self.playground_height or head.col > self.plauground_width:
            dead = True
        return dead

    def hit_body_check(self):  ##检测是否撞到自己
        dead = False
        head = self.head.copy()
        for snake_body_points in self.snake_body[1:]:  ##注意排除第0个元素 即蛇头自身
            if snake_body_points.row == head.row and snake_body_points.col == head.col:
                dead = True
                break
        return dead


@app.get('/echo')
async def echo(text: str) -> str:
    return text


@app.post('/start-game')
async def start_game(room_id: str) -> None:
    game = ...
    games[room_id] = game


@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket) -> NoReturn:
    await websocket.accept()
    while True:
        data = await websocket.receive_text()

        await websocket.send_text(f'Message text was: {data}')
