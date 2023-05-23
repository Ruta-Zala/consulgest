import { Meta, StoryFn } from '@storybook/vue3';
import { defineComponent } from 'vue';
import dashboardImage from '../../assets/images/pie-chart.svg';
import { IconMenu } from '../../icons';
import Component from './header.component.vue';

export default {
	title: 'Components / Header',
	component: Component,
} as Meta;

const html = String.raw;

export const Header: StoryFn = (args) =>
	defineComponent({
		components: { Component },
		setup: () => ({ dashboardImage, IconMenu, ...args }),
		template: html`<Component
			:src="dashboardImage"
			alt="pie chart"
			title="Dashboard"
			sub-title="Monday, June 6, 2022"
			:icon="IconMenu"
		/>`,
	});
