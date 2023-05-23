<template>
	<div
		class="navbar min-h-min flex-col sm:flex-row px-8 lg:px-16 shadow-xl relative bg-white py-3"
	>
		<PageMenu :options="menuOptions" />
	</div>
</template>

<script lang="ts" setup>
import { useI18n } from 'vue-i18n';
import PageMenu from '../../../components/page-menu/page-menu.component.vue';

const { t } = useI18n();
const menuOptions = [
	{
		title: t('consul.header.dropdown.dropdown_first'),
		href: '/consul',
	},
	{
		title: t('consul.header.dropdown.dropdown_second'),
		href: '/consul/behavioural',
	},
];
</script>
