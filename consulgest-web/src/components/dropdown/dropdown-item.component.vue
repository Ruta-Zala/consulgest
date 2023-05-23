<template>
	<MenuItem as="li" class="text-sm text-c-dark-blue cursor-pointer">
		<slot />
	</MenuItem>
</template>

<script lang="ts" setup>
import { MenuItem } from '@headlessui/vue';
</script>
