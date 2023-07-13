<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { RouterView } from 'vue-router';
import 'element-plus/lib/locale/lang/zh-cn';

import sampleApi from './apis/sample';
import GameBoard from './components/GameBoard';
import Layout from './components/Layout';
import UserCenter from './pages/UserCenter';
import chat from './pages/chat';
import combat from './pages/combat';
import home from './pages/home';
import leisure from './pages/leisure';
import register from './pages/register';
import setting from './pages/setting';
import shop from './pages/shop/shop.vue';

const roomId = ref('');
const testEcho = (echo: string) => {
  var temp = sampleApi.echo(echo);
  temp.then((result) => {
    console.log('result:', result);
  });
};
</script>

<template>
  <layout>
    <!-- <button @click="testEcho('1')">测试</button> -->
    <router-view />
  </layout>
</template>
