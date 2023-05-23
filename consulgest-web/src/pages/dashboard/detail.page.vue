<template>
	<div class="flex gap-8 items-start flex-col lg:flex-row">
		<div class="grid gap-6 w-full lg:w-2/3 xl:w-9/12">
			<div
				class="w-full flex flex-wrap 2xl:flex-nowrap gap-6 border-b border-b-c-grey pb-6"
			>
				<div class="w-full pt-4 flex flex-col gap-6 2xl:w-9/12">
					<CardHeader title="All dossier closure rate">
						<template #endTitle>
							<DatepickerInput
								input-class="test bg-c-ghost-white border-none w-36"
							/>
						</template>
					</CardHeader>
					<StackedBarChart :chart-data="chartData" class="w-full hello" />
				</div>
				<div
					class="w-full bg-c-linear p-4 rounded-xl flex flex-col gap-6 2xl:w-3/12"
				>
					<div class="flex items-center justify-center flex-col mt-2">
						<div class="relative">
							<PieChart
								:stroke-width="30"
								:diameter="210"
								:payload-values="pieChartTwoPayload"
							/>
							<div
								class="flex flex-col absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 text-c-dark-blue items-center"
							>
								<span class="text-3xl font-semibold">132</span>
								<span>dossiers</span>
							</div>
						</div>
					</div>
					<div class="flex flex-col gap-4">
						<ChartCard
							border-color="border-c-vivid-green"
							text-color="text-c-dark"
							icon-color="text-c-vivid-green"
						>
							<template #default>
								<div class="flex items-center justify-center gap-2">
									<span class="text-c-vivid-green text-2xl font-semibold"
										>92</span
									>
									<Badge
										:percentage="70"
										text-color="text-white"
										bg-color="bg-c-vivid-green"
										:icon="IconTrendingUp"
									/>
								</div>
								<span class="text-c-dark-blue text-sm text-center font-medium"
									>Positive dossiers</span
								>
							</template>
						</ChartCard>
						<ChartCard
							border-color="border-c-light-orange"
							icon-color="text-c-light-orange"
							bg-position="left"
						>
							<template #default>
								<div class="flex items-center justify-center gap-2">
									<span class="text-c-light-orange text-2xl font-semibold"
										>40</span
									>
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
					</div>
				</div>
			</div>
			<div class="w-full overflow-hidden">
				<CardHeader title="LOT list">
					<template #afterTitle>
						<div class="flex items-center gap-4 border-l border-c-coral-blue">
							<span
								class="badge text-white bg-c-deep-blue ml-4 px-4 h-9 border-none"
								>132</span
							>
						</div>
					</template>
					<template #endTitle>
						<Dropdown
							:label="t('dashboard.my_dashboard.table_card.filter_title')"
						>
							<DropdownItem>
								<span>{{
									t('dashboard.my_dashboard.table_card.filter_title')
								}}</span>
							</DropdownItem>
						</Dropdown>
					</template>
				</CardHeader>
				<div class="flex my-4 w-full overflow-auto pb-4">
					<Table
						:columns="columns"
						:data="data"
						:page="page"
						:page-size="pageSize"
						@row-click="rowClick"
					/>
				</div>
				<div class="text-end">
					<Pagination
						v-model="page"
						:total="totalPage.length"
						class="rounded-xl"
					/>
				</div>
			</div>
		</div>
		<div class="w-full grid gap-6 lg:w-2/6 xl:w-3/12">
			<ChartCard
				title="Acount collected"
				text-color="text-white"
				icon-color="text-white"
				bg-color="bg-c-linear-blue"
			>
				<template #default>
					<div class="flex items-center gap-2">
						<span class="text-white font-medium text-base xl:text-xl"
							>12,875 €</span
						>
						<Badge
							:percentage="10"
							text-color="text-c-deep-blue"
							bg-color="bg-white"
						/>
					</div>
					<div
						class="flex items-center border-t border-white text-white pt-2 mt-3 gap-2"
					>
						<span class="text-sm">Total debt amount:</span>
						<span class="font-medium text-base xl:text-lg">108,490 €</span>
					</div>
				</template>
			</ChartCard>
			<Card>
				<CardHeader title="Dificulty level">
					<template #endTitle>
						<Dropdown label="By Portfolio" class="bg-c-linear rounded-md">
							<DropdownItem>
								<span>{{
									t('dashboard.my_dashboard.pieChart_card.filter_title')
								}}</span>
							</DropdownItem>
						</Dropdown>
					</template>
				</CardHeader>
				<div class="flex items-center justify-center mt-9 flex-col gap-8">
					<div class="relative">
						<PieChart
							:stroke-width="30"
							:diameter="210"
							:payload-values="pieChartPayload"
						/>
						<div
							class="flex flex-col absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 text-c-dark-blue items-center"
						>
							<span class="text-3xl font-semibold">300</span>
							<span>Dossiers</span>
						</div>
					</div>
					<ChartList :columns="pieChartColumns" :show-item-dot="true" />
				</div>
			</Card>
			<Card class="flex flex-col gap-4">
				<CardHeader :title="t('dashboard.my_dashboard.barChart_card.title')">
					<template #endTitle>
						<Dropdown label="By Position">
							<DropdownItem>
								<span>{{
									t('dashboard.my_dashboard.barChart_card.filter_title')
								}}</span>
							</DropdownItem>
						</Dropdown>
					</template>
				</CardHeader>
				<div class="flex items-center justify-center flex-col gap-5">
					<BarChart :chart-data="barChartData" :height="237" />
					<ListCard
						title="Total positive conclusions"
						value="410"
						text-color="text-c-dark-blue"
						class="bg-c-linear w-full"
						:icon="IconBookOpen"
						:font-bold="true"
					/>
					<ChartList :columns="barChartColumns" :show-item-dot="true" />
				</div>
			</Card>
		</div>
	</div>
</template>

<script lang="ts" setup>
import { useI18n } from 'vue-i18n';
import { ref } from 'vue';
import Card from '../../components/card/card.component.vue';
import CardHeader from '../../components/card/card-header/card-header.component.vue';
import { IconTrendingUp, IconBookOpen, IconTrendingDown } from '../../icons';
import Badge from '../../components/badge/badge.component.vue';
import ChartCard from '../../components/chart-card/chart-card.component.vue';
import DatepickerInput from '../../components/datepicker/datepicker.component.vue';
import Dropdown from '../../components/dropdown/dropdown.component.vue';
import DropdownItem from '../../components/dropdown/dropdown-item.component.vue';
import BarChart from '../../components/bar-chart/bar-chart.component.vue';
import PieChart from '../../components/pie-circle/pie-circle.component.vue';
import Table from '../../components/table/table.component.vue';
import Pagination from '../../components/pagination/pagination.component.vue';
import { chunk } from '../../utils/chunk';
import ChartList from '../../components/chart-list/chart-list.component.vue';
import ListCard from '../../components/list-card/list-card.component.vue';
import StackedBarChart from '../../components/stacked-bar-chart/stacked-bar-chart.component.vue';
import { router } from '../../router';

const { t } = useI18n();

const page = ref(0);

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
const pageSize = 2;
const totalPage = chunk(data, pageSize);

const pieChartPayload = [
	{ color: '#072EF5', value: 250 },
	{ color: '#2AD7B3', value: 308 },
	{ color: '#EC7E0E', value: 520 },
	{ color: '#A955EB', value: 130 },
];

const pieChartTwoPayload = [
	{ color: '#0DE4E4', value: 528 },
	{ color: '#EC7E0E', value: 50 },
];

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

const barChartColumns = [
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

const pieChartColumns = [
	{
		label: 'Easy',
		value: '300',
		itemDotClass: 'bg-c-success',
	},
	{
		label: 'Normal',
		value: '1,000',
		itemDotClass: 'bg-c-deep-blue',
	},
	{
		label: 'Dificult',
		value: '260',
		itemDotClass: 'bg-c-purple',
	},
	{
		label: 'Hard',
		value: '300',
		itemDotClass: 'bg-c-warning',
	},
];
const chartData = {
	labels: ['Jan', 'Feb', 'March', 'Apr', 'May', 'June'],
	datasets: [
		{
			label: 'Negative',
			data: [40, 39, 20, 80, 59, 80, 40],
		},
		{
			label: 'Positive',
			data: [5, 36, 10, 40, 39, 30, 10],
		},
	],
};

function rowClick() {
	router.push('/dashboard/lot/1');
}
</script>

<style>
#bar-chart,
#line-chart {
	width: 100% !important;
	height: 100% !important;
}
</style>
