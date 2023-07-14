import gameApi from '@/apis/game';
import noteApi from '@/apis/note';
import sampleApi from '@/apis/sample';
import userApi from '@/apis/user';
import wsGameApi from '@/apis/ws/game';

export const apis = {
  game: gameApi,
  note: noteApi,
  user: userApi,
  sample: sampleApi,
  ws: {
    game: wsGameApi,
  },
};
