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
import register from './pages/register'
import home from './pages/home';
import leisure from './pages/leisure';
import setting from './pages/setting';
import shop from './pages/shop/shop.vue';
<<<<<<< HEAD
=======
import leisure from './pages/leisure'
import battle from './pages/battle'
>>>>>>> d82ce2550715abff68f681d6da34c079ebd9af9d

const roomId = ref('');
</script>

<template>
  <layout>
    <router-view />
  </layout>
<<<<<<< HEAD
=======
  <login />
  <register />
  <chat />
  <home />
  <setting />
  <shop />
  <leisure />
  <battle />
>>>>>>> d82ce2550715abff68f681d6da34c079ebd9af9d
</template>
