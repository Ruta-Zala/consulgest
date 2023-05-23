import { Meta, StoryFn } from '@storybook/vue3';
import { defineComponent } from '@vue/runtime-core';
import { IconTrendingDown, IconTrendingUp, IconCalender } from '../../icons';
import Badge from '../badge/badge.component.vue';
import Avatar from '../avatar/avatar.component.vue';
import Component from './chart-card.component.vue';

export default {
	title: 'Components / Chart Card',
	component: Component,
} as Meta;

const html = String.raw;

export const ChartCard: StoryFn = () => {
	return defineComponent({
		components: {
			ChartCard: Component,
			Badge,
			IconCalender,
			Avatar,
		},
		setup: () => ({ IconTrendingUp, IconTrendingDown }),
		template: html` <div class="grid grid-cols-1 gap-4">
			<ChartCard
				title="Phone Collection"
				border-color="border-c-deep-blue"
				text-color="text-c-dark"
				icon-color="text-c-deep-blue"
			>
				<template #default>
					<div class="flex items-center gap-2">
						<span class="text-c-dark text-xl font-medium">2.000,22 €</span>
						<Badge
							:percentage="20"
							:icon="IconTrendingUp"
							text-color="text-white"
							bg-color="bg-c-deep-blue"
						/>
					</div>
				</template>
			</ChartCard>
			<ChartCard
				title="Positive closures (>90%)"
				border-color="border-c-vivid-green"
				text-color="text-c-dark"
				icon-color="text-c-vivid-green"
			>
				<template #default>
					<div class="flex items-center gap-2">
						<span class="text-c-dark text-xl font-medium">1230</span>
						<Badge
							:percentage="5"
							text-color="text-white"
							bg-color="bg-c-vivid-green"
						/>
					</div>
				</template>
			</ChartCard>
			<ChartCard
				title="Top suggested collector"
				border-color="border-c-light-orange"
				text-color="text-c-dark"
				icon-color="text-c-light-orange"
			>
				<template #default>
					<div class="flex items-center gap-2">
						<div class="flex items-center gap-2">
							<Avatar
								alt="image"
								src="https://picsum.photos/36/36"
								size="w-9 h-9"
							/>
							<span class="text-c-dark">Hanna Martin</span>
						</div>
						<Badge
							:percentage="20"
							text-color="text-white"
							bg-color="bg-c-light-orange"
						/>
					</div>
				</template>
			</ChartCard>
			<ChartCard
				title="Acount collected"
				text-color="text-white"
				icon-color="text-white"
				bg-color="bg-c-linear-blue"
			>
				<template #default>
					<span class="text-white text-xl font-medium">180.441,00 €</span>
				</template>
			</ChartCard>
			<ChartCard
				title="Total collected"
				text-color="text-white"
				icon-color="text-white"
				bg-color="bg-c-linear-blue"
			>
				<template #default>
					<div class="flex items-center gap-2">
						<span class="text-white text-xl font-medium">2.000,22 €</span>
						<Badge
							:percentage="20"
							text-color="text-c-deep-blue"
							bg-color="bg-white"
						/>
					</div>
					<div
						class="flex items-center border-t border-white text-white pt-2 mt-3 gap-2"
					>
						<span>Entrusted:</span>
						<span class="text-lg font-medium">180.441,00 €</span>
					</div>
				</template>
			</ChartCard>
			<ChartCard
				title="Lot ID / Name"
				border-color="border-c-grey"
				icon-color="text-c-vivid-green"
				:simple-card="true"
			>
				<template #default>
					<div class="flex items-center gap-2">
						<span class="text-c-dark-blue text-xl font-medium"
							>Late Bank export #3</span
						>
						<div
							class="bg-c-grey-bg text-c-light-grey p-2 gap-2 rounded-full flex items-center"
						>
							<IconCalender class="w-4 h-4" />
							<span class="text-sm">11/10/2023</span>
						</div>
					</div>
				</template>
			</ChartCard>
			<ChartCard
				title="Profile"
				value="32 000,00 €"
				icon-color="text-c-vivid-green"
				border-color="border-c-grey"
				:simple-card="true"
			>
				<template #default>
					<div class="flex items-center gap-2">
						<span class="text-c-dark-blue text-xl font-medium"
							>CRV - RB1 RB001</span
						>
						<span class="text-sm text-c-dark-blue"
							>Casa di rispormio di Volterra S.P.A</span
						>
					</div>
				</template>
			</ChartCard>
			<ChartCard
				title="Pratice ID"
				border-color="border-c-grey"
				icon-color="text-c-vivid-green"
				:simple-card="true"
			>
				<template #default>
					<span class="text-c-dark-blue text-xl font-medium">494578</span>
				</template>
			</ChartCard>
			<ChartCard
				border-color="border-c-light-orange"
				icon-color="text-c-light-orange"
				bgPosition="left"
			>
				<template #default>
					<div class="flex items-center justify-center gap-2">
						<span class="text-c-light-orange text-2xl font-semibold">24</span>
						<Badge
							:percentage="30"
							text-color="text-white"
							bg-color="bg-c-light-orange"
							:icon="IconTrendingDown"
						/>
					</div>
					<span class="text-c-dark-blue text-sm text-center font-medium"
						>Negative dossiers</span
					>
				</template>
			</ChartCard>
		</div>`,
	});
};
