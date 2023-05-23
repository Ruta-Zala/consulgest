<template>
	<div class="flex gap-9 flex-col lg:flex-row">
		<div class="flex flex-col gap-6 w-full lg:w-8/12 xl:w-9/12">
			<div class="flex flex-col flex-wrap gap-4 lg:flex-row">
				<ChartCard
					class="w-auto"
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
					class="w-auto"
					title="Profile"
					border-color="border-c-grey"
					icon-color="text-c-vivid-green"
					:simple-card="true"
				>
					<template #default>
						<div class="flex items-center gap-2">
							<span class="text-c-dark-blue text-xl font-medium"
								>CRV - RB1 RB001</span
							>
							<span class="text-c-dark text-sm"
								>Casa di rispormio di Volterra S.P.A</span
							>
						</div>
					</template>
				</ChartCard>
				<ChartCard
					class="w-full lg:w-72"
					title="Pratice ID"
					border-color="border-c-grey"
					icon-color="text-c-vivid-green"
					:simple-card="true"
				>
					<template #default>
						<div class="flex items-center gap-2">
							<span class="text-c-dark-blue text-xl font-medium">494578</span>
						</div>
					</template>
				</ChartCard>
			</div>
			<div class="flex justify-between">
				<div class="flex flex-wrap items-center gap-3">
					<h3 class="text-c-dark-blue font-medium">Case Information</h3>
					<span
						class="text-c-deep-blue bg-c-linear px-4 py-1 rounded-3xl text-sm"
						>Re-entrusted</span
					>
					<button
						class="bg-c-vivid-green px-4 py-1 rounded-3xl text-white text-sm flex gap-2 items-center"
					>
						Case closed <input type="checkbox" />
					</button>
				</div>
				<IconDots class="h-8 w-8" />
			</div>
			<div
				class="grid grid-cols-1 gap-y-3 2xl:grid-cols-5 xl:grid-cols-3 md:grid-cols-2 md:gap-y-8"
			>
				<div class="flex flex-col gap-2 border-l px-4 py-1 border-l-c-grey">
					<div class="flex items-center gap-2">
						<IconUser class="h-4 w-4 text-c-light-grey" />
						<h6 class="text-sm text-c-light-grey">Debt Collector</h6>
					</div>
					<div class="flex items-center gap-2">
						<Avatar
							alt="image"
							src="https://picsum.photos/80/80"
							size="w-8 h-8"
						/>
						<h5 class="text-c-dark text-base">Sara Smith</h5>
					</div>
				</div>
				<div class="flex flex-col gap-2 border-l px-4 py-1 border-l-c-grey">
					<div class="flex items-center gap-2">
						<IconMoney class="h-4 w-4 text-c-light-grey" />
						<h6 class="text-sm text-c-light-grey">Debt collector custody</h6>
					</div>
					<h5 class="text-c-dark text-base">August, 12 2021</h5>
				</div>
				<div class="flex flex-col gap-2 border-l px-4 py-1 border-l-c-grey">
					<div class="flex items-center gap-2">
						<IconMoney class="h-4 w-4 text-c-light-grey" />
						<h6 class="text-sm text-c-light-grey">Debt collector deadline</h6>
					</div>
					<h5 class="text-c-dark text-base">August, 12 2021</h5>
				</div>
				<div class="flex flex-col gap-2 border-l px-4 py-1 border-l-c-grey">
					<div class="flex items-center gap-2">
						<IconMoney class="h-4 w-4 text-c-light-grey" />
						<h6 class="text-sm text-c-light-grey">Expiration</h6>
					</div>
					<h5 class="text-c-dark text-base">August, 12 2021</h5>
				</div>
				<div class="flex flex-col gap-2 border-l px-4 py-1 border-l-c-grey">
					<div class="flex items-center gap-2">
						<IconMoney class="h-4 w-4 text-c-light-grey" />
						<h6 class="text-sm text-c-light-grey">Transfer date</h6>
					</div>
					<h5 class="text-c-dark text-base">August, 12 2021</h5>
				</div>
				<div class="flex flex-col gap-2 border-l px-4 py-1 border-l-c-grey">
					<div class="flex items-center gap-2">
						<h6 class="text-sm text-c-light-grey">Temporary process</h6>
					</div>
					<h5 class="text-c-dark text-base">--</h5>
				</div>
				<div class="flex flex-col gap-2 border-l px-4 py-1 border-l-c-grey">
					<div class="flex items-center gap-2">
						<h6 class="text-sm text-c-light-grey">Backoffice status</h6>
					</div>
					<h5 class="text-c-dark text-base">--</h5>
				</div>
				<div class="flex flex-col gap-2 border-l px-4 py-1 border-l-c-grey">
					<div class="flex items-center gap-2">
						<h6 class="text-sm text-c-light-grey">Outcome code</h6>
					</div>
					<h5 class="text-c-dark text-base">16 - Payment received</h5>
				</div>
				<div class="flex flex-col gap-2 border-l px-4 py-1 border-l-c-grey">
					<div class="flex items-center gap-2">
						<h6 class="text-sm text-c-light-grey">last Status</h6>
					</div>
					<h5 class="text-c-dark text-base">Payment received</h5>
				</div>
				<div
					class="flex flex-col gap-2 border-l items-start px-4 py-1 border-l-c-grey"
				>
					<div class="flex items-center gap-2">
						<h6 class="text-sm text-c-light-grey">Status</h6>
					</div>
					<span
						class="text-c-vivid-green bg-c-vivid-green bg-opacity-5 text-sm font-semibold px-4 py-1 rounded-3xl text-start md:text-base"
					>
						CS-Positiva
					</span>
				</div>
			</div>
			<Card class="flex flex-col gap-6">
				<CardHeader title="Debt breakdown" />
				<LineChart
					class="flex-1 max-h-72"
					:chart-data="lineChartData"
					y-title="% pickup rate"
					x-title="time (hours)"
				/>
				<div class="flex gap-14">
					<div class="flex items-center gap-2">
						<span class="bg-c-deep-blue w-2.5 h-2.5 block rounded-full"></span>
						<span class="text-c-dark-blue text-sm">Debt</span>
					</div>
					<div class="flex items-center gap-2">
						<span
							class="bg-c-light-orange w-2.5 h-2.5 block rounded-full"
						></span>
						<span class="text-c-dark-blue text-sm">Cached</span>
					</div>
					<div class="flex items-center gap-2">
						<span class="bg-c-success w-2.5 h-2.5 block rounded-full"></span>
						<span class="text-c-dark-blue text-sm">Residue</span>
					</div>
					<div class="flex items-center gap-2">
						<span class="bg-c-purple w-2.5 h-2.5 block rounded-full"></span>
						<span class="text-c-dark-blue text-sm">Promises</span>
					</div>
				</div>
			</Card>
			<div class="flex flex-col gap-6">
				<CardHeader title="Contacts sources"></CardHeader>
				<div class="flex flex-col flex-nowrap gap-6 md:flex-row md:flex-wrap">
					<Card class="p-4 w-full md:w-72">
						<div class="flex justify-between items-center mb-6">
							<div class="flex items-center gap-3">
								<IconPhone class="h-4 w-4 text-c-light-grey" />
								<span class="text-sm text-c-dark-blue">Phone</span>
								<button
									class="text-sm border border-c-vivid-green py-1 px-2.5 text-c-dark-blue rounded-3xl flex gap-2 items-center"
								>
									<span
										class="w-3 h-3 bg-c-success inline-block rounded-full"
									></span>
									Active
								</button>
							</div>
							<IconDots class="h-8 w-8" />
						</div>
						<div class="flex flex-col gap-3">
							<span class="text-c-dark-blue text-lg mb-4">+00 05854322330</span>
							<p class="text-c-dark-blue text-sm">
								Do not call this number at night.Phone provided by the mother
							</p>
							<div class="flex gap-2">
								<span
									class="border border-c-light-grey text-sm inline-block text-c-light-grey py-1 px-4 rounded-3xl"
									>SmS</span
								>
								<span
									class="border border-c-light-grey text-sm inline-block text-c-light-grey py-1 px-4 rounded-3xl"
									>Call</span
								>
								<span
									class="border border-c-light-grey text-sm inline-block text-c-light-grey py-1 px-4 rounded-3xl"
									>Call</span
								>
							</div>
							<button
								class="bg-c-linear h-9 text-c-dark-blue flex justify-between items-center px-4 rounded-lg text-sm"
							>
								Calls done <span>32</span>
							</button>
						</div>
					</Card>
					<Card class="p-4 w-full md:w-72">
						<div class="flex justify-between items-center mb-6">
							<div class="flex items-center gap-3">
								<IconPhone class="h-4 w-4 text-c-light-grey" />
								<span class="text-sm text-c-dark-blue">Phone</span>
								<button
									class="text-sm border border-c-pink py-1 px-2.5 text-c-dark-blue rounded-3xl flex gap-2 items-center"
								>
									<span
										class="w-3 h-3 bg-c-pink inline-block rounded-full"
									></span>
									Dead
								</button>
							</div>
							<IconDots class="h-8 w-8" />
						</div>
						<div class="flex flex-col gap-3">
							<span class="text-c-dark-blue text-lg mb-4">+00 0585432543</span>
							<p class="text-c-dark-blue text-sm">No awser after 20 calls</p>
							<div class="flex gap-2">
								<span
									class="border border-c-light-grey text-sm inline-block text-c-light-grey py-1 px-4 rounded-3xl"
									>SmS</span
								>
							</div>
							<button
								class="bg-c-linear h-9 text-c-dark-blue flex justify-between items-center px-4 rounded-lg text-sm"
							>
								Calls done <span>20</span>
							</button>
						</div>
					</Card>
					<Card class="p-4 w-full md:w-72">
						<div class="flex justify-between items-center mb-6">
							<div class="flex items-center gap-3">
								<IconMail class="h-4 w-4 text-c-light-grey" />
								<span class="text-sm text-c-dark-blue">Email</span>
								<button
									class="text-sm border border-c-vivid-green py-1 px-2.5 text-c-dark-blue rounded-3xl flex gap-2 items-center"
								>
									<span
										class="w-3 h-3 bg-c-success inline-block rounded-full"
									></span>
									Active
								</button>
							</div>
							<IconDots class="h-8 w-8" />
						</div>
						<div class="flex flex-col gap-3">
							<span class="text-c-dark-blue text-lg mb-4"
								>josh.a.s@email.io</span
							>
							<p class="text-c-dark-blue text-sm">Some emails bounce</p>
							<button
								class="bg-c-linear h-9 text-c-dark-blue flex justify-between items-center px-4 rounded-lg text-sm"
							>
								Emails sent <span>100</span>
							</button>
						</div>
					</Card>
				</div>
			</div>
		</div>
		<div class="flex flex-col gap-6 w-full lg:w-4/12 xl:w-3/12">
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
			<Card
				class="relative border-c-deep-blue gap-4 flex flex-col items-center"
			>
				<Avatar
					alt="image"
					src="https://picsum.photos/80/80"
					size="w-20 h-20"
				/>
				<div>
					<span class="text-xl font-medium text-c-dark-blue"
						>Josh Anderson Smith</span
					>
					<div
						class="text-c-dark flex justify-center items-center mt-2 text-sm"
					>
						<IconBook class="h-4 w-4 mr-2 text-c-dark-blue" /> CRV - RB1 RB001
					</div>
				</div>
				<div class="w-full">
					<div
						class="flex justify-between text-sm border-b border-c-coral-blue pb-2.5"
					>
						<span class="text-c-light-grey flex items-center gap-2">
							<IconUser class="h-5 w-5" />Age</span
						><span class="text-c-dark-blue">32</span>
					</div>
					<div
						class="flex justify-between text-sm border-b border-c-coral-blue py-2.5"
					>
						<span class="text-c-light-grey flex items-center gap-2"
							><IconLocation class="h-5 w-5" /> Location</span
						><span class="text-c-dark-blue">Italy</span>
					</div>
					<div class="flex justify-between text-sm pt-2.5">
						<span class="text-c-light-grey flex items-center gap-2">
							<IconMail class="h-5 w-5" /> Email</span
						><span class="text-c-dark-blue">josh.a.s@email.io</span>
					</div>
				</div>
				<div
					class="bg-c-linear flex justify-center rounded-lg items-center gap-3 py-2.5 text-center text-c-deep-blue w-full"
				>
					<IconPhone class="w-5 h-5" />
					<span class="text-sm">+305 5551 55884</span>
				</div>
				<button
					class="flex w-full justify-center items-center gap-3.5 text-c-light-grey"
				>
					<IconDropdown class="w-4 h-4" />
					<span class="text-xs uppercase tracking-widest"
						>View all details</span
					>
				</button>
			</Card>
			<Card class="flex flex-col gap-4">
				<CardHeader title="Collector assinged">
					<template #endTitle>
						<IconDots class="h-8 w-8 text-c-coral-blue" />
					</template>
				</CardHeader>
				<div class="flex gap-4 items-center">
					<Avatar
						alt="image"
						src="https://picsum.photos/80/80"
						size="h-14 w-14"
					/>
					<div class="flex flex-col gap-1">
						<h5 class="text-c-dark-blue text-lg font-medium">Sara Smith</h5>
						<span class="text-c-light-grey text-sm">+000 000 000</span>
					</div>
				</div>
				<div class="w-full">
					<div
						class="flex justify-between text-sm border-b border-c-coral-blue py-2.5 pr-4"
					>
						<div class="flex items-center gap-2.5">
							<IconPhone class="h-4 w-4 text-c-dark-blue" />
							<span class="text-c-dark-blue">Phone call</span>
						</div>
						<span class="text-c-deep-blue font-semibold">80%</span>
					</div>
					<div
						class="flex justify-between text-sm border-b border-c-coral-blue py-2.5 pr-4"
					>
						<div class="flex items-center gap-2.5">
							<IconMail class="h-4 w-4 text-c-dark-blue" />
							<span class="text-c-dark-blue">Email</span>
						</div>
						<span class="text-c-deep-blue font-semibold">10%</span>
					</div>
					<div class="flex justify-between text-sm pt-2.5 pr-4">
						<div class="flex items-center gap-2.5">
							<IconUser class="h-4 w-4 text-c-dark-blue" />
							<span class="text-c-dark-blue">Personal</span>
						</div>
						<span class="text-c-deep-blue font-semibold">10%</span>
					</div>
				</div>
			</Card>
			<Card class="flex gap-7 flex-col">
				<CardHeader title="Profile Notes" />
				<p class="text-c-light-grey">
					This person is very temperamental and tends to be agressive on phone.
					Please address it carefully.
				</p>
			</Card>
			<Card>
				<CardHeader :title="t('dossiers.detail.pie_chart.title')" />
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
import ChartCard from '../../../components/chart-card/chart-card.component.vue';
import Badge from '../../../components/badge/badge.component.vue';
import Avatar from '../../../components/avatar/avatar.component.vue';
import Card from '../../../components/card/card.component.vue';
import CardHeader from '../../../components/card/card-header/card-header.component.vue';
import PieChart from '../../../components/pie-circle/pie-circle.component.vue';
import ChartList from '../../../components/chart-list/chart-list.component.vue';
import ListCard from '../../../components/list-card/list-card.component.vue';
import LineChart from '../../../components/line-chart/line-chart.component.vue';
import {
	IconPhone,
	IconBook,
	IconUser,
	IconLocation,
	IconDropdown,
	IconDots,
	IconMail,
	IconCalender,
	IconMoney,
} from '../../../icons';

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
const pieChartPayload = [
	{ color: '#072EF5', value: 250 },
	{ color: '#2AD7B3', value: 308 },
	{ color: '#EC7E0E', value: 520 },
	{ color: '#A955EB', value: 130 },
];
</script>
