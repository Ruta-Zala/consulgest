import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

// keep in sync with .storybook/main.js
export default defineConfig({
	server: {
		host: true,
		port: 3000,
		open: true,
	},
	define: {
		// https://vue-i18n.intlify.dev/guide/advanced/optimization.html#reduce-bundle-size-with-feature-build-flags
		__VUE_I18N_FULL_INSTALL__: true,
		__VUE_I18N_LEGACY_API__: false,
		__INTLIFY_PROD_DEVTOOLS__: false,
	},
	plugins: [vue()],
});
