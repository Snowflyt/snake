import asyncio
import time
from typing import Literal, TypeAlias, TypedDict
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


class PointDto(TypedDict):
    x: int
    y: int


@dataclass
class Point:
    x: int  # pylint: disable=invalid-name
    y: int  # pylint: disable=invalid-name

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def copy(self) -> 'Point':
        return Point(self.x, self.y)

    def to_dto(self) -> PointDto:
        return PointDto(x=self.x, y=self.y)


Direction: TypeAlias = Literal['left', 'right', 'up', 'down']


class BoardDto(TypedDict):
    height: int
    width: int


@dataclass
class Board:
    height: int
    width: int

    def to_dto(self) -> BoardDto:
        return BoardDto(height=self.height, width=self.width)


class SnakeDto(TypedDict):
    body_points: list[PointDto]
    user_id: int


DEFAULT_SNAKE_CODE = '''
def step(snake, other_snakes, board):
    pass
'''


class Snake:
    def __init__(self, *, body_nodes: list[Point], color: Color = RGB(0, 0, 0),
                 board: Board, user_id: int, code: str = DEFAULT_SNAKE_CODE) -> None:
        """
        :param body_nodes: 蛇身节点，蛇头为第一个节点
        :param color: 蛇身颜色
        :param board: 场地
        :raises ValueError: 蛇身节点不合法（相邻节点不在同一行或同一列、节点重复，或节点数小于 2）
        """

        self._color = color
        self._board = board
        self._user_id = user_id
        self._code = code

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
    def user_id(self) -> int:
        return self._user_id

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

    def forward(self, other_snakes: list['Snake']) -> None:
        globals_ = {}
        locals_ = {}
        exec(self._code, globals_, locals_)
        step_func = locals_['step']
        step_func(self, other_snakes, self._board)

        if self._direction == 'up':
            self._body_points.insert(0, Point(self.head.x, self.head.y - 1))
        elif self._direction == 'left':
            self._body_points.insert(0, Point(self.head.x - 1, self.head.y))
        elif self._direction == 'down':
            self._body_points.insert(0, Point(self.head.x, self.head.y + 1))
        else:
            self._body_points.insert(0, Point(self.head.x + 1, self.head.y))

        self._body_points.pop()

    def to_dto(self) -> SnakeDto:
        return {
            'body_points': [point.to_dto() for point in self.body_points],
            'user_id': self.user_id,
        }


class GameDto(TypedDict):
    room_id: str
    snakes: list[SnakeDto]
    board: BoardDto
    round: int


@dataclass
class Game:
    room_id: str
    snakes: list[Snake]
    board: Board
    round: int = 0

    def to_dto(self) -> GameDto:
        return {
            'room_id': self.room_id,
            'snakes': [snake.to_dto() for snake in self.snakes],
            'board': self.board.to_dto(),
            'round': self.round
        }


games: dict[str, Game] = {}


@dataclass
class CreateGameInput:
    room_id: str
    user_ids: list[int]


@app.post('/game')
def start_game(ipt: CreateGameInput) -> GameDto:
    board = Board(width=50, height=50)
    snake_gap = board.width // (len(ipt.user_ids) + 1)
    snakes = [Snake(body_nodes=[Point((idx + 1) * snake_gap, 10),
                                Point((idx + 1) * snake_gap, 40)],
                    board=board, user_id=user_id)
              for idx, user_id in enumerate(ipt.user_ids)]

    game = Game(room_id=ipt.room_id, snakes=snakes,
                board=board, round=0)
    games[ipt.room_id] = game

    return game.to_dto()


class UpdateCodePayload(TypedDict):
    code: str


class UpdateCodeMessage(TypedDict):
    type: Literal['update-code']
    payload: UpdateCodePayload


IncomingMessage: TypeAlias = UpdateCodeMessage


class UpdateGamePayload(TypedDict):
    game: GameDto


class UpdateGameMessage(TypedDict):
    type: Literal['update-game']
    payload: UpdateGamePayload


OutgoingMessage: TypeAlias = UpdateGameMessage


async def update_code(payload: UpdateCodePayload) -> None:
    ...


async def update_game(payload: UpdateGamePayload) -> None:
    ...


@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket) -> None:
    await websocket.accept()

    last_time = time.time()

    async def receive_handle():
        while True:
            msg: IncomingMessage = await websocket.receive_json()
            if msg:
                if msg['type'] == 'update-code':
                    await update_code(msg['payload'])

    receiver_task = asyncio.create_task(receive_handle())

    try:
        while True:
            # Send updates periodically
            if time.time() - last_time > 1:
                last_time = time.time()

                for game in games.values():
                    for snake in game.snakes:
                        other_snakes = filter(
                            lambda s: s != snake, game.snakes)
                        snake.forward(other_snakes=list(other_snakes))

                    await websocket.send_json(UpdateGameMessage(
                        type='update-game',
                        payload=UpdateGamePayload(game=game.to_dto())))
            else:
                # Sleep a bit to prevent high CPU usage
                await asyncio.sleep(0.1)

    except Exception as exc:
        print(f"Error in websocket communication: {exc}")

    finally:
        receiver_task.cancel()  # Stop the receiver task when exit
