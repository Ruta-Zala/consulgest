<template>
	<div class="h-screen grid grid-cols-[auto_minmax(0,1fr)] overflow-hidden">
		<SidebarComponent />
		<div
			class="overflow-y-auto bg-c-ghost-white overflow-x-hidden flex flex-col"
		>
			<RouterView name="default" />
		</div>
	</div>
</template>

<script lang="ts" setup>
import { RouterView } from 'vue-router';
import SidebarComponent from '../components/sidebar.component.vue';
</script>
