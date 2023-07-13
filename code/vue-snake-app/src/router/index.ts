import { createRouter, createWebHistory } from 'vue-router';

<<<<<<< HEAD
import UserCenter from '../pages/UserCenter';
import Battle from '../pages/battle';
import Chat from '../pages/chat';
import Combat from '../pages/combat';
import Home from '../pages/home';
import Leisure from '../pages/leisure';
import Login from '../pages/login';
import MegaMenu from '../pages/megaMenu';
import NewChat from '../pages/newChat';
import NewChatContent from '../pages/newChatContent';
import NewLogin from '../pages/newLogin';
import NewRegister from '../pages/newRegister';
import NewUserCenter from '../pages/newUserCenter';
import Register from '../pages/register';
import Setting from '../pages/setting';
import Shop from '../pages/shop';
=======
import BattlePage from '@/pages/battle';
import ChatPage from '@/pages/chat';
import CombatPage from '@/pages/combat';
import HomePage from '@/pages/home';
import LeisurePage from '@/pages/leisure';
import LoginPage from '@/pages/login';
import NewChatPage from '@/pages/newChat';
import NewChatContentPage from '@/pages/newChatContent';
import NewLoginPage from '@/pages/newLogin';
import NewRegisterPage from '@/pages/newRegister';
import NewUserCenterPage from '@/pages/newUserCenter';
import RegisterPage from '@/pages/register';
import SettingsPage from '@/pages/settings';
import ShopPage from '@/pages/shop';
import UserCenterPage from '@/pages/userCenter';
>>>>>>> 6beca03979371e6b8a0d664957c644919e955502

import type { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
<<<<<<< HEAD
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
  { path: '/newChat', component: NewChat },
  { path: '/newChatContent', component: NewChatContent },
  { path: '/', component: MegaMenu },
=======
  { path: '/', component: HomePage },
  { path: '/register', component: RegisterPage },
  { path: '/login', component: LoginPage },
  { path: '/combat', component: CombatPage },
  { path: '/user-center', component: UserCenterPage },
  { path: '/chat', component: ChatPage },
  { path: '/leisure', component: LeisurePage },
  { path: '/settings', component: SettingsPage },
  { path: '/shop', component: ShopPage },
  { path: '/battle', component: BattlePage },
  { path: '/new-login', component: NewLoginPage },
  { path: '/new-register', component: NewRegisterPage },
  { path: '/new-user-center', component: NewUserCenterPage },
  { path: '/new-chat', component: NewChatPage },
  { path: '/new-chat-content', component: NewChatContentPage },
>>>>>>> 6beca03979371e6b8a0d664957c644919e955502
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
