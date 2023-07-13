import { getLuminance, toHex, rgba } from 'color2k';
import * as seedrandom from 'seedrandom';

/**
 * 根据字符串生成亮度在 0.2 ~ 0.4 之间的颜色
 * @param str 用作 Seed 的字符串
 * @returns
 */
export const generateColor = (str: string) => {
  const rng = seedrandom(str);

  /** @type {string} */
  let color;
  do {
    const r = Math.floor(rng() * 255);
    const g = Math.floor(rng() * 255);
    const b = Math.floor(rng() * 255);
    color = rgba(r, g, b, 1);
  } while (getLuminance(color) > 0.4 || getLuminance(color) < 0.2);

  return toHex(color);
};
