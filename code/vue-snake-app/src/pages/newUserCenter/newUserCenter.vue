<!-- component -->
<!-- component -->
<template>
  <a
    href="#"
    class="mb-6 flex items-center text-2xl font-semibold text-gray-900 dark:text-white">
    <img
      class="mr-2 h-8 w-8"
      src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Snake.svg/800px-Snake.svg.png"
      alt="logo" />
    CodeSnake
  </a>
  <div class="flex flex-row justify-between">
    <img
      id="u226_img"
      class="inline"
      src="../../assets/images/个人中心/u177.svg" />

    <img
      id="u227_img"
      class="inline"
      src="../../assets/images/个人中心/u178.svg" />
  </div>
  <div class="w-100 flex flex-row justify-between">
    <button class="text-2xl font-bold" @click="$router.go(-1)">Back</button>
    <button class="text-2xl font-bold" @click="$router.push('./setting')">
      Setting
    </button>
  </div>
  <div class="font-mono my-16 min-h-screen bg-gray-200 pt-2">
    <div class="container mx-auto">
      <div class="inputs mx-auto w-full max-w-2xl p-6">
        <h2 class="text-2xl text-gray-900">Account Setting</h2>
        <form class="mt-6 border-t border-gray-400 pt-4">
          <div class="-mx-3 mb-6 flex flex-wrap">
            <div class="mb-6 w-full px-3 md:w-full">
              <label
                class="mb-2 block text-xs font-bold uppercase tracking-wide text-gray-700"
                for="grid-text-1"
                >email address</label
              >
              <input
                id="grid-text-1"
                class="block w-full appearance-none rounded-md border border-gray-400 bg-white px-4 py-3 leading-tight text-gray-700 shadow-inner focus:border-gray-500 focus:outline-none"
                type="text"
                placeholder="Enter email"
                required />
            </div>
            <div class="mb-6 w-full px-3 md:w-full">
              <label
                class="mb-2 block text-xs font-bold uppercase tracking-wide text-gray-700"
                >password</label
              >
              <button
                class="appearance-none rounded-md border border-gray-400 bg-gray-200 px-2 py-1 text-gray-900 shadow-sm">
                change your password
              </button>
            </div>
            <div class="mb-6 w-full px-3 md:w-full">
              <label
                class="mb-2 block text-xs font-bold uppercase tracking-wide text-gray-700"
                >pick your country</label
              >
              <div class="relative inline-block w-full shrink">
                <select
                  class="block w-full appearance-none rounded border border-gray-400 bg-white px-4 py-2 pr-8 text-gray-600 shadow-inner">
                  <option>choose ...</option>
                  <option>USA</option>
                  <option>France</option>
                  <option>Spain</option>
                  <option>UK</option>
                </select>
                <div
                  class="pointer-events-none absolute right-0 top-0 mt-3 flex items-center px-2 text-gray-600">
                  <svg
                    class="h-4 w-4 fill-current"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20">
                    <path
                      d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />
                  </svg>
                </div>
              </div>
            </div>
            <div class="mb-6 w-full px-3 md:w-full">
              <label
                class="mb-2 block text-xs font-bold uppercase tracking-wide text-gray-700"
                >fav language</label
              >
              <div class="relative inline-block w-full shrink">
                <select
                  class="block w-full appearance-none rounded border border-gray-400 bg-white px-4 py-2 pr-8 text-gray-600 shadow-inner">
                  <option>choose ...</option>
                  <option>English</option>
                  <option>France</option>
                  <option>Spanish</option>
                </select>
                <div
                  class="pointer-events-none absolute right-0 top-0 mt-3 flex items-center px-2 text-gray-600">
                  <svg
                    class="h-4 w-4 fill-current"
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20">
                    <path
                      d="M9.293 12.95l.707.707L15.657 8l-1.414-1.414L10 10.828 5.757 6.586 4.343 8z" />
                  </svg>
                </div>
              </div>
            </div>
            <div class="personal w-full border-t border-gray-400 pt-4">
              <h2 class="text-2xl text-gray-900">Personal info:</h2>
              <div class="mt-4 flex items-center justify-between">
                <div class="mb-6 w-full px-3 md:w-1/2">
                  <label
                    class="mb-2 block text-xs font-bold uppercase tracking-wide text-gray-700"
                    >first name</label
                  >
                  <input
                    class="block w-full appearance-none rounded-md border border-gray-400 bg-white px-4 py-3 leading-tight text-gray-700 shadow-inner focus:border-gray-500 focus:outline-none"
                    type="text"
                    required />
                </div>
                <div class="mb-6 w-full px-3 md:w-1/2">
                  <label
                    class="mb-2 block text-xs font-bold uppercase tracking-wide text-gray-700"
                    >last name</label
                  >
                  <input
                    class="block w-full appearance-none rounded-md border border-gray-400 bg-white px-4 py-3 leading-tight text-gray-700 shadow-inner focus:border-gray-500 focus:outline-none"
                    type="text"
                    required />
                </div>
              </div>
              <div class="mb-6 w-full px-3 md:w-full">
                <label
                  class="mb-2 block text-xs font-bold uppercase tracking-wide text-gray-700"
                  >user name</label
                >
                <input
                  class="block w-full appearance-none rounded-md border border-gray-400 bg-white px-4 py-3 leading-tight text-gray-700 shadow-inner focus:border-gray-500 focus:outline-none"
                  type="text"
                  required />
              </div>
              <div class="mb-6 w-full px-3 md:w-full">
                <label
                  class="mb-2 block text-xs font-bold uppercase tracking-wide text-gray-700"
                  >Bio</label
                >
                <textarea
                  class="h-20 w-full resize-none rounded-md border border-gray-400 bg-gray-100 px-3 py-2 font-medium leading-normal shadow-inner placeholder:text-gray-700 focus:bg-white focus:outline-none"
                  required></textarea>
              </div>
              <div class="flex justify-end">
                <button
                  class="mr-3 appearance-none rounded-md border border-gray-400 bg-gray-200 px-2 py-1 text-gray-900 shadow-sm"
                  type="submit">
                  save changes
                </button>
              </div>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
