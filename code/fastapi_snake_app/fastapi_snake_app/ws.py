import asyncio
import random
import time
from typing import Literal, TypeAlias, TypedDict, Protocol
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


class PlayerDto(TypedDict):
    id: str
    name: str


@dataclass
class Player:
    id: str  # pylint: disable=invalid-name
    name: str

    def to_dto(self) -> PlayerDto:
        return {'id': self.id, 'name': self.name}


class SnakeDto(TypedDict):
    body_points: list[PointDto]
    player: PlayerDto


@dataclass
class SnakeInfo:
    body_points: list[Point]
    head: Point
    direction: Direction
    player: Player


class StepFunc(Protocol):
    def __call__(self, snake: SnakeInfo, other_snakes: list[SnakeInfo], board: Board) -> Literal['TURN_LEFT', 'TURN_RIGHT', 'KEEP_STRAIGHT']:
        ...


DEFAULT_SNAKE_CODE = '''
def step(snake, other_snakes, board) -> Literal['TURN_LEFT', 'TURN_RIGHT', 'KEEP_STRAIGHT']:
    return 'KEEP_STRAIGHT'
'''


class Snake:
    def __init__(self, *, body_nodes: list[Point], color: Color = RGB(0, 0, 0),
                 board: Board, player: Player, code: str = DEFAULT_SNAKE_CODE) -> None:
        """
        :param body_nodes: 蛇身节点，蛇头为第一个节点
        :param color: 蛇身颜色
        :param board: 场地
        :raises ValueError: 蛇身节点不合法（相邻节点不在同一行或同一列、节点重复，或节点数小于 2）
        """

        self._color = color
        self._board = board
        self._player = player
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
    def code(self) -> str:
        return self._code

    def update_code(self, code: str) -> None:
        try:
            step_func = self.__parse_step_func(code)
            action = step_func(snake=self.to_info(),
                               other_snakes=[],
                               board=self._board)
            if action not in ('TURN_LEFT', 'TURN_RIGHT', 'KEEP_STRAIGHT'):
                raise ValueError('Invalid code')
            self._code = code
            print(f'Player(id="{self.player.id}", name="{self.player.name}"): Code updated')
            print(self._code)
        except Exception:
            return

    @property
    def player(self) -> Player:
        return self._player

    @property
    def head(self) -> Point:
        return self._body_points[0]

    @property
    def body_points(self) -> list[Point]:
        return self._body_points

    @property
    def direction(self) -> Direction:
        return self._direction

    def _turn_left(self) -> None:
        if self._direction == 'up':
            self._direction = 'left'
        elif self._direction == 'left':
            self._direction = 'down'
        elif self._direction == 'down':
            self._direction = 'right'
        else:
            self._direction = 'up'

    def _turn_right(self) -> None:
        if self._direction == 'up':
            self._direction = 'right'
        elif self._direction == 'right':
            self._direction = 'down'
        elif self._direction == 'down':
            self._direction = 'left'
        else:
            self._direction = 'up'

    @staticmethod
    def __parse_step_func(code: str) -> StepFunc:
        globals_ = {
            'Literal': Literal,
        }
        locals_ = {}
        exec(code, globals_, locals_)  # pylint: disable=exec-used
        return locals_['step']

    def forward(self, other_snakes: list['Snake']) -> None:
        step_func = self.__parse_step_func(self._code)

        action: Literal['TURN_LEFT', 'TURN_RIGHT', 'KEEP_STRAIGHT'] = step_func(
            snake=self.to_info(),
            other_snakes=[snake.to_info() for snake in other_snakes],
            board=self._board)

        if action == 'TURN_LEFT':
            self._turn_left()
        elif action == 'TURN_RIGHT':
            self._turn_right()

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
            'body_points': [point.to_dto() for point in self._body_points],
            'player': self._player.to_dto()
        }

    def to_info(self) -> SnakeInfo:
        return SnakeInfo(body_points=self._body_points,
                         head=self.head,
                         direction=self._direction,
                         player=self._player)


class GameDto(TypedDict):
    snakes: list[SnakeDto]
    board: BoardDto
    round: int


@dataclass
class Game:
    snakes: list[Snake]
    board: Board
    round: int = 1

    def to_dto(self) -> GameDto:
        return {
            'snakes': [snake.to_dto() for snake in self.snakes],
            'board': self.board.to_dto(),
            'round': self.round
        }


games: dict[str, Game] = {}


@dataclass
class StartGameInput:
    room_id: str
    player: Player


BOARD_WIDTH = 50
BOARD_HEIGHT = 50


@app.post('/game')
def start_game(ipt: StartGameInput) -> GameDto:
    def generate_snake_head_and_after_head() -> tuple[Point, Point]:
        head = Point(random.randint(3, BOARD_WIDTH - 3),
                     random.randint(3, BOARD_HEIGHT - 3))
        after_head = [Point(head.x, head.y + 1),
                      Point(head.x, head.y - 1),
                      Point(head.x + 1, head.y),
                      Point(head.x - 1, head.y)][random.randint(0, 3)]
        return head, after_head

    head, after_head = generate_snake_head_and_after_head()

    if ipt.room_id not in games:
        board = Board(width=BOARD_WIDTH, height=BOARD_HEIGHT)
        snakes = [Snake(body_nodes=[head, after_head],
                        board=board, player=ipt.player)]
        game = Game(snakes=snakes, board=board, round=1)
        games[ipt.room_id] = game
    else:
        game = games[ipt.room_id]
        while any(head in snake.body_points or after_head in snake.body_points
                  for snake in game.snakes):
            head, after_head = generate_snake_head_and_after_head()
        game.snakes.append(Snake(body_nodes=[head, after_head],
                                 board=game.board, player=ipt.player))

    return game.to_dto()


@app.delete('/game/{room_id}')
def end_game(room_id: str, player_id: str) -> None:
    if room_id in games:
        games[room_id].snakes = list(
            filter(lambda snake: snake.player.id != player_id,
                   games[room_id].snakes))
        if games[room_id].snakes == []:
            del games[room_id]


class UpdateCodePayload(TypedDict):
    player_id: int
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


async def update_code(room_id: str, payload: UpdateCodePayload) -> None:
    player_id, code = payload['player_id'], payload['code']

    game = games[room_id]
    for snake in game.snakes:
        if snake.player.id == player_id:
            snake.update_code(code)
            break


async def update_game(game: Game) -> None:
    for snake in game.snakes:
        other_snakes = filter(lambda s: s != snake,  # pylint: disable=cell-var-from-loop
                              game.snakes)
        snake.forward(other_snakes=list(other_snakes))


@app.websocket('/game/{room_id}')
async def websocket_endpoint(websocket: WebSocket, room_id: str) -> None:
    await websocket.accept()

    last_time = time.time()

    async def receive_handle():
        while True:
            msg: IncomingMessage = await websocket.receive_json()
            if msg:
                if msg['type'] == 'update-code':
                    await update_code(room_id=room_id, payload=msg['payload'])

    receiver_task = asyncio.create_task(receive_handle())

    try:
        while True:
            # Send updates periodically
            if time.time() - last_time > 0.5:
                last_time = time.time()

                game = games[room_id]
                await update_game(game)

                await websocket.send_json(UpdateGameMessage(
                    type='update-game',
                    payload=UpdateGamePayload(game=game.to_dto())))
            else:
                # Sleep a bit to prevent high CPU usage
                await asyncio.sleep(0.1)

    except Exception as exc:
        print(f'Error in websocket communication: {exc}')

    finally:
        receiver_task.cancel()  # Stop the receiver task when exit
