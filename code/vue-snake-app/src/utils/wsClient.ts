import { camelize, snakeize } from '@/utils/snakeCamel';

export interface WebSocketClient<
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  TIncomingMessage extends Record<string, any> = Record<string, any>,
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  TOutgoingMessage extends Record<string, any> = Record<string, any>,
> {
  on(event: 'message', listener: (data: TIncomingMessage) => void): void;
  on(event: 'open' | 'close' | 'error', listener: () => void): void;
  send(data: TOutgoingMessage): void;
  close(): void;
}

export const createWebSocketClient = <
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  TIncomingMessage extends Record<string, any> = Record<string, any>,
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  TOutgoingMessage extends Record<string, any> = Record<string, any>,
>(
  url: string | URL,
  protocols?: string | string[] | undefined,
): WebSocketClient<TIncomingMessage, TOutgoingMessage> => {
  const _ws = new WebSocket(url, protocols);

  const _onMessageListeners: ((data: TIncomingMessage) => void)[] = [];
  const _onOpenListeners: (() => void)[] = [];
  const _onCloseListeners: (() => void)[] = [];
  const _onErrorListeners: (() => void)[] = [];

  _ws.addEventListener('message', (event) => {
    const data = camelize(JSON.parse(event.data)) as TIncomingMessage;
    _onMessageListeners.forEach((listener) => listener(data));
  });
  _ws.addEventListener('open', () => {
    _onOpenListeners.forEach((listener) => listener());
  });
  _ws.addEventListener('close', () => {
    _onCloseListeners.forEach((listener) => listener());
  });
  _ws.addEventListener('error', () => {
    _onErrorListeners.forEach((listener) => listener());
  });

  return {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    on(event: string, listener: any) {
      switch (event) {
        case 'message':
          _onMessageListeners.push(listener);
          break;
        case 'open':
          _onOpenListeners.push(listener);
          break;
        case 'close':
          _onCloseListeners.push(listener);
          break;
        case 'error':
          _onErrorListeners.push(listener);
          break;
        default:
          throw new Error(`Unknown event: ${event}`);
      }
    },

    send(data: TOutgoingMessage) {
      _ws.send(JSON.stringify(snakeize(data)));
    },

    close() {
      _ws.close();
    },
  };
};
