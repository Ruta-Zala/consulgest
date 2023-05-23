<template>
	<div class="absolute left-0 right-0 bottom-0 p-4 bg-white">
		<ul class="flex justify-center text-c-light-grey text-sm font-normal">
			<li class="mx-4">
				<a href="">{{ t('onboarding.footer.copyright_text') }}</a>
			</li>
			<li class="h-2 w-2 bg-c-grey rounded-full mt-1.5 mx-4"></li>
			<li class="mx-4">
				<a href="">{{ t('onboarding.footer.terms_of_service') }}</a>
			</li>
			<li class="h-2 w-2 bg-c-grey rounded-full mt-1.5 mx-4"></li>
			<li class="mx-4">
				<a href="">{{ t('onboarding.footer.privacy_policy') }}</a>
			</li>
		</ul>
	</div>
</template>
<script lang="ts" setup>
import { useI18n } from 'vue-i18n';

const { t } = useI18n();
</script>
