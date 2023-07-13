<script setup lang="ts">
import { RouterView } from 'vue-router';

import 'element-plus/lib/locale/lang/zh-cn';

import Layout from './components/Layout';
</script>

<template>
  <layout>
    <router-view />
  </layout>
</template>
