import { Meta, StoryFn } from '@storybook/vue3';
import { defineComponent } from '@vue/runtime-core';
import Component from './card-badge.component.vue';

export default {
	title: 'Components / Card Badge',
	component: Component,
} as Meta;

const html = String.raw;

export const CardBadge: StoryFn = () =>
	defineComponent({
		components: { CardBadge: Component },
		template: html` <CardBadge :percentage="20" title="5947833" />`,
	});
