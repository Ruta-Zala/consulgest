import { Meta, StoryFn } from '@storybook/vue3';
import { defineComponent } from '@vue/runtime-core';
import { IconBook, IconReplay, IconTrendingUp } from '../../icons';
import Component from './small-card.component.vue';

export default {
	title: 'Components / Small Card',
	component: Component,
} as Meta;

const html = String.raw;

export const SmallCard: StoryFn = () => {
	return defineComponent({
		components: {
			SmallCard: Component,
		},
		setup: () => ({ IconReplay, IconBook, IconTrendingUp }),
		template: html`
			<div class="grid grid-cols-4 gap-10">
				<div class="border-r border-c-input-grey">
					<SmallCard
						title="With payment"
						value="32"
						totalValue="500"
						icon-color="text-c-deep-blue"
						:icon="IconBook"
					/>
				</div>
				<div class="border-r border-c-input-grey">
					<SmallCard
						title="Without payment"
						value="300"
						totalValue="500"
						icon-color="text-c-pink"
						:icon="IconBook"
					/>
				</div>
				<div class="border-r border-c-input-grey">
					<SmallCard
						title="With payment"
						value="12%"
						icon-color="text-c-success"
						:icon="IconReplay"
					/>
				</div>
				<div>
					<SmallCard
						title="With payment"
						value="+12%"
						icon-color="text-c-success"
						:icon="IconTrendingUp"
					/>
				</div>
			</div>
		`,
	});
};
