import { Meta, StoryFn } from '@storybook/vue3';
import { defineComponent } from '@vue/runtime-core';
import Component from './user-card.component.vue';

export default {
	title: 'Components / User Card',
	component: Component,
} as Meta;

const html = String.raw;

export const UserCard: StoryFn = () => {
	return defineComponent({
		components: { UserCard: Component },
		template: html`
			<UserCard
				:percentage="20"
				title="positive closure"
				profile-image="https://picsum.photos/72/72"
				name="Josh Anderson Smith"
				bookName="CRV - RB1 RB001"
				difficultyLevel="Easy"
				collectionType="phone"
				:collectionPercentage="20"
				collectorName="Hanna Martin"
				collectorImage="https://picsum.photos/42/42"
			/>
		`,
	});
};
