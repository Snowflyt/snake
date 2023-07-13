import { request } from '@/utils/request';

export interface Note {
  id: number;
  text: string;
  completed: boolean;
}

export interface CreateNoteInput {
  text: string;
  completed: boolean;
}

const noteApi = {
  async findAll(): Promise<Note[]> {
    return await request.get('/api/notes');
  },

  async create(input: CreateNoteInput): Promise<Note> {
    return await request.post('/api/note', {
      data: input,
    });
  },
};

export default noteApi;
