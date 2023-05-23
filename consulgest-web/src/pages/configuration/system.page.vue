<template>
	<div class="py-16 px-20 w-full bg-white flex-1">
		<h3 class="text-[22px] text-c-dark-blue font-medium mb-4">
			{{ t('configuration.system.header_text') }}
		</h3>
		<Form v-slot="{ errors }" :validation-schema="schema" @submit="onSubmit">
			<div class="flex flex-col lg:flex-row">
				<div class="w-full lg:w-3/4">
					<div class="form-control relative mb-4">
						<label class="label pb-1 text-sm">
							<span
								class="label-text"
								:class="[
									errors.companyName ? 'text-red-500 ' : 'text-c-dark-blue',
								]"
							>
								{{ t('configuration.system.form.company_name') }}
							</span>
						</label>
						<Field v-slot="{ field }" type="text" name="companyName">
							<div class="relative">
								<input
									type="text"
									class="input w-full input-bordered text-c-dark-blue focus:outline-none focus:border-c-deep-blue"
									:placeholder="t('placeholder.type_here')"
									:class="[
										errors.companyName
											? 'border-red-500'
											: 'border-c-input-grey',
									]"
									v-bind="field"
								/>
							</div>
						</Field>
						<div class="text-red-500 absolute -bottom-5 text-xs">
							{{ errors.companyName }}
						</div>
					</div>
					<div class="flex">
						<div class="grow relative mr-4 mb-4">
							<label class="label pb-1 text-sm w-fit">
								<span
									class="label-text"
									:class="[errors.email ? 'text-red-500 ' : 'text-c-dark-blue']"
								>
									{{ t('configuration.system.form.email') }}
								</span>
							</label>
							<Field v-slot="{ field }" type="email" name="email">
								<div class="relative">
									<input
										type="text"
										class="input w-full input-bordered text-c-dark-blue focus:outline-none focus:border-c-deep-blue"
										:placeholder="t('placeholder.type_here')"
										:class="[
											errors.email ? 'border-red-500' : 'border-c-input-grey',
										]"
										v-bind="field"
									/>
								</div>
							</Field>
							<div class="text-red-500 absolute -bottom-5 text-xs">
								{{ errors.email }}
							</div>
						</div>
						<div class="grow relative mb-4">
							<label class="label pb-1 text-sm w-fit">
								<span
									class="label-text"
									:class="[errors.phone ? 'text-red-500 ' : 'text-c-dark-blue']"
								>
									{{ t('configuration.system.form.phone') }}
								</span>
							</label>
							<Field v-slot="{ field }" type="text" name="phone">
								<div class="relative">
									<input
										type="text"
										class="input w-full input-bordered text-c-dark-blue focus:outline-none focus:border-c-deep-blue"
										:placeholder="t('placeholder.type_here')"
										:class="[
											errors.phone ? 'border-red-500' : 'border-c-input-grey',
										]"
										v-bind="field"
									/>
								</div>
							</Field>
							<div class="text-red-500 absolute -bottom-5 text-xs">
								{{ errors.phone }}
							</div>
						</div>
					</div>
					<div class="flex">
						<div class="grow relative mr-4 mb-4">
							<label class="label pb-1 text-sm w-fit">
								<span
									class="label-text"
									:class="[
										errors.location ? 'text-red-500 ' : 'text-c-dark-blue',
									]"
								>
									{{ t('configuration.system.form.location') }}
								</span>
							</label>
							<Field v-slot="{ field }" type="location" name="location">
								<div class="relative">
									<input
										type="text"
										class="input w-full input-bordered text-c-dark-blue focus:outline-none focus:border-c-deep-blue"
										:placeholder="t('placeholder.type_here')"
										:class="[
											errors.location
												? 'border-red-500'
												: 'border-c-input-grey',
										]"
										v-bind="field"
									/>
								</div>
							</Field>
							<div class="text-red-500 absolute -bottom-5 text-xs">
								{{ errors.location }}
							</div>
						</div>
						<div class="grow relative mr-4 mb-4">
							<label class="label pb-1 text-sm w-fit">
								<span
									class="label-text"
									:class="[errors.state ? 'text-red-500 ' : 'text-c-dark-blue']"
								>
									{{ t('configuration.system.form.state') }}
								</span>
							</label>
							<Field v-slot="{ field }" type="text" name="state">
								<div class="relative">
									<select
										class="text-sm font-normal select w-full input-bordered text-c-dark-blue focus:outline-none focus:border-c-deep-blue"
										:class="[
											errors.state ? 'border-red-500' : 'border-c-input-grey',
										]"
										v-bind="field"
									>
										<option value="">
											{{ t('configuration.system.form.select') }}
										</option>
										<option value="Milan">Milan</option>
									</select>
								</div>
							</Field>
							<div class="text-red-500 absolute -bottom-5 text-xs">
								{{ errors.state }}
							</div>
						</div>
						<div class="grow relative mb-4">
							<label class="label pb-1 text-sm w-fit">
								<span
									class="label-text"
									:class="[
										errors.zipCode ? 'text-red-500 ' : 'text-c-dark-blue',
									]"
								>
									{{ t('configuration.system.form.zip_code') }}
								</span>
							</label>
							<Field v-slot="{ field }" type="text" name="zipCode">
								<div class="relative">
									<input
										type="text"
										class="input w-full input-bordered text-c-dark-blue focus:outline-none focus:border-c-deep-blue"
										:placeholder="t('placeholder.type_here')"
										:class="[
											errors.zipCode ? 'border-red-500' : 'border-c-input-grey',
										]"
										v-bind="field"
									/>
								</div>
							</Field>
							<div class="text-red-500 absolute -bottom-5 text-xs">
								{{ errors.zipCode }}
							</div>
						</div>
					</div>
					<div class="form-control relative">
						<label class="label pb-1 text-sm w-fit">
							<span
								class="label-text"
								:class="[
									errors.userStatus ? 'text-red-500 ' : 'text-c-dark-blue',
								]"
							>
								{{ t('configuration.system.form.user_status') }}
							</span>
						</label>
						<Field v-slot="{ field }" type="text" name="userStatus">
							<div class="relative">
								<select
									class="text-sm font-normal select w-1/2 input-bordered text-c-dark-blue focus:outline-none focus:border-c-deep-blue"
									:class="[
										errors.userStatus
											? 'border-red-500'
											: 'border-c-input-grey',
									]"
									v-bind="field"
								>
									<option value="">
										{{ t('configuration.system.form.select') }}
									</option>
									<option
										v-for="(status, index) in userStatuses"
										:key="index"
										:value="status.value"
									>
										{{ status.name }}
									</option>
								</select>
							</div>
						</Field>
						<div class="text-red-500 absolute -bottom-5 text-xs">
							{{ errors.userStatus }}
						</div>
					</div>
				</div>
				<div class="w-full lg:w-1/4">
					<div
						class="border border-c-grey h-[367px] w-full lg:w-3/4 mx-auto my-5 lg:my-0 px-4"
					>
						<h4 class="pl-4 pt-6 text-base font-normal text-c-dark-blue">
							{{ t('configuration.system.form.system_logo') }}
						</h4>
						<img
							src="../../assets/images/logo.png"
							:alt="t('configuration.system.form.system_logo')"
							class="mx-auto my-6 w-[192px]"
						/>
						<label
							class="grid justify-center w-full h-auto p-3 transition bg-white border-2 border-dashed rounded-md appearance-none cursor-pointer border-c-deep-blue focus:outline-none"
						>
							<div class="flex items-center">
								<span class="font-normal text-c-dark-blue text-sm">
									{{ t('configuration.system.form.replace_logo') }}
								</span>
							</div>
							<input type="file" name="file_upload" class="hidden" />
						</label>
					</div>
				</div>
			</div>
			<div class="mt-16 text-right w-full">
				<a
					class="btn btn-link mr-8 text-sm font-normal text-c-dark-blue capitalize"
				>
					{{ t('configuration.system.form.cancel') }}
				</a>
				<button type="submit" class="btn btn-primary w-28 capitalize">
					{{ t('configuration.system.form.save') }}
				</button>
			</div>
		</Form>
	</div>
</template>

<script lang="ts" setup>
import { useI18n } from 'vue-i18n';
import { ref } from 'vue';
import { Form, Field } from 'vee-validate';
import { object, string } from 'yup';
import { phone, zipCode } from '../../utils/regex';

const { t } = useI18n();

const schema = object().shape({
	companyName: string().required(
		t('configuration.system.form.error_messages.company_name_required'),
	),
	email: string()
		.required(t('configuration.system.form.error_messages.email_required'))
		.email(t('configuration.system.form.error_messages.email_invalid')),
	phone: string()
		.required(t('configuration.system.form.error_messages.phone_required'))
		.matches(
			phone,
			t('configuration.system.form.error_messages.phone_invalid'),
		),
	location: string().required(
		t('configuration.system.form.error_messages.location_required'),
	),
	state: string().required(
		t('configuration.system.form.error_messages.state_required'),
	),
	zipCode: string()
		.required(t('configuration.system.form.error_messages.zip_required'))
		.matches(
			zipCode,
			t('configuration.system.form.error_messages.zip_invalid'),
		),
	userStatus: string().required(
		t('configuration.system.form.error_messages.user_status_required'),
	),
});

const userStatuses = [
	{
		name: t('configuration.system.user_statuses.active'),
		value: t('configuration.system.user_statuses.active'),
	},
	{
		name: t('configuration.system.user_statuses.frozen'),
		value: t('configuration.system.user_statuses.frozen'),
	},
	{
		name: t('configuration.system.user_statuses.blocked'),
		value: t('configuration.system.user_statuses.blocked'),
	},
];

const success = ref(false);
function onSubmit() {
	success.value = true;
}
</script>
