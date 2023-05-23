<template>
	<Bar
		:chart-data="chartData"
		:chart-id="chartId"
		:dataset-id-key="datasetIdKey"
		:width="width"
		:height="height"
		:chart-options="chartOptions"
	/>
</template>

<script setup lang="ts">
import { Bar } from 'vue-chartjs';
import {
	Chart as ChartJS,
	Title,
	Tooltip,
	Legend,
	BarElement,
	CategoryScale,
	LinearScale,
	ChartData,
} from 'chart.js';
import { PropType } from '@vue/runtime-core';

ChartJS.register(
	Title,
	Tooltip,
	Legend,
	BarElement,
	CategoryScale,
	LinearScale,
);

defineProps({
	chartId: {
		type: String,
		default: 'bar-chart',
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
		type: Object as PropType<ChartData<'bar', number[], unknown>>,
		required: true,
	},
});

const chartOptions = {
	responsive: true,
	maintainAspectRatio: false,
	plugins: {
		legend: {
			display: false,
		},
	},
	scales: {
		x: {
			ticks: {
				display: false,
			},
			grid: {
				display: true,
				borderDash: [10],
			},
		},
	},
};
</script>
