<template>
	<div class="h-full flex flex-col">
		<Header
			:src="configurationImage"
			:alt="t('configuration.header.image_alt')"
			:title="t('configuration.header.title')"
			:icon="IconConfiguration"
			:sub-title="t('configuration.header.links.link_first')"
		/>
		<ConfigurationMenu />
		<RouterView name="default" />
	</div>
</template>

<script setup>
import { useI18n } from 'vue-i18n';
import configurationImage from '../assets/images/undraw-goals-full.svg';
import { IconConfiguration } from '../icons';
import Header from '../components/header/header.component.vue';
import ConfigurationMenu from '../pages/configuration/components/menu.component.vue';
const { t } = useI18n();
</script>
