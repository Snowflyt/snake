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
                @click="$router.push('./newLogin')">
                Login
              </button>
              <button
                type="button"
                href="#"
                class="mr-1 rounded-lg bg-blue-700 px-4 py-2 text-sm font-medium text-white hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 md:mr-2 md:px-5 md:py-2.5"
                @click="$router.push('./newRegister')">
                Sign up
              </button>
              <!-- <button
                data-collapse-toggle="mega-menu-icons"
                type="button"
                class="inline-flex h-10 w-10 items-center justify-center rounded-lg p-2 text-sm text-gray-500 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600 md:hidden"
                aria-controls="mega-menu-icons"
                aria-expanded="false">
                <span class="sr-only">Open main menu</span>
                <svg
                  class="h-5 w-5"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 17 14">
                  <path
                    stroke="currentColor"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M1 1h15M1 7h15M1 13h15" />
                </svg>
              </button> -->
            </div>
            <div
              id="mega-menu-icons"
              class="hidden w-full items-center justify-between md:order-1 md:flex md:w-auto">
              <ul
                class="mt-4 flex flex-col font-medium md:mt-0 md:flex-row md:space-x-8">
                <!-- <li>
                  <a
                    href="#"
                    class="block border-b border-gray-100 py-2 pl-3 pr-4 text-blue-600 hover:bg-gray-50 dark:border-gray-700 dark:text-blue-500 dark:hover:bg-gray-700 dark:hover:text-blue-500 md:border-0 md:p-0 md:hover:bg-transparent md:hover:text-blue-600 md:dark:hover:bg-transparent md:dark:hover:text-blue-500"
                    aria-current="page"
                    >Home</a
                  >
                </li> -->
                <!-- <li>
            <button
              id="mega-menu-icons-dropdown-button"
              data-dropdown-toggle="mega-menu-icons-dropdown"
              class="flex w-full items-center justify-between border-b border-gray-100 py-2 pl-3 pr-4 font-medium text-gray-900 hover:bg-gray-50 dark:border-gray-700 dark:text-white dark:hover:bg-gray-700 dark:hover:text-blue-500 md:w-auto md:border-0 md:p-0 md:hover:bg-transparent md:hover:text-blue-600 md:dark:hover:bg-transparent md:dark:hover:text-blue-500">
              Company
              <svg
                class="ml-2.5 h-2.5 w-2.5"
                aria-hidden="true"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 10 6">
                <path
                  stroke="currentColor"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="m1 1 4 4 4-4" />
              </svg>
            </button>
            <div
              id="mega-menu-icons-dropdown"
              class="absolute z-10 grid hidden w-auto grid-cols-2 rounded-lg border border-gray-100 bg-white text-sm shadow-md dark:border-gray-700 dark:bg-gray-700 md:grid-cols-3">
              <div class="p-4 pb-0 text-gray-900 dark:text-white md:pb-4">
                <ul
                  class="space-y-4"
                  aria-labelledby="mega-menu-icons-dropdown-button">
                  <li>
                    <a
                      href="#"
                      class="group flex items-center text-gray-500 hover:text-blue-600 dark:text-gray-400 dark:hover:text-blue-500">
                      <span class="sr-only">About us</span>
                      <svg
                        class="mr-2 h-3 w-3 text-gray-400 group-hover:text-blue-600 dark:text-gray-500 dark:group-hover:text-blue-500"
                        aria-hidden="true"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="currentColor"
                        viewBox="0 0 20 20">
                        <path
                          d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z" />
                      </svg>
                      About Us
                    </a>
                  </li>
                  <li>
                    <a
                      href="#"
                      class="group flex items-center text-gray-500 hover:text-blue-600 dark:text-gray-400 dark:hover:text-blue-500">
                      <span class="sr-only">Library</span>
                      <svg
                        class="mr-2 h-3 w-3 text-gray-400 group-hover:text-blue-600 dark:text-gray-500 dark:group-hover:text-blue-500"
                        aria-hidden="true"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="currentColor"
                        viewBox="0 0 20 20">
                        <path
                          d="m1.56 6.245 8 3.924a1 1 0 0 0 .88 0l8-3.924a1 1 0 0 0 0-1.8l-8-3.925a1 1 0 0 0-.88 0l-8 3.925a1 1 0 0 0 0 1.8Z" />
                        <path
                          d="M18 8.376a1 1 0 0 0-1 1v.163l-7 3.434-7-3.434v-.163a1 1 0 0 0-2 0v.786a1 1 0 0 0 .56.9l8 3.925a1 1 0 0 0 .88 0l8-3.925a1 1 0 0 0 .56-.9v-.786a1 1 0 0 0-1-1Z" />
                        <path
                          d="M17.993 13.191a1 1 0 0 0-1 1v.163l-7 3.435-7-3.435v-.163a1 1 0 1 0-2 0v.787a1 1 0 0 0 .56.9l8 3.925a1 1 0 0 0 .88 0l8-3.925a1 1 0 0 0 .56-.9v-.787a1 1 0 0 0-1-1Z" />
                      </svg>
                      Library
                    </a>
                  </li>
                  <li>
                    <a
                      href="#"
                      class="group flex items-center text-gray-500 hover:text-blue-600 dark:text-gray-400 dark:hover:text-blue-500">
                      <span class="sr-only">Resources</span>
                      <svg
                        class="mr-2 h-3 w-3 text-gray-400 group-hover:text-blue-600 dark:text-gray-500 dark:group-hover:text-blue-500"
                        aria-hidden="true"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="currentColor"
                        viewBox="0 0 18 18">
                        <path
                          d="M15.977.783A1 1 0 0 0 15 0H3a1 1 0 0 0-.977.783L.2 9h4.239a2.99 2.99 0 0 1 2.742 1.8 1.977 1.977 0 0 0 3.638 0A2.99 2.99 0 0 1 13.561 9H17.8L15.977.783ZM6 2h6a1 1 0 1 1 0 2H6a1 1 0 0 1 0-2Zm7 5H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Z" />
                        <path
                          d="M1 18h16a1 1 0 0 0 1-1v-6h-4.439a.99.99 0 0 0-.908.6 3.978 3.978 0 0 1-7.306 0 .99.99 0 0 0-.908-.6H0v6a1 1 0 0 0 1 1Z" />
                      </svg>
                      Resources
                    </a>
                  </li>
                  <li>
                    <a
                      href="#"
                      class="group flex items-center text-gray-500 hover:text-blue-600 dark:text-gray-400 dark:hover:text-blue-500">
                      <span class="sr-only">Pro Version</span>
                      <svg
                        class="mr-2 h-3 w-3 text-gray-400 group-hover:text-blue-600 dark:text-gray-500 dark:group-hover:text-blue-500"
                        aria-hidden="true"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="currentColor"
                        viewBox="0 0 20 20">
                        <path
                          d="m7.164 3.805-4.475.38L.327 6.546a1.114 1.114 0 0 0 .63 1.89l3.2.375 3.007-5.006ZM11.092 15.9l.472 3.14a1.114 1.114 0 0 0 1.89.63l2.36-2.362.38-4.475-5.102 3.067Zm8.617-14.283A1.613 1.613 0 0 0 18.383.291c-1.913-.33-5.811-.736-7.556 1.01-1.98 1.98-6.172 9.491-7.477 11.869a1.1 1.1 0 0 0 .193 1.316l.986.985.985.986a1.1 1.1 0 0 0 1.316.193c2.378-1.3 9.889-5.5 11.869-7.477 1.746-1.745 1.34-5.643 1.01-7.556Zm-3.873 6.268a2.63 2.63 0 1 1-3.72-3.72 2.63 2.63 0 0 1 3.72 3.72Z" />
                      </svg>
                      Pro Version
                    </a>
                  </li>
                </ul>
              </div>
              <div class="p-4 pb-0 text-gray-900 dark:text-white md:pb-4">
                <ul class="space-y-4">
                  <li>
                    <a
                      href="#"
                      class="group flex items-center text-gray-500 hover:text-blue-600 dark:text-gray-400 dark:hover:text-blue-500">
                      <span class="sr-only">Blog</span>
                      <svg
                        class="mr-2 h-3 w-3 text-gray-400 group-hover:text-blue-600 dark:text-gray-500 dark:group-hover:text-blue-500"
                        aria-hidden="true"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="currentColor"
                        viewBox="0 0 20 20">
                        <path
                          d="M19 4h-1a1 1 0 1 0 0 2v11a1 1 0 0 1-2 0V2a2 2 0 0 0-2-2H2a2 2 0 0 0-2 2v15a3 3 0 0 0 3 3h14a3 3 0 0 0 3-3V5a1 1 0 0 0-1-1ZM3 4a1 1 0 0 1 1-1h3a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V4Zm9 13H4a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-3H4a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-3H4a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-3h-2a1 1 0 0 1 0-2h2a1 1 0 1 1 0 2Zm0-3h-2a1 1 0 0 1 0-2h2a1 1 0 1 1 0 2Z" />
                        <path d="M6 5H5v1h1V5Z" />
                      </svg>
                      Blog
                    </a>
                  </li>
                  <li>
                    <a
                      href="#"
                      class="group flex items-center text-gray-500 hover:text-blue-600 dark:text-gray-400 dark:hover:text-blue-500">
                      <span class="sr-only">Newsletter</span>
                      <svg
                        class="mr-2 h-3 w-3 text-gray-400 group-hover:text-blue-600 dark:text-gray-500 dark:group-hover:text-blue-500"
                        aria-hidden="true"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="currentColor"
                        viewBox="0 0 20 20">
                        <path
                          d="m17.418 3.623-.018-.008a6.713 6.713 0 0 0-2.4-.569V2h1a1 1 0 1 0 0-2h-2a1 1 0 0 0-1 1v2H9.89A6.977 6.977 0 0 1 12 8v5h-2V8A5 5 0 1 0 0 8v6a1 1 0 0 0 1 1h8v4a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1v-4h6a1 1 0 0 0 1-1V8a5 5 0 0 0-2.582-4.377ZM6 12H4a1 1 0 0 1 0-2h2a1 1 0 0 1 0 2Z" />
                      </svg>
                      Newsletter
                    </a>
                  </li>
                  <li>
                    <a
                      href="#"
                      class="group flex items-center text-gray-500 hover:text-blue-600 dark:text-gray-400 dark:hover:text-blue-500">
                      <span class="sr-only">Playground</span>
                      <svg
                        class="mr-2 h-3 w-3 text-gray-400 group-hover:text-blue-600 dark:text-gray-500 dark:group-hover:text-blue-500"
                        aria-hidden="true"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="currentColor"
                        viewBox="0 0 18 18">
                        <path
                          d="M6.143 0H1.857A1.857 1.857 0 0 0 0 1.857v4.286C0 7.169.831 8 1.857 8h4.286A1.857 1.857 0 0 0 8 6.143V1.857A1.857 1.857 0 0 0 6.143 0Zm10 0h-4.286A1.857 1.857 0 0 0 10 1.857v4.286C10 7.169 10.831 8 11.857 8h4.286A1.857 1.857 0 0 0 18 6.143V1.857A1.857 1.857 0 0 0 16.143 0Zm-10 10H1.857A1.857 1.857 0 0 0 0 11.857v4.286C0 17.169.831 18 1.857 18h4.286A1.857 1.857 0 0 0 8 16.143v-4.286A1.857 1.857 0 0 0 6.143 10ZM17 13h-2v-2a1 1 0 0 0-2 0v2h-2a1 1 0 0 0 0 2h2v2a1 1 0 0 0 2 0v-2h2a1 1 0 0 0 0-2Z" />
                      </svg>
                      Playground
                    </a>
                  </li>
                  <li>
                    <a
                      href="#"
                      class="group flex items-center text-gray-500 hover:text-blue-600 dark:text-gray-400 dark:hover:text-blue-500">
                      <span class="sr-only">License</span>
                      <svg
                        class="mr-2 h-3 w-3 text-gray-400 group-hover:text-blue-600 dark:text-gray-500 dark:group-hover:text-blue-500"
                        aria-hidden="true"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="currentColor"
                        viewBox="0 0 14 20">
                        <path
                          d="M13.383.076a1 1 0 0 0-1.09.217L11 1.586 9.707.293a1 1 0 0 0-1.414 0L7 1.586 5.707.293a1 1 0 0 0-1.414 0L3 1.586 1.707.293A1 1 0 0 0 0 1v18a1 1 0 0 0 1.707.707L3 18.414l1.293 1.293a1 1 0 0 0 1.414 0L7 18.414l1.293 1.293a1 1 0 0 0 1.414 0L11 18.414l1.293 1.293A1 1 0 0 0 14 19V1a1 1 0 0 0-.617-.924ZM10 15H4a1 1 0 1 1 0-2h6a1 1 0 0 1 0 2Zm0-4H4a1 1 0 1 1 0-2h6a1 1 0 1 1 0 2Zm0-4H4a1 1 0 0 1 0-2h6a1 1 0 1 1 0 2Z" />
                      </svg>
                      License
                    </a>
                  </li>
                </ul>
              </div>
              <div class="p-4 text-gray-900 dark:text-white">
                <ul class="space-y-4">
                  <li>
                    <a
                      href="#"
                      class="group flex items-center text-gray-500 hover:text-blue-600 dark:text-gray-400 dark:hover:text-blue-500">
                      <span class="sr-only">Contact Us</span>
                      <svg
                        class="mr-2 h-3 w-3 text-gray-400 group-hover:text-blue-600 dark:text-gray-500 dark:group-hover:text-blue-500"
                        aria-hidden="true"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="currentColor"
                        viewBox="0 0 14 20">
                        <path
                          d="M12 0H2a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2ZM7.5 17.5h-1a1 1 0 0 1 0-2h1a1 1 0 0 1 0 2ZM12 13H2V4h10v9Z" />
                      </svg>
                      Contact Us
                    </a>
                  </li>
                  <li>
                    <a
                      href="#"
                      class="group flex items-center text-gray-500 hover:text-blue-600 dark:text-gray-400 dark:hover:text-blue-500">
                      <span class="sr-only">Support Center</span>
                      <svg
                        class="mr-2 h-3 w-3 text-gray-400 group-hover:text-blue-600 dark:text-gray-500 dark:group-hover:text-blue-500"
                        aria-hidden="true"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="currentColor"
                        viewBox="0 0 21 21">
                        <path
                          d="m5.4 2.736 3.429 3.429A5.046 5.046 0 0 1 10.134 6c.356.01.71.06 1.056.147l3.41-3.412c.136-.133.287-.248.45-.344A9.889 9.889 0 0 0 10.269 1c-1.87-.041-3.713.44-5.322 1.392a2.3 2.3 0 0 1 .454.344Zm11.45 1.54-.126-.127a.5.5 0 0 0-.706 0l-2.932 2.932c.029.023.049.054.078.077.236.194.454.41.65.645.034.038.078.067.11.107l2.927-2.927a.5.5 0 0 0 0-.707Zm-2.931 9.81c-.024.03-.057.052-.081.082a4.963 4.963 0 0 1-.633.639c-.041.036-.072.083-.115.117l2.927 2.927a.5.5 0 0 0 .707 0l.127-.127a.5.5 0 0 0 0-.707l-2.932-2.931Zm-1.442-4.763a3.036 3.036 0 0 0-1.383-1.1l-.012-.007a2.955 2.955 0 0 0-1-.213H10a2.964 2.964 0 0 0-2.122.893c-.285.29-.509.634-.657 1.013l-.01.016a2.96 2.96 0 0 0-.21 1 2.99 2.99 0 0 0 .489 1.716c.009.014.022.026.032.04a3.04 3.04 0 0 0 1.384 1.1l.012.007c.318.129.657.2 1 .213.392.015.784-.05 1.15-.192.012-.005.02-.013.033-.018a3.011 3.011 0 0 0 1.676-1.7v-.007a2.89 2.89 0 0 0 0-2.207 2.868 2.868 0 0 0-.27-.515c-.007-.012-.02-.025-.03-.039Zm6.137-3.373a2.53 2.53 0 0 1-.35.447L14.84 9.823c.112.428.166.869.16 1.311-.01.356-.06.709-.147 1.054l3.413 3.412c.132.134.249.283.347.444A9.88 9.88 0 0 0 20 11.269a9.912 9.912 0 0 0-1.386-5.319ZM14.6 19.264l-3.421-3.421c-.385.1-.781.152-1.18.157h-.134c-.356-.01-.71-.06-1.056-.147l-3.41 3.412a2.503 2.503 0 0 1-.443.347A9.884 9.884 0 0 0 9.732 21H10a9.9 9.9 0 0 0 5.044-1.388 2.519 2.519 0 0 1-.444-.348ZM1.735 15.6l3.426-3.426a4.608 4.608 0 0 1-.013-2.367L1.735 6.4a2.507 2.507 0 0 1-.35-.447 9.889 9.889 0 0 0 0 10.1c.1-.164.217-.316.35-.453Zm5.101-.758a4.957 4.957 0 0 1-.651-.645c-.033-.038-.077-.067-.11-.107L3.15 17.017a.5.5 0 0 0 0 .707l.127.127a.5.5 0 0 0 .706 0l2.932-2.933c-.03-.018-.05-.053-.078-.076ZM6.08 7.914c.03-.037.07-.063.1-.1.183-.22.384-.423.6-.609.047-.04.082-.092.129-.13L3.983 4.149a.5.5 0 0 0-.707 0l-.127.127a.5.5 0 0 0 0 .707L6.08 7.914Z" />
                      </svg>
                      Support Center
                    </a>
                  </li>
                  <li>
                    <a
                      href="#"
                      class="group flex items-center text-gray-500 hover:text-blue-600 dark:text-gray-400 dark:hover:text-blue-500">
                      <span class="sr-only">Terms</span>
                      <svg
                        class="mr-2 h-3 w-3 text-gray-400 group-hover:text-blue-600 dark:text-gray-500 dark:group-hover:text-blue-500"
                        aria-hidden="true"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="currentColor"
                        viewBox="0 0 18 20">
                        <path
                          d="M16 1h-3.278A1.992 1.992 0 0 0 11 0H7a1.993 1.993 0 0 0-1.722 1H2a2 2 0 0 0-2 2v15a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2Zm-3 14H5a1 1 0 0 1 0-2h8a1 1 0 0 1 0 2Zm0-4H5a1 1 0 0 1 0-2h8a1 1 0 1 1 0 2Zm0-5H5a1 1 0 0 1 0-2h2V2h4v2h2a1 1 0 1 1 0 2Z" />
                      </svg>
                      Terms
                    </a>
                  </li>
                </ul>
              </div>
            </div>
          </li> -->
                <!-- <li>
                  <a
                    href="#"
                    class="block border-b border-gray-100 py-2 pl-3 pr-4 text-gray-900 hover:bg-gray-50 dark:border-gray-700 dark:text-white dark:hover:bg-gray-700 dark:hover:text-blue-500 md:border-0 md:p-0 md:hover:bg-transparent md:hover:text-blue-600 md:dark:hover:bg-transparent md:dark:hover:text-blue-500"
                    >Team</a
                  >
                </li> -->
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
