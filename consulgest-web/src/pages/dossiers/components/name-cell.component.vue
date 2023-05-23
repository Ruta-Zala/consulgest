<template>
	<div class="flex gap-2 items-center">
		<div
			class="bg-c-deep-blue text-white h-9 min-w-[36px] w-9 rounded-full flex items-center justify-center font-bold"
		>
			{{ firstTwoWordsLetters }}
		</div>
		<div>{{ value }}</div>
		<div
			class="bg-c-success bg-opacity-5 px-2 text-sm py-1 text-c-success rounded-full"
		>
			{{ row.status }}
		</div>
	</div>
</template>

<script setup lang="ts">
import { computed, PropType } from 'vue';

const props = defineProps({
	value: {
		type: String as PropType<string>,
		required: true,
	},
	row: {
		type: Object as PropType<{ status: string }>,
		required: true,
	},
});

const firstTwoWordsLetters = computed(() => {
	const words = props.value
		.split(' ')
		.map((word) => word.trim())
		.filter(Boolean);

	return words
		.flatMap((word) => word.slice(0, 1))
		.slice(0, 2)
		.join('');
});
</script>
