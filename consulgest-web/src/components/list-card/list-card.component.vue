<template>
	<div
		class="flex items-center gap-2 px-4 py-2 rounded-md bg-opacity-5"
		:class="bgColor"
	>
		<div class="flex items-center justify-center">
			<component :is="icon" class="w-5 h-5" :class="textColor" />
		</div>
		<div class="truncate text-sm flex-1 text-c-dark-blue">
			{{ title }}
		</div>
		<div
			class="tracking-wide text-c-dark-blue"
			:class="[fontBold ? 'text-xl font-semibold' : 'text-sm']"
		>
			{{ value }}
		</div>
	</div>
</template>
<script setup lang="ts">
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
	textColor: {
		type: String as PropType<string>,
		default: 'text-gray-600',
	},
	bgColor: {
		type: String as PropType<string>,
		default: 'bg-gray-600',
	},
	icon: {
		type: Object as PropType<Component>,
		required: true,
	},
	fontBold: {
		type: Boolean,
		default: false,
	},
});
</script>
