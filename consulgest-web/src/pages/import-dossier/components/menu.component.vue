<template>
	<div
		class="navbar min-h-min flex-col xl:flex-row xl:justify-between xl:py-3 px-8 lg:px-16 shadow-xl relative bg-white py-3"
	>
		<div class="left">
			<PageMenu v-if="!isHistoryPage" :options="menuOptions" />
			<div v-else class="flex items-center">
				<div class="text-c-dark-blue mr-3">
					{{ t('import_dossier.header.links.link_second') }}
				</div>
				<div
					class="w-32 lg:w-40 mx-2 flex items-center justify-center relative text-c-dark-blue"
				>
					<DatepickerInput
						input-class="border-0 bg-c-ghost-white"
						input-placeholder="Form"
					/>
				</div>
				<div
					class="w-32 lg:w-40 mx-2 flex items-center justify-center relative text-c-dark-blue"
				>
					<DatepickerInput
						input-class="border-0 bg-c-ghost-white"
						input-placeholder="Form"
					/>
				</div>
				<div class="h-10 lg:h-12 mx-2 lg:mr-4 lg:ml-2 w-px bg-c-grey"></div>
				<button
					class="btn btn-outline min-h-8 h-11 font-normal border-0 text-c-dark-blue bg-c-ghost-white"
				>
					<span class="pl-3">{{
						t('import_dossier.header.links.link_third')
					}}</span>
					<IconMoney class="w-6 h-6" />
				</button>
			</div>
		</div>
		<div class="right">
			<div class="mt-3 xl:mt-0 flex items-center justify-end flex-1">
				<div class="mx-3">
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
				</div>
			</div>
		</div>
	</div>
</template>

<script lang="ts" setup>
import { useI18n } from 'vue-i18n';
import { useRoute } from 'vue-router';
import { computed } from 'vue';
import { IconMoney, IconSearch } from '../../../icons';
import DatepickerInput from '../../../components/datepicker/datepicker.component.vue';
import PageMenu from '../../../components/page-menu/page-menu.component.vue';

const { t } = useI18n();
const route = useRoute();

const isHistoryPage = computed(() => {
	return route.path.includes('/import-dossier/history-logs');
});

const menuOptions = [
	{
		title: t('import_dossier.header.links.link_first'),
		href: '/import-dossier/history-logs',
	},
];
</script>
