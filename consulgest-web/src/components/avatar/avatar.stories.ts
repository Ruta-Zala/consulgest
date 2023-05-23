import { Meta, StoryFn } from '@storybook/vue3';
import { defineComponent } from 'vue';
import Component from './avatar.component.vue';

export default {
	title: 'Components / Avatar',
	component: Component,
} as Meta;

const html = String.raw;

export const Avatar: StoryFn = () =>
	defineComponent({
		components: { Avatar: Component },
		template: html`
			<Avatar alt="image" src="https://picsum.photos/42/42" size="w-20 h-20" />
		`,
	});
