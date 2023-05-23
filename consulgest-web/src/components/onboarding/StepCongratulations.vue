<template>
	<div class="text-center mt-8 w-full">
		<h1 class="text-c-dark-blue text-4xl font-semibold">
			{{ t('onboarding.steps.congratulations.title') }}, Walter!
		</h1>
		<h4 class="text-c-dark-blue text-lg font-light mb-20">
			{{ t('onboarding.steps.congratulations.description') }}
		</h4>
		<img
			class="mx-auto mb-20"
			src="../../assets/images/undraw-outer-space.svg"
		/>
		<button
			class="btn btn-primary px-8 border-none normal-case h-[50px] mr-6"
			@click="previousTab()"
		>
			{{ t('onboarding.steps.congratulations.add_csv') }}
		</button>
		<RouterLink v-slot="{ navigate }" to="/dashboard">
			<button
				class="btn btn-secondary px-8 border-none normal-case h-[50px]"
				@click="navigate"
			>
				{{ t('onboarding.steps.congratulations.move_dashboard') }}
			</button>
		</RouterLink>
	</div>
</template>
<script lang="ts" setup>
import { useI18n } from 'vue-i18n';

const emit = defineEmits<{
	(e: 'previous-tab'): void;
}>();

const { t } = useI18n();

const previousTab = () => {
	emit('previous-tab');
};
</script>
