<template>
	<div class="flex gap-6 items-start flex-col lg:flex-row">
		<div class="grid gap-6 w-full lg:w-8/12 xl:w-10/12">
			<div class="grid grid-cols-1 gap-4 md:grid-cols-2 xl:grid-cols-4">
				<ChartCard
					title="Phone Collection"
					border-color="border-c-deep-blue"
					text-color="text-c-dark"
					icon-color="text-c-deep-blue"
				>
					<template #default>
						<div class="flex items-center gap-2">
							<span class="text-c-dark text-xl font-medium">32 000,00 €</span>
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
					title="Email Collection"
					border-color="border-c-purple"
					text-color="text-c-dark"
					icon-color="text-c-purple"
				>
					<template #default>
						<div class="flex items-center gap-2">
							<span class="text-c-dark text-xl font-medium">32 000,00 €</span>
							<Badge
								:percentage="20"
								:icon="IconTrendingUp"
								text-color="text-white"
								bg-color="bg-c-purple"
							/>
						</div>
					</template>
				</ChartCard>
				<ChartCard
					title="Total Collected"
					border-color="border-c-vivid-green"
					text-color="text-c-dark"
					icon-color="text-c-vivid-green"
				>
					<template #default>
						<div class="flex items-center gap-2">
							<span class="text-c-dark text-xl font-medium">32 000,00 €</span>
							<Badge
								:percentage="20"
								:icon="IconTrendingDown"
								text-color="text-white"
								bg-color="bg-c-vivid-green"
							/>
						</div>
					</template>
				</ChartCard>
				<ChartCard
					title="Remaining collection"
					border-color="border-c-light-orange"
					text-color="text-c-dark"
					icon-color="text-c-light-orange"
				>
					<template #default>
						<div class="flex items-center gap-2">
							<span class="text-c-dark text-xl font-medium">32 000,00 €</span>
							<Badge
								:percentage="20"
								:icon="IconTrendingUp"
								text-color="text-white"
								bg-color="bg-c-light-orange"
							/>
						</div>
					</template>
				</ChartCard>
			</div>
			<div class="grid grid-cols-1 gap-4 xl:grid-cols-2">
				<Card class="flex flex-col gap-4 p-4 shadow-none">
					<CardHeader :title="t('dossiers.detail.line_chart.title')">
						<template #afterTitle>
							<Dropdown label="Time">
								<DropdownItem>
									<span>Time</span>
								</DropdownItem>
							</Dropdown>
						</template>
						<template #endTitle>
							<Dropdown label="Phone Calls">
								<DropdownItem>
									<span>Phone Calls</span>
								</DropdownItem>
							</Dropdown>
						</template>
					</CardHeader>
					<div class="flex-1 w-full gap-4 flex flex-col">
						<LineChart
							class="flex-1 max-h-72"
							:chart-data="lineChartData"
							y-title="% pickup rate"
							x-title="time (hours)"
						/>
						<ChartList :columns="lineData" :show-item-dot="true"></ChartList>
					</div>
				</Card>
				<Card class="flex flex-col gap-4 p-4 shadow-none">
					<CardHeader :title="t('dossiers.detail.bar_chart.title')">
						<template #endTitle>
							<Dropdown label="By Position">
								<DropdownItem>
									<span>By Position</span>
								</DropdownItem>
							</Dropdown>
						</template>
					</CardHeader>
					<div class="w-full gap-4 flex flex-col">
						<BarChart :chart-data="barChartData" class="max-h-72" />
						<ListCard
							title="Total conclusions"
							value="140"
							text-color="text-c-dark-blue"
							bg-color="bg-c-dark-blue"
							:icon="IconBookOpen"
							:font-bold="true"
						/>
						<ChartList :columns="barData" :show-item-dot="true"></ChartList>
					</div>
				</Card>
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
						<Dropdown label="Status">
							<DropdownItem>
								<span>Status</span>
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
								<label for="" class="flex items-center justify-center ml-auto">
									<input
										type="checkbox"
										class="w-[18px] h-[18px] rounded checkbox"
									/>
								</label>
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
			<div class="relative border border-c-deep-blue rounded-xl p-4">
				<div class="gap-4 flex flex-col items-center">
					<Avatar
						alt="image"
						src="https://picsum.photos/80/80"
						size="w-20 h-20"
					/>
					<div class="text-center">
						<span class="text-xl font-medium text-c-dark-blue"
							>Josh Anderson Smith</span
						>
						<span
							class="text-c-dark flex justify-center items-center mt-2 text-sm"
						>
							<IconBook class="h-4 w-4 mr-2 text-c-dark-blue" /> CRV - RB1 RB001
						</span>
					</div>
					<div class="w-full">
						<div
							class="flex justify-between text-sm border-b border-c-coral-blue pb-2"
						>
							<span class="text-c-light-grey">Age</span
							><span class="text-c-dark-blue">32</span>
						</div>
						<div
							class="flex justify-between text-sm border-b border-c-coral-blue py-2"
						>
							<span class="text-c-light-grey">Location</span
							><span class="text-c-dark-blue">Italy</span>
						</div>
						<div class="flex justify-between text-sm pt-2">
							<span class="text-c-light-grey">Email</span
							><span class="text-c-dark-blue">josh.a.s@email.io</span>
						</div>
					</div>
					<div
						class="bg-c-linear flex justify-center rounded-lg items-center gap-3 py-2 text-center text-c-deep-blue w-full"
					>
						<IconPhone class="w-5 h-5" />
						<span class="text-sm">+305 5551 55884</span>
					</div>
					<div>
						<button
							class="flex w-full justify-center items-center gap-3 text-c-light-grey"
						>
							<IconDropdown class="w-4" />
							<span class="text-xs uppercase tracking-widest"
								>View all details</span
							>
						</button>
					</div>
				</div>
			</div>
			<div
				class="border flex flex-col gap-4 border-c-coral-blue rounded-xl p-4"
			>
				<div class="flex justify-between items-center">
					<h3 class="text-c-dark-blue text-sm">Main collector</h3>
					<IconDots class="h-8 w-8" />
				</div>
				<div class="flex gap-4 items-center">
					<Avatar
						alt="image"
						src="https://picsum.photos/52/42"
						size="w-14 h-14"
					/>
					<div class="flex flex-col gap-1">
						<h5 class="text-c-dark-blue text-lg font-medium">Sara Smith</h5>
						<span class="text-c-light-grey block text-sm">+000 000 000</span>
					</div>
				</div>
				<div>
					<div
						class="flex justify-between text-sm border-b border-c-coral-blue py-2 pr-4"
					>
						<div class="flex items-center gap-2">
							<span>
								<IconPhone class="h-4 w-4 text-c-dark-blue" />
							</span>
							<span class="text-c-dark-blue">Phone call</span>
						</div>
						<span class="text-c-deep-blue font-semibold">20</span>
					</div>
					<div
						class="flex justify-between text-sm border-b border-c-coral-blue py-2 pr-4"
					>
						<div class="flex items-center gap-2">
							<span>
								<IconMail class="h-4 w-4 text-c-dark-blue" />
							</span>
							<span class="text-c-dark-blue">Email</span>
						</div>
						<span class="text-c-deep-blue font-semibold">30</span>
					</div>
					<div class="flex justify-between text-sm py-2 pr-4">
						<div class="flex items-center gap-2">
							<span>
								<IconUser class="h-4 w-4 text-c-dark-blue" />
							</span>
							<span class="text-c-dark-blue">Personal</span>
						</div>
						<span class="text-c-deep-blue font-semibold">0</span>
					</div>
				</div>
				<div
					class="bg-c-linear flex justify-between px-4 rounded-lg items-center gap-3 py-2 text-center"
				>
					<div class="flex items-center gap-2">
						<span
							class="bg-c-deep-blue text-white h-6 flex justify-center items-center w-9 text-sm rounded-3xl"
							>03</span
						>
						<span class="text-sm text-c-dark-blue">Other collectors</span>
					</div>
					<span>
						<IconDropdown class="h-3 w-3 text-c-deep-blue rotate-180" />
					</span>
				</div>
				<div class="w-full flex items-center justify-between">
					<div class="flex items-center gap-4">
						<Avatar
							alt="image"
							src="https://picsum.photos/52/42"
							size="w-8 h-8"
						/>
						<div class="flex flex-col">
							<span class="text-c-dark-blue text-sm block">Hanna Martin</span>
							<span class="text-c-light-grey text-sm">Phone call</span>
						</div>
					</div>
					<span
						class="bg-c-linear text-sm text-c-light-grey font-semibold rounded-3xl w-6 h-6 flex items-center justify-center"
						>2</span
					>
				</div>
			</div>
			<Card>
				<CardHeader :title="t('dossiers.detail.pie_chart.title')"> </CardHeader>
				<div class="flex gap-4 flex-col mt-4">
					<div class="flex justify-center relative">
						<PieChart
							:stroke-width="14"
							:diameter="210"
							:payload-values="pieChartPayload"
						/>
						<div
							class="absolute top-2/4 left-2/4 -translate-x-2/4 -translate-y-2/4 flex flex-col items-center text-c-dark-blue"
						>
							<span class="text-2xl font-semibold">Easy</span>
							<span class="text-sm">Dossier</span>
						</div>
					</div>
					<ListCard
						title="Time"
						value="90 days"
						text-color="text-c-dark-blue"
						bg-color="bg-c-dark-blue"
						:icon="IconCalender"
					/>
					<ChartList :columns="pieData" :show-item-dot="true"></ChartList>
				</div>
			</Card>
		</div>
	</div>
</template>

<script lang="ts" setup>
import { useI18n } from 'vue-i18n';
import Card from '../../../components/card/card.component.vue';
import CardHeader from '../../../components/card/card-header/card-header.component.vue';
import {
	IconBook,
	IconCalender,
	IconBookOpen,
	IconCpu,
	IconTrendingDown,
	IconTrendingUp,
	IconPhone,
	IconDropdown,
	IconDots,
	IconUser,
	IconMail,
	IconBackgroundGradient,
	IconArrowAlt,
} from '../../../icons';
import Dropdown from '../../../components/dropdown/dropdown.component.vue';
import DropdownItem from '../../../components/dropdown/dropdown-item.component.vue';
import LineChart from '../../../components/line-chart/line-chart.component.vue';
import BarChart from '../../../components/bar-chart/bar-chart.component.vue';
import PieChart from '../../../components/pie-circle/pie-circle.component.vue';
import ChartCard from '../../../components/chart-card/chart-card.component.vue';
import Avatar from '../../../components/avatar/avatar.component.vue';
import ChartList from '../../../components/chart-list/chart-list.component.vue';
import ListCard from '../../../components/list-card/list-card.component.vue';
import Badge from '../../../components/badge/badge.component.vue';

const { t } = useI18n();

const pieData = [
	{
		label: 'Calls',
		value: '23',
		itemDotClass: 'bg-c-vivid-green',
	},
	{
		label: 'Collected',
		value: '15 954,766€',
		itemDotClass: 'bg-c-deep-blue',
	},
	{
		label: 'Emails',
		value: '32',
		itemDotClass: 'bg-c-warning',
	},
];
const barData = [
	{
		label: 'Phone Collection',
		value: '200',
		itemDotClass: 'bg-c-success',
	},
	{
		label: 'Pre-decaying loans',
		value: '70',
		itemDotClass: 'bg-c-deep-blue',
	},
	{
		label: 'Post-decaying loans',
		value: '110',
		itemDotClass: 'bg-c-purple',
	},
	{
		label: 'Non performing loans (NPL)',
		value: '30',
		itemDotClass: 'bg-c-warning',
	},
];
const lineData = [
	{
		label: 'Number of calls',
		value: '200',
		itemDotClass: 'bg-c-deep-blue',
	},
	{
		label: 'Success rate',
		value: '70',
		itemDotClass: 'bg-c-success',
	},
	{
		label: 'Pickut rate',
		value: '15%',
		itemDotClass: 'bg-c-warning',
	},
];

const commonObj = {
	tension: 0.4,
	pointRadius: 0,
	borderWidth: 4,
	pointHoverRadius: 8,
	pointBorderColor: '#fff',
};
const lineChartData = {
	labels: ['8am', '10am', '12am', '2pm', '4pm', '6pm', '8pm', '10pm'],
	datasets: [
		{
			label: t('dossiers.detail.line_chart.data.data_one'),
			borderColor: ['#072EF5'],
			data: [0, 20, 25, 75, 50, 0, 58, 33],
			fill: true,
			backgroundColor: 'rgba(224, 224, 224, 0.3)',
			pointBackgroundColor: '#072EF5',
			...commonObj,
		},
		{
			label: t('dossiers.detail.line_chart.data.data_two'),
			borderColor: ['#2AD7B3'],
			data: [10, 20, 30, 40, 50, 60, 100],
			pointBackgroundColor: '#2AD7B3',
			...commonObj,
		},
		{
			label: t('dossiers.detail.line_chart.data.data_three'),
			borderColor: ['#A955EB'],
			data: [20, 20, 10, 23, 59, 1, 4, 32],
			pointBackgroundColor: '#A955EB',
			...commonObj,
		},
	],
};

const barChartData = {
	labels: [
		t('category.category_one'),
		t('category.category_two'),
		t('category.category_three'),
		t('category.category_four'),
	],
	datasets: [
		{
			backgroundColor: ['#072EF5', '#2AD7B3', '#A955EB', '#EC7E0E'],
			borderRadius: 10,
			data: [300, 120, 89, 3],
		},
	],
};

const pieChartPayload = [
	{ color: '#072EF5', value: 250 },
	{ color: '#2AD7B3', value: 308 },
	{ color: '#EC7E0E', value: 520 },
	{ color: '#A955EB', value: 130 },
];
</script>
