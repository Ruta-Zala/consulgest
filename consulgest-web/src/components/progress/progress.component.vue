<template>
	<div class="flex items-center gap-7">
		<div class="h-2 rounded-full bg-c-success bg-opacity-10 flex-1">
			<div
				role="progressbar"
				class="h-full rounded-full bg-c-success"
				:style="{ width: `${progress}%` }"
				:aria-valuenow="progress"
				aria-valuemin="0"
				aria-valuemax="100"
			/>
		</div>
		<div v-if="progressValue" class="text-sm font-semibold text-c-dark-blue">
			{{ progress }}%
		</div>
	</div>
</template>

<script setup lang="ts">
import { PropType } from 'vue';

defineProps({
	progress: {
		type: Number as PropType<number>,
		required: true,
	},
	progressValue: {
		type: Boolean as PropType<boolean>,
		default: false,
	},
});
</script>
