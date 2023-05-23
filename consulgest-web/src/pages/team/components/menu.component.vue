<template>
	<div
		class="navbar flex-col xl:flex-row xl:py-0 px-8 lg:px-16 shadow-xl relative bg-white"
	>
		<div v-if="isTeamPage">
			<PageMenu :options="menuOptions" />
		</div>
		<div v-else class="flex gap-4 items-center">
			<Dropdown :label="t('team.header.links.link_first')" />
			<Dropdown :label="t('team.header.links.link_second')" />
		</div>
		<div class="mt-3 xl:mt-0 flex items-center justify-end flex-1 gap-4">
			<div class="relative text-c-light-grey">
				<IconSearch
					class="absolute top-2/4 transform -translate-y-2/4 left-4 h-4 w-4"
				></IconSearch>
				<input
					type="text"
					class="input bg-c-ghost-white min-h-8 h-11 w-full max-w-full pl-11 bg-c-linear placeholder-current focus:outline-none"
					placeholder="Search for..."
				/>
			</div>
			<div class="dropdown">
				<button
					class="btn border-none min-h-8 h-11 bg-c-ghost-white gap-2 flex-nowrap whitespace-nowrap text-c-dark-blue hover:bg-c-ghost-white"
				>
					<IconDropdownFilter class="w-4 h-4" />
					<span>{{ t('filter.filter_title') }}</span>
					<span class="badge text-white bg-c-deep-blue px-2 text-xs">3</span>
				</button>
				<div
					tabindex="0"
					class="dropdown-content menu p-6 shadow-l bg-base-100 rounded-lg w-80 flex gap-2 right-0"
				>
					<span>{{ t('team.header.filter.filter_add') }}</span>
					<div class="dropdown dropdown-end relative w-full">
						<button
							class="btn border-c-grey bg-transparent w-full gap-2 flex flex-row justify-between text-c-dark-blue hover:bg-c-ghost-white"
						>
							<span>{{ t('team.header.filter.filter_another') }}</span>
							<span><IconDropdown class="w-3 h-3" /></span>
						</button>
					</div>
					<div class="dropdown dropdown-end relative w-full">
						<button
							class="btn border-c-grey bg-transparent w-full gap-2 flex flex-row justify-between text-c-dark-blue hover:bg-c-ghost-white"
						>
							<span>{{ t('team.header.filter.filter_here') }}</span>
							<span><IconDropdown class="w-3 h-3" /></span>
						</button>
					</div>
					<DatepickerInput input-placeholder="From"></DatepickerInput>
					<DatepickerInput input-placeholder="To"></DatepickerInput>
					<div class="flex gap-4 justify-end mt-4">
						<button class="text-c-dark-blue btn btn-ghost w-28">
							{{ t('team.header.filter.cancel_btn') }}
						</button>
						<button
							class="bg-c-dark-blue rounded-md text-sm font-semibold btn btn-white text-white w-28"
						>
							{{ t('filter.filter_title') }}
						</button>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script lang="ts" setup>
import { useI18n } from 'vue-i18n';
import { useRoute } from 'vue-router';
import { computed } from 'vue';
import { IconSearch, IconDropdown, IconDropdownFilter } from '../../../icons';
import DatepickerInput from '../../../components/datepicker/datepicker.component.vue';
import Dropdown from '../../../components/dropdown/dropdown.component.vue';
import PageMenu from '../../../components/page-menu/page-menu.component.vue';

const { t } = useI18n();
const route = useRoute();

const isTeamPage = computed(() => {
	return (
		route.path.includes('/team/user') ||
		route.path.includes('/team/preferences') ||
		route.path.includes('/team/password')
	);
});

const menuOptions = [
	{
		title: t('team.user_profile.header.links.link_first'),
		href: '/team/user',
	},
	{
		title: t('team.user_profile.header.links.link_second'),
		href: '/team/preferences',
	},
	{
		title: t('team.user_profile.header.links.link_third'),
		href: '/team/password',
	},
];
</script>
