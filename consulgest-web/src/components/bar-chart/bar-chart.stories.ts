import { Meta, StoryFn } from '@storybook/vue3';
import { defineComponent } from '@vue/runtime-core';
import Component from './bar-chart.component.vue';

export default {
	title: 'Components / Bar Chart',
	component: Component,
} as Meta;

const chartData = {
	labels: [
		'Phone Collection',
		'Pre-decaying loans',
		'Post-decaying loans',
		'Non performing loans (NPL)',
	],
	datasets: [
		{
			backgroundColor: ['#072EF5', '#2AD7B3', '#A955EB', '#EC7E0E'],
			borderRadius: 10,
			data: [300, 120, 89, 3],
		},
	],
};

const html = String.raw;

export const BarChart: StoryFn = () => {
	return defineComponent({
		components: { BarChart: Component },
		setup: () => ({ chartData }),
		template: html`
			<div class="max-w-md">
				<BarChart :chart-data="chartData" />
			</div>
		`,
	});
};
