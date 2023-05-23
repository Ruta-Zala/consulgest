import { Meta, StoryFn } from '@storybook/vue3';
import { defineComponent } from '@vue/runtime-core';
import Component from './progress-widget.component.vue';

export default {
	title: 'Components / Progress Widget',
	component: Component,
} as Meta;

const items = [
	{ title: 'Project 1', value: '32:05 Hrs', progress: 10 },
	{ title: 'UI/UX Design', value: '23:05 Hrs', progress: 90 },
];

const html = String.raw;

export const ProgressWidget: StoryFn = () => {
	return defineComponent({
		components: { ProgressWidget: Component },
		setup: () => ({ items }),
		template: html`
			<ProgressWidget title="Most invested projects" :items="items" />
		`,
	});
};
