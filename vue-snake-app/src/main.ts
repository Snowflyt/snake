import ElementPlus from 'element-plus';
import { createApp } from 'vue';
import 'element-plus/dist/index.css';

import App from './App.vue';

import './style.scss';

createApp(App).use(ElementPlus).mount('#app');
