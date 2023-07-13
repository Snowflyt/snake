<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';

import { apis } from '@/utils/apis';

const router = useRouter();

const username = ref('');
const password = ref('');
const phone = ref('');
const verifyCode = ref('');

const handleSubmitChange = async () => {
  try {
    const response = apis.user.login({
      username: username.value,
      password: password.value,
    });
    console.log(response);
    alert('登录成功');
    router.push('/');
  } catch (error) {
    console.log(error);
    alert('登录数据有误');
  }
};
</script>

<template>
  <div
    class="relative top-[10%] flex h-[10%] content-center items-center justify-center">
    <p class="text-5xl font-bold">登录界面</p>
  </div>
  <div
    class="flex h-[90%] w-[100%] flex-wrap content-center items-center justify-center">
    <img class="grow-1 w-[20%]" src="../../assets/images/登录/u1.svg" />
    <el-tabs class="grow-6 flex w-[40%] flex-wrap">
      <el-tab-pane label="密码登录">
        <el-form>
          <el-form-item class="" label="用户名">
            <el-input v-model="username" />
          </el-form-item>
          <el-form-item label="密码">
            <el-input v-model="password" />
          </el-form-item>
          <el-form-item>
            <div class="flex justify-center">
              <button
                type="button"
                class="rounded border-2 border-black p-2 text-3xl font-bold"
                round
                @click="handleSubmitChange">
                登录
              </button>
              <button
                class="rounded border-2 border-black p-2 text-3xl font-bold"
                type="button"
                round
                @click="$router.push('/register')">
                注册
              </button>
            </div>
          </el-form-item>
        </el-form>
      </el-tab-pane>
      <el-tab-pane label="手机登录">
        <el-form>
          <el-form-item label="手机">
            <el-input v-model="phone" />
          </el-form-item>
          <el-form-item label="验证码">
            <el-input v-model="verifyCode" />
          </el-form-item>
          <el-form-item>
            <div class="flex justify-center">
              <button
                class="rounded border-2 border-black p-2 text-3xl font-bold"
                type="button"
                round
                @click="$router.push('/')">
                登录
              </button>
              <button
                class="rounded border-2 border-black p-2 text-3xl font-bold"
                type="button"
                round
                @click="$router.push('/register')">
                注册
              </button>
            </div>
          </el-form-item>
        </el-form>
      </el-tab-pane>
      <el-tab-pane label="扫码登录">
        <div class="relative">
          <img class="inline w-[50%]" src="../../assets/tdimensioncode.png" />
          <button
            class="absolute inline h-[50%] rounded border-2 border-black p-2 text-3xl font-bold"
            @click="$router.push('/')">
            登录
          </button>
          <button
            type="button"
            class="absolute top-[50%] inline h-[50%] rounded border-2 border-black p-2 text-3xl font-bold"
            @click="handleSubmitChange">
            注册
          </button>
        </div>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>
