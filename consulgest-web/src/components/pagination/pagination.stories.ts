import { Meta, StoryFn } from '@storybook/vue3';
import { defineComponent } from '@vue/runtime-core';
import { ref } from 'vue';
import Component from './pagination.component.vue';

export default {
	title: 'Components / Pagination',
	component: Component,
} as Meta;

const html = String.raw;

export const Pagination: StoryFn = () => {
	return defineComponent({
		components: { Pagination: Component },
		setup: () => ({ page: ref(1) }),
		template: html`<Pagination v-model="page" :last-page="8" />`,
	});
};
