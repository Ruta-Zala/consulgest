import { Meta, StoryFn } from '@storybook/vue3';
import { defineComponent } from '@vue/runtime-core';
import { ref } from 'vue';
import Component from './toggle.component.vue';

export default {
	title: 'Components / Toggle',
	component: Component,
} as Meta;

const html = String.raw;

export const Toggle: StoryFn = () => {
	return defineComponent({
		components: {
			Toggle: Component,
		},
		setup() {
			const checked1 = ref(false);
			const checked2 = ref(false);
			return { checked1, checked2 };
		},
		template: html` <div class="w-fit">
			<Toggle v-model="checked1" label="Label 1" />
			<Toggle v-model="checked2" label="Label 2" />
		</div>`,
	});
};
