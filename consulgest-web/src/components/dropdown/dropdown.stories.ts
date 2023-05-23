import { Meta, StoryFn } from '@storybook/vue3';
import { defineComponent } from '@vue/runtime-core';
import DropdownItem from './dropdown-item.component.vue';
import Component from './dropdown.component.vue';

export default {
	title: 'Components / Dropdown',
	component: Component,
} as Meta;

const html = String.raw;

export const Dropdown: StoryFn = () => {
	return defineComponent({
		components: { Dropdown: Component, DropdownItem },
		template: html`
			<div class="flex gap-5">
				<Dropdown label="By Value">
					<DropdownItem>
						<div class="text-sm flex items-center gap-4 justify-between py-2">
							<div class="flex items-center gap-2">
								<div class="w-3 h-3 bg-c-dark-blue rounded-full"></div>
								<span>Phone Collection</span>
							</div>
							<span>51%</span>
						</div>
						<hr class="border-c-grey" />
					</DropdownItem>
					<DropdownItem>
						<div class="text-sm flex items-center gap-4 justify-between py-2">
							<div class="flex items-center gap-2">
								<div class="w-3 h-3 bg-c-dark-blue rounded-full"></div>
								<span>Pre-decaying loans</span>
							</div>
							<span>41%</span>
						</div>
					</DropdownItem>
				</Dropdown>
			</div>
		`,
	});
};
