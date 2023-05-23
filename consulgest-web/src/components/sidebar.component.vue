<template>
	<div
		class="flex flex-col w-20 justify-between py-6 shadow-xl z-10 items-center"
	>
		<div>
			<img src="../assets/images/logo.png" alt="logo" class="w-11 h-11" />
		</div>
		<div class="flex flex-col justify-center items-center gap-3 mt-6">
			<RouterLink v-slot="{ isActive, href, navigate }" to="/dashboard">
				<a
					class="rounded-lg btn-square flex items-center justify-center"
					:href="href"
					:class="
						isActive
							? 'text-c-deep-blue bg-c-ghost-white'
							: 'bg-transparent text-c-dark-blue'
					"
					@click="navigate"
				>
					<IconMenu class="h-5 w-5" />
				</a>
			</RouterLink>
			<RouterLink v-slot="{ isActive, href, navigate }" to="/dossiers">
				<a
					class="rounded-lg btn-square flex items-center justify-center"
					:href="href"
					:class="
						isActive
							? 'text-c-deep-blue bg-c-ghost-white'
							: 'bg-transparent text-c-dark-blue'
					"
					@click="navigate"
				>
					<IconBook class="h-6 w-6" />
				</a>
			</RouterLink>
			<RouterLink v-slot="{ isActive, href, navigate }" to="/consul">
				<a
					class="rounded-lg btn-square flex items-center justify-center"
					:href="href"
					:class="
						isActive
							? 'text-c-deep-blue bg-c-ghost-white'
							: 'bg-transparent text-c-dark-blue'
					"
					@click="navigate"
				>
					<IconCpu class="h-6 w-6" />
				</a>
			</RouterLink>
			<RouterLink v-slot="{ isActive, href, navigate }" to="/team">
				<a
					class="rounded-lg btn-square flex items-center justify-center"
					:href="href"
					:class="
						isActive
							? 'text-c-deep-blue bg-c-ghost-white'
							: 'bg-transparent text-c-dark-blue'
					"
					@click="navigate"
				>
					<IconUsers class="h-6 w-6" />
				</a>
			</RouterLink>
			<RouterLink v-slot="{ href, navigate }" to="/import-dossier">
				<a
					class="rounded-lg btn-square flex items-center justify-center bg-c-success text-white"
					:href="href"
					@click="navigate"
				>
					<IconDownload class="h-6 w-6" />
				</a>
			</RouterLink>
		</div>
		<div class="flex flex-col justify-center items-center gap-3">
			<div class="divider"></div>
			<img
				width="42"
				height="42"
				src="https://picsum.photos/42/42"
				alt="avatar"
				class="rounded-full"
			/>
			<RouterLink v-slot="{ isActive, href, navigate }" to="/configuration">
				<a
					class="rounded-lg btn-square flex items-center justify-center"
					:href="href"
					:class="
						isActive
							? 'text-c-deep-blue bg-c-ghost-white'
							: 'bg-transparent text-c-dark-blue'
					"
					@click="navigate"
				>
					<IconSetting class="h-6 w-6" />
				</a>
			</RouterLink>
			<RouterLink v-slot="{ isActive, href, navigate }" to="/">
				<a
					class="rounded-lg btn-square flex items-center justify-center"
					:href="href"
					:class="
						isActive
							? 'text-c-deep-blue bg-c-ghost-white'
							: 'bg-transparent text-c-dark-blue'
					"
					@click="navigate"
				>
					<IconLogout class="h-6 w-6" />
				</a>
			</RouterLink>
		</div>
	</div>
</template>

<script setup lang="ts">
import { RouterLink } from 'vue-router';
import {
	IconMenu,
	IconBook,
	IconCpu,
	IconUsers,
	IconDownload,
	IconSetting,
	IconLogout,
} from '../icons';
</script>
