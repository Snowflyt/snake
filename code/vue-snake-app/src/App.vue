<script setup lang="ts">
import { ref, onMounted } from 'vue';
import 'element-plus/lib/locale/lang/zh-cn';

import sampleApi from './apis/sample';
import GameBoard from './components/GameBoard';
import Layout from './components/Layout';
import login from './pages/login';
import register from './pages/register';
import chat from './pages/chat';
import home from './pages/home';

const roomId = ref('');

onMounted(async () => {
  const res = await sampleApi.echo('hello');
  console.log(res);
});
</script>

<template>
  <layout>
    <div class="flex h-8 w-full flex-row bg-slate-500">
      <el-form-item label="Activity name">
        <el-input v-model="roomId" />
      </el-form-item>
    </div>
    <game-board />
  </layout>
  <login />
  <register />
  <chat />
  <home />
</template>
