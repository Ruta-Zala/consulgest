import { createI18n } from 'vue-i18n';
import en from './locales/en.json';
import it from './locales/it.json';

export const i18n = createI18n({
	legacy: false,
	locale: import.meta.env.PROD ? 'it' : 'en',
	fallbackLocale: 'en',
	messages: { en, it },
});
