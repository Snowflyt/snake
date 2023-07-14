import { request } from '@/utils/request';
import { camelize, snakeize } from '@/utils/snakeCamel';

import type { Snakeize } from '@/@types/utils';

interface Point {
  x: number;
  y: number;
}

interface PlayerDto {
  id: string;
  name: string;
  score: number;
}

interface SnakeDto {
  bodyPoints: Point[];
  player: PlayerDto;
  color: string;
}

interface FoodDto {
  point: Point;
  color: string;
}

interface BoardDto {
  width: number;
  height: number;
  foods: FoodDto[];
}

interface GameDto {
  snakes: SnakeDto[];
  players: PlayerDto[];
  board: BoardDto;
}

export interface JoinGameInput {
  roomId: string;
  player: {
    id: string;
    name: string;
  };
  snakeColor: string;
}

export interface QuitGameInput {
  roomId: string;
  playerId: string;
}

const gameApi = {
  async join(input: JoinGameInput): Promise<GameDto> {
    const game = await request.post<Snakeize<GameDto>>('/api/game', {
      data: snakeize(input),
    });
    return camelize(game);
  },

  async quit({ playerId, roomId }: QuitGameInput): Promise<void> {
    return await request.delete(`/api/game/${roomId}`, {
      params: snakeize({ playerId }),
    });
  },
};

export default gameApi;
