<template>
	<div>
		<div class="text-base font-medium text-c-dark-blue mb-7">
			{{ title }}
		</div>
		<div v-for="item in items" :key="item.title" class="mb-4 last:mb-0">
			<div
				class="flex justify-between mb-2 text-sm text-c-dark-blue tracking-wide"
			>
				<span>{{ item.title }}</span>
				<span class="font-semibold">{{ item.value }}</span>
			</div>
			<Progress :progress="item.progress" />
		</div>
	</div>
</template>

<script lang="ts" setup>
import { PropType } from 'vue';
import Progress from '../progress/progress.component.vue';

defineProps({
	title: {
		type: String as PropType<string>,
		required: true,
	},
	items: {
		type: Array as PropType<
			Array<{
				title: string;
				value: string;
				progress: number;
			}>
		>,
		default: () => [],
	},
});
</script>
