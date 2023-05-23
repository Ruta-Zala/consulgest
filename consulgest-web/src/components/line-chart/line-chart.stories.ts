import { Meta, StoryFn } from '@storybook/vue3';
import { defineComponent } from '@vue/runtime-core';
import Component from './line-chart.component.vue';

export default {
	title: 'Components / Line Chart',
	component: Component,
} as Meta;

const commonObj = {
	tension: 0.4,
	pointRadius: 0,
	borderWidth: 4,
	pointHoverRadius: 8,
	pointBorderColor: '#fff',
};

const chartData = {
	labels: ['Jan', 'Feb', 'Mar'],
	datasets: [
		{
			label: 'Phone Collection',
			borderColor: ['#072EF5'],
			data: [300, 100, 200, 300],
			fill: true,
			backgroundColor: 'rgba(224, 224, 224, 0.3)',
			pointBackgroundColor: '#072EF5',
			...commonObj,
		},
		{
			label: 'Pre-decaying loans',
			borderColor: ['#2AD7B3'],
			data: [120, 100, 200, 300],
			pointBackgroundColor: '#2AD7B3',
			...commonObj,
		},
		{
			label: 'Post-Decaying loans',
			borderColor: ['#A955EB'],
			data: [89, 120, 100, 20],
			pointBackgroundColor: '#A955EB',
			...commonObj,
		},
		{
			label: 'Non Performant Loans',
			borderColor: ['#EC7E0E'],
			data: [3, 89, 120, 100],
			pointBackgroundColor: '#EC7E0E',
			...commonObj,
		},
	],
};

const html = String.raw;

export const LineChart: StoryFn = () => {
	return defineComponent({
		components: { LineChart: Component },
		setup: () => ({ chartData }),
		template: html` <LineChart :chart-data="chartData" :width="900" /> `,
	});
};
