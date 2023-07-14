<script setup lang="ts">
import { ElMessage } from 'element-plus';
import { ref } from 'vue';

import { apis } from '@/utils/apis';

const id = ref(0);
const preferredLang = ref('');
const password = ref('');
const username = ref('');
const phone = ref('');

const handleSubmitChange = async () => {
  try {
    const user = await apis.user.create({
      id: id.value,
      phoneNumber: phone.value,
      languageExcellent: preferredLang.value,
      username: username.value,
      password: password.value,
    });
    console.log('result:', user);
  } catch {
    ElMessage.error('信息填写错误');
  }
};
</script>

<template>
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
    <button class="text-2xl font-bold" @click="$router.go(-1)">返回</button>
    <button class="text-2xl font-bold" @click="$router.push('/settings')">
      设置
    </button>
  </div>
  <div class="flex justify-center">
    <p class="text-6xl font-bold">个人信息修改</p>
  </div>
  <div class="relative h-[60%]">
    <img
      class="relative left-[20%] top-[35%] w-[20%]"
      src="../../assets/images/个人中心/u176.svg" />

    <el-form class="absolute left-[50%] top-[35%] w-[30%]">
      <el-form-item label="ID">
        <el-input v-model.number="id" type="number" />
      </el-form-item>

      <el-form-item label="擅长语言">
        <el-input v-model="preferredLang" />
      </el-form-item>
      <el-form-item label="用户名">
        <el-input v-model="username" />
      </el-form-item>
      <el-form-item label="密码">
        <el-input v-model="password" />
      </el-form-item>
      <el-form-item label="手机号">
        <el-input v-model="phone" />
      </el-form-item>
      <el-form-item>
        <button
          type="button"
          class="rounded border-2 border-black p-2 text-3xl font-bold"
          @click="handleSubmitChange">
          提交修改
        </button>
      </el-form-item>
    </el-form>
  </div>
  <div class="h-[20%]"></div>
</template>

<style scoped lang="scss">
img {
  width: auto;
  height: auto;
  max-width: 100%;
  max-height: 100%;
}
</style>
