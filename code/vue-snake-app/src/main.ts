import { createApp } from 'vue';

import App from './App.vue';
import router from './router';
import './style.scss';

// // eslint-disable-next-line import/default
// import router from './router';

const app = createApp(App);
// Make sure to _use_ the router instance to make the
// whole app router-aware.
app.use(router);
app.mount('#app');
