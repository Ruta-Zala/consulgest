<template>
	<div
		class="relative overflow-hidden p-4 rounded-lg z-0 flex flex-col justify-center gap-1"
		:class="bgColor ? `border-none ${bgColor}` : `border ${borderColor}`"
	>
		<IconChartBackgroundGradient
			v-if="!simpleCard"
			class="absolute bottom-0 h-full -z-10"
			:class="[
				iconColor,
				bgPosition === 'left' ? 'left-0 scale-x-[-1]' : 'right-0',
			]"
		/>
		<div class="text-sm" :class="textColor">{{ title }}</div>
		<slot />
	</div>
</template>

<script lang="ts" setup>
import { PropType } from 'vue';
import { IconChartBackgroundGradient } from '../../icons/index';

defineProps({
	title: {
		type: String as PropType<string>,
		default: undefined,
		required: false,
	},
	borderColor: {
		type: String as PropType<string>,
		default: 'border-c-deep-blue',
	},
	textColor: {
		type: String as PropType<string>,
		default: 'text-c-dark-blue',
	},
	iconColor: {
		type: String as PropType<string>,
		default: 'text-white',
	},
	bgColor: {
		type: String as PropType<string>,
		default: undefined,
		required: false,
	},
	simpleCard: {
		type: Boolean as PropType<boolean>,
		default: undefined,
		required: false,
	},
	bgPosition: {
		type: String as PropType<string>,
		default: 'right',
		required: false,
	},
});
</script>
