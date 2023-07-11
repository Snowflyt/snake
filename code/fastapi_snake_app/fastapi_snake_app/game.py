from typing import Literal, NoReturn, TypeAlias

from fastapi import WebSocket

from fastapi_snake_app.main import app

games = {}
# 颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class Point:
    """
    坐标类
    """

    def __init__(self, row: int = 0, col: int = 0):
        """
        :param row: 横坐标
        :param col: 纵坐标
        """

        self.row = row
        self.col = col

    def copy(self):
        return Point(self.row, self.col)


Direction: TypeAlias = Literal['left', 'right', 'up', 'down']


class Snake:
    """
    贪吃蛇类
    """

    def __init__(self, *, length: int, color: str, row: int, col: int,
                 height: int = 400, width: int = 400) -> None:
        """
        :param length: 蛇身长度
        :param color: 蛇身颜色F
        :param row: 蛇头横坐标
        :param col: 蛇头纵坐标
        :param height: 场地高度, 默认 400
        :param width: 场地宽度, 默认 400
        """

        self.length = length  # 设置蛇身长度
        self.color = color
        self.playground_height = height  # 设置场地高度
        self.playground_width = width  # 设置场地宽度
        self.head = Point(row, col)  # 设置初始蛇头坐标
        self.snake_body: list[Point] = []  # 一个数组 用于保存蛇的身体坐标
        self.dead = False  # 表明是否死亡
        for i in range(length):  # 根据长度初始化蛇身体
            body_part = Point(row, col + i)  # 初始蛇身横向排列
            self.snake_body.append(body_part)

        self.direction: Direction = 'left'  # 默认初始移动方向为向左

    def move(self, direction_next: Direction = 'left') -> None:  # 默认未来移动方向为向左
        head = self.head.copy()
        # 注意移动方向不能与当前前进方向相反，并且在获取未来移动方向后更新head坐标
        if direction_next == 'up' and self.direction in ['left', 'right']:
            self.direction = 'up'
            head.row -= 1
            self.head.row -= 1  # 更新头位置
        elif direction_next == 'down' and self.direction in ['left', 'right']:
            self.direction = 'down'
            head.row += 1
            self.head.row += 1
        elif direction_next == 'left' and self.direction in ['up', 'down']:
            self.direction == 'left'
            head.col -= 1
            self.head.col -= 1
        elif direction_next == 'right' and self.direction in ['up', 'down']:
            self.direction == 'right'
            head.col += 1
            self.head.col += 1

        # 在更新完毕蛇头位置之后，需要更新蛇体位置,把蛇头插入最新位置，即可更新所有点的位置，然后把最后一个点pop即可
        self.snake_body.insert(0, head)
        self.snake_body.pop()

    def is_hit_wall(self) -> bool:  # 检测是否撞到墙
        dead = False
        head = self.head.copy()
        if (head.col < 0 or head.row < 0 or
                head.row > self.playground_height or head.col > self.playground_width):
            dead = True
        return dead

    def is_hit_body(self) -> bool:  # 检测是否撞到自己
        dead = False
        head = self.head.copy()
        for snake_body_points in self.snake_body[1:]:  # 注意排除第0个元素 即蛇头自身
            if snake_body_points.row == head.row and snake_body_points.col == head.col:
                dead = True
                break
        return dead


def hit_snake_check(snake1: Snake, snake2: Snake):
    head1 = snake1.head.copy()
    head2 = snake2.head.copy()
    body1 = snake1.snake_body.copy()
    body2 = snake2.snake_body.copy()
    for snake_body1_points in body1:
        if snake_body1_points.row == head2.row and snake_body1_points.col == head2.col:
            snake2.dead = True
            break
    for snake_body2_points in body2:
        if snake_body2_points.row == head1.row and snake_body2_points.col == head1.col:
            snake1.dead = True
            break


def game_judgement(snake1: Snake, snake2: Snake):
    """
    4个int返回值，
    0：没有胜负发生
    1：snake1胜利
    2：snake2胜利
    3：平局
    """
    if snake1.is_hit_wall():
        snake1.dead = True
    if snake1.is_hit_body():
        snake1.dead = True
    if snake2.is_hit_wall():
        snake2.dead = True
    if snake2.is_hit_body():
        snake2.dead = True
    hit_snake_check(snake1, snake2)
    if snake1.dead and snake2.dead:
        print("Tie!")
        return 3
    elif snake2.dead is True and snake1.dead is False:
        print("snake1 wins!")
        return 1
    elif snake1.dead is True and snake2.dead is False:
        print("snake2 wins")
        return 2
    else:
        return 0


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
