import { Meta, StoryFn } from '@storybook/vue3';
import { defineComponent } from '@vue/runtime-core';
import { IconCpu } from '../../icons';
import Component from './actions-panel.component.vue';

export default {
	title: 'Components / Actions Panel',
	component: Component,
} as Meta;

const html = String.raw;

export const ActionsPanel: StoryFn = () => {
	return defineComponent({
		components: {
			ActionsPanel: Component,
		},
		setup: () => ({ IconCpu }),
		template: html`
			<ActionsPanel title="AI Action" :icon="IconCpu">
				<span>Open Actions Panel</span>
			</ActionsPanel>
		`,
	});
};
