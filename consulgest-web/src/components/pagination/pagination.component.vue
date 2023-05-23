<template>
	<ul class="inline-flex border border-c-coral-blue rounded-lg h-10">
		<li>
			<button
				class="flex items-center border-r h-full px-3"
				:class="{ 'cursor-not-allowed': modelValue === 0 }"
				:disabled="modelValue === 0"
				@click="emit('update:modelValue', modelValue - 1)"
			>
				<IconDropdown class="h-3 w-3 text-c-polo-blue rotate-90" />
			</button>
		</li>
		<li v-for="(item, index) in total" :key="index">
			<button
				:class="index === modelValue ? 'bg-blue-50' : ''"
				class="border-r border-c-coral-blue h-full px-3 text-c-dark-blue text-sm min-w-[38px]"
				@click="emit('update:modelValue', index)"
			>
				{{ item }}
			</button>
		</li>
		<li>
			<button
				class="flex items-center px-3 h-full"
				:class="{ 'cursor-not-allowed': modelValue === total - 1 }"
				:disabled="modelValue === total - 1"
				@click="emit('update:modelValue', modelValue + 1)"
			>
				<IconDropdown class="h-3 w-3 text-c-polo-blue -rotate-90" />
			</button>
		</li>
	</ul>
</template>

<script setup lang="ts">
import { IconDropdown } from '../../icons/index';

defineProps({
	modelValue: {
		type: Number,
		required: true,
	},
	total: {
		type: Number,
		required: true,
	},
});

const emit = defineEmits(['update:modelValue']);
</script>
