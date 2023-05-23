<template>
	<div>
		<div class="text-center mt-8 w-full">
			<h1 class="text-c-dark-blue text-4xl font-semibold">
				{{ t('onboarding.steps.welcome.title') }}, Walter
			</h1>
			<h4 class="text-c-dark-blue text-lg font-light mb-20">
				{{ t('onboarding.steps.welcome.description') }}
			</h4>
			<img
				class="mx-auto"
				src="../../assets/images/undraw-goals.svg"
				alt="undraw goal"
			/>
		</div>

		<div class="mb-8 flex gap-8 mx-auto mt-16 w-2/4 justify-end">
			<RouterLink to="/dashboard" class="text-c-dark-blue btn btn-ghost">
				{{ t('commonButtons.skip') }}
			</RouterLink>
			<button
				class="btn btn-primary border-none capitalize w-[117px] h-[50px]"
				@click="nextTab()"
			>
				{{ t('commonButtons.next_btn') }}
			</button>
		</div>
	</div>
</template>
<script lang="ts" setup>
import { useI18n } from 'vue-i18n';

const { t } = useI18n();

const emit = defineEmits<{
	(e: 'next-tab'): void;
}>();

const nextTab = () => {
	emit('next-tab');
};
</script>
