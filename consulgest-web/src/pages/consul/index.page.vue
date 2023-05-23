<template>
	<div class="flex gap-6 flex-col">
		<div class="flex flex-col gap-2">
			<span>Bank portfolio:</span>
			<div class="flex gap-8 items-center">
				<button
					class="px-4 py-2 rounded-md w-full gap-2 flex flex-row items-center justify-between text-c-dark-blue bg-c-ghost-white"
				>
					<span>CSV #543544 - Regionato Bank</span>
					<span>
						<IconDropdown class="w-3 h-3" />
					</span>
				</button>
				<div
					class="flex gap-4 border border-c-input-grey rounded-md px-4 py-3 text-c-dark"
				>
					<span>Dossiers:</span>
					<span class="font-semibold">1000</span>
				</div>
			</div>
		</div>
		<hr class="border-c-grey" />
		<div class="flex flex-row gap-6 items-start">
			<div class="grid gap-6 w-full lg:w-8/12 xl:w-10/12">
				<div class="flex flex-col gap-4 shadow-none">
					<CardHeader title="Stopped cash balance">
						<template #endTitle>
							<DatepickerInput
								input-class="bg-c-ghost-white border-none w-36"
							/>
						</template>
					</CardHeader>
					<div class="flex-1 w-full gap-4 flex flex-col">
						<LineBarChart class="flex-1 max-h-72" :chart-data="lineData" />
						<div class="flex gap-14">
							<div class="flex items-center gap-2">
								<span
									class="bg-c-vivid-green w-2.5 h-2.5 block rounded-full"
								></span>
								<span class="text-c-dark-blue text-sm"
									>Stopped cash balance</span
								>
							</div>
							<div class="flex items-center gap-2">
								<span
									class="bg-c-deep-blue w-2.5 h-2.5 block rounded-full"
								></span>
								<span class="text-c-dark-blue text-sm">Amount Collected</span>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="grid gap-6 w-full lg:w-4/12 xl:w-2/12">
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
					title="Cash Balance KPI"
					border-color="border-c-vivid-green"
					text-color="text-c-dark"
					icon-color="text-c-vivid-green"
				>
					<template #default>
						<div class="flex items-center gap-2">
							<span class="text-c-vivid-green text-2xl font-semibold">2%</span>
							<Badge
								:icon="IconTrendingUp"
								text-color="text-white"
								bg-color="bg-c-vivid-green"
							/>
						</div>
					</template>
				</ChartCard>
				<ChartCard
					title="Current Instalments number:"
					border-color="border-c-grey"
					icon-color="text-c-vivid-green"
					:simple-card="true"
				>
					<template #default>
						<span class="text-c-dark-blue text-xl font-medium">1</span>
					</template>
				</ChartCard>
			</div>
		</div>
		<div class="flex flex-col flex-wrap gap-4">
			<div class="flex flex-col justify-between lg:flex-row">
				<div class="flex items-center text-c-dark-blue gap-2">
					<IconCpu class="h-8 w-8" />
					<div class="text-lg font-medium">IA Suggestions & Actions</div>
					<span
						class="bg-c-deep-blue text-white h-6 flex justify-center items-center w-9 text-sm rounded-3xl"
						>03</span
					>
				</div>
				<div class="flex gap-2 items-center">
					<div class="flex gap-2 items-center">
						<div
							class="cursor-pointer border border-current text-c-input-grey rounded-full w-8 h-8 flex items-center justify-center"
						>
							<IconArrowAlt class="h-4 w-4 rotate-180" />
						</div>
						<div
							class="cursor-pointer border border-current text-c-dark-blue rounded-full w-8 h-8 flex items-center justify-center"
						>
							<IconArrowAlt class="h-4 w-4" />
						</div>
					</div>
					<Dropdown label="Action">
						<DropdownItem>
							<span>Action</span>
						</DropdownItem>
					</Dropdown>
					<Dropdown label="Easy level">
						<DropdownItem>
							<span>Easy level</span>
						</DropdownItem>
					</Dropdown>
					<Dropdown label="Success rate">
						<DropdownItem>
							<span>Success rate</span>
						</DropdownItem>
					</Dropdown>
				</div>
			</div>
			<div class="flex flex-wrap gap-4">
				<div class="grid grid-cols-2 mt-6">
					<div
						class="border border-c-grey flex flex-col items-center gap-4 p-4 rounded-lg"
					>
						<div class="flex gap-2 mb-0 w-full items-center">
							<IconCpu class="h-5 w-5 text-c-deep-blue" />
							<h5 class="text-c-dark-blue">Suggested action</h5>
						</div>
						<span class="bg-c-linear p-5 rounded-3xl">
							<IconPhone class="h-6 m-auto text-c-deep-blue" />
						</span>
						<div class="flex gap-2 items-center">
							<h3 class="text-c-dark-blue text-lg">Phone Call</h3>
							<span
								class="border border-c-vivid-green bg-c-light-green text-c-vivid-green px-4 py-0 rounded-3xl font-semibold"
								>60%</span
							>
						</div>
						<div
							class="relative w-full gap-1 flex flex-col overflow-hidden px-4 py-2 border rounded-lg border-c-vivid-green"
						>
							<IconBackgroundGradient
								class="absolute right-0 bottom-0 h-full text-c-vivid-green"
							/>
							<div class="text-sm text-c-dark-blue">
								Potential action result
							</div>
							<div
								class="text-c-dark-blue flex gap-2 items-center text-lg font-medium"
							>
								+ 20.000,00 €
								<span
									class="text-sm text-c-deep-blue bg-c-linear py-1 px-3 rounded-3xl"
									>+5% KPI</span
								>
							</div>
						</div>
						<div
							class="bg-c-linear gap-2 w-full rounded-lg p-2 flex justify-between"
						>
							<h5 class="text-c-dark-blue text-sm">Suggested collectors</h5>
							<span
								class="text-white text-sm bg-c-deep-blue px-2 py-0 rounded-3xl"
								>03</span
							>
						</div>
						<div class="w-full flex items-center justify-between">
							<div class="flex items-center gap-4">
								<Avatar
									alt="image"
									src="https://picsum.photos/36/36"
									size="w-8 h-8"
								/>
								<span class="text-c-dark-blue text-sm">Hanna Martin</span>
							</div>
							<span
								class="bg-c-linear inline-block px-2 text-sm text-c-dark-blue py-0 rounded-3xl"
								>80%</span
							>
						</div>
						<div class="w-full flex items-center justify-between">
							<div class="flex items-center gap-4">
								<Avatar
									alt="image"
									src="https://picsum.photos/36/36"
									size="w-8 h-8"
								/>
								<span class="text-c-dark-blue text-sm">John Petter</span>
							</div>
							<span
								class="bg-c-linear inline-block px-2 text-sm text-c-dark-blue py-0 rounded-3xl"
								>76%</span
							>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script lang="ts" setup>
import CardHeader from '../../components/card/card-header/card-header.component.vue';
import {
	IconCpu,
	IconPhone,
	IconBackgroundGradient,
	IconArrowAlt,
	IconTrendingUp,
	IconDropdown,
} from '../../icons';
import Dropdown from '../../components/dropdown/dropdown.component.vue';
import DropdownItem from '../../components/dropdown/dropdown-item.component.vue';
import DatepickerInput from '../../components/datepicker/datepicker.component.vue';
import LineBarChart from '../../components/line-bar-chart/line-bar-chart.component.vue';
import ChartCard from '../../components/chart-card/chart-card.component.vue';
import Avatar from '../../components/avatar/avatar.component.vue';
import Badge from '../../components/badge/badge.component.vue';

const lineData = {
	labels: ['01', '02', '03', '04'],
	datasets: [
		{
			label: 'Dataset 1',
			data: [60, 20, 30, 400],
		},
		{
			label: 'Dataset 2',
			data: [120, 230, 400, 500, 600],
		},
	],
};
</script>
