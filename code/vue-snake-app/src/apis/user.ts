import { request } from '@/utils/request';
import { snakeize, camelize } from '@/utils/snakeCamel';

export interface UserDto {
  id: number;
  username: string;
  password: string;
  phoneNumber: string;
  level: number;
  experience: number;
  commonMoney: number;
  specialMoney: number;
  totalStarts: number;
  rank: string;
  score: number;
  languageExcellent: string;
  profileURL: string;
}

export interface LoginInput {
  username: string;
  password: string;
}

export interface LoginResponse {
  message: string;
}

export interface RegisterInput {
  username: string;
  password: string;
  phoneNumber: string;
}

export interface RegisterResponse {
  message: string;
}

export interface CreateUserInput {
  id?: number;
  username: string;
  password: string;
  phoneNumber: string;
  languageExcellent?: string;
}

export interface UpdateUserInput {
  username?: string;
  password?: string;
  phoneNumber?: string;
  languageExcellent?: string;
}

export interface UpdateUserResponse {
  message: string;
  /**
   * 用户名
   */
  user: string;
}

const userApi = {
  async login(input: LoginInput): Promise<LoginInput> {
    return await request.post('/api/login', { data: input });
  },

  async register(input: RegisterInput): Promise<RegisterResponse> {
    return await request.post('/api/register', { data: snakeize(input) });
  },

  async create(input: CreateUserInput): Promise<UserDto> {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const user: any = await request.post('/api/user', {
      data: snakeize(input),
    });
    return camelize(user) as UserDto;
  },

  async update(
    userId: number,
    input: UpdateUserInput,
  ): Promise<UpdateUserResponse> {
    return await request.post('/api/user', {
      params: snakeize({ userId }),
      data: snakeize(input),
    });
  },
};

export default userApi;
