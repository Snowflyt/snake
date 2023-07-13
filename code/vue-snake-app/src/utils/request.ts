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

type RequestOptions = Omit<RequestInit, 'method'> & {
  params?: Record<string, string>;
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  data?: any;
};

const _request = async <R = unknown>(
  url: string | URL,
  method: 'GET' | 'POST' | 'PUT' | 'PATCH' | 'DELETE',
  options?: RequestOptions,
): Promise<R> => {
  const response = await fetch(buildURL(url, options?.params), {
    ...options,
    ...(options?.data ? { body: JSON.stringify(options.data) } : {}),
    method,
    headers: {
      'Content-Type': 'application/json',
    },
  });
  if (!response.ok) {
    throw new Error(response.statusText);
  }
  return await response.json();
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
    options?: RequestOptions,
  ): Promise<R> {
    return await _request(url, 'GET', options);
  },

  /**
   * 通过 DELETE 方法请求 JSON 数据
   * @param url
   * @param options
   * @returns
   */
  async delete<R = unknown>(
    url: string | URL,
    options?: RequestOptions,
  ): Promise<R> {
    return await _request(url, 'DELETE', options);
  },

  /**
   * 通过 POST 方法请求 JSON 数据
   * @param url
   * @param options
   * @returns
   */
  async post<R = unknown>(url: string, options?: RequestOptions): Promise<R> {
    return await _request(url, 'POST', options);
  },

  /**
   * 通过 PUT 方法请求 JSON 数据
   * @param url
   * @param options
   * @returns
   */
  async put<R = unknown>(url: string, options?: RequestOptions): Promise<R> {
    return await _request(url, 'PUT', options);
  },

  /**
   * 通过 PATCH 方法请求 JSON 数据
   * @param url
   * @param options
   * @returns
   */
  async patch<R = unknown>(url: string, options?: RequestOptions): Promise<R> {
    return await _request(url, 'PATCH', options);
  },
};
