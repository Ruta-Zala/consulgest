<template>
	<div class="flex flex-col items-center flex-1">
		<div>
			<img src="../../assets/images/dashboard.svg" alt="home" />
		</div>
		<div class="flex flex-col mt-6 items-center text-c-dark-blue">
			<span class="text-3xl font-medium">{{ t('dashboard.home.title') }}</span>
			<p class="mt-1 mb-6 max-w-xl mx-auto text-center">
				{{ t('dashboard.home.sub_title') }}
			</p>
			<span class="font-semibold">{{ t('dashboard.home.description') }}</span>
		</div>
		<div class="mt-12 pb-10">
			<RouterLink
				:to="{ path: '/import-dossier' }"
				class="flex flex-col items-center w-60 p-4 bg-white border border-c-grey rounded-xl shadow-2xl hover:border-c-deep-blue"
			>
				<IconUpload class="mb-4 text-c-deep-blue w-10 h-10" />
				<span class="font-semibold text-c-dark-blue">
					{{ t('dashboard.home.upload_btn') }}
				</span>
			</RouterLink>
		</div>
		<DashboardModal />
	</div>
</template>

<script lang="ts" setup>
import { useI18n } from 'vue-i18n';
import { IconUpload } from '../../icons';
import DashboardModal from './components/modal.component.vue';

const { t } = useI18n();
</script>
