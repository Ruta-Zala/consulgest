<template>
	<div class="py-16 px-20 w-full text-c-dark-blue bg-white flex-1">
		<h3 class="text-[22px] text-c-dark-blue font-medium mb-4">
			{{ t('configuration.preferences.header_text') }}
		</h3>
		<div class="space-y-2">
			<span class="text-sm font-normal">{{
				t('configuration.preferences.avatar_color')
			}}</span>
			<ul class="flex flex-row">
				<li class="pr-6 flex items-center">
					<div
						:class="[
							'rounded-full h-12 w-12',
							'flex justify-center items-center',
							'text-white font-semibold text-xl',
							`${avatarColor}`,
						]"
					>
						Ij
					</div>
				</li>
				<li
					v-for="(avatar, index) in avatarColorClasses"
					:key="index"
					class="pr-6 flex items-center"
				>
					<div
						:class="[
							'cursor-pointer rounded-full p-[2px]',
							'border-2 border-transparent',
							avatar.border,
						]"
						@click="setAvatarColor(avatar.color)"
					>
						<div :class="['rounded-full h-3 w-3', `${avatar.color}`]"></div>
					</div>
				</li>
			</ul>
		</div>
		<div class="mt-8">
			<h3 class="text-[22px] font-medium mb-4">
				{{ t('configuration.preferences.language_region') }}
			</h3>
			<div class="form-control relative">
				<label class="label pb-1 text-sm w-fit">
					<span class="label-text text-c-dark-blue">
						{{ t('configuration.preferences.language_interface') }}
					</span>
				</label>
				<div class="relative">
					<select
						id="language-interface"
						class="text-sm font-normal select w-1/3 input-bordered text-c-dark-blue focus:outline-none focus:border-c-deep-blue"
					>
						<option value="English">English</option>
					</select>
				</div>
			</div>
			<div class="form-control relative">
				<label class="label pb-1 text-sm w-fit">
					<span class="label-text text-c-dark-blue">
						{{ t('configuration.preferences.timezone') }}
					</span>
				</label>
				<div class="relative">
					<select
						id="timezone"
						class="text-sm font-normal select w-1/3 input-bordered text-c-dark-blue focus:outline-none focus:border-c-deep-blue"
					>
						<option value="Europe/Lisbon">Europe/Lisbon</option>
					</select>
				</div>
			</div>

			<h3 class="text-[22px] font-medium mt-8">
				{{ t('configuration.preferences.system_preferences') }}
			</h3>

			<div class="border-b-2 border-b-c-grey w-full flex mt-6 py-4">
				<div class="relative my-auto mr-6">
					<Toggle id="systemNotification" />
				</div>
				<div class="relative">
					<label for="systemNotification" class="cursor-pointer">
						<h1 class="text-base font-semibold">
							{{ t('configuration.preferences.system_notifications') }}
						</h1>
						<span class="text-sm font-normal">{{
							t('configuration.preferences.system_notifications_detail')
						}}</span>
					</label>
				</div>
			</div>
			<div class="border-b-2 border-b-c-grey w-full flex py-4">
				<div class="relative my-auto mr-6">
					<Toggle id="useDarkMode" />
				</div>
				<div class="relative">
					<label for="useDarkMode" class="cursor-pointer">
						<h1 class="text-base font-semibold">
							{{ t('configuration.preferences.use_dark_mode') }}
						</h1>
						<span class="text-sm font-normal">{{
							t('configuration.preferences.system_general_text')
						}}</span>
					</label>
				</div>
			</div>
			<div class="border-b-2 border-b-c-grey w-full flex py-4">
				<div class="relative my-auto mr-6">
					<Toggle id="showNotifications" />
				</div>
				<div class="relative">
					<label for="showNotifications" class="cursor-pointer">
						<h1 class="text-base font-semibold">
							{{ t('configuration.preferences.show_ai_notifications') }}
						</h1>
						<span class="text-sm font-normal">{{
							t('configuration.preferences.system_general_text')
						}}</span>
					</label>
				</div>
			</div>
			<div class="border-b-2 border-b-c-grey w-full flex py-4">
				<div class="relative my-auto mr-6">
					<Toggle id="trackGoals" />
				</div>
				<div class="relative">
					<label for="trackGoals" class="cursor-pointer">
						<h1 class="text-base font-semibold">
							{{ t('configuration.preferences.track_goals') }}
						</h1>
						<span class="text-sm font-normal">{{
							t('configuration.preferences.system_general_text')
						}}</span>
					</label>
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
	</div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { useI18n } from 'vue-i18n';
import Toggle from '../../components/toggle/toggle.component.vue';

const { t } = useI18n();

const avatarColorClasses = [
	{ color: 'bg-c-linear-orizon', border: 'hover:border-[#7368FF]' },
	{ color: 'bg-c-grey', border: 'hover:border-c-grey' },
	{ color: 'bg-c-blue', border: 'hover:border-c-blue' },
	{ color: 'bg-c-warning', border: 'hover:border-c-warning' },
	{ color: 'bg-c-deep-blue', border: 'hover:border-c-deep-blue' },
	{ color: 'bg-[#828282]', border: 'hover:border-[#828282]' },
	{ color: 'bg-[#F2C94C]', border: 'hover:border-[#F2C94C]' },
	{ color: 'bg-[#EB5757]', border: 'hover:border-[#EB5757]' },
	{ color: 'bg-[#BB6BD9]', border: 'hover:border-[#BB6BD9]' },
	{ color: 'bg-[#2F80ED]', border: 'hover:border-[#2F80ED]' },
	{ color: 'bg-c-success', border: 'hover:border-c-success' },
];

const avatarColor = ref('bg-c-deep-blue');

const setAvatarColor = (color: string) => {
	avatarColor.value = color;
};
</script>
