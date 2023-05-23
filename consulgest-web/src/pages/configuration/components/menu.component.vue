<template>
	<div class="navbar py-0 px-8 lg:px-16 shadow-xl relative bg-white">
		<PageMenu :options="menuOptions" />
		<div class="flex items-center justify-end flex-1">
			<div class="mr-4">
				<div class="relative text-c-light-grey">
					<IconSearch
						class="absolute top-2/4 transform -translate-y-2/4 left-4 h-4"
					></IconSearch>
					<input
						type="text"
						class="input min-h-8 h-11 bg-c-ghost-white w-full max-w-full pl-11 bg-c-linear placeholder-current focus:outline-none"
						:placeholder="t('configuration.header.search_placeholder')"
					/>
				</div>
			</div>
		</div>
	</div>
</template>

<script lang="ts" setup>
import { useI18n } from 'vue-i18n';
import { IconSearch } from '../../../icons';
import PageMenu from '../../../components/page-menu/page-menu.component.vue';

const { t } = useI18n();

const menuOptions = [
	{
		title: t('configuration.header.links.link_first'),
		href: '/configuration/system',
	},
	{
		title: t('configuration.header.links.link_second'),
		href: '/configuration/preferences',
	},
	{
		title: t('configuration.header.links.link_third'),
		href: '/configuration/permissions',
	},
	{
		title: t('configuration.header.links.link_fourth'),
		href: '/configuration/payments',
	},
];
</script>
