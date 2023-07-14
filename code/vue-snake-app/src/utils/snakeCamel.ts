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
export const camelize = <
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  T extends Array<Record<string, any>> | Record<string, any>,
>(
  obj: T,
  { deep = true }: { deep?: boolean } = {},
): Camelize<T> => {
  if (Array.isArray(obj))
    return obj.map((item) => camelize(item)) as Camelize<T>;

  const result = {} as Camelize<T>;
  for (const [key, value] of Object.entries(obj)) {
    const newKey = snakeToCamel(key) as keyof Camelize<T>;
    let newValue: Camelize<T>[keyof Camelize<T>] = value;
    if (deep && typeof value === 'object' && value !== null) {
      if (Array.isArray(value)) {
        newValue = value.map((item) =>
          camelize(item),
        ) as Camelize<T>[keyof Camelize<T>];
      } else {
        newValue = camelize(value) as Camelize<T>[keyof Camelize<T>];
      }
    }
    result[newKey] = newValue;
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
export const snakeize = <
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  T extends Array<Record<string, any>> | Record<string, any>,
>(
  obj: T,
  { deep = true }: { deep?: boolean } = {},
): Snakeize<T> => {
  if (Array.isArray(obj))
    return obj.map((item) => snakeize(item)) as Snakeize<T>;

  const result = {} as Snakeize<T>;
  for (const [key, value] of Object.entries(obj)) {
    const newKey = camelToSnake(key) as keyof Snakeize<T>;
    let newValue: Snakeize<T>[keyof Snakeize<T>] = value;
    if (deep && typeof value === 'object' && value !== null) {
      if (Array.isArray(value)) {
        newValue = value.map((item) =>
          snakeize(item),
        ) as Snakeize<T>[keyof Snakeize<T>];
      } else {
        newValue = snakeize(value) as Snakeize<T>[keyof Snakeize<T>];
      }
    }
    result[newKey] = newValue;
  }
  return result;
};
