<template>
	<div
		class="py-1 px-3 rounded-3xl flex items-center font-semibold gap-2"
		:class="[textColor, bgColor]"
	>
		<component :is="icon" v-if="icon" class="h-5 w-5" />
		<span v-if="percentage" class="leading-4">{{ percentage }}%</span>
	</div>
</template>

<script lang="ts" setup>
import type { Component, PropType } from 'vue';

defineProps({
	percentage: {
		type: Number as PropType<number>,
		default: undefined,
		required: false,
	},
	icon: {
		type: Object as PropType<Component>,
		default: undefined,
		required: false,
	},
	textColor: {
		type: String as PropType<string>,
		default: 'text-white',
	},
	bgColor: {
		type: String as PropType<string>,
		default: 'bg-c-deep-blue',
	},
});
</script>
