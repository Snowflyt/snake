<template>
  <div class="h-[100%]">
    <section
      class="h-[100#] bg-white bg-[url('https://flowbite.s3.amazonaws.com/docs/jumbotron/hero-pattern.svg')] dark:bg-gray-900 dark:bg-[url('https://flowbite.s3.amazonaws.com/docs/jumbotron/hero-pattern-dark.svg')]">
      <div
        class="relative z-10 mx-auto h-[100%] max-w-screen-xl px-4 py-8 text-center lg:py-16">
        <nav class="relative top-[1%]">
          <div
            class="mx-auto flex max-w-screen-xl flex-wrap items-center justify-between p-4">
            <a href="#" class="flex items-center">
              <img
                class="mr-3 h-8"
                src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Snake.svg/800px-Snake.svg.png"
                alt="logo" />
              <span
                class="self-center whitespace-nowrap text-2xl font-semibold dark:text-white"
                >CodeSnake</span
              >
            </a>
            <div class="flex items-center md:order-2">
              <button
                type="button"
                href="#"
                class="mr-1 rounded-lg px-4 py-2 text-sm font-medium text-gray-800 hover:bg-gray-50 focus:outline-none focus:ring-4 focus:ring-gray-300 dark:text-white dark:hover:bg-gray-700 dark:focus:ring-gray-800 md:mr-2 md:px-5 md:py-2.5"
                @click="$router.push('/new-login')">
                Login
              </button>
              <button
                type="button"
                href="#"
                class="mr-1 rounded-lg bg-blue-700 px-4 py-2 text-sm font-medium text-white hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 md:mr-2 md:px-5 md:py-2.5"
                @click="$router.push('/new-register')">
                Sign up
              </button>
            </div>
            <div
              id="mega-menu-icons"
              class="hidden w-full items-center justify-between md:order-1 md:flex md:w-auto">
              <ul>
                class="mt-4 flex flex-col font-medium md:mt-0 md:flex-row
                md:space-x-8">
              </ul>
            </div>
          </div>
        </nav>
        <h1
          class="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 dark:text-white md:text-5xl lg:text-6xl">
          Not only to play, but also to learn! Light up your algorithmic path
          with games!
        </h1>
        <p
          class="mb-8 text-lg font-normal text-gray-500 dark:text-gray-200 sm:px-16 lg:px-48 lg:text-xl">
          Our mission is to provide everyone with a better understanding and
          mastery of algorithms by playing Snake while providing unlimited
          entertainment. We believe that learning is more efficient and fun in a
          relaxed and enjoyable environment. We make computer science accessible
          so that learning to code can be enjoyed by all.
        </p>
      </div>
      <div
        class="absolute left-0 top-0 z-0 h-full w-full bg-gradient-to-b from-blue-50 to-transparent dark:from-blue-900"></div>
    </section>
  </div>
</template>
