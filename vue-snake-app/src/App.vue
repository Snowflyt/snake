<script setup lang="ts">
import { ref } from 'vue';

import GameBoard from './components/GameBoard';
import Layout from './components/Layout';

const roomId = ref('');
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
</template>
