import time
from typing import Literal, NoReturn, TypeAlias, TypeVar, TypedDict, Generic, Any
from dataclasses import dataclass

from fastapi import WebSocket

from fastapi_snake_app.main import app


@dataclass
class RGB:
    r: int  # pylint: disable=invalid-name
    g: int  # pylint: disable=invalid-name
    b: int  # pylint: disable=invalid-name

    def __str__(self) -> str:
        return f'rgb({self.r}, {self.g}, {self.b})'


Color: TypeAlias = RGB

# 颜色
BLACK = RGB(0, 0, 0)
WHITE = RGB(255, 255, 255)
RED = RGB(255, 0, 0)
GREEN = RGB(0, 255, 0)


@dataclass
class Point:
    x: int  # pylint: disable=invalid-name
    y: int  # pylint: disable=invalid-name

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def copy(self) -> 'Point':
        return Point(self.x, self.y)


Direction: TypeAlias = Literal['left', 'right', 'up', 'down']


@dataclass
class Board:
    height: int
    width: int


class Snake:
    def __init__(self, *, body_nodes: list[Point], color: Color, board: Board) -> None:
        """
        :param body_nodes: 蛇身节点，蛇头为第一个节点
        :param color: 蛇身颜色
        :param board: 场地
        :raises ValueError: 蛇身节点不合法（相邻节点不在同一行或同一列、节点重复，或节点数小于 2）
        """

        self._color = color
        self._board = board

        if len(body_nodes) < 2:
            raise ValueError('Invalid body nodes')

        self._body_points: list[Point] = []
        for node1, node2 in zip(body_nodes, body_nodes[1:]):
            if node1.x == node2.x:
                if node1.y < node2.y:
                    y_start = node1.y
                    y_end = node2.y
                elif node1.y > node2.y:
                    y_start = node2.y
                    y_end = node1.y
                else:
                    raise ValueError('Invalid body nodes')

                for y in range(y_start, y_end):  # pylint: disable=invalid-name
                    self._body_points.append(Point(node1.x, y))
                continue

            if node1.y == node2.y:
                if node1.x < node2.x:
                    x_start = node1.x
                    x_end = node2.x
                elif node1.x > node2.x:
                    x_start = node2.x
                    x_end = node1.x
                else:
                    raise ValueError('Invalid body nodes')

                for x in range(x_start, x_end):  # pylint: disable=invalid-name
                    self._body_points.append(Point(x, node1.y))
                continue

            raise ValueError('Invalid body nodes')
        self._body_points.append(body_nodes[-1])

        head, after_head = body_nodes[0], body_nodes[1]

        if head.x == after_head.x:
            if head.y < after_head.y:
                self._direction: Direction = 'up'
            else:
                self._direction = 'down'
        else:
            if head.x < after_head.x:
                self._direction = 'left'
            else:
                self._direction = 'right'

    @property
    def color(self) -> Color:
        return self._color

    @property
    def head(self) -> Point:
        return self._body_points[0]

    @property
    def body_points(self) -> list[Point]:
        return self._body_points

    @property
    def direction(self) -> Direction:
        return self._direction

    def turn_left(self) -> None:
        if self._direction == 'up':
            self._direction = 'left'
        elif self._direction == 'left':
            self._direction = 'down'
        elif self._direction == 'down':
            self._direction = 'right'
        else:
            self._direction = 'up'

    def turn_right(self) -> None:
        if self._direction == 'up':
            self._direction = 'right'
        elif self._direction == 'right':
            self._direction = 'down'
        elif self._direction == 'down':
            self._direction = 'left'
        else:
            self._direction = 'up'

    def forward(self) -> None:
        if self._direction == 'up':
            self._body_points.insert(0, Point(self.head.x, self.head.y - 1))
        elif self._direction == 'left':
            self._body_points.insert(0, Point(self.head.x - 1, self.head.y))
        elif self._direction == 'down':
            self._body_points.insert(0, Point(self.head.x, self.head.y + 1))
        else:
            self._body_points.insert(0, Point(self.head.x + 1, self.head.y))

        self._body_points.pop()


T = TypeVar('T')


class OutgoingMessage(TypedDict, Generic[T]):
    type: str
    data: T


class IncomingMessage(TypedDict, Generic[T]):
    type: str
    data: T


class UpdateCodePayload(TypedDict):
    code: str


async def update_code(payload: UpdateCodePayload) -> None:
    ...


class UpdateGamePayload(TypedDict):
    game: str


async def update_game(payload: UpdateGamePayload) -> None:
    ...


@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket) -> NoReturn:
    await websocket.accept()

    last_time = time.time()
    while True:
        data: IncomingMessage[Any] = await websocket.receive_json()

        if data['type'] == 'update-code':
            await update_code(data['data'])

        # Send a message to update the game every second
        if time.time() - last_time > 1:
            last_time = time.time()
            await websocket.send_json(OutgoingMessage(type='update-game', data=await update_game(data['data'])))
