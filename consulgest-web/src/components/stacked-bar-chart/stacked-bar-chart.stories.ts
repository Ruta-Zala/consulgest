import { Meta, StoryFn } from '@storybook/vue3';
import { defineComponent } from '@vue/runtime-core';
import Component from './stacked-bar-chart.component.vue';

export default {
	title: 'Components / Stacked Bar Chart',
	component: Component,
} as Meta;

const chartData = {
	labels: ['Jan', 'Feb', 'March', 'Apr', 'May', 'June', 'July'],
	datasets: [
		{
			label: 'Positive',
			data: [1, 36, 10, 40, 39, 30, 10],
		},
		{
			label: 'Negative',
			data: [40, 39, 20, 80, 59, 80, 40],
		},
	],
};

const html = String.raw;

export const StackedBarChart: StoryFn = () => {
	return defineComponent({
		components: { StackedBarChart: Component },
		setup: () => ({ chartData }),
		template: html`
			<div class="max-w-md">
				<StackedBarChart :chart-data="chartData" />
			</div>
		`,
	});
};
