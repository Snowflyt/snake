<script setup lang="ts">
import { ref } from 'vue';

const username = ref('');
const password = ref('');
</script>

<template>
  <div class="mx-auto w-4/5">
    <div class="mb-7 flex justify-center">
      <img class="" src="../../assets/images/注册/u24.svg" />
    </div>
    <div class="mb-3 flex justify-center text-2xl font-bold">用户注册</div>
    <el-form-item label="请输入您的手机号：">
      <el-input v-model="username"></el-input>
    </el-form-item>
    <el-form-item class="mr-4" label="请输入验证码：">
      <el-input v-model="password"></el-input>
    </el-form-item>
    <div class="flex justify-center">
      <button
        class="w-32 rounded-md bg-black p-4 text-white"
        @click="$router.push('/home')">
        注册
      </button>
    </div>
  </div>
</template>
