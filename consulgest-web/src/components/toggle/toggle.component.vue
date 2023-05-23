<template>
	<div class="form-control">
		<label class="label cursor-pointer space-x-2">
			<span v-if="label" class="label-text" v-text="label"></span>
			<input
				v-bind="$attrs"
				type="checkbox"
				class="toggle toggle-primary"
				:value="modelValue"
				@input="
					$emit(
						'update:modelValue',
						($event.target as HTMLInputElement).checked,
					)
				"
			/>
		</label>
	</div>
</template>

<script lang="ts" setup>
import { PropType } from 'vue';
defineProps({
	label: {
		type: String as PropType<string | undefined>,
		default: undefined,
	},
	modelValue: {
		type: Boolean as PropType<boolean>,
		default: false,
	},
});

defineEmits(['update:modelValue']);
</script>

<script lang="ts">
export default {
	inheritAttrs: false,
};
</script>

<style scoped>
.toggle {
	width: 49px;
	height: 26px;
	box-shadow: calc(var(--handleoffset) * -1) 0 0 2px #c4d6f6 inset,
		0 0 0 2px #c4d6f6 inset;
	background-color: #fff;
}
.toggle-primary:checked,
.toggle-primary[checked='true'] {
	background-color: #fff !important;
	box-shadow: var(--handleoffset) 0 0 2px #072ef5 inset, 0 0 0 2px #072ef5 inset;
}
</style>
