import { request } from '@/utils/request';
import { camelize, snakeize } from '@/utils/snakeCamel';

import type { GameDto } from '@/@types/game';
import type { Snakeize } from '@/@types/utils';

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
