<template>
  <div id="base" class="">
    <img class="" src="../../assets/images/登录/u1.svg" />
    <el-tabs class="">
      <el-tab-pane label="密码登录">
        <el-form class="" label-width="120px">
          <el-form-item label="UserName">
            <el-input v-model="UserName" />
          </el-form-item>
          <el-form-item label="Password">
            <el-input v-model="Password" />
          </el-form-item>
        </el-form>
      </el-tab-pane>
      <el-tab-pane label="验证码登录"> </el-tab-pane>
      <el-tab-pane label="扫码登录"> </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script setup lang="ts">
const UserName = '';
const Password = '';
</script>
