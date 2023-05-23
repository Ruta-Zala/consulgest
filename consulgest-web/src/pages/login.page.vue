<template>
	<div>
		<div class="hero h-screen font-sans">
			<div
				class="hero-content max-w-full flex-col lg:flex-row w-full h-full justify-start lg:justify-center gap-8 2xl:gap-14 overflow-auto lg:overflow-hidden"
			>
				<div class="h-full max-w-lg relative">
					<div
						v-for="(banner, index) in bannerList"
						:key="index"
						class="h-full relative"
						:class="index === currentIndex ? 'block' : 'hidden'"
					>
						<div class="relative h-full w-full">
							<img
								:src="`/src/assets/images${banner.imgSrc}`"
								:alt="banner.imgSrc"
								class="rounded-3xl h-full max-w-full object-cover"
							/>
							<div
								class="bg-black opacity-60 absolute inset-0 rounded-3xl"
							></div>
						</div>
						<div
							class="absolute text-white px-2 w-full md:px-16 top-5 md:top-56"
						>
							<IconPowerAI class="h-16 w-16 max-w-2xl"></IconPowerAI>
							<div class="mt-10">
								<span class="text-3xl">{{ banner.title }}</span>
								<div class="mt-10 text-2xl font-light">
									{{ banner.subTitle }}
								</div>
							</div>
							<ul class="flex justify-end gap-2 pt-9">
								<li
									v-for="(step, indexList) in bannerList"
									:key="indexList"
									class="h-2 w-2 rounded-full"
									:class="
										indexList === currentIndex ? 'bg-c-deep-blue' : 'bg-c-grey'
									"
								></li>
							</ul>
						</div>
					</div>
				</div>
				<div class="flex-1 h-full flex justify-between flex-col">
					<div class="pt-8">
						<img
							src="../assets/images/logo.png"
							alt="logo"
							class="max-w-sm rounded-lg w-12"
						/>
					</div>
					<div class="flex justify-center">
						<div class="w-full xl:w-4/6 2xl:w-2/6 relative mb-16">
							<h1 class="text-3xl text-c-dark-blue font-semibold mt-4 lg:mt-0">
								{{ t('login.right_sidebar.title') }}
							</h1>
							<p class="pb-12 pt-3 text-c-dark-blue">
								{{ t('login.right_sidebar.sub_title') }}
							</p>
							<Form
								v-slot="{ errors }"
								:validation-schema="schema"
								@submit="onSubmit"
							>
								<div class="form-control w-full relative mb-5">
									<label class="label pb-1">
										<span
											class="label-text"
											:class="[
												errors.userName ? 'text-red-500 ' : 'text-c-light-grey',
											]"
										>
											{{ t('login.right_sidebar.user_name') }}
										</span>
									</label>
									<Field v-slot="{ field }" name="userName">
										<div class="relative">
											<IconPerson
												class="absolute top-2/4 transform -translate-y-2/4 left-4 text-c-dark-blue w-4 h-4"
											></IconPerson>
											<input
												v-model="username"
												type="text"
												class="input input-bordered w-full pl-11 focus:outline-none focus:border-c-deep-blue text-c-dark-blue"
												:placeholder="t('placeholder.type_here')"
												:class="[
													errors.userName ? 'border-red-500' : 'border-c-grey',
												]"
												v-bind="field"
											/>
										</div>
									</Field>
									<div class="text-red-500 absolute -bottom-5 text-xs">
										{{ errors.userName }}
									</div>
								</div>
								<div class="form-control w-full relative mb-5">
									<label class="label pb-1">
										<span
											class="label-text"
											:class="[
												errors.userPassword
													? 'text-red-500 '
													: 'text-c-light-grey',
											]"
										>
											{{ t('login.right_sidebar.password') }}
										</span>
									</label>
									<Field v-slot="{ field }" type="password" name="userPassword">
										<div class="relative">
											<IconPasswordKey
												class="absolute top-2/4 transform -translate-y-2/4 left-4 text-c-dark-blue w-4 h-4"
											>
											</IconPasswordKey>
											<input
												v-model="password"
												:type="hidePassword ? 'password' : 'type'"
												class="input input-bordered w-full pl-11 focus:outline-none focus:border-c-deep-blue text-c-dark-blue"
												:placeholder="t('placeholder.type_here')"
												:class="[
													errors.userPassword
														? 'border-red-500'
														: 'border-c-grey',
												]"
												v-bind="field"
											/>
											<button
												class="btn btn-link btn-xs absolute top-3 right-4"
												@click.prevent="toggleShow"
											>
												<IconPassword
													v-if="!hidePassword"
													class="text-c-dark-blue w-4 h-4"
												>
												</IconPassword>
												<IconPasswordHide
													v-else
													class="text-c-dark-blue w-4 h-4"
												>
												</IconPasswordHide>
											</button>
										</div>
									</Field>
									<div class="text-red-500 absolute -bottom-5 text-xs">
										{{ errors.userPassword }}
									</div>
								</div>
								<div
									class="flex items-center justify-between text-c-light-grey pb-10"
								>
									<div class="form-control">
										<label class="label cursor-pointer">
											<input type="checkbox" :checked="true" class="checkbox" />
											<span class="label-text pl-2 text-c-light-grey">
												{{ t('login.right_sidebar.remember') }}
											</span>
										</label>
									</div>
									<a class="link link-hover text-sm"
										>{{ t('login.right_sidebar.forgot_password') }}?</a
									>
								</div>
								<button type="submit" class="btn btn-primary mr-1 w-full">
									{{ t('login.right_sidebar.title') }}
								</button>
							</Form>
							<div
								v-show="success"
								:class="errorMessage ? 'alert-error' : 'alert-success'"
								class="alert shadow-lg my-10 absolute -bottom-25"
							>
								<div>
									<svg
										xmlns="http://www.w3.org/2000/svg"
										class="stroke-current flex-shrink-0 h-6 w-6"
										fill="none"
										viewBox="0 0 24 24"
									>
										<path
											stroke-linecap="round"
											stroke-linejoin="round"
											stroke-width="2"
											d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
										/>
									</svg>
									<span v-if="errorMessage">{{ errorMessage }}</span>
									<span v-else>{{
										t('login.right_sidebar.success_message')
									}}</span>
								</div>
							</div>
						</div>
					</div>
					<p
						class="text-c-light-grey text-sm flex justify-center pb-8 pt-8 lg:pt-0"
					>
						© 2022 {{ t('login.right_sidebar.footer') }}
					</p>
				</div>
			</div>
		</div>
	</div>
</template>

<script lang="ts" setup>
import { useI18n } from 'vue-i18n';
import { ref, onMounted } from 'vue';
import { Form, Field } from 'vee-validate';
import { object, string } from 'yup';
import { useRouter } from 'vue-router';
import {
	IconPowerAI,
	IconPerson,
	IconPasswordKey,
	IconPassword,
	IconPasswordHide,
} from '../icons';
import { apiService } from '../api.service';
import { useCurrentUser } from '../composables/use-current-user';

const router = useRouter();

const { t } = useI18n();

const schema = object().shape({
	userName: string().required(t('login.right_sidebar.user_name_error')),
	userPassword: string().required(t('login.right_sidebar.password_error')),
});
const success = ref(false);
const currentIndex = ref(0);
const bannerList = [
	{
		imgSrc: '/login-slider-1.png',
		icon: 'IconPerson',
		title: 'Powerfull AI!',
		subTitle:
			'The days for running around and expect the best are over! Prioritise customers that are more likely to closure and increase results!',
	},
	{
		imgSrc: '/login-slider-2.png',
		icon: 'IconPerson',
		title: 'All-in-one dashboard',
		subTitle:
			'Specialized dashboard with easy and quick access to the most important metrics and suggestions that will assist you at closing cases and increase profitability',
	},
	{
		imgSrc: '/login-slider-3.png',
		icon: 'IconPerson',
		title: 'Consulgest',
		subTitle:
			"We are an all-in-one platform to manage all your debtor's dossiers from multiple sources, with a fully integrated AI system assisting and providing you with metrics and the best-associated course of action to increase the collection rate and diminish losses.",
	},
];

const username = ref('');
const password = ref('');
const hidePassword = ref(true);
let errorMessage = ref('');
const currentUser = useCurrentUser();

function onSubmit() {
	apiService
		.post('login/', {
			username: username.value,
			password: password.value,
		})
		.then((res) => {
			localStorage.setItem('access_token', res.data.access_token);
			currentUser.value = res.data.user;
			router.push('/onboarding');
		})
		.catch((e) => {
			success.value = true;
			errorMessage = e.response.data.non_field_errors.join('/n');
		});
}

function setAutoRoll() {
	setInterval(function () {
		addIndex();
	}, 2000);
}

function addIndex() {
	const newIndex = currentIndex.value + 1;
	currentIndex.value = newIndex === bannerList.length ? 0 : newIndex;
}

function toggleShow() {
	hidePassword.value = !hidePassword.value;
}

onMounted(() => {
	setAutoRoll();
});
</script>
