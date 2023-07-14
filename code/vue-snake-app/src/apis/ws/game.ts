import { createWebSocketClient } from '@/utils/wsClient';

import type { GameDto } from '@/@types/game';

interface UpdateGamePayload {
  game: GameDto;
}

interface UpdateGameMessage {
  type: 'update-game';
  payload: UpdateGamePayload;
}

interface CodeUpdateConfirmMessage {
  type: 'code-update-confirm';
  payload: '';
}

type IncomingMessage = UpdateGameMessage | CodeUpdateConfirmMessage;

interface UpdateCodePayload {
  playerId: string;
  code: string;
}

interface UpdateCodeMessage {
  type: 'update-code';
  payload: UpdateCodePayload;
}

type OutgoingMessage = UpdateCodeMessage;

const HOST = '101.132.165.23';
const PORT = 8000;

const wsGameApi = {
  createClient(input: { roomId: string }) {
    return createWebSocketClient<IncomingMessage, OutgoingMessage>(
      `ws://${HOST}:${PORT}/game/${input.roomId}`,
    );
  },
};

export default wsGameApi;
