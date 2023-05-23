<template>
	<div class="flex items-center gap-4 overflow-hidden">
		<div :class="iconColor">
			<div
				:class="[
					'w-12 h-12 relative flex items-center justify-center',
					'before:absolute before:w-full before:h-full',
					'before:bg-current before:opacity-5 before:rounded-full',
				]"
			>
				<div class="flex items-center justify-center">
					<component :is="icon" class="w-6 h-6" />
				</div>
			</div>
		</div>
		<div class="overflow-hidden">
			<div class="truncate text-sm text-c-dark-blue font-normal mb-1">
				{{ title }}
			</div>
			<div class="flex items-center">
				<div class="tracking-wide text-2xl font-semibold" :class="iconColor">
					{{ value }}
				</div>
				<div
					v-if="totalValue !== null"
					class="text-xl font-medium text-c-dark-blue"
				>
					<span class="mx-2">/</span>{{ totalValue }}
				</div>
			</div>
		</div>
	</div>
</template>

<script lang="ts" setup>
import type { PropType, Component } from 'vue';

defineProps({
	title: {
		type: String as PropType<string>,
		required: true,
	},
	value: {
		type: String as PropType<string>,
		required: true,
	},
	totalValue: {
		type: String as PropType<string>,
		default: null,
	},
	iconColor: {
		type: String as PropType<string>,
		default: 'text-gray-600',
	},
	icon: {
		type: Object as PropType<Component>,
		required: true,
	},
});
</script>
