import { createRouter, createWebHistory } from 'vue-router';

import UserCenter from '../pages/UserCenter';
import Combat from '../pages/combat';
import Login from '../pages/login';

import type { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  { path: '/login', component: Login },
  { path: '/combat', component: Combat },
  { path: '/userCenter', component: UserCenter },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
