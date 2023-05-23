<template>
	<div class="py-16 px-20 w-full text-c-dark-blue bg-white flex-1">
		<h3 class="text-[22px] font-medium mt-8">
			{{ t('configuration.permission.header_text') }}
		</h3>
		<div class="mt-8">
			<div class="bg-c-grey-bg w-full flex py-2 items-center font-medium">
				<div class="flex-1 ml-2">
					{{ t('configuration.permission.toggle_header_one') }}
				</div>
				<div class="w-28 flex justify-center">
					{{ t('configuration.permission.toggle_one') }}
				</div>
				<div class="w-28 flex justify-center">
					{{ t('configuration.permission.toggle_two') }}
				</div>
				<div class="w-28 flex justify-center">
					{{ t('configuration.permission.toggle_third') }}
				</div>
			</div>
			<div>
				<div class="border-b-2 border-b-c-grey w-full flex py-4 items-center">
					<div class="flex-1 ml-2">
						{{ t('configuration.permission.toggle_action_one') }}
					</div>
					<div class="w-28 flex justify-center">
						<Toggle id="useDarkMode" />
					</div>
					<div class="w-28 flex justify-center">
						<Toggle id="useDarkMode" />
					</div>
					<div class="w-28 flex justify-center">
						<Toggle id="useDarkMode" />
					</div>
				</div>
				<div class="border-b-2 border-b-c-grey w-full flex py-4 items-center">
					<div class="flex-1 ml-2">
						{{ t('configuration.permission.toggle_action_two') }}
					</div>
					<div class="w-28 flex justify-center">
						<Toggle id="useDarkMode" />
					</div>
					<div class="w-28 flex justify-center">
						<Toggle id="useDarkMode" />
					</div>
					<div class="w-28 flex justify-center">
						<Toggle id="useDarkMode" />
					</div>
				</div>
				<div class="border-b-2 border-b-c-grey w-full flex py-4 items-center">
					<div class="flex-1 ml-2">
						{{ t('configuration.permission.toggle_action_third') }}
					</div>
					<div class="w-28 flex justify-center">
						<Toggle id="useDarkMode" />
					</div>
					<div class="w-28 flex justify-center">
						<Toggle id="useDarkMode" />
					</div>
					<div class="w-28 flex justify-center">
						<Toggle id="useDarkMode" />
					</div>
				</div>
			</div>
		</div>
		<div class="mt-14">
			<div class="bg-c-grey-bg w-full flex py-2 items-center font-medium">
				<div class="flex-1 ml-2">
					{{ t('configuration.permission.toggle_header_two') }}
				</div>
				<div class="w-28 flex justify-center">
					{{ t('configuration.permission.toggle_one') }}
				</div>
				<div class="w-28 flex justify-center">
					{{ t('configuration.permission.toggle_two') }}
				</div>
				<div class="w-28 flex justify-center">
					{{ t('configuration.permission.toggle_third') }}
				</div>
			</div>
			<div>
				<div class="border-b-2 border-b-c-grey w-full flex py-4 items-center">
					<div class="flex-1 ml-2">
						{{ t('configuration.permission.toggle_dossiers_one') }}
					</div>
					<div class="w-28 flex justify-center">
						<Toggle id="useDarkMode" />
					</div>
					<div class="w-28 flex justify-center">
						<Toggle id="useDarkMode" />
					</div>
					<div class="w-28 flex justify-center">
						<Toggle id="useDarkMode" />
					</div>
				</div>
				<div class="border-b-2 border-b-c-grey w-full flex py-4 items-center">
					<div class="flex-1 ml-2">
						{{ t('configuration.permission.toggle_dossiers_two') }}
					</div>
					<div class="w-28 flex justify-center">
						<Toggle id="useDarkMode" />
					</div>
					<div class="w-28 flex justify-center">
						<Toggle id="useDarkMode" />
					</div>
					<div class="w-28 flex justify-center">
						<Toggle id="useDarkMode" />
					</div>
				</div>
				<div class="border-b-2 border-b-c-grey w-full flex py-4 items-center">
					<div class="flex-1 ml-2">
						{{ t('configuration.permission.toggle_dossiers_third') }}
					</div>
					<div class="w-28 flex justify-center">
						<Toggle id="useDarkMode" />
					</div>
					<div class="w-28 flex justify-center">
						<Toggle id="useDarkMode" />
					</div>
					<div class="w-28 flex justify-center">
						<Toggle id="useDarkMode" />
					</div>
				</div>
			</div>
		</div>
		<div class="mt-16 text-right w-full">
			<a
				class="btn btn-link mr-8 text-sm font-normal text-c-dark-blue capitalize"
			>
				{{ t('configuration.system.form.cancel') }}
			</a>
			<button
				type="submit"
				class="btn btn-primary w-28 font-semibold capitalize"
			>
				{{ t('configuration.system.form.save') }}
			</button>
		</div>
	</div>
</template>

<script lang="ts" setup>
import { useI18n } from 'vue-i18n';
import Toggle from '../../components/toggle/toggle.component.vue';

const { t } = useI18n();
</script>
