import ElementPlus from 'element-plus';
import { createApp } from 'vue';
import 'element-plus/dist/index.css';

import App from './App.vue';
import router from './router';

import './style.scss';

createApp(App).use(ElementPlus).use(router).mount('#app');
