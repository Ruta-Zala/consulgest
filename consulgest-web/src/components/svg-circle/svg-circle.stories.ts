import { Meta, StoryFn } from '@storybook/vue3';
import { defineComponent } from '@vue/runtime-core';
import Component from './svg-circle.component.vue';
export default {
	title: 'Components / Svg Circle',
	component: Component,
} as Meta;

const html = String.raw;

export const SvgCircle: StoryFn = () => {
	return defineComponent({
		components: { SvgCircle: Component },
		template: html`
			<div class="inline-grid items-center justify-items-center">
				<SvgCircle
					:stroke-width="14"
					:diameter="210"
					:total="100"
					:current="65"
					class="row-span-full col-span-full text-red-100"
				/>
				<SvgCircle
					:stroke-width="14"
					:diameter="160"
					:total="100"
					:current="25"
					class="row-span-full col-span-full"
					foreground-color="text-c-success"
				/>
			</div>
		`,
	});
};
