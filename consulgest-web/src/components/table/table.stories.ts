import { Meta, StoryFn } from '@storybook/vue3';
import { defineComponent } from '@vue/runtime-core';
import Component from './table.component.vue';

export default {
	title: 'Components / Table',
	component: Component,
} as Meta;

const data = [
	{
		id: '1',
		dossier_name: 'CRV - RB1 RB001',
		n_d_g: '4349',
		debtor: 'Louis Adjanohoun',
		position: 'Phone Col.',
		statistical_taking: '60%',
	},
	{
		id: '2',
		dossier_name: 'CRV - RB1 RB003',
		n_d_g: '9439',
		debtor: 'aouis Adjanohoun',
		position: 'dPhone Col.',
		statistical_taking: '20%',
	},
	{
		id: '3',
		dossier_name: 'CRV - RB1 RB0043',
		n_d_g: '1349',
		debtor: 'vouis Adjanohoun',
		position: 'zPhone Col.',
		statistical_taking: '40%',
	},
	{
		id: '4',
		dossier_name: 'CRV - RB1 RB003',
		n_d_g: '9439',
		debtor: 'aouis Adjanohoun',
		position: 'dPhone Col.',
		statistical_taking: '20%',
	},
	{
		id: '5',
		dossier_name: 'CRV - RB1 RB0043',
		n_d_g: '1349',
		debtor: 'vouis Adjanohoun',
		position: 'zPhone Col.',
		statistical_taking: '40%',
	},
	{
		id: '6',
		dossier_name: 'CRV - RB1 RB003',
		n_d_g: '9439',
		debtor: 'aouis Adjanohoun',
		position: 'dPhone Col.',
		statistical_taking: '20%',
	},
	{
		id: '7',
		dossier_name: 'CRV - RB1 RB0043',
		n_d_g: '1349',
		debtor: 'vouis Adjanohoun',
		position: 'zPhone Col.',
		statistical_taking: '40%',
	},
	{
		id: '8',
		dossier_name: 'CRV - RB1 RB001',
		n_d_g: '4349',
		debtor: 'Louis Adjanohoun',
		position: 'Phone Col.',
		statistical_taking: '60%',
	},
];
const columns = [
	{
		label: 'id',
		value: 'id',
	},
	{
		label: 'Dossier Name',
		value: 'dossier_name',
	},
	{
		label: 'N.D.G',
		value: 'n_d_g',
	},
	{
		label: 'Debtor',
		value: 'debtor',
	},
	{
		label: 'Position',
		value: 'position',
	},
	{
		label: 'Statistical Taking',
		value: 'statistical_taking',
	},
];

const html = String.raw;

export const Table: StoryFn = () => {
	return defineComponent({
		components: { Component },
		setup: () => ({ data, columns }),
		template: html`<Component :columns="columns" :data="data" />`,
	});
};
