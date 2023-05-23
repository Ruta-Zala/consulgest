<template>
	<div>
		<div class="flex justify-between items-center">
			<span class="text-sm font-semibold text-c-dark-blue">
				{{ t('dashboard.welcome_modal.guide') }}
			</span>
			<ul class="flex justify-center gap-2">
				<li
					v-for="(step, index) in steps"
					:key="index"
					class="h-2 w-2 rounded-full"
					:class="{
						'bg-c-success': steps.indexOf(step) < steps.indexOf(selected),
						'bg-c-grey': steps.indexOf(step) > steps.indexOf(selected),
						'bg-c-deep-blue': step === selected,
					}"
				></li>
			</ul>
		</div>
		<div class="steps overflow-x-hidden w-full">
			<transition name="slide-fade" appear="appear">
				<component :is="stepsComponents[selected]" />
			</transition>
		</div>
		<div class="flex gap-4 justify-end mt-8">
			<button
				v-if="currentIndex > 0"
				class="text-c-dark-blue btn btn-ghost w-28"
				@click="previousTab()"
			>
				{{ t('commonButtons.back_btn') }}
			</button>
			<button class="btn btn-primary w-28" @click="nextTab()">
				{{ t('commonButtons.next_btn') }}
			</button>
		</div>
	</div>
</template>
<script lang="ts" setup>
import { useI18n } from 'vue-i18n';
import { ref } from 'vue';
import CarouselItem from './carousel-item.component.vue';

const stepsComponents = {
	StepOne: CarouselItem,
	StepTwo: CarouselItem,
	StepThree: CarouselItem,
	StepFour: CarouselItem,
};

const steps = ['StepOne', 'StepTwo', 'StepThree', 'StepFour'] as const;
const { t } = useI18n();
const currentIndex = ref(0);
const selected = ref<typeof steps[number]>(steps[0]);
const emit = defineEmits(['close']);

const previousTab = () => {
	currentIndex.value--;
	selected.value = steps[currentIndex.value];
};

const nextTab = () => {
	currentIndex.value++;
	selected.value = steps[currentIndex.value];
	if (currentIndex.value === steps.length) {
		emit('close', false);
	}
};
</script>

<style scoped>
.slide-fade-enter-active {
	transition: all 0.5s ease-in-out;
}

.slide-fade-enter-from,
.slide-fade-leave-to {
	transform: translateX(100%);
	opacity: 0;
}
</style>
