import { Meta, StoryFn } from '@storybook/vue3';
import { defineComponent } from '@vue/runtime-core';
import DatepickerInput from '../../datepicker/datepicker.component.vue';
import Dropdown from '../../dropdown/dropdown.component.vue';
import { IconDropdown } from '../../../icons';
import Card from '../card.component.vue';
import Component from './card-header.component.vue';

export default {
	title: 'Components / Card Header',
	component: Component,
} as Meta;

const html = String.raw;

export const CardHeader: StoryFn = () => {
	return defineComponent({
		components: {
			CardHeader: Component,
			DatepickerInput,
			IconDropdown,
			Card,
			Dropdown,
		},
		template: html`
			<Card>
				<CardHeader title="Expected income weight">
					<template #afterTitle>
						<Dropdown label="By Value">
							<DropdownItem>
								<span>By Value</span>
							</DropdownItem>
						</Dropdown>
					</template>
					<template #endTitle>
						<DatepickerInput input-class="test bg-c-ghost-white border-none" />
					</template>
				</CardHeader>
			</Card>
		`,
	});
};
