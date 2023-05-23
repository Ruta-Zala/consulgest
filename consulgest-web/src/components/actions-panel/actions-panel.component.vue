<template>
	<Disclosure v-slot="{ open }">
		<DisclosureButton
			class="w-full bg-c-grey-bg py-4 px-6 flex items-center space-x-2 text-sm text-c-dark-blue"
		>
			<component :is="icon" class="w-4 h-4" />
			<span>{{ title }}</span>
			<span class="flex items-center">
				<IconDropdown class="w-2 h-2" :class="open ? 'rotate-180' : ''" />
			</span>
		</DisclosureButton>
		<DisclosurePanel class="bg-c-grey-bg pb-4 px-6">
			<slot />
		</DisclosurePanel>
	</Disclosure>
</template>

<script setup lang="ts">
import { Disclosure, DisclosureButton, DisclosurePanel } from '@headlessui/vue';
import { DefineComponent, PropType } from 'vue';
import { IconDropdown } from '../../icons';

defineProps({
	title: {
		type: String,
		required: true,
	},
	icon: {
		type: Object as PropType<DefineComponent>,
		required: true,
	},
});
</script>
