<template>
	<svg
		:viewBox="`0 0 ${diameter} ${diameter}`"
		:width="diameter"
		:height="diameter"
		xmlns="http://www.w3.org/2000/svg"
	>
		<circle
			:cx="radius"
			:cy="radius"
			:r="radius - halfStrokeWidth"
			fill="none"
			:class="['stroke-current', backgroundColor]"
			:stroke-width="strokeWidth"
		/>
		<path
			:class="['stroke-current', foregroundColor]"
			:stroke-width="strokeWidth"
			stroke-linecap="round"
			fill="none"
			:d="path"
		/>
	</svg>
</template>

<script lang="ts" setup>
import { computed } from '@vue/runtime-core';
import { PropType } from 'vue';
import { describeArc } from '../../utils/describe-arc';
import { wrap } from '../../utils/wrap';
import { normalizeRatio } from '../../utils/normalize-ratio';

const props = defineProps({
	diameter: {
		type: Number as PropType<number>,
		required: true,
	},
	strokeWidth: {
		type: Number as PropType<number>,
		required: true,
	},
	backgroundColor: {
		type: String as PropType<string>,
		default: 'text-c-charts-bg',
	},
	foregroundColor: {
		type: String as PropType<string>,
		default: 'text-c-deep-blue',
	},
	total: {
		type: Number as PropType<number>,
		default: 100,
	},
	current: {
		type: Number as PropType<number>,
		default: 0,
	},
});
const radius = computed(() => props.diameter / 2);
const halfStrokeWidth = computed(() => props.strokeWidth / 2);

const path = computed(() => {
	const ratio = normalizeRatio(props.current, 0, props.total);

	// Don't draw anything
	if (ratio === 0) {
		return '';
	}

	return describeArc(
		radius.value,
		radius.value,
		radius.value - halfStrokeWidth.value,
		0,
		wrap(ratio * 360, 0, 360),
	);
});
</script>
