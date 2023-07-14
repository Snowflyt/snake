import { createRouter, createWebHistory } from 'vue-router';

import BattlePage from '@/pages/battle';
import ChatPage from '@/pages/chat';
import CombatPage from '@/pages/combat';
import GamePage from '@/pages/game';
import HomePage from '@/pages/home';
import LeisurePage from '@/pages/leisure';
import LoginPage from '@/pages/login';
import MegaMenuPage from '@/pages/megaMenu';
import NewChatPage from '@/pages/newChat';
import NewChatContentPage from '@/pages/newChatContent';
import NewLoginPage from '@/pages/newLogin';
import NewRegisterPage from '@/pages/newRegister';
import NewUserCenterPage from '@/pages/newUserCenter';
import RegisterPage from '@/pages/register';
import SettingsPage from '@/pages/settings';
import ShopPage from '@/pages/shop';
import UserCenterPage from '@/pages/userCenter';

import type { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  { path: '/', component: MegaMenuPage },
  { path: '/home', component: HomePage },
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
  { path: '/game', component: GamePage },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
