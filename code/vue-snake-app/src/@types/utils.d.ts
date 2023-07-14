export type CamelToSnake<S extends string> =
  CamelToSnakeHelper<S> extends `_${infer T}` ? T : CamelToSnakeHelper<S>;
type CamelToSnakeHelper<S extends string> = S extends `${infer T}${infer U}`
  ? `${T extends Capitalize<T>
      ? '_'
      : ''}${Lowercase<T>}${CamelToSnakeHelper<U>}`
  : S;

export type Snakeize<T> = T extends Array<infer U>
  ? Array<Snakeize<U>>
  : {
      [K in keyof T as CamelToSnakeHelper<K & string>]: T[K] extends Record<
        string,
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        any
      >
        ? // eslint-disable-next-line @typescript-eslint/no-explicit-any
          T[K] extends Array<Record<string, any>>
          ? Array<Snakeize<T[K][number]>>
          : Snakeize<T[K]>
        : T[K];
    };

export type SnakeToCamel<S extends string> =
  SnakeToCamelHelper<S> extends `${infer T}${infer U}`
    ? `${Uncapitalize<T>}${SnakeToCamelHelper<U>}`
    : S;
type SnakeToCamelHelper<S extends string> = S extends `${infer T}_${infer U}`
  ? `${Capitalize<T>}${SnakeToCamelHelper<Capitalize<U>>}`
  : S;

export type Camelize<T> = T extends Array<infer U>
  ? Array<Camelize<U>>
  : {
      [K in keyof T as SnakeToCamel<K & string>]: T[K] extends Record<
        string,
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        any
      >
        ? // eslint-disable-next-line @typescript-eslint/no-explicit-any
          T[K] extends Array<Record<string, any>>
          ? Array<Camelize<T[K][number]>>
          : Camelize<T[K]>
        : T[K];
    };
