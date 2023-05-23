<template>
	<div
		class="navbar py-0 px-8 lg:px-16 min-h-fit"
		:class="collapseHeader ? 'h-[178px]' : 'h-[64px]'"
	>
		<div class="navbar-start text-c-dark-blue">
			<div class="flex items-center">
				<div class="mr-3 lg:mr-4">
					<slot v-if="avatar" name="avatar"></slot>
					<component :is="icon" v-else class="h-12 w-12" />
				</div>
				<IconDropdown v-if="subPage" class="h-4 w-4 rotate-90 mr-2" />
				<span class="text-[28px] font-bold">{{ title }}</span>
			</div>
			<div
				v-if="subTitle != null"
				class="h-10 lg:h-12 mx-2 lg:mx-6 w-px bg-c-input-grey"
			/>
			<slot name="afterTitle"></slot>
			<div class="text-2xl font-light">{{ subTitle }}</div>
		</div>
		<div class="navbar-end h-full">
			<div class="h-full overflow-hidden flex items-center">
				<img :src="src" :alt="alt" class="h-full" />
			</div>
			<button
				class="btn btn-ghost flex items-center text-c-light-grey focus:outline-none w-28"
				:class="{ 'self-baseline mt-4': collapseHeader }"
				@click="toggleHeader"
			>
				<div
					v-if="!collapseHeader"
					class="flex items-center gap-2 w-full justify-between"
				>
					<span class="text-sm">{{ t('commonButtons.show') }}</span>
					<IconPassword class="h-4 w-4" />
				</div>
				<div v-else class="flex items-center gap-2 w-full justify-between">
					<span class="text-sm">{{ t('commonButtons.hide') }}</span>
					<IconPasswordHide class="h-4 w-4" />
				</div>
			</button>
		</div>
	</div>
</template>

<script lang="ts" setup>
import { ref, DefineComponent, PropType } from 'vue';
import { useI18n } from 'vue-i18n';
import { IconPassword, IconPasswordHide } from '../../icons';
import IconDropdown from '../../icons/IconDropdown.vue';

const { t } = useI18n();

const collapseHeader = ref(false);

function toggleHeader() {
	collapseHeader.value = !collapseHeader.value;
}

defineProps({
	src: {
		type: String,
		required: true,
	},
	alt: {
		type: String,
		required: true,
	},
	title: {
		type: String,
		required: true,
	},
	subTitle: {
		type: String,
		default: null,
		required: false,
	},
	icon: {
		type: Object as PropType<DefineComponent>,
		required: true,
	},
	avatar: {
		type: Boolean as PropType<boolean>,
		default: false,
	},
	subPage: {
		type: Boolean as PropType<boolean>,
		default: false,
	},
});
</script>
