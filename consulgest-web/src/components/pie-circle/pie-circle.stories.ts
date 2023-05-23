import { Meta, StoryFn } from '@storybook/vue3';
import { defineComponent } from '@vue/runtime-core';
import Component from './pie-circle.component.vue';

export default {
	title: 'Components / Pie Circle',
	component: Component,
} as Meta;

const payloadValueOne = [
	{ color: '#072EF5', value: 250 },
	{ color: '#2AD7B3', value: 308 },
	{ color: '#EC7E0E', value: 520 },
	{ color: '#A955EB', value: 130 },
];

const payloadValueTwo = [
	{ color: '#072EF5', value: 250 },
	{ color: '#2AD7B3', value: 308 },
];

const payloadValueThree = [
	{ color: '#072EF5', value: 250 },
	{ color: '#2AD7B3', value: 308 },
	{ color: '#EC7E0E', value: 520 },
];

const html = String.raw;

export const PieCircle: StoryFn = () => {
	return defineComponent({
		components: { PieCircle: Component },
		setup: () => ({ payloadValueOne, payloadValueTwo, payloadValueThree }),
		template: html`
			<div class="flex gap-6">
				<PieCircle
					:stroke-width="14"
					:diameter="210"
					:payload-values="payloadValueOne"
				/>
				<PieCircle
					:stroke-width="14"
					:diameter="210"
					:payload-values="payloadValueTwo"
				/>
				<PieCircle
					:stroke-width="14"
					:diameter="210"
					:payload-values="payloadValueThree"
				/>
			</div>
		`,
	});
};
