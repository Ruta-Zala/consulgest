<template>
	<DatePicker
		mode="date"
		:model-value="modelValue"
		:popover="{ visibility: visibility, positionFixed: false }"
		@update:model-value="$emit('update:modelValue', $event)"
	>
		<template #default="{ inputValue, inputEvents, togglePopover }">
			<div class="flex relative text-c-dark-blue">
				<input
					class="min-h-8 h-11 appearance-none w-full text-gray-700 focus:outline-none input max-w-full bg-c-grey-bg pr-9 placeholder-current"
					:value="inputValue"
					:class="inputClass"
					:placeholder="inputPlaceholder"
					v-on="inputEvents"
				/>
				<div class="absolute right-4 top-2/4 transform -translate-y-2/4">
					<IconCalender
						class="cursor-pointer outline-0 w-4 h-4"
						@click="togglePopover()"
					></IconCalender>
				</div>
			</div>
		</template>
	</DatePicker>
</template>

<script lang="ts" setup>
import { PropType } from '@vue/runtime-core';
import { DatePicker } from 'v-calendar';
import { IconCalender } from '../../icons';

defineEmits(['update:modelValue']);
defineProps({
	modelValue: {
		type: Date as PropType<Date>,
		default: undefined,
	},
	inputPlaceholder: {
		type: String as PropType<string>,
		default: 'Select Date',
	},
	visibility: {
		type: String as PropType<string>,
		default: 'click',
	},
	inputClass: {
		type: String as PropType<string>,
		default: undefined,
		required: false,
	},
});
</script>
