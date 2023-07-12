import { createRouter, createWebHistory } from 'vue-router';

import UserCenter from '../pages/UserCenter';
import combat from '../pages/combat';
import login from '../pages/login';

const routes = [
  { path: '/login', component: login },
  { path: './combat', component: combat },
  { path: './UserCenter', component: UserCenter },
];

const router = new createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
