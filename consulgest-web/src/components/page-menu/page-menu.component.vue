<template>
	<ul class="menu menu-horizontal flex-wrap p-0 text-sm gap-2">
		<li v-for="(menu, index) in options" :key="index">
			<RouterLink v-slot="{ isActive }" :to="menu.href" class="p-0 rounded-lg">
				<span
					:class="[
						'rounded-lg min-h-8 h-11 flex items-center px-4',
						'hover:bg-c-ghost-white',
						'hover:text-c-deep-blue',
						border,
						isActive === true ? activeClass : 'text-c-dark-blue',
					]"
				>
					{{ menu.title }}</span
				>
			</RouterLink>
		</li>
	</ul>
</template>

<script lang="ts" setup>
import { PropType } from 'vue';
import { RouterLink } from 'vue-router';

type PageMenu = {
	title: string;
	href: string;
};

defineProps({
	options: {
		type: Array as PropType<Array<PageMenu>>,
		required: true,
	},
	border: {
		type: String,
		default: 'border border-c-grey hover:border-c-deep-blue',
	},
	activeClass: {
		type: String,
		default: 'border-c-deep-blue bg-c-grey-bg text-c-deep-blue',
	},
});
</script>
