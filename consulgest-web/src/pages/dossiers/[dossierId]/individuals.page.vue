<template>
	<div class="flex gap-9 flex-col lg:flex-row">
		<div class="flex flex-col gap-10 w-full lg:w-8/12 xl:w-9/12">
			<div class="flex flex-col gap-10">
				<CardHeader title="Debtors">
					<template #afterTitle>
						<div class="flex items-center gap-4 border-l border-c-coral-blue">
							<span
								class="badge text-white bg-c-deep-blue ml-4 px-4 h-9 border-none"
								>01</span
							>
						</div>
					</template>
				</CardHeader>
				<Card class="flex flex-col gap-6 border-c-light-orange sm:p-4 md:p-6">
					<div class="flex justify-between items-start">
						<ul class="flex flex-wrap items-center gap-4 md:gap-2">
							<li>
								<Avatar
									alt="image"
									src="https://picsum.photos/80/80"
									size="w-8 h-8"
								/>
							</li>
							<li>
								<p class="text-c-dark-blue text-sm font-medium xl:text-lg">
									Conte Grande di Luxuro Luigi e C. Societa'in Accomoandita
									Semplice
								</p>
							</li>
							<li>
								<a
									href="#"
									class="bg-c-light-yellow h-7 w-20 text-c-warning font-semibold text-sm flex justify-center items-center rounded-3xl px-2"
									>Debtor</a
								>
							</li>
							<li>
								<a
									href="#"
									class="h-7 w-20 bg-c-light-green flex items-center justify-center text-sm rounded-xl text-c-success font-semibold"
									>Active</a
								>
							</li>
						</ul>
						<IconDots class="h-8 w-8" />
					</div>
					<div
						class="grid grid-cols-1 gap-y-3 sm:gap-y-4 sm:grid-cols-2 lg:grid-cols-3 2xl:grid-cols-5"
					>
						<div class="flex flex-col gap-2 px-4 py-1">
							<div class="flex items-center gap-2">
								<IconCalender class="h-4 w-4 text-c-light-grey" />
								<h6 class="text-sm text-c-light-grey">Birthdate</h6>
							</div>
							<div class="flex items-center gap-2">
								<h5 class="text-c-dark-black text-sm md:text-base">
									August, 12 2021
								</h5>
							</div>
						</div>
						<div class="flex flex-col gap-2 border-l px-4 py-1 border-l-c-grey">
							<div class="flex items-center gap-2">
								<IconLocation class="h-4 w-4 text-c-light-grey" />
								<h6 class="text-sm text-c-light-grey">Birth Location</h6>
							</div>
							<h5 class="text-c-dark-black text-sm md:text-base">Italy</h5>
						</div>
						<div class="flex flex-col gap-2 border-l px-4 py-1 border-l-c-grey">
							<div class="flex items-center gap-2">
								<IconCalender class="h-4 w-4 text-c-light-grey" />
								<h6 class="text-sm text-c-light-grey">Dead date</h6>
							</div>
							<h5 class="text-c-dark-black text-sm md:text-base">--</h5>
						</div>
						<div class="flex flex-col gap-2 border-l px-4 py-1 border-l-c-grey">
							<div class="flex items-center gap-2">
								<IconLocation class="h-4 w-4 text-c-light-grey" />
								<h6 class="text-sm text-c-light-grey">IVA number</h6>
							</div>
							<h5 class="text-c-dark-black text-sm md:text-base">
								543234564333
							</h5>
						</div>
						<div class="flex flex-col gap-2 border-l px-4 py-1 border-l-c-grey">
							<div class="flex items-center gap-2">
								<IconPhone class="h-4 w-4 text-c-light-grey" />
								<h6 class="text-sm text-c-light-grey">Phone number</h6>
							</div>
							<h5 class="text-c-dark-black text-sm md:text-base">
								543234564333
							</h5>
						</div>
					</div>
					<div class="flex flex-col gap-4">
						<div class="flex items-center justify-between">
							<span class="flex items-center gap-2 text-c-light-grey text-sm">
								<IconLocation class="w-4 h-4" />Main address</span
							>
							<button
								class="text-c-dark-blue px-4 text-sm underline underline-offset-2"
							>
								View all
							</button>
						</div>
						<div
							class="bg-c-linear flex p-4 rounded-md justify-between overflow-auto"
						>
							<table class="overflow-auto w-full">
								<tbody
									class="grid gap-5 grid-cols-[200px_100px_100px_100px_100px_400px] 2xl:grid-cols-[200px_100px_100px_100px_100px_auto]"
								>
									<tr>
										<td>
											<h5 class="text-c-deep-blue text-sm">Residence</h5>
											<span class="text-c-dark-blue text-xs sm:text-sm"
												>Viale Europe, 168 loc Lido Di <br />
												Camaire</span
											>
										</td>
									</tr>
									<tr>
										<td>
											<h5 class="text-c-light-grey text-sm">City</h5>
											<span class="text-c-dark-blue text-xs sm:text-sm"
												>Camaiore</span
											>
										</td>
									</tr>
									<tr>
										<td>
											<h5 class="text-c-light-grey text-sm">Province</h5>
											<span class="text-c-dark-blue text-xs sm:text-sm"
												>LU</span
											>
										</td>
									</tr>
									<tr>
										<td>
											<h5 class="text-c-light-grey text-sm">Province</h5>
											<span class="text-c-dark-blue text-xs sm:text-sm"
												>LU</span
											>
										</td>
									</tr>
									<tr>
										<td>
											<h5 class="text-c-light-grey text-sm">CAP</h5>
											<span class="text-c-dark-blue text-sm">5505</span>
										</td>
									</tr>
									<tr>
										<td>
											<h5 class="text-c-light-grey text-sm">Notes</h5>
											<span class="text-c-dark-blue text-xs sm:text-sm"
												>This location is bad to find the person. Usually hes
												not here</span
											>
										</td>
									</tr>
								</tbody>
							</table>
							<IconDots class="h-8 w-8" />
						</div>
					</div>
					<div class="flex flex-col gap-2">
						<span class="flex items-center gap-2 text-c-light-grey text-sm">
							<IconCalender class="w-4 h-4" /> Notes</span
						>
						<p class="text-c-dark-blue text-sm xl:text-base">
							This person is very temperamental and tends to be agressive on
							phone. Please address it carefully.
						</p>
					</div>
					<div class="flex flex-wrap gap-3 sm:gap-2">
						<div
							class="flex items-center justify-between border w-52 border-c-grey h-10 px-5 rounded-md"
						>
							<span class="flex items-center text-sm gap-2 text-c-dark-blue">
								<IconCalender class="w-4 h-4" />Profile.csv</span
							>
							<span class="text-sm text-c-light-grey">1.5 mb</span>
						</div>
						<div
							class="flex items-center justify-between border w-52 border-c-grey h-10 px-5 rounded-md"
						>
							<span class="flex items-center text-sm gap-2 text-c-dark-blue">
								<IconCalender class="w-4 h-4" />Revision.doc</span
							>
							<span class="text-sm text-c-light-grey">1.5 mb</span>
						</div>
					</div>
				</Card>
			</div>
			<div class="flex flex-col gap-10">
				<CardHeader title="Garantees">
					<template #afterTitle>
						<div class="flex items-center gap-4 border-l border-c-coral-blue">
							<span
								class="badge text-white bg-c-deep-blue ml-4 px-4 h-9 border-none"
								>03</span
							>
						</div>
					</template>
					<template #endTitle>
						<button
							class="btn border-none min-h-8 h-11 bg-c-ghost-white gap-2 flex-nowrap whitespace-nowrap text-c-dark-blue hover:bg-c-ghost-white"
						>
							<span>{{ t('filter.filter_title') }}</span>
							<span class="badge bg-c-deep-blue ml-2 px-2 text-white">3</span>
							<IconDropdown class="w-4 h-4" />
						</button>
					</template>
				</CardHeader>
				<div class="flex flex-col flex-nowrap gap-6 md:flex-row md:flex-wrap">
					<Card class="p-4 w-full md:w-72">
						<div class="flex justify-between items-center mb-5">
							<ul class="flex gap-2">
								<li>
									<a
										href="#"
										class="bg-c-light-pink h-7 w-24 text-c-purple font-semibold text-sm flex justify-center items-center rounded-3xl px-2"
										>Garantee</a
									>
								</li>
								<li>
									<a
										href="#"
										class="h-7 w-20 bg-c-light-green flex items-center justify-center text-sm rounded-xl text-c-success font-semibold"
										>Active</a
									>
								</li>
							</ul>
							<IconDots class="h-8 w-8" />
						</div>
						<div class="flex items-center gap-2 mb-8">
							<Avatar
								alt="image"
								src="https://picsum.photos/80/80"
								size="w-8 h-8"
							/>
							<p class="text-c-dark-blue text-sm">
								Fondo di Garanzia L23 N662 Medicredito CE
							</p>
						</div>
						<div class="flex flex-col gap-6 border-b border-b-c-grey pb-8 mb-5">
							<div class="flex items-center justify-between">
								<span class="flex items-center gap-2 text-c-light-grey">
									<IconCalender class="w-4 h-4" /> Birthdate</span
								>
								<span class="text-c-dark-blue text-sm">August, 12 2021</span>
							</div>
							<div class="flex items-center justify-between">
								<span class="flex items-center gap-2 text-c-light-grey">
									<IconCalender class="w-4 h-4" /> Death date</span
								>
								<span class="text-c-dark-blue text-sm">--</span>
							</div>
							<div class="flex items-center justify-between">
								<span class="flex items-center gap-2 text-c-light-grey">
									<IconLocation class="w-4 h-4" />Birth location</span
								>
								<span class="text-c-dark-blue text-sm">Italy</span>
							</div>
							<div class="flex items-center justify-between">
								<span class="flex items-center gap-2 text-c-light-grey">
									<IconMoney class="w-4 h-4" />IVA</span
								>
								<span class="text-c-dark-blue text-sm">543234564333</span>
							</div>
						</div>
						<div class="flex items-center justify-between mb-5">
							<span class="flex items-center gap-2 text-c-light-grey">
								<IconLocation class="w-4 h-4" />Main address</span
							>
							<button
								class="text-c-light-grey text-sm underline underline-offset-2"
							>
								View all
							</button>
						</div>
						<div class="border-b border-b-c-grey pb-5 mb-5">
							<span class="text-c-deep-blue text-sm">Residence</span>
							<p class="text-c-dark-blue text-sm">
								Viale Europe, 168 loc Lido Di Camaire
							</p>
						</div>
						<div class="flex flex-col gap-2">
							<div
								class="flex items-center justify-between border border-c-grey h-10 px-5 rounded-md"
							>
								<span class="flex items-center text-sm gap-2 text-c-dark-blue">
									<IconMoney class="w-4 h-4" />Profile.csv</span
								>
								<span class="text-sm text-c-light-grey">1.5 mb</span>
							</div>
							<div
								class="flex items-center justify-between border border-c-grey h-10 px-5 rounded-md"
							>
								<span class="flex items-center gap-2 text-c-dark-blue text-sm">
									<IconMoney class="w-4 h-4" />Profile.csv</span
								>
								<span class="text-sm text-c-light-grey">1.5 mb</span>
							</div>
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
			<Card class="flex gap-7 flex-col">
				<CardHeader title="Profile Notes" />
				<p class="text-c-light-grey">
					This person is very temperamental and tends to be agressive on phone.
					Please address it carefully.
				</p>
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
import {
	IconPhone,
	IconUser,
	IconDropdown,
	IconDots,
	IconMail,
	IconCalender,
	IconMoney,
	IconLocation,
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
const pieChartPayload = [
	{ color: '#072EF5', value: 250 },
	{ color: '#2AD7B3', value: 308 },
	{ color: '#EC7E0E', value: 520 },
	{ color: '#A955EB', value: 130 },
];
</script>
