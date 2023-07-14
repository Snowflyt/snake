<script setup lang="ts">
import { ElMessage } from 'element-plus';
import { ref } from 'vue';

let ws: WebSocket;

const clientId = ref(0);
const messageContent = ref('');

function connect(event: MouseEvent) {
  ElMessage.info('开始连接');
  ws = new WebSocket('ws://101.132.165.23:8000/ws/' + clientId.value);
  ws.onclose = function (event) {
    if (event.wasClean) {
      ElMessage.info(
        `[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`,
      );
    } else {
      // 例如服务器进程被杀死或网络中断
      // 在这种情况下，event.code 通常为 1006
      ElMessage.info('[close] Connection died');
    }
  };

  ws.onerror = (error) => {
    ElMessage.error(`${error}`);
  };

  ws.onmessage = function (event) {
    const messages = document.getElementById('chatMainContent') as HTMLElement;

    const messageOut = document.createElement('li');
    messageOut.className = 'flex justify-start';

    const message = document.createElement('div');
    message.className =
      'relative max-w-xl rounded px-4 py-2 text-gray-700 shadow';

    const content = document.createTextNode(event.data);
    message.appendChild(content);
    messageOut.appendChild(message);
    messages.appendChild(messageOut);
  };
  event.preventDefault();
}

function sendMessage() {
  console.log('fdfs');
  const messages = document.getElementById('chatMainContent') as HTMLElement;

  const messageOut = document.createElement('li');
  messageOut.className = 'flex justify-start';
  const message = document.createElement('div');
  message.className =
    'relative max-w-xl rounded px-4 py-2 text-gray-700 shadow';
  ws.send(messageContent.value);
  const content = document.createTextNode(messageContent.value);
  message.appendChild(content);
  messageOut.appendChild(message);
  messages.appendChild(messageOut);
  messageContent.value = '';
}
</script>

<template>
  <div class="container mx-auto">
    <div class="max-w-2xl rounded border">
      <div>
        <div class="w-full">
          <div class="relative items-center border-b border-gray-300 p-3">
            <div class="flex">
              <img
                class="h-10 w-10 rounded-full object-cover"
                src="https://cdn.pixabay.com/photo/2018/01/15/07/51/woman-3083383__340.jpg"
                alt="username" />
              <span class="ml-2 block font-bold text-gray-600">聊天室</span>
              <span
                class="absolute left-10 top-3 h-3 w-3 rounded-full bg-green-600">
              </span>
              <button
                class="relative left-[35%] inline rounded border-2 border-black p-2"
                @click="connect">
                connect
              </button>
            </div>
          </div>
          <div class="relative h-[40rem] w-full overflow-y-auto p-6">
            <ul id="chatMainContent" class="space-y-2"></ul>
          </div>

          <div
            class="flex w-full items-center justify-between border-t border-gray-300 p-3">
            <input
              v-model="messageContent"
              type="text"
              placeholder="Message"
              class="mx-3 block w-full rounded-full bg-gray-100 py-2 pl-4 outline-none focus:text-gray-700"
              name="message"
              required />
            <button type="button">
              <svg
                class="h-5 w-5 origin-center rotate-90 text-gray-500"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                style="cursor: hand"
                @click="sendMessage">
                <path
                  d="M10.894 2.553a1 1 0 00-1.788 0l-7 14a1 1 0 001.169 1.409l5-1.429A1 1 0 009 15.571V11a1 1 0 112 0v4.571a1 1 0 00.725.962l5 1.428a1 1 0 001.17-1.408l-7-14z" />
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
