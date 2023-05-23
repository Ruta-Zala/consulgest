<template>
	<Header
		:src="HeaderImage"
		:alt="importImgAlt"
		:title="importTitle"
		:icon="IconBook"
	/>
	<ImportDossierMenuComponent />
	<div class="bg-white py-16 px-20 flex-1">
		<RouterView name="default" />
	</div>
</template>

<script setup>
import { useI18n } from 'vue-i18n';
import { RouterView } from 'vue-router';
import Header from '../components/header/header.component.vue';
import HeaderImage from '../assets/images/dossier_import.svg';
import { IconBook } from '../icons';
import ImportDossierMenuComponent from '../pages/import-dossier/components/menu.component.vue';

const { t } = useI18n();
const importTitle = t('import_dossier.header.title');
const importImgAlt = t('import_dossier.header.img_alt');
</script>
