import type {
  SnakeToCamel,
  CamelToSnake,
  Snakeize,
  Camelize,
} from '@/@types/utils';

/**
 * 将 snake_case 字符串转换为 camelCase 字符串
 * @param str snake_case 字符串
 * @returns camelCase 字符串
 */
export const snakeToCamel = <S extends string>(str: S): SnakeToCamel<S> =>
  str.replace(/(_\w)/g, (m) => m[1].toUpperCase()) as SnakeToCamel<S>;

/**
 * 将对象的 key 从 camelCase 转换为 snake_case
 * @param obj key 为 camelCase 的对象
 * @returns key 为 snake_case 的对象
 */
// eslint-disable-next-line @typescript-eslint/no-explicit-any
export const camelize = <T extends Record<string, any>>(
  obj: T,
): Camelize<T> => {
  const result = {} as Camelize<T>;
  for (const [key, value] of Object.entries(obj)) {
    const newKey = snakeToCamel(key) as keyof Camelize<T>;
    result[newKey] = value as Camelize<T>[keyof Camelize<T>];
  }
  return result;
};

/**
 * 将 camelCase 字符串转换为 snake_case 字符串
 * @param str camelCase 字符串
 * @returns snake_case 字符串
 */
export const camelToSnake = <S extends string>(str: S) =>
  str.replace(/[A-Z]/g, (m) => '_' + m.toLowerCase()) as CamelToSnake<S>;

/**
 * 将对象的 key 从 snake_case 转换为 camelCase
 * @param obj key 为 snake_case 的对象
 * @returns key 为 camelCase 的对象
 */
// eslint-disable-next-line @typescript-eslint/no-explicit-any
export const snakeize = <T extends Record<string, any>>(
  obj: T,
): Snakeize<T> => {
  const result = {} as Snakeize<T>;
  for (const [key, value] of Object.entries(obj)) {
    const newKey = camelToSnake(key) as keyof Snakeize<T>;
    result[newKey] = value as Snakeize<T>[keyof Snakeize<T>];
  }
  return result;
};
