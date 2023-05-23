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
			<div class="truncate text-xl text-c-dark-blue font-medium mb-1">
				{{ title }}
				<small>{{ afterTitle }}</small>
			</div>
			<div class="text-c-polo-blue tracking-wide text-sm">
				{{ subtitle }}
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
	afterTitle: {
		type: String as PropType<string>,
	},
	subtitle: {
		type: String as PropType<string>,
		required: true,
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
