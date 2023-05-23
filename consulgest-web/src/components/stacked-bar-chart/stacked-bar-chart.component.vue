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
import { computed } from 'vue';

ChartJS.register(
	Title,
	Tooltip,
	Legend,
	BarElement,
	CategoryScale,
	LinearScale,
);

const props = defineProps({
	chartId: {
		type: String,
		default: 'stacked-bar-chart',
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
	xTitle: {
		type: String,
		default: 'time (days)',
	},
	yTitle: {
		type: String,
		default: 'Amount',
	},
});
const dataSetColor = ['#F6A44F', '#0DE4E4'];

const chartData = computed(() => {
	return {
		labels: props.chartData.labels,
		datasets: props.chartData.datasets.map((item, index) => ({
			label: item.label,
			backgroundColor: dataSetColor[index % 2],
			data: item.data,
		})),
	};
});
const chartOptions = computed(() => {
	return {
		responsive: true,
		maintainAspectRatio: false,
		plugins: {
			legend: {
				display: false,
			},
		},
		barThickness: 20,
		borderRadius: {
			topLeft: 20,
			topRight: 20,
			bottomLeft: 20,
			bottomRight: 20,
		},
		borderSkipped: false,
		borderWidth: 3,
		borderColor: 'white',
		scales: {
			x: {
				title: {
					display: true,
					text: props.xTitle,
					color: '#C4D6F7',
				},
				stacked: true,
				grid: {
					borderDash: [10],
				},
			},
			y: {
				title: {
					display: true,
					text: props.yTitle,
					color: '#C4D6F7',
				},
				stacked: true,
				grid: {
					borderDash: [10],
				},
			},
		},
	};
});
</script>
