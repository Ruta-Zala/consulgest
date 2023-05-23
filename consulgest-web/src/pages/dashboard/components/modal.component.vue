<template>
	<Dialog as="div" :open="isOpen">
		<DialogPanel
			as="div"
			class="w-6/12 fixed bottom-14 right-14 max-w-md rounded-2xl bg-white p-6 shadow-xl"
		>
			<DashboardCarousel @close="closeModal" />
		</DialogPanel>
	</Dialog>
</template>

<script setup>
import { ref } from 'vue';
import { Dialog, DialogPanel } from '@headlessui/vue';

import DashboardCarousel from './carousel.component.vue';

const isOpen = ref(true);

function closeModal(value) {
	isOpen.value = value;
}
</script>
