<template>
	<div
		class="px-3 py-2 flex items-center justify-center rounded-tl-lg rounded-tr-lg bg-c-deep-blue text-white"
	>
		<IconCpu class="h-5 w-5 mr-2 text-white" />
		<div class="flex items-center gap-1 text-sm font-semibold">
			<span>{{ percentage }}%</span>
			<span>{{ title }}</span>
		</div>
	</div>
</template>

<script lang="ts" setup>
import { IconCpu } from '../../icons/index';

defineProps({
	percentage: {
		type: Number,
		required: true,
	},
	title: {
		type: String,
		required: true,
	},
});
</script>
