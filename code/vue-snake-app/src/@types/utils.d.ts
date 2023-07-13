export type CamelToSnake<S extends string> =
  CamelToSnakeHelper<S> extends `_${infer T}` ? T : CamelToSnakeHelper<S>;
type CamelToSnakeHelper<S extends string> = S extends `${infer T}${infer U}`
  ? `${T extends Capitalize<T>
      ? '_'
      : ''}${Lowercase<T>}${CamelToSnakeHelper<U>}`
  : S;

export type Snakeize<T> = {
  [K in keyof T as CamelToSnakeHelper<K & string>]: T[K];
};

export type SnakeToCamel<S extends string> =
  SnakeToCamelHelper<S> extends `${infer T}${infer U}`
    ? `${Uncapitalize<T>}${SnakeToCamelHelper<U>}`
    : S;
type SnakeToCamelHelper<S extends string> = S extends `${infer T}_${infer U}`
  ? `${Capitalize<T>}${SnakeToCamelHelper<Capitalize<U>>}`
  : S;

export type Camelize<T> = {
  [K in keyof T as SnakeToCamel<K & string>]: T[K];
};
