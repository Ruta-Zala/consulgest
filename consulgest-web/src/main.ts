import './styles.css';
import { createApp } from 'vue';
import { RouterView } from 'vue-router';
import { router } from './router';
import { i18n } from './i18n';

createApp(RouterView).use(router).use(i18n).mount('#app');
