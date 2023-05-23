import { Meta, StoryFn } from '@storybook/vue3';
import { defineComponent } from '@vue/runtime-core';
import Component from './line-bar-chart.component.vue';

export default {
	title: 'Components / Line Bar Chart',
	component: Component,
} as Meta;

const chartData = {
	labels: ['01', '02', '03', '04'],
	datasets: [
		{
			label: 'Dataset 1',
			data: [60, 20, 30, 400],
		},
		{
			label: 'Dataset 2',
			data: [120, 230, 400, 500, 600],
		},
	],
};

const html = String.raw;

export const LineBarChart: StoryFn = () => {
	return defineComponent({
		components: { LineBarChart: Component },
		setup: () => ({ chartData }),
		template: html`
			<div class="max-w-md">
				<LineBarChart :chart-data="chartData" />
			</div>
		`,
	});
};
