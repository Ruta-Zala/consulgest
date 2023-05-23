<template>
	<div
		class="navbar min-h-min flex-col xl:flex-row xl:py-3 px-8 lg:px-16 shadow-xl relative bg-white py-3"
	>
		<div v-if="!route.params.dossierId" class="flex items-center gap-4">
			<PageMenu :options="menuOptions" />
			<DatepickerInput input-placeholder="From" class="w-36"></DatepickerInput>
			<DatepickerInput input-placeholder="To" class="w-36"></DatepickerInput>
			<Dropdown label="Position"> </Dropdown>
		</div>
		<div v-else class="flex items-center gap-4">
			<PageMenu :options="menuDetailOptions" />
		</div>
		<div
			class="mt-3 xl:mt-0 flex items-center justify-between lg:justify-end flex-1 gap-3"
		>
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
					</div>
					<div class="flex gap-4 justify-end mt-4">
						<button class="text-c-dark-blue btn btn-ghost w-28">
							{{ t('commonButtons.cancel') }}
						</button>
						<button class="btn bg-c-deep-blue w-28 text-white">
							{{ t('commonButtons.filter') }}
						</button>
					</div>
				</div>
			</div>
			<button
				v-if="isDetailPage"
				class="btn btn-outline min-h-8 border-c-coral-blue text-c-dark-blue h-11"
			>
				<IconUnion class="w-4 h-4" />
				<span class="pl-3">{{ t('dossiers.common_button.export_as') }}</span>
			</button>
		</div>
	</div>
</template>

<script lang="ts" setup>
import { useI18n } from 'vue-i18n';
import { useRoute } from 'vue-router';
import { computed } from 'vue';
import {
	IconSearch,
	IconUnion,
	IconDropdown,
	IconDropdownFilter,
	IconMoney,
} from '../../../icons';
import DatepickerInput from '../../../components/datepicker/datepicker.component.vue';
import Dropdown from '../../../components/dropdown/dropdown.component.vue';
import PageMenu from '../../../components/page-menu/page-menu.component.vue';

const route = useRoute();
const { t } = useI18n();

const isDetailPage = computed(() => {
	return route.path.includes('/dossiers/details');
});

const menuOptions = [
	{
		title: t('dossiers.header.links.link_first'),
		href: '/dossiers',
	},
];

const menuDetailOptions = [
	{
		title: t('dossiers.header.sub_links.link_first'),
		href: `/dossiers/${route.params.dossierId}/overview`,
	},
	{
		title: t('dossiers.header.sub_links.link_second'),
		href: `/dossiers/${route.params.dossierId}/details`,
	},
	{
		title: t('dossiers.header.sub_links.link_third'),
		href: `/dossiers/${route.params.dossierId}/individuals`,
	},
	{
		title: t('dossiers.header.sub_links.link_four'),
		href: `/dossiers/${route.params.dossierId}/address-book`,
	},
	{
		title: t('dossiers.header.sub_links.link_five'),
		href: '/dashboard',
	},
	{
		title: t('dossiers.header.sub_links.link_six'),
		href: '/dashboard',
	},
];
</script>
