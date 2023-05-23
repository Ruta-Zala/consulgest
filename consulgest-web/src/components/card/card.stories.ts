import { Meta, StoryFn } from '@storybook/vue3';
import { defineComponent } from '@vue/runtime-core';
import Component from './card.component.vue';

export default {
	title: 'Components / Card',
	component: Component,
} as Meta;

const html = String.raw;

export const Card: StoryFn = () =>
	defineComponent({
		components: { Card: Component },
		template: html`<Card>Lorem ipsum dolor sit amet.</Card>`,
	});
