<template>
	<Header
		:src="consulImage"
		:alt="consulImgAlt"
		:title="consulTitle"
		:icon="IconCpu"
		:sub-title="consulSubTitle"
	/>
	<ConsulMenuComponent />
	<div class="bg-white py-16 px-20 flex-1">
		<RouterView name="default" />
	</div>
</template>

<script setup lang="ts">
import { useI18n } from 'vue-i18n';
import { RouterView } from 'vue-router';
import Header from '../components/header/header.component.vue';
import consulImage from '../assets/images/dashboard.svg';
import { IconCpu } from '../icons';
import ConsulMenuComponent from '../pages/consul/components/menu.component.vue';

const { t } = useI18n();
const consulTitle = t('consul.header.title');
const consulSubTitle = t('consul.header.sub_title');
const consulImgAlt = t('consul.header.img_alt');
</script>
