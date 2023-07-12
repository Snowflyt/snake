<template>
<<<<<<< HEAD
  <div
    class="relative top-[10%] flex h-[10%] content-center items-center justify-center">
    <p class="text-5xl">登录界面</p>
  </div>
  <div
    class="flex h-[90%] w-[100%] flex-wrap content-center items-center justify-center">
    <img class="grow-1 w-[20%]" src="../../assets/images/登录/u1.svg" />
    <el-tabs class="grow-6 flex w-[40%] flex-wrap">
=======
  <div id="base" class="">
    <img class="" src="../../assets/images/登录/u1.svg" />
    <el-tabs class="">
>>>>>>> e11e971cb5b2e7100d9fb58eaef9535aceafc106
      <el-tab-pane label="密码登录">
        <el-form>
          <el-form-item class="" label="用户名">
            <el-input v-model="UserName" />
          </el-form-item>
          <el-form-item label="密码">
            <el-input v-model="Password" />
          </el-form-item>
          <el-form-item>
            <el-button class="" type="primary" round> 登录</el-button>
          </el-form-item>
        </el-form>
      </el-tab-pane>
      <el-tab-pane label="验证码登录">
        <el-form>
          <el-form-item label="手机">
            <el-input v-model="Telephone" />
          </el-form-item>
          <el-form-item label="验证码">
            <el-input v-model="VerifyCode" />
          </el-form-item>
          <el-form-item>
            <el-button class="left-50 font-lg" type="primary" round>
              登录</el-button
            >
          </el-form-item>
        </el-form>
      </el-tab-pane>
      <el-tab-pane label="扫码登录"> </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
var UserName = ref('');
var Password = ref('');
var Telephone: number = ref('');
var VerifyCode: number = ref('');
</script>
