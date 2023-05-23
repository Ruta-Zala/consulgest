import { Meta, StoryFn } from '@storybook/vue3';
import { defineComponent } from '@vue/runtime-core';
import Component from './progress.component.vue';

export default {
	title: 'Components / Progress',
	component: Component,
} as Meta;
const html = String.raw;

export const Progress: StoryFn = () => {
	return defineComponent({
		components: { Component },
		template: html`
			<Component :progress="90" :progress-value="true" />
			<Component :progress="90" />
		`,
	});
};
