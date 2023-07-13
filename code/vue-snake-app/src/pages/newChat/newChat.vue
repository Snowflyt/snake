<template>
  <div class="container mx-auto">
    <div class="min-w-full rounded border lg:grid lg:grid-cols-3">
      <div class="border-r border-gray-300 lg:col-span-1">
        <div class="m-3">
          <div class="relative text-gray-600">
            <span class="absolute inset-y-0 left-0 flex items-center pl-2">
              <svg
                fill="none"
                stroke="currentColor"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                viewBox="0 0 24 24"
                class="h-6 w-6 text-gray-300">
                <path d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
              </svg>
            </span>
            <input
              type="search"
              class="block w-full rounded bg-gray-100 py-2 pl-10 outline-none"
              name="search"
              placeholder="Search"
              required />
          </div>
        </div>

        <ul class="h-[32rem] overflow-auto">
          <h2 class="my-2 ml-2 text-lg text-gray-600">Chats</h2>
          <li>
            <b
              class="flex cursor-pointer items-center border-b border-gray-300 px-3 py-2 text-sm transition duration-150 ease-in-out hover:bg-gray-100 focus:outline-none">
              <img
                class="h-10 w-10 rounded-full object-cover"
                src="https://cdn.pixabay.com/photo/2018/09/12/12/14/man-3672010__340.jpg"
                alt="username" />
              <div class="w-full pb-2">
                <div class="flex justify-between">
                  <span class="ml-2 block font-semibold text-gray-600"
                    >Jhon Don</span
                  >
                  <span class="ml-2 block text-sm text-gray-600"
                    >25 minutes</span
                  >
                </div>
                <span class="ml-2 block text-sm text-gray-600">bye</span>
              </div>
            </b>
            <b
              class="flex cursor-pointer items-center border-b border-gray-300 bg-gray-100 px-3 py-2 text-sm transition duration-150 ease-in-out focus:outline-none">
              <img
                class="h-10 w-10 rounded-full object-cover"
                src="https://cdn.pixabay.com/photo/2016/06/15/15/25/loudspeaker-1459128__340.png"
                alt="username" />
              <div class="w-full pb-2">
                <div class="flex justify-between">
                  <span class="ml-2 block font-semibold text-gray-600"
                    >Same</span
                  >
                  <span class="ml-2 block text-sm text-gray-600"
                    >50 minutes</span
                  >
                </div>
                <span class="ml-2 block text-sm text-gray-600">Good night</span>
              </div>
            </b>
            <b
              class="flex cursor-pointer items-center border-b border-gray-300 px-3 py-2 text-sm transition duration-150 ease-in-out hover:bg-gray-100 focus:outline-none">
              <img
                class="h-10 w-10 rounded-full object-cover"
                src="https://cdn.pixabay.com/photo/2018/01/15/07/51/woman-3083383__340.jpg"
                alt="username" />
              <div class="w-full pb-2">
                <div class="flex justify-between">
                  <span class="ml-2 block font-semibold text-gray-600"
                    >Emma</span
                  >
                  <span class="ml-2 block text-sm text-gray-600">6 hour</span>
                </div>
                <span class="ml-2 block text-sm text-gray-600"
                  >Good Morning</span
                >
              </div>
            </b>
          </li>
        </ul>
      </div>
      <div class="hidden lg:col-span-2 lg:block">
        <div class="w-full">
          <div class="relative flex items-center border-b border-gray-300 p-3">
            <img
              class="h-10 w-10 rounded-full object-cover"
              src="https://cdn.pixabay.com/photo/2018/01/15/07/51/woman-3083383__340.jpg"
              alt="username" />
            <span class="ml-2 block font-bold text-gray-600">Emma</span>
            <span
              class="absolute left-10 top-3 h-3 w-3 rounded-full bg-green-600">
            </span>
          </div>
          <div class="relative h-[40rem] w-full overflow-y-auto p-6">
            <ul class="space-y-2">
              <li class="flex justify-start">
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
              </li>
            </ul>
          </div>

          <div
            class="flex w-full items-center justify-between border-t border-gray-300 p-3">
            <button>
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
            </button>

            <input
              type="text"
              placeholder="Message"
              class="mx-3 block w-full rounded-full bg-gray-100 py-2 pl-4 outline-none focus:text-gray-700"
              name="message"
              required />
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
                  d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 01-3-3V5a3 3 0 116 0v6a3 3 0 01-3 3z" />
              </svg>
            </button>
            <button type="submit">
              <svg
                class="h-5 w-5 origin-center rotate-90 text-gray-500"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
                fill="currentColor">
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

<script setup lang="ts"></script>
