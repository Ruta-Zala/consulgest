<template>
	<div class="flex flex-col" :class="{ 'h-screen': !skipWelcome }">
		<Header v-if="!skipWelcome" class="mt-12" />
		<ul class="flex justify-center gap-2" :class="{ 'mt-24': !skipWelcome }">
			<li
				v-for="step in stepsComponents.length"
				:key="step"
				class="h-2 w-2 rounded-full"
				:class="{
					'bg-c-grey': step !== selected + 1 && step > selected + 1,
					'bg-c-deep-blue': step === selected + 1,
					'bg-c-success': step < selected + 1,
				}"
			></li>
		</ul>
		<div
			class="flex-1 flex flex-col relative overflow-x-hidden w-full overflow-y-auto"
		>
			<transition name="slide-fade">
				<div class="flex flex-col overflow-auto">
					<keep-alive :key="selected">
						<component
							:is="stepsComponents[selected].component"
							v-if="stepsComponents"
							:uploaded-file="uploadFile"
							@previous-tab="stepsComponents[selected].prev"
							@next-tab="stepsComponents[selected].next"
						/>
					</keep-alive>
				</div>
			</transition>
		</div>
		<div v-if="!skipWelcome" class="relative mt-2 pt-3">
			<Footer />
		</div>
	</div>
</template>

<script lang="ts" setup>
import type { Component } from 'vue';
import { ref } from 'vue';
import Header from './Header.vue';
import Footer from './Footer.vue';
import StepWelcome from './StepWelcome.vue';
import StepSelect from './StepSelect.vue';
import StepImport from './StepImport.vue';
import StepCongratulations from './StepCongratulations.vue';

const props = defineProps({
	skipWelcome: {
		type: Boolean,
		default: false,
		required: false,
	},
});

const selected = ref(0);
const uploadFile = ref();

const previousTab = () => {
	selected.value = selected.value - 1;
};

const backToCsvTab = () => {
	selected.value = selected.value - 2;
};

const nextTab = () => {
	selected.value = selected.value + 1;
};

const nextTabSelect = (csv: any, file: any) => {
	nextTab();
	uploadFile.value = { csv, file };
};

type Step = {
	component: Component;
	next: (...args: any[]) => void;
	prev: () => void;
};

const allComponents: Step[] = [
	{ component: StepWelcome, next: nextTab, prev: previousTab },
	{ component: StepSelect, next: nextTabSelect, prev: previousTab },
	{ component: StepImport, next: nextTab, prev: previousTab },
	{ component: StepCongratulations, next: nextTab, prev: backToCsvTab },
];

const stepsComponents = props.skipWelcome
	? allComponents.slice(1)
	: allComponents;
</script>

<style scoped>
.slide-fade-enter-active {
	transition: all 0.5s ease-out;
}

.slide-fade-leave-active {
	transition: all 0.2s cubic-bezier(0, 0.5, 0.8, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
	transform: translateX(100%);
	opacity: 0;
}
</style>
