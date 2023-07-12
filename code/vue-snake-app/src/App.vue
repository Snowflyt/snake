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
import login from './pages/login';
import register from './pages/register';

const roomId = ref('');
</script>

<template>
  <layout>
    <router-view />
  </layout>
</template>
