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
    <router-link to="/login">返回</router-link>
    <b>设置</b>
  </div>
  <div class="relative h-[60%]">
    <img
      class="relative left-[20%] top-[35%] w-[20%]"
      src="../../assets/images/个人中心/u176.svg" />

    <el-form class="absolute left-[50%] top-[35%] w-[30%]">
      <el-form-item label="ID">
        <el-input v-model="ID" />
      </el-form-item>
      <el-form-item label="段位">
        <el-input v-model="Grade" />
      </el-form-item>
      <el-form-item label="擅长语言">
        <el-input v-model="PreferredLang" />
      </el-form-item>
      <el-form-item label="个人简介">
        <el-input v-model="PersonalInfo" />
      </el-form-item>
    </el-form>
  </div>
  <div class="h-[20%]"></div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
var ID = ref('');
var Grade = ref('');
var PreferredLang = ref('');
var PersonalInfo = ref('');
</script>

<style>
img {
  width: auto;
  height: auto;
  max-width: 100%;
  max-height: 100%;
}
</style>
