import { Meta, StoryFn } from '@storybook/vue3';
import { defineComponent } from '@vue/runtime-core';
import Card from '../card/card.component.vue';
import { IconOutcome, IconWatch } from '../../icons';
import Component from './small-widget.component.vue';

export default {
	title: 'Components / Small Widget',
	component: Component,
} as Meta;

const html = String.raw;

export const SmallWidget: StoryFn = () => {
	return defineComponent({
		components: {
			SmallWidget: Component,
			Card,
		},
		setup: () => ({ IconWatch, IconOutcome }),
		template: html`
			<div class="grid grid-cols-3 gap-10">
				<Card>
					<SmallWidget
						title="160"
						subtitle="Positivie Outcomes"
						icon-color="text-c-pink"
						:icon="IconOutcome"
					/>
				</Card>
				<Card>
					<SmallWidget
						title="3000"
						subtitle="Negative Outcomes"
						icon-color="text-c-dark-blue"
						:icon="IconWatch"
					/>
				</Card>
				<Card>
					<SmallWidget
						title="12%"
						subtitle="Conversion Rate"
						icon-color="text-c-dark-blue"
						:icon="IconWatch"
					/>
				</Card>
			</div>
		`,
	});
};
