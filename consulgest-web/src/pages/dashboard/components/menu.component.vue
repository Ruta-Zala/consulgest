<template>
	<div
		class="navbar min-h-min flex-col sm:flex-row px-8 lg:px-16 shadow-xl relative bg-white py-3"
	>
		<div class="flex items-center gap-4">
			<PageMenu :options="menuOptions" />
			<button
				class="flex items-center gap-3 text-c-dark-blue border border-dashed border-c-grey rounded-lg min-h-8 h-11 px-4"
			>
				<span>{{ t('dashboard.header.links.link_second') }}</span>
				<IconPlus class="h-3" />
			</button>
		</div>
		<div class="mt-3 sm:mt-0 flex items-center justify-end flex-1 gap-3">
			<div class="relative text-c-light-grey ml-2">
				<IconSearch
					class="absolute top-2/4 transform -translate-y-2/4 left-4 h-4 w-4"
				></IconSearch>
				<input
					type="text"
					class="min-h-8 h-11 input bg-c-ghost-white w-full max-w-full pl-11 bg-c-linear placeholder-current focus:outline-none"
					placeholder="Search for..."
				/>
			</div>
			<div class="dropdown dropdown-hover">
				<button
					class="btn border-none min-h-8 h-11 bg-c-ghost-white gap-2 flex-nowrap whitespace-nowrap text-c-dark-blue hover:bg-c-ghost-white"
				>
					<IconDropdownFilter class="w-4 h-4" />
					<span>{{ t('filter.filter_title') }}</span>
					<span class="badge bg-c-deep-blue ml-2 px-2 text-white">3</span>
				</button>
				<div
					tabindex="0"
					class="dropdown-content menu p-6 shadow-l bg-base-100 rounded-lg w-[475px] flex gap-2 right-0"
				>
					<span class="text-c-dark-blue">{{ t('filter.filter_title') }}</span>
					<div class="flex flex-col gap-2 w-full">
						<div class="flex gap-4 items-center">
							<div class="w-24 text-sm text-c-light-grey">
								{{ t('filter.filter_region') }}
							</div>
							<div class="dropdown dropdown-end relative w-full">
								<button
									class="btn border-c-grey bg-transparent w-full gap-2 flex flex-row justify-between text-c-dark-blue hover:bg-c-ghost-white"
								>
									<span class="font-normal">{{ t('filter.filter_all') }}</span>
									<span><IconDropdown class="w-3 h-3" /></span>
								</button>
							</div>
						</div>
						<div class="flex gap-4 items-center">
							<div class="w-24 text-sm text-c-light-grey">
								{{ t('filter.filter_city') }}
							</div>
							<div class="dropdown dropdown-end relative w-full">
								<button
									class="btn border-c-grey bg-transparent w-full gap-2 flex flex-row justify-between text-c-dark-blue hover:bg-c-ghost-white"
								>
									<span class="font-normal">{{ t('filter.filter_all') }}</span>
									<span><IconDropdown class="w-3 h-3" /></span>
								</button>
							</div>
						</div>
						<div class="flex gap-4 items-center">
							<div class="w-24 text-sm text-c-light-grey">
								{{ t('filter.filter_province') }}
							</div>
							<div class="dropdown dropdown-end relative w-full">
								<button
									class="btn border-c-grey bg-transparent w-full gap-2 flex flex-row justify-between text-c-dark-blue hover:bg-c-ghost-white"
								>
									<span class="font-normal">{{ t('filter.filter_all') }}</span>
									<span><IconDropdown class="w-3 h-3" /></span>
								</button>
							</div>
						</div>
						<div class="flex gap-4 items-center">
							<div class="w-24 text-sm text-c-light-grey">
								{{ t('filter.filter_forfeiture') }}
							</div>
							<div class="dropdown dropdown-end relative w-full">
								<button
									class="btn border-c-grey bg-transparent w-full gap-2 flex flex-row justify-between text-c-dark-blue hover:bg-c-ghost-white"
								>
									<span class="font-normal">{{ t('filter.filter_all') }}</span>
									<span><IconDropdown class="w-3 h-3" /></span>
								</button>
							</div>
						</div>
						<div class="flex gap-4 items-center">
							<div class="w-24 text-sm text-c-light-grey">
								{{ t('filter.filter_amount') }}
							</div>
							<div class="flex gap-2 w-full">
								<div class="dropdown dropdown-end relative w-full">
									<button
										class="btn border-c-grey bg-transparent w-full gap-2 flex flex-row justify-between text-c-dark-blue hover:bg-c-ghost-white"
									>
										<span class="font-normal">{{
											t('filter.filter_greater_than')
										}}</span>
										<span><IconDropdown class="w-3 h-3" /></span>
									</button>
								</div>
								<div class="dropdown dropdown-end relative w-full">
									<button
										class="btn border-c-grey bg-transparent w-full gap-2 flex flex-row justify-between text-c-dark-blue hover:bg-c-ghost-white"
									>
										<span class="font-normal">0.000</span>
										<span><IconMoney class="w-5 h-5" /></span>
									</button>
								</div>
							</div>
						</div>
						<div class="flex gap-4 items-center">
							<div class="w-24 text-sm text-c-light-grey">
								{{ t('filter.filter_date') }}
							</div>
							<div class="flex gap-2 w-full">
								<div class="dropdown dropdown-end relative w-full">
									<DatepickerInput
										input-placeholder="From"
										class="w-full"
									></DatepickerInput>
								</div>
								<div class="dropdown dropdown-end relative w-full">
									<DatepickerInput input-placeholder="To"></DatepickerInput>
								</div>
							</div>
						</div>
					</div>
					<div class="flex gap-4 justify-end mt-4">
						<button class="text-c-dark-blue btn btn-ghost w-28">
							{{ t('commonButtons.cancel') }}
						</button>
						<button class="btn btn-primary w-28">
							{{ t('commonButtons.filter') }}
						</button>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script lang="ts" setup>
import { useI18n } from 'vue-i18n';
import {
	IconMoney,
	IconDropdown,
	IconDropdownFilter,
	IconPlus,
	IconSearch,
} from '../../../icons';
import DatepickerInput from '../../../components/datepicker/datepicker.component.vue';
import PageMenu from '../../../components/page-menu/page-menu.component.vue';

const { t } = useI18n();
const menuOptions = [
	{
		title: t('dashboard.header.links.link_first'),
		href: '/dashboard/detail',
	},
];
</script>
