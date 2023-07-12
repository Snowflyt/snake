<script setup lang="ts">
import { ref, onMounted } from 'vue';
import 'element-plus/lib/locale/lang/zh-cn';

import sampleApi from './apis/sample';
import GameBoard from './components/GameBoard';
import Layout from './components/Layout';
import UserCenter from './pages/UserCenter';
import combat from './pages/combat';
import login from './pages/login';
const roomId = ref('');

onMounted(async () => {
  const res = await sampleApi.echo('hello');
  console.log(res);
});
</script>

<template>
  <!-- <layout>
    <div class="flex h-8 w-full flex-row bg-slate-500">
      <el-form-item label="Activity name">
        <el-input v-model="roomId" />
      </el-form-item>
    </div>
    <game-board />
  </layout> -->

  <combat />
</template>
