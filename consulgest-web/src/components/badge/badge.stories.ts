import { Meta, StoryFn } from '@storybook/vue3';
import { defineComponent } from '@vue/runtime-core';
import { IconTrendingUp, IconTrendingDown } from '../../icons';
import Component from './badge.component.vue';

export default {
	title: 'Components / Badge',
	component: Component,
} as Meta;

const html = String.raw;

export const Badge: StoryFn = () =>
	defineComponent({
		components: { Badge: Component },
		setup: () => ({ IconTrendingUp, IconTrendingDown }),
		template: html`
			<div class="flex gap-5">
				<Badge :percentage="20" :icon="IconTrendingUp" />
				<Badge :percentage="20" :icon="IconTrendingDown" />
				<Badge :percentage="20" bg-color="bg-c-dark-blue" />
				<Badge :icon="IconTrendingDown" text-color="text-c-vivid-green" />
			</div>
		`,
	});
