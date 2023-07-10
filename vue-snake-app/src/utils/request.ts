/**
 * 构建 URL
 * @param url
 * @param params
 * @returns
 */
const buildURL = (url: string | URL, params?: Record<string, string>): URL => {
  let urlObject: URL;
  try {
    urlObject = new URL(url);
  } catch {
    try {
      urlObject = new URL(url, window.location.origin);
    } catch (error) {
      throw new Error('无效的 URL');
    }
  }

  if (!params) return urlObject;

  for (const [key, value] of Object.entries(params)) {
    urlObject.searchParams.append(key, value);
  }

  return urlObject;
};

/**
 * 对 fetch API 进行简单封装
 */
export const request = {
  /**
   * 通过 GET 方法请求 JSON 数据
   * @param url
   * @param options
   * @returns
   */
  async get<R = unknown>(
    url: string | URL,
    options?: Omit<RequestInit, 'method'> & { params?: Record<string, string> },
  ): Promise<R> {
    const response = await fetch(buildURL(url, options?.params), {
      ...options,
      method: 'GET',
      headers: {
        'Content-Type': 'application/json;charset=utf-8',
      },
    });
    if (!response.ok) {
      throw new Error(response.statusText);
    }
    return await response.json();
  },

  /**
   * 通过 DELETE 方法请求 JSON 数据
   * @param url
   * @param options
   * @returns
   */
  async delete<R = unknown>(
    url: string | URL,
    options?: Omit<RequestInit, 'method'> & { params?: Record<string, string> },
  ): Promise<R> {
    const response = await fetch(buildURL(url, options?.params), {
      ...options,
      method: 'GET',
      headers: {
        'Content-Type': 'application/json;charset=utf-8',
      },
    });
    if (!response.ok) {
      throw new Error(response.statusText);
    }
    return await response.json();
  },

  /**
   * 通过 POST 方法请求 JSON 数据
   * @param url
   * @param options
   * @returns
   */
  async post<R = unknown>(
    url: string,
    options?: Omit<RequestInit, 'method'> & {
      params?: Record<string, string>;
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      data?: any;
    },
  ): Promise<R> {
    const response = await fetch(buildURL(url, options?.params), {
      ...options,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json;charset=utf-8',
      },
      ...(options?.data !== undefined
        ? { body: JSON.stringify(options.data) }
        : {}),
    });
    if (!response.ok) {
      throw new Error(response.statusText);
    }
    return await response.json();
  },

  /**
   * 通过 PUT 方法请求 JSON 数据
   * @param url
   * @param options
   * @returns
   */
  async put<R = unknown>(
    url: string,
    options?: Omit<RequestInit, 'method'> & {
      params?: Record<string, string>;
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      data?: any;
    },
  ): Promise<R> {
    const response = await fetch(buildURL(url, options?.params), {
      ...options,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json;charset=utf-8',
      },
      ...(options?.data !== undefined
        ? { body: JSON.stringify(options.data) }
        : {}),
    });
    if (!response.ok) {
      throw new Error(response.statusText);
    }
    return await response.json();
  },

  /**
   * 通过 PATCH 方法请求 JSON 数据
   * @param url
   * @param options
   * @returns
   */
  async patch<R = unknown>(
    url: string,
    options?: Omit<RequestInit, 'method'> & {
      params?: Record<string, string>;
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      data?: any;
    },
  ): Promise<R> {
    const response = await fetch(buildURL(url, options?.params), {
      ...options,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json;charset=utf-8',
      },
      ...(options?.data !== undefined
        ? { body: JSON.stringify(options.data) }
        : {}),
    });
    if (!response.ok) {
      throw new Error(response.statusText);
    }
    return await response.json();
  },
};
