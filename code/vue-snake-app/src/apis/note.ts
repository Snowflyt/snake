import { request } from '@/utils/request';

export interface NoteDto {
  id: number;
  text: string;
  completed: boolean;
}

export interface CreateNoteInput {
  text: string;
  completed: boolean;
}

const noteApi = {
  async findAll(): Promise<NoteDto[]> {
    return await request.get('/api/notes');
  },

  async create(input: CreateNoteInput): Promise<NoteDto> {
    return await request.post('/api/note', {
      data: input,
    });
  },
};

export default noteApi;
