import { Meta, StoryFn } from '@storybook/vue3';
import { defineComponent } from 'vue';
import Component from './page-menu.component.vue';

export default {
	title: 'Components / PageMenu',
	component: Component,
} as Meta;

const menuOptions = [
	{ title: 'Menu 1', href: '/dashboard' },
	{ title: 'Menu 2', href: '/dashboard' },
	{ title: 'Menu 3', href: '/dashboard' },
];

const html = String.raw;

export const PageMenu: StoryFn = () =>
	defineComponent({
		components: { PageMenu: Component },
		setup: () => ({ menuOptions }),
		template: html`<PageMenu :options="menuOptions" />`,
	});
