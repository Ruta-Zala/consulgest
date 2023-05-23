import { Meta, StoryFn } from '@storybook/vue3';
import { defineComponent } from '@vue/runtime-core';
import Component from './chart-list.component.vue';

export default {
	title: 'Components / ChartList',
	component: Component,
} as Meta;

const columns = [
	{
		label: 'Phone Collection',
		value: '200',
		itemDotClass: 'bg-c-success',
		textColor: 'text-c-success',
	},
	{
		label: 'Pre-decaying loans',
		value: '70',
		itemDotClass: 'bg-c-deep-blue',
	},
	{
		label: 'Post-decaying loans',
		value: '110',
		itemDotClass: 'bg-c-purple',
	},
	{
		label: 'Non performing loans (NPL)',
		value: '30',
		itemDotClass: 'bg-c-warning',
	},
];

const html = String.raw;

export const ChartList: StoryFn = () => {
	return defineComponent({
		components: { ChartList: Component },
		setup: () => ({ columns }),
		template: html`<ChartList :columns="columns" :showItemDot="true" />`,
	});
};
