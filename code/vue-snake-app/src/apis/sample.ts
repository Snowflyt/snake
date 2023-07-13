import { request } from '@/utils/request';

const sampleApi = {
  async echo(text: string): Promise<string> {
    return await request.get('/api/echo', { params: { text } });
  },
};

export default sampleApi;
