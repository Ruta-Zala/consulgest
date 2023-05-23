import '../src/styles.css';
import { Parameters, setup } from '@storybook/vue3';

import { i18n } from '../src/i18n';
import { router } from '../src/router';

setup((app) => {
	app.use(i18n);
	app.use(router);
});

export const parameters: Parameters = {
	actions: { argTypesRegex: '^on[A-Z].*' },
	controls: {
		matchers: {
			color: /(background|color)$/i,
			date: /Date$/,
		},
	},
	options: {
		storySort: {
			method: 'alphabetical',
		},
	},
};
