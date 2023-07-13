import { createRouter, createWebHistory } from 'vue-router';

import UserCenter from '../pages/UserCenter';
import Battle from '../pages/battle';
import Chat from '../pages/chat';
import Combat from '../pages/combat';
import Home from '../pages/home';
import Leisure from '../pages/leisure';
import Login from '../pages/login';
import NewLogin from '../pages/newLogin';
import NewRegister from '../pages/newRegister';
import NewUserCenter from '../pages/newUserCenter';
import Register from '../pages/register';
import Setting from '../pages/setting';
import Shop from '../pages/shop';

import type { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  { path: '/login', component: Login },
  { path: '/combat', component: Combat },
  { path: '/userCenter', component: UserCenter },
  { path: '/chat', component: Chat },
  { path: '/home', component: Home },
  { path: '/leisure', component: Leisure },
  { path: '/register', component: Register },
  { path: '/setting', component: Setting },
  { path: '/shop', component: Shop },
  { path: '/battle', component: Battle },
  { path: '/newLogin', component: NewLogin },
  { path: '/newRegister', component: NewRegister },
  { path: '/newUserCenter', component: NewUserCenter },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
