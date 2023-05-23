<template>
	<svg
		:viewBox="`0 0 ${diameter} ${diameter}`"
		:width="diameter"
		:height="diameter"
		xmlns="http://www.w3.org/2000/svg"
	>
		<g v-for="(value, index) in chartData" :key="index">
			<circle
				:cx="radius"
				:cy="radius"
				:r="radius - halfStrokeWidth"
				:stroke="value.color"
				:stroke-width="strokeWidth"
				:stroke-dasharray="adjustedCircumference"
				:stroke-dashoffset="value.strokeDashoffset"
				stroke-linecap="round"
				fill="transparent"
				:transform="value.transform"
			/>
		</g>
	</svg>
</template>

<script setup lang="ts">
import { computed } from '@vue/runtime-core';
import { PropType } from 'vue';

type PayloadValue = {
	color: string;
	value: number;
};

const props = defineProps({
	diameter: {
		type: Number as PropType<number>,
		required: true,
	},
	strokeWidth: {
		type: Number as PropType<number>,
		required: true,
	},
	payloadValues: {
		type: Array as PropType<Array<PayloadValue>>,
		required: true,
	},
});

const valuesSum = computed(() =>
	props.payloadValues.reduce((acc, val) => acc + val.value, 0),
);

const radius = computed(() => props.diameter / 2);
const halfStrokeWidth = computed(() => props.strokeWidth / 2);
const circumference = computed(() => 2 * Math.PI * radius.value);
const adjustedCircumference = computed(() => circumference.value - 2);

const chartData = computed(() => {
	let angleOffset = -80;

	const data = props.payloadValues.map(({ color, value }) => {
		const valueAsPercentage = value / valuesSum.value;
		const strokeDiff = valueAsPercentage * circumference.value;
		const strokeDashoffset = circumference.value - strokeDiff;
		const transform = `rotate(${angleOffset}, ${radius.value}, ${radius.value})`;

		angleOffset = angleOffset + valueAsPercentage * 360;

		return { color, value, transform, strokeDashoffset };
	});

	// TBD: should we sort data!?
	return data.sort((a, b) => b.value - a.value);
});
</script>
