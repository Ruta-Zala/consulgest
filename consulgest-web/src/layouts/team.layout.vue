<template>
	<Header
		v-if="isTeamPage"
		:src="teamImage"
		:alt="teamImgAlt"
		:title="teamUserTitle"
		:icon="IconUsers"
		:sub-title="subUserTitle"
		:avatar="true"
		:sub-page="true"
	>
		<template #avatar>
			<div
				class="bg-c-deep-blue text-white h-9 min-w-[36px] w-9 rounded-full flex items-center justify-center font-bold"
			>
				IJ
			</div>
		</template>
	</Header>
	<Header
		v-else
		:src="teamImage"
		:alt="teamImgAlt"
		:title="teamTitle"
		:icon="IconUsers"
		:sub-title="subTitle"
	>
		<template #afterTitle>
			<div
				class="badge text-white bg-c-deep-blue px-5 text-xl mr-4 h-8 border-none"
			>
				32
			</div>
		</template>
	</Header>
	<TeamMenuComponent />
	<div class="bg-white py-11 px-16 flex-1">
		<RouterView name="default" />
	</div>
</template>

<script setup lang="ts">
import { useI18n } from 'vue-i18n';
import { RouterView, useRoute } from 'vue-router';
import { computed } from 'vue';
import Header from '../components/header/header.component.vue';
import teamImage from '../assets/images/team.svg';
import { IconUsers } from '../icons';
import TeamMenuComponent from '../pages/team/components/menu.component.vue';

const { t } = useI18n();
const teamTitle = t('team.header.title');
const teamUserTitle = t('team.user_profile.header.title');
const teamImgAlt = t('team.header.img_alt');
const subTitle = t('team.header.sub_title');
const subUserTitle = t('team.user_profile.header.sub_title');

const route = useRoute();

const isTeamPage = computed(() => {
	return (
		route.path.includes('/team/user') ||
		route.path.includes('/team/preferences') ||
		route.path.includes('/team/password')
	);
});
</script>
