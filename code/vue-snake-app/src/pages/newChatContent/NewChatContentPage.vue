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
            <ul id="chatMainContent" class="space-y-2">
              <!-- <li class="flex justify-start">
                <div
                  class="relative max-w-xl rounded px-4 py-2 text-gray-700 shadow">
                  <span class="block">Hi</span>
                </div>
              </li>
              <li class="flex justify-end">
                <div
                  class="relative max-w-xl rounded bg-gray-100 px-4 py-2 text-gray-700 shadow">
                  <span class="block">Hiiii</span>
                </div>
              </li>
              <li class="flex justify-end">
                <div
                  class="relative max-w-xl rounded bg-gray-100 px-4 py-2 text-gray-700 shadow">
                  <span class="block">how are you?</span>
                </div>
              </li>
              <li class="flex justify-start">
                <div
                  class="relative max-w-xl rounded px-4 py-2 text-gray-700 shadow">
                  <span class="block"
                    >Lorem ipsum dolor sit, amet consectetur adipisicing elit.
                  </span>
                </div>
              </li> -->
            </ul>
          </div>

          <div
            class="flex w-full items-center justify-between border-t border-gray-300 p-3">
            <!-- <button>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-6 w-6 text-gray-500"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor">
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </button>
            <button>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5 text-gray-500"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor">
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13" />
              </svg>
            </button> -->

            <input
              v-model="messageContent"
              type="text"
              placeholder="Message"
              class="mx-3 block w-full rounded-full bg-gray-100 py-2 pl-4 outline-none focus:text-gray-700"
              name="message"
              required />
            <!-- <button>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="h-5 w-5 text-gray-500"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor">
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z" />
              </svg>
            </button> -->
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
<<<<<<< HEAD:code/vue-snake-app/src/pages/newChatContent/newChatContent.vue
<script setup>
import { ref } from 'vue';
var ws = null;
var client_id = ref(0);
const messageContent = ref('');
function connect(event) {
  alert('开始连接');
  ws = new WebSocket('ws://101.132.165.23:8000/ws/' + client_id.value);
  ws.onclose = function (event) {
    if (event.wasClean) {
      alert(
        `[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`,
      );
    } else {
      // 例如服务器进程被杀死或网络中断
      // 在这种情况下，event.code 通常为 1006
      alert('[close] Connection died');
    }
  };

  ws.onerror = function (error) {
    alert(`[error] ${error.message}`);
  };
  ws.onmessage = function (event) {
    var messages = document.getElementById('chatMainContent');

    var messageOut = document.createElement('li');
    messageOut.className = 'flex justify-start';

    var message = document.createElement('div');
    message.className =
      'relative max-w-xl rounded px-4 py-2 text-gray-700 shadow';

    var content = document.createTextNode(event.data);
    message.appendChild(content);
    messageOut.appendChild(message);
    messages.appendChild(messageOut);
  };
  //ws.onopen = () => ws.send(messageContent.value);
  event.preventDefault();
}
function sendMessage() {
  console.log('fdfs');
  var messages = document.getElementById('chatMainContent');

  var messageOut = document.createElement('li');
  messageOut.className = 'flex justify-start';
  //messageOut.classList.add('flex', 'justify-start');
  var message = document.createElement('div');
  message.className =
    'relative max-w-xl rounded px-4 py-2 text-gray-700 shadow';
  // message.classList.add(
  //   'relative',
  //   'max-w-xl',
  //   ' rounded',
  //   'px-4',
  //   ' py-2',
  //   'text-gray-700',
  //   'shadow',
  // );
  ws.send(messageContent.value);
  var content = document.createTextNode(messageContent.value);
  message.appendChild(content);
  messageOut.appendChild(message);
  messages.appendChild(messageOut);
  messageContent.value = '';
}
</script>
=======
>>>>>>> 6beca03979371e6b8a0d664957c644919e955502:code/vue-snake-app/src/pages/newChatContent/NewChatContentPage.vue
