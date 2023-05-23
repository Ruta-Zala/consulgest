<template>
	<Menu v-slot="{ open }" as="div" class="relative inline-block text-left">
		<MenuButton
			class="min-h-8 h-11 relative text-sm flex items-center gap-2 rounded-lg focus:outline-none py-2 w-full border"
			:class="[
				open
					? 'border-c-deep-blue text-c-deep-blue'
					: 'border-transparent text-c-dark-blue',
				icon ? 'px-2' : 'px-4',
			]"
		>
			<span v-if="icon">
				<component
					:is="icon"
					class="w-4 h-4"
					:class="open ? 'text-c-deep-blue' : 'text-c-input-grey'"
				/>
			</span>
			<span v-if="label" class="block truncate text-left flex-1">{{
				label
			}}</span>
			<span v-if="arrowDropDown" class="flex items-center pointer-events-none">
				<IconDropdown
					class="w-2 h-2"
					:class="open ? 'rotate-180 text-c-deep-blue' : 'text-c-dark-blue'"
				/>
			</span>
		</MenuButton>

		<transition
			enter-active-class="transition duration-100 ease-out"
			enter-from-class="transform scale-95 opacity-0"
			enter-to-class="transform scale-100 opacity-100"
			leave-active-class="transition duration-75 ease-in"
			leave-from-class="transform scale-100 opacity-100"
			leave-to-class="transform scale-95 opacity-0"
		>
			<MenuItems
				v-if="open"
				as="ul"
				class="z-20 mt-2 absolute origin-top-right bg-white rounded-lg w-full max-h-52 focus:outline-none whitespace-nowrap shadow-l overflow-x-hidden"
				:class="position === 'right' ? 'right-0' : 'left-0'"
			>
				<slot />
			</MenuItems>
		</transition>
	</Menu>
</template>

<script lang="ts" setup>
import type { Component, PropType } from 'vue';
import { Menu, MenuButton, MenuItems } from '@headlessui/vue';
import { IconDropdown } from '../../icons';

defineProps({
	label: {
		type: String as PropType<string>,
		default: undefined,
		required: false,
	},
	icon: {
		type: Object as PropType<Component>,
		default: undefined,
		required: false,
	},
	position: {
		type: String as PropType<string>,
		default: 'left',
		required: false,
	},
	arrowDropDown: {
		type: Boolean as PropType<boolean>,
		default: true,
	},
});
</script>
