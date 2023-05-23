<template>
	<Header
		v-if="isAllDossier"
		:src="dossiersImage"
		:alt="dossiersImgAlt"
		:title="dossiersTitle"
		:icon="IconBook"
		:sub-title="dossiersSubTitle"
	>
		<template #afterTitle>
			<div class="flex items-center gap-4">
				<span
					class="badge text-white bg-c-deep-blue px-5 text-xl mr-4 h-8 border-none"
					>544</span
				>
			</div>
		</template>
	</Header>
	<Header
		v-else
		:src="dossiersImage"
		:alt="dossiersImgAlt"
		:title="dossiersTitle"
		:icon="IconBook"
		:sub-title="dossiersSubTitle"
	>
		<template #afterTitle>
			<div class="flex items-center gap-4">Josh Anderson Smith</div>
		</template>
	</Header>
	<keep-alive :key="currentDossierId">
		<DossiersMenuComponent />
	</keep-alive>
	<div class="bg-white p-16 flex-1">
		<RouterView name="default" :update:dossier-id="onDossierIdUpdate" />
	</div>
</template>

<script setup>
import { useI18n } from 'vue-i18n';
import { RouterView, useRoute } from 'vue-router';
import { ref, watch, computed } from 'vue';
import Header from '../components/header/header.component.vue';
import dossiersImage from '../assets/images/dossiers.svg';
import { IconBook } from '../icons';
import DossiersMenuComponent from '../pages/dossiers/components/menu.component.vue';

const { t } = useI18n();
const dossiersTitle = t('dossiers.header.title');
const dossiersSubTitle = '';
const dossiersImgAlt = t('dossiers.header.img_alt');
const dossierId = ref(0);
const currentDossierId = computed(() => dossierId.value);
const route = useRoute();
const isAllDossier = computed(() => {
	return route.matched.some((record) => record.name === 'dossiers');
});
function onDossierIdUpdate(dossierId) {
	dossierId.value = Number(dossierId);
}

watch(
	() => route.params.dossierId,
	(newVal) => {
		dossierId.value = Number(newVal);
	},
);
</script>
