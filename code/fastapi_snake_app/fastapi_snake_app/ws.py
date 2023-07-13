import asyncio
import random
import time
from typing import Literal, TypeAlias, TypedDict, Protocol
from dataclasses import dataclass

from fastapi import WebSocket

from fastapi_snake_app.main import app


Color: TypeAlias = str


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


class FoodDto(TypedDict):
    point: PointDto
    color: Color


@dataclass
class FoodInfo:
    point: Point
    color: Color


@dataclass
class Food:
    point: Point
    color: Color

    def to_dto(self) -> FoodDto:
        return FoodDto(point=self.point.to_dto(), color=self.color)

    def to_info(self) -> FoodInfo:
        return FoodInfo(point=self.point, color=self.color)


class BoardDto(TypedDict):
    height: int
    width: int
    foods: list[FoodDto]


@dataclass
class BoardInfo:
    height: int
    width: int
    foods: list[FoodInfo]


@dataclass
class Board:
    height: int
    width: int
    foods: list[Food]

    def to_dto(self) -> BoardDto:
        return BoardDto(height=self.height, width=self.width,
                        foods=[food.to_dto() for food in self.foods])

    def to_info(self) -> BoardInfo:
        return BoardInfo(height=self.height, width=self.width,
                         foods=[food.to_info() for food in self.foods])


class PlayerDto(TypedDict):
    id: str
    name: str
    score: int


@dataclass
class Player:
    id: str  # pylint: disable=invalid-name
    name: str
    score: int = 0

    def to_dto(self) -> PlayerDto:
        return {'id': self.id, 'name': self.name, 'score': self.score}


class SnakeDto(TypedDict):
    body_points: list[PointDto]
    player: PlayerDto
    color: Color


@dataclass
class SnakeInfo:
    body_points: list[Point]
    head: Point
    direction: Direction
    player: Player


class StepFunc(Protocol):
    def __call__(self, snake: SnakeInfo, other_snakes: list[SnakeInfo], board: BoardInfo) \
            -> Literal['TURN_LEFT', 'TURN_RIGHT', 'KEEP_STRAIGHT']:
        ...


DEFAULT_SNAKE_CODE = '''
def step(snake, other_snakes, board):
    """
    每一步的决策函数，返回值为 'TURN_LEFT', 'TURN_RIGHT', 'KEEP_STRAIGHT' 之一

    :param snake: 自己的蛇，如 SnakeInfo(
        body_points=[Point(x=0, y=0), Point(x=0, y=1), Point(x=0, y=2)],
        head=Point(x=0, y=0),
        direction='up',  # 'up', 'down', 'left', 'right'
        player=Player(id='2j3lj66x', name='Alice'),
    )
    :param other_snakes: 其他蛇的信息，如 [SnakeInfo(...), SnakeInfo(...)]
    :param board: 地图信息，如 BoardInfo(
        width=20,
        height=20,
        foods=[Food(point=Point(x=1, y=1), color='#ff0000'), Food(...)],
    )
    """

    return 'KEEP_STRAIGHT'
'''


class Snake:
    def __init__(self, *, body_nodes: list[Point], color: Color,
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
                               board=self._board.to_info())
            if action not in ('TURN_LEFT', 'TURN_RIGHT', 'KEEP_STRAIGHT'):
                raise ValueError('Invalid code')
            self._code = code
            print(
                f'Player(id="{self.player.id}", name="{self.player.name}"): Code updated')
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
    def tail(self) -> list[Point]:
        return self._body_points[1:]

    @property
    def body_points(self) -> list[Point]:
        return self._body_points

    @property
    def direction(self) -> Direction:
        return self._direction

    @property
    def tail_direction(self) -> Direction:
        last, before_last = self._body_points[-1], self._body_points[-2]
        if last.x == before_last.x:
            if last.y < before_last.y:
                return 'up'
            return 'down'
        if last.x < before_last.x:
            return 'left'
        return 'right'

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
        locals_ = {}
        exec(code, {}, locals_)  # pylint: disable=exec-used
        return locals_['step']

    @property
    def next_head(self) -> Point:
        if self._direction == 'up':
            return Point(self.head.x, self.head.y - 1)
        if self._direction == 'left':
            return Point(self.head.x - 1, self.head.y)
        if self._direction == 'down':
            return Point(self.head.x, self.head.y + 1)
        return Point(self.head.x + 1, self.head.y)

    @property
    def next_tail(self) -> list[Point]:
        return self.next_body_points[1:]

    @property
    def next_body_points(self) -> list[Point]:
        return [self.next_head] + self._body_points[:-1]

    def forward(self, other_snakes: list['Snake']) -> None:
        step_func = self.__parse_step_func(self._code)

        action: Literal['TURN_LEFT', 'TURN_RIGHT', 'KEEP_STRAIGHT'] = step_func(
            snake=self.to_info(),
            other_snakes=[snake.to_info() for snake in other_snakes],
            board=self._board.to_info())

        if action == 'TURN_LEFT':
            self._turn_left()
        elif action == 'TURN_RIGHT':
            self._turn_right()

        self._body_points = self.next_body_points

    def would_hit(self, other: 'Snake') -> bool:
        return self.next_head in other.body_points

    def would_hit_itself(self) -> bool:
        return self.next_head in self.next_tail

    def would_hit_wall(self) -> bool:
        return (self.next_head.x <= 0 or self.next_head.x > self._board.width or
                self.next_head.y <= 0 or self.next_head.y > self._board.height)

    @property
    def length(self) -> int:
        return len(self._body_points)

    @length.setter
    def length(self, value: int) -> None:
        if value < 2:
            raise ValueError('Invalid length')

        if value < self.length:
            self._body_points = self._body_points[:value]
            return

        last = self._body_points[-1]
        if self.tail_direction == 'up':
            for i in range(value - self.length):
                self._body_points.append(Point(last.x, last.y - i - 1))
        elif self.tail_direction == 'left':
            for i in range(value - self.length):
                self._body_points.append(Point(last.x - i - 1, last.y))
        elif self.tail_direction == 'down':
            for i in range(value - self.length):
                self._body_points.append(Point(last.x, last.y + i + 1))
        else:
            for i in range(value - self.length):
                self._body_points.append(Point(last.x + i + 1, last.y))

    def to_dto(self) -> SnakeDto:
        return {
            'body_points': [point.to_dto() for point in self._body_points],
            'player': self._player.to_dto(),
            'color': self._color,
        }

    def to_info(self) -> SnakeInfo:
        return SnakeInfo(body_points=self._body_points,
                         head=self.head,
                         direction=self._direction,
                         player=self._player)


class GameDto(TypedDict):
    snakes: list[SnakeDto]
    players: list[PlayerDto]
    board: BoardDto
    iteration: int


@dataclass
class Game:
    snakes: list[Snake]
    players: list[Player]
    board: Board
    iteration: int = 0

    def generate_snake(self, *, color: Color, player: Player) -> Snake:
        def generate_snake_head_and_after_head() -> tuple[Point, Point]:
            head = Point(random.randint(3, BOARD_WIDTH - 3),
                         random.randint(3, BOARD_HEIGHT - 3))
            after_head = [Point(head.x, head.y + 1),
                          Point(head.x, head.y - 1),
                          Point(head.x + 1, head.y),
                          Point(head.x - 1, head.y)][random.randint(0, 3)]
            return head, after_head

        head, after_head = generate_snake_head_and_after_head()

        while any(head in snake.body_points or after_head in snake.body_points
                  for snake in self.snakes):
            head, after_head = generate_snake_head_and_after_head()

        snake = Snake(body_nodes=[head, after_head],
                      board=self.board, player=player, color=color)
        self.snakes.append(snake)

        return snake

    def to_dto(self) -> GameDto:
        return {
            'snakes': [snake.to_dto() for snake in self.snakes],
            'players': [player.to_dto() for player in self.players],
            'board': self.board.to_dto(),
            'iteration': self.iteration,
        }


games: dict[str, Game] = {}


@dataclass
class StartGameInput:
    room_id: str
    player: Player
    snake_color: Color


BOARD_WIDTH = 50
BOARD_HEIGHT = 50


@app.post('/game')
def start_game(ipt: StartGameInput) -> GameDto:
    if ipt.room_id not in games:
        board = Board(width=BOARD_WIDTH, height=BOARD_HEIGHT, foods=[])
        game = Game(snakes=[], players=[], board=board)
        game.generate_snake(color=ipt.snake_color, player=ipt.player)
        games[ipt.room_id] = game
    else:
        game = games[ipt.room_id]
        game.generate_snake(color=ipt.snake_color, player=ipt.player)

    game.players.append(ipt.player)

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


def update_game(game: Game) -> None:
    for snake in game.snakes:
        other_snakes = [other_snake for other_snake in game.snakes
                        if other_snake != snake]

        # 碰撞检测
        if (snake.would_hit_itself() or snake.would_hit_wall() or
                any(snake.would_hit(other_snake) for other_snake in other_snakes)):
            game.board.foods += [Food(point=point, color=snake.color)
                                 for point in snake.body_points]
            game.snakes.remove(snake)
            game.generate_snake(color=snake.color, player=snake.player)
            snake.player.score //= 2

        # 吃食物
        if snake.next_head in map(lambda food: food.point, game.board.foods):
            snake.length += 1
            game.board.foods = [food for food in game.board.foods
                                if food.point != snake.next_head]
            snake.player.score += 1

        # 生成食物
        if len(game.board.foods) < 10 and random.random() < 0.1:
            point = Point(random.randint(3, BOARD_WIDTH - 3),
                          random.randint(3, BOARD_HEIGHT - 3))
            while (any(food.point == point for food in game.board.foods) or
                   any(point in snake.body_points for snake in game.snakes)):
                point = Point(random.randint(3, BOARD_WIDTH - 3),
                              random.randint(3, BOARD_HEIGHT - 3))
            game.board.foods.append(Food(point=point, color='#087f5b'))

        snake.forward(other_snakes=list(other_snakes))


@app.websocket('/game/{room_id}')
async def websocket_endpoint(websocket: WebSocket, room_id: str) -> None:
    await websocket.accept()

    game = games[room_id]

    last_iteration = game.iteration
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

                if game.iteration == last_iteration:
                    game.iteration += 1
                    last_iteration = game.iteration

                    update_game(game)

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
