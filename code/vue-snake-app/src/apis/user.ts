import { request } from '@/utils/request';
import { camelize, snakeize } from '@/utils/snakeCamel';

import type { Snakeize } from '@/@types/utils';

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
  async login(input: LoginInput): Promise<LoginResponse> {
    return await request.post('/api/login', { data: snakeize(input) });
  },

  async register(input: RegisterInput): Promise<RegisterResponse> {
    return await request.post('/api/register', { data: snakeize(input) });
  },

  async findAll(): Promise<UserDto[]> {
    const users = await request.get<Snakeize<UserDto[]>>('/api/users');
    return camelize(users);
  },

  async create(input: CreateUserInput): Promise<UserDto> {
    const user = await request.post<Snakeize<UserDto>>('/api/user', {
      data: snakeize(input),
    });
    return camelize(user);
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
