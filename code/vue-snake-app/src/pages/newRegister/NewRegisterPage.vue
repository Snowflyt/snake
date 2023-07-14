<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';

import { apis } from '@/utils/apis';

const username = ref('');
const password = ref('');
const phone = ref('');
const confirmedPassword = ref('');

const router = useRouter();
const handleSubmitChange = async () => {
  if (password.value != confirmedPassword.value) {
    alert('密码不一致');
    return;
  }

  try {
    const data = await apis.user.register({
      username: username.value,
      password: password.value,
      phoneNumber: phone.value,
    });
    console.log(data);
    alert('注册成功');
    router.push('/home');
  } catch (error) {
    console.log(error);
    alert('注册数据有误');
  }
};
</script>

<template class="bg-gray-50 dark:bg-gray-900">
  <div
    class="mx-auto flex flex-col items-center justify-center px-6 py-8 md:h-screen lg:py-0">
    <a
      href="#"
      class="mb-6 flex items-center text-2xl font-semibold text-gray-900 dark:text-white">
      <img
        class="mr-2 h-8 w-8"
        src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Snake.svg/800px-Snake.svg.png"
        alt="logo" />
      CodeSnake
    </a>
    <div
      class="w-full rounded-lg bg-white shadow dark:border dark:border-gray-700 dark:bg-gray-800 sm:max-w-md md:mt-0 xl:p-0">
      <div class="space-y-4 p-6 sm:p-8 md:space-y-6">
        <h1
          class="text-xl font-bold leading-tight tracking-tight text-gray-900 dark:text-white md:text-2xl">
          Create and account
        </h1>
        <form class="space-y-4 md:space-y-6" action="#">
          <div>
            <label
              for="email"
              class="mb-2 block text-sm font-medium text-gray-900 dark:text-white"
              >Your email</label
            >
            <input
              id="email"
              v-model="username"
              type="email"
              name="email"
              class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-gray-900 focus:border-primary-600 focus:ring-primary-600 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder:text-gray-400 dark:focus:border-blue-500 dark:focus:ring-blue-500 sm:text-sm"
              placeholder="name@company.com"
              required />
          </div>
          <div>
            <label
              for="password"
              class="mb-2 block text-sm font-medium text-gray-900 dark:text-white"
              >Password</label
            >
            <input
              id="password"
              v-model="password"
              type="password"
              name="password"
              placeholder="••••••••"
              class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-gray-900 focus:border-primary-600 focus:ring-primary-600 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder:text-gray-400 dark:focus:border-blue-500 dark:focus:ring-blue-500 sm:text-sm"
              required />
          </div>
          <div>
            <label
              for="confirm-password"
              class="mb-2 block text-sm font-medium text-gray-900 dark:text-white"
              >Confirm password</label
            >
            <input
              id="confirm-password"
              v-model="confirmedPassword"
              type="password"
              name="confirm-password"
              placeholder="••••••••"
              class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-gray-900 focus:border-primary-600 focus:ring-primary-600 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder:text-gray-400 dark:focus:border-blue-500 dark:focus:ring-blue-500 sm:text-sm"
              required />
          </div>
          <div>
            <label
              class="mb-2 block text-sm font-medium text-gray-900 dark:text-white"
              >PhoneNumber</label
            >
            <input
              id="telephone"
              v-model="phone"
              name="telephone"
              placeholder="12345678911"
              class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-gray-900 focus:border-primary-600 focus:ring-primary-600 dark:border-gray-600 dark:bg-gray-700 dark:text-white dark:placeholder:text-gray-400 dark:focus:border-blue-500 dark:focus:ring-blue-500 sm:text-sm"
              required />
          </div>
          <div class="flex items-start">
            <div class="flex h-5 items-center">
              <input
                id="terms"
                aria-describedby="terms"
                type="checkbox"
                class="focus:ring-3 h-4 w-4 rounded border border-gray-300 bg-gray-50 focus:ring-primary-300 dark:border-gray-600 dark:bg-gray-700 dark:ring-offset-gray-800 dark:focus:ring-primary-600"
                required />
            </div>
            <div class="ml-3 text-sm">
              <label
                for="terms"
                class="font-light text-gray-500 dark:text-gray-300"
                >I accept the
                <a
                  class="font-medium text-primary-600 hover:underline dark:text-primary-500"
                  href="#"
                  >Terms and Conditions</a
                ></label
              >
            </div>
          </div>
          <button
            type="button"
            class="w-full rounded-lg bg-primary-600 px-5 py-2.5 text-center text-sm font-medium text-white hover:bg-primary-700 focus:outline-none focus:ring-4 focus:ring-primary-300 dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800"
            @click="handleSubmitChange">
            Create an account
          </button>
          <p class="text-sm font-light text-gray-500 dark:text-gray-400">
            Already have an account?
            <b
              href="#"
              class="font-medium text-primary-600 hover:underline dark:text-primary-500"
              @click="$router.push('/new-login')"
              >Login here</b
            >
          </p>
        </form>
      </div>
    </div>
  </div>
</template>
