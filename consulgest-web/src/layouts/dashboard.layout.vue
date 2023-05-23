<template>
	<Header
		:src="dashboardImage"
		:alt="dashboardImgAlt"
		:title="dashboardTitle"
		:icon="IconMenu"
		:sub-title="subTitle"
	/>
	<DashboardMenuComponent />
	<div class="bg-white p-16 flex-1">
		<RouterView name="default" />
	</div>
</template>

<script setup>
import { useI18n } from 'vue-i18n';
import { RouterView } from 'vue-router';
import Header from '../components/header/header.component.vue';
import dashboardImage from '../assets/images/pie-chart.svg';
import { IconMenu } from '../icons';
import DashboardMenuComponent from '../pages/dashboard/components/menu.component.vue';

const { t } = useI18n();
const dashboardTitle = t('dashboard.header.title');
const dashboardImgAlt = t('dashboard.header.img_alt');

const date = new Date();
const currentDate = date.toLocaleString('default', { dateStyle: 'full' });

const subTitle = currentDate;
</script>
