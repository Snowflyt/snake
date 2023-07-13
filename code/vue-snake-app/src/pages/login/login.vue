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
            <el-input v-model="UserName" />
          </el-form-item>
          <el-form-item label="密码">
            <el-input v-model="Password" />
          </el-form-item>
          <el-form-item>
            <div class="flex justify-center">
              <button
                type="button"
                class="font-blod rounded border-2 border-black p-2 text-3xl"
                round
                @click="handleSubmitChange">
                登录
              </button>
              <button
                class="font-blod rounded border-2 border-black p-2 text-3xl"
                type="primary"
                round
                @click="
                  () => {
                    $router.push('/register');
                  }
                ">
                注册
              </button>
            </div>
          </el-form-item>
        </el-form>
      </el-tab-pane>
      <el-tab-pane label="手机登录">
        <el-form>
          <el-form-item label="手机">
            <el-input v-model="Telephone" />
          </el-form-item>
          <el-form-item label="验证码">
            <el-input v-model="VerifyCode" />
          </el-form-item>
          <el-form-item>
            <div class="flex justify-center">
              <button
                class="font-blod rounded border-2 border-black p-2 text-3xl"
                type="primary"
                round
                @click="
                  () => {
                    $router.push('/home');
                  }
                ">
                登录
              </button>
              <button
                class="font-blod rounded border-2 border-black p-2 text-3xl"
                type="primary"
                round
                @click="
                  () => {
                    $router.push('/register');
                  }
                ">
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
            class="font-blod absolute inline h-[50%] rounded border-2 border-black p-2 text-3xl"
            @click="
              () => {
                $router.push('/home');
              }
            ">
            登录
          </button>
          <button
            type="button"
            class="font-blod absolute top-[50%] inline h-[50%] rounded border-2 border-black p-2 text-3xl"
            @click="handleSubmitChange">
            注册
          </button>
        </div>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script setup lang="ts">
import axios from 'axios';
import { ref } from 'vue';

import sampleApi from '../../apis/sample';
var UserName = ref('');
var Password = ref('');
var Telephone: number = ref('');
var VerifyCode: number = ref('');
const handleSubmitChange = async () => {
  axios
    .post('http://101.132.165.23:8000/login', {
      username: UserName.value,
      password: Password.value,
    })
    .then(function (response) {
      console.log(response.data);
      alert('登录成功');
      setTimeout(() => {
        $router.push('./home');
      }, 2000);
    })
    .catch(function (error) {
      console.log(error);
      alert('登录数据有误');
    });
};

</script>
