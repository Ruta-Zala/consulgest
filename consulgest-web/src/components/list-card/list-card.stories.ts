import { Meta, StoryFn } from '@storybook/vue3';
import { defineComponent } from '@vue/runtime-core';
import { IconMoney, IconReplay, IconCalender, IconBookOpen } from '../../icons';
import Component from './list-card.component.vue';

export default {
	title: 'Components / List Card',
	component: Component,
} as Meta;

const html = String.raw;

export const ListCard: StoryFn = () => {
	return defineComponent({
		components: { ListCard: Component },
		setup: () => ({ IconMoney, IconReplay, IconCalender, IconBookOpen }),
		template: html`
			<div class="flex gap-2 flex-col">
				<ListCard
					title="Entrusted"
					value="32 230,45 €"
					text-color="text-c-warning"
					class="bg-c-warning"
					:icon="IconMoney"
				/>
				<ListCard
					title="Returned"
					value="32 230,45 €"
					text-color="text-c-success"
					class="bg-c-success"
					:icon="IconReplay"
				/>
				<ListCard
					title="Time"
					value="90 days"
					text-color="text-c-dark-blue"
					class="bg-c-dark-blue"
					:icon="IconCalender"
				/>
				<ListCard
					title="Total conclusions"
					value="140"
					text-color="text-c-dark-blue"
					class="bg-c-dark-blue"
					:icon="IconBookOpen"
					:font-bold="true"
				/>
			</div>
		`,
	});
};
