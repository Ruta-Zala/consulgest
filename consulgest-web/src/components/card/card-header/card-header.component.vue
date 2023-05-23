<template>
	<div class="flex justify-between items-center text-c-dark-blue">
		<div class="flex items-center gap-4">
			<div class="font-medium text-lg">{{ title }}</div>
			<div><slot name="afterTitle" /></div>
		</div>
		<div><slot name="endTitle" /></div>
	</div>
</template>

<script lang="ts" setup>
import { PropType } from 'vue';

defineProps({
	title: {
		type: String as PropType<string>,
		required: true,
	},
});
</script>
