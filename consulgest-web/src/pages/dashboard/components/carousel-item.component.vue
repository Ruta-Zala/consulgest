<template>
	<div class="carousel-item w-full flex-col">
		<div class="flex flex-col text-c-dark-blue mt-5">
			<span class="text-2xl font-semibold leading-10">
				{{ t('dashboard.welcome_modal.title') }}
			</span>
			<span>{{ t('dashboard.welcome_modal.sub_title') }}</span>
		</div>
		<img
			src="../../../assets/images/carousel-item.png"
			class="rounded-box mt-8"
			alt="item carousel"
		/>
	</div>
</template>
<script lang="ts" setup>
import { useI18n } from 'vue-i18n';
const { t } = useI18n();
</script>
