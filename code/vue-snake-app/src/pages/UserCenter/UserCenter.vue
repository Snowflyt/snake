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
    <button class="text-2xl font-bold" @click="$router.push('./setting')">
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
        <el-input v-model.number="ID" type="number" />
      </el-form-item>

      <el-form-item label="擅长语言">
        <el-input v-model="PreferredLang" />
      </el-form-item>
      <el-form-item label="用户名">
        <el-input v-model="UserName" />
      </el-form-item>
      <el-form-item label="密码">
        <el-input v-model="Password" />
      </el-form-item>
      <el-form-item label="手机号">
        <el-input v-model="Phonenumber" />
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

<script setup lang="ts">
import { ref } from 'vue';

import sampleApi from '../../apis/sample';
const ID: number = ref(0);
const PreferredLang = ref('');
const Password = ref('');
const UserName = ref('');
const Phonenumber = ref('');

const handleSubmitChange = async () => {
  console.log('start');

  try {
    const data = {
      id: ID.value,
      phone_number: Phonenumber.value,
      language_excellent: PreferredLang.value,
      username: UserName.value,
      password: Password.value,
    };
    console.log(data);
    const res = await sampleApi.createUsers(data);
    res.then((result) => {
      console.log('result:', result);
    });
  } catch {
    alert('信息填写错误');
  }
};
</script>

<style>
img {
  width: auto;
  height: auto;
  max-width: 100%;
  max-height: 100%;
}
</style>
