<template>
	<Line
		:chart-data="chartData"
		:chart-id="chartId"
		:dataset-id-key="datasetIdKey"
		:width="width"
		:height="height"
		:chart-options="chartOptions"
	/>
</template>

<script setup lang="ts">
import { Line } from 'vue-chartjs';
import {
	Chart as ChartJS,
	Title,
	Tooltip,
	Legend,
	LineElement,
	LinearScale,
	PointElement,
	CategoryScale,
	Filler,
	ChartOptions,
	ChartData,
	ScatterDataPoint,
} from 'chart.js';
import { PropType } from '@vue/runtime-core';

ChartJS.register(
	Title,
	Tooltip,
	Legend,
	LineElement,
	LinearScale,
	PointElement,
	Filler,
	CategoryScale,
);

const props = defineProps({
	chartId: {
		type: String,
		default: 'line-chart',
	},
	datasetIdKey: {
		type: String,
		default: 'label',
	},
	width: {
		type: Number,
		default: 400,
	},
	height: {
		type: Number,
		default: 400,
	},
	chartData: {
		type: Object as PropType<
			ChartData<'line', (number | ScatterDataPoint | null)[], unknown>
		>,
		required: true,
	},
	xTitle: {
		type: String,
		default: 'Period of time',
	},
	yTitle: {
		type: String,
		default: '% weight',
	},
});

const chartOptions: ChartOptions<'line'> = {
	responsive: true,
	maintainAspectRatio: false,
	plugins: {
		legend: {
			display: false,
		},
		tooltip: {
			mode: 'index',
			intersect: false,
			backgroundColor: '#ffffff',
			titleColor: '#000000',
			bodyColor: '#000000',
			cornerRadius: 12,
			padding: 16,
			usePointStyle: true,
			bodySpacing: 6,
		},
	},

	scales: {
		y: {
			type: 'linear',
			display: true,
			position: 'left',
			title: {
				display: true,
				text: props.yTitle,
				color: '#C4D6F7',
			},
		},
		x: {
			ticks: {
				display: true,
			},
			title: {
				display: true,
				text: props.xTitle,
				color: '#C4D6F7',
			},
			grid: {
				display: true,
				borderDash: [10],
			},
		},
	},
};
</script>
