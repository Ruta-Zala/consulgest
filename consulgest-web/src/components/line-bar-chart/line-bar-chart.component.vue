<template>
	<Bar
		:chart-id="chartId"
		:chart-data="chartData"
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
	PointElement,
	ChartData,
	LineController,
	LineElement,
} from 'chart.js';
import { PropType } from '@vue/runtime-core';
import { computed } from 'vue';

ChartJS.register(
	Title,
	Tooltip,
	Legend,
	BarElement,
	LineElement,
	CategoryScale,
	LinearScale,
	PointElement,
	LineController,
);

const props = defineProps({
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

const dataSetColor = ['#0DE4E4', '#072EF5'];

const chartData = computed(() => {
	return {
		labels: props.chartData.labels,
		datasets: props.chartData.datasets.map((item, index) => ({
			label: item.label,
			backgroundColor: dataSetColor[index % 2],
			data: item.data,
			type: index % 2 ? 'bar' : 'line',
			order: index % 2 ? 1 : 0,
		})),
	};
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
			grid: {
				borderDash: [8, 4],
				color: '#C4D6F6',
				drawTicks: true,
				offset: true,
				zeroLineColor: 'transparent',
			},
		},
		y: {
			grid: {
				borderDash: [8, 4],
				color: '#C4D6F6',
				drawTicks: false,
				offset: true,
			},
		},
	},
	barThickness: 38,
	borderRadius: 4,
	borderSkipped: false,
	pointRadius: 9,
	pointBorderWidth: 3,
	pointBorderColor: 'rgb(255,255,255)',
};
</script>
