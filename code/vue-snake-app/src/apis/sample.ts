import { request } from '../utils/request';

interface UserDto {
  username: string;
  password: string;
}

const sampleApi = {
  async echo(text: string): Promise<string> {
    return await request.get('/api/echo', { params: { text } });
  },

  async readUsers(): Promise<any> {
    return await request.get('api/user');
  },

  async createUsers(data: {
    id: number;
    phone_number: string;
    language_excellent: string;
    username: string;
    password: string;
  }): Promise<any> {
    return await request.post('api/user', {
      data,
    });
  },

  async login(data: { username: string; password: string }): Promise<string[]> {
    return await request.post('api/login', { data });
  },
};

export default sampleApi;
