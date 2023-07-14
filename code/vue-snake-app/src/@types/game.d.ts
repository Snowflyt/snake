export interface Point {
  x: number;
  y: number;
}

export interface PlayerDto {
  id: string;
  name: string;
  score: number;
}

export interface SnakeDto {
  bodyPoints: Point[];
  player: PlayerDto;
  color: string;
}

export interface FoodDto {
  point: Point;
  color: string;
}

export interface BoardDto {
  width: number;
  height: number;
  foods: FoodDto[];
}

export interface GameDto {
  snakes: SnakeDto[];
  players: PlayerDto[];
  board: BoardDto;
}
