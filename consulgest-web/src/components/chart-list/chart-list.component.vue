<template>
	<div class="w-full">
		<div
			v-for="item in columns"
			:key="item.label + item.value"
			class="text-c-dark-blue flex items-center flex-1 py-2 border-b border-c-gray last:border-b-0"
		>
			<div
				v-if="showItemDot"
				class="h-3 w-3 rounded-full mr-4"
				:class="item.itemDotClass"
			/>
			<div class="flex-1 truncate">{{ item.label }}</div>
			<div :class="item.textColor ? `${item.textColor} font-semibold` : ''">
				{{ item.value }}
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">
defineProps({
	columns: {
		type: Object,
		required: true,
	},
	showItemDot: {
		type: Boolean,
		required: true,
	},
});
</script>
