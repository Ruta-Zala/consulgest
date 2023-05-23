<template>
	<div class="w-full">
		<h3 class="text-[22px] text-c-dark-blue font-medium mb-4">
			{{ t('team.user.header_text') }}
		</h3>
		<Form v-slot="{ errors }" :validation-schema="schema" @submit="onSubmit">
			<div class="flex flex-col lg:flex-row">
				<div class="w-full">
					<div class="block md:flex">
						<div class="flex-1 relative md:mr-4 mb-4">
							<label class="label pb-1 text-sm w-fit">
								<span
									class="label-text"
									:class="[
										errors.firstName ? 'text-red-500 ' : 'text-c-dark-blue',
									]"
								>
									{{ t('team.user.form.first_name') }}
								</span>
							</label>
							<Field v-slot="{ field }" type="text" name="firstName">
								<div class="relative">
									<input
										type="text"
										class="input w-full input-bordered text-c-dark-blue focus:outline-none focus:border-c-deep-blue"
										:placeholder="t('placeholder.type_here')"
										:class="[
											errors.firstName
												? 'border-red-500'
												: 'border-c-input-grey',
										]"
										v-bind="field"
									/>
								</div>
							</Field>
							<div class="text-red-500 absolute -bottom-5 text-xs">
								{{ errors.firstName }}
							</div>
						</div>
						<div class="flex-1 relative mb-4">
							<label class="label pb-1 text-sm w-fit">
								<span
									class="label-text"
									:class="[
										errors.surname ? 'text-red-500 ' : 'text-c-dark-blue',
									]"
								>
									{{ t('team.user.form.surname') }}
								</span>
							</label>
							<Field v-slot="{ field }" type="text" name="surname">
								<div class="relative">
									<input
										type="text"
										class="input w-full input-bordered text-c-dark-blue focus:outline-none focus:border-c-deep-blue"
										:placeholder="t('placeholder.type_here')"
										:class="[
											errors.surname ? 'border-red-500' : 'border-c-input-grey',
										]"
										v-bind="field"
									/>
								</div>
							</Field>
							<div class="text-red-500 absolute -bottom-5 text-xs">
								{{ errors.surname }}
							</div>
						</div>
					</div>
					<div class="block md:flex">
						<div class="flex-1 relative md:mr-4 mb-4">
							<label class="label pb-1 text-sm w-fit">
								<span
									class="label-text"
									:class="[errors.email ? 'text-red-500 ' : 'text-c-dark-blue']"
								>
									{{ t('team.user.form.email') }}
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
						<div class="flex-1 relative mb-4">
							<label class="label pb-1 text-sm w-fit">
								<span
									class="label-text"
									:class="[errors.phone ? 'text-red-500 ' : 'text-c-dark-blue']"
								>
									{{ t('team.user.form.phone') }}
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
					<div class="block md:flex">
						<div class="flex-1 relative md:mr-4 mb-4">
							<label class="label pb-1 text-sm w-fit">
								<span
									class="label-text"
									:class="[
										errors.location ? 'text-red-500 ' : 'text-c-dark-blue',
									]"
								>
									{{ t('team.user.form.company') }}
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
						<div class="flex-1 relative mb-4">
							<label class="label pb-1 text-sm w-fit">
								<span
									class="label-text"
									:class="[errors.role ? 'text-red-500 ' : 'text-c-dark-blue']"
								>
									{{ t('team.user.form.role') }}
								</span>
							</label>
							<Field v-slot="{ field }" type="text" name="role">
								<div class="relative">
									<select
										class="text-sm font-normal select w-full input-bordered text-c-dark-blue focus:outline-none focus:border-c-deep-blue"
										:class="[
											errors.role ? 'border-red-500' : 'border-c-input-grey',
										]"
										v-bind="field"
									>
										<option value="">
											{{ t('team.user.form.select') }}
										</option>
										<option value="User">User</option>
									</select>
								</div>
							</Field>
							<div class="text-red-500 absolute -bottom-5 text-xs">
								{{ errors.role }}
							</div>
						</div>
					</div>
					<div class="form-control relative md:mr-4">
						<label class="label pb-1 text-sm w-fit">
							<span
								class="label-text"
								:class="[
									errors.userStatus ? 'text-red-500 ' : 'text-c-dark-blue',
								]"
							>
								{{ t('team.user.form.user_status') }}
							</span>
						</label>
						<Field v-slot="{ field }" type="text" name="userStatus">
							<div class="relative">
								<select
									class="text-sm font-normal select w-full md:w-1/2 input-bordered text-c-dark-blue focus:outline-none focus:border-c-deep-blue"
									:class="[
										errors.userStatus
											? 'border-red-500'
											: 'border-c-input-grey',
									]"
									v-bind="field"
								>
									<option value="">
										{{ t('team.user.form.select') }}
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
			</div>
			<div class="mt-16 text-right w-full">
				<a
					class="btn btn-link mr-8 text-sm font-normal text-c-dark-blue capitalize"
				>
					{{ t('team.user.form.cancel') }}
				</a>
				<button
					type="submit"
					class="btn btn-primary w-28 font-semibold bg-c-dark-blue capitalize"
				>
					{{ t('team.user.form.save') }}
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
import { phone } from '../../../utils/regex';

const { t } = useI18n();

const schema = object().shape({
	firstName: string().required(
		t('team.user.form.error_messages.first_name_required'),
	),
	surname: string().required(
		t('team.user.form.error_messages.surname_required'),
	),
	email: string()
		.required(t('team.user.form.error_messages.email_required'))
		.email(t('team.user.form.error_messages.email_invalid')),
	phone: string()
		.required(t('team.user.form.error_messages.phone_required'))
		.matches(phone, t('team.user.form.error_messages.phone_invalid')),
	location: string().required(
		t('team.user.form.error_messages.location_required'),
	),
	role: string().required(t('team.user.form.error_messages.role_required')),
	userStatus: string().required(
		t('team.user.form.error_messages.user_status_required'),
	),
});

const userStatuses = [
	{
		name: t('team.user.user_statuses.active'),
		value: t('team.user.user_statuses.active'),
	},
	{
		name: t('team.user.user_statuses.frozen'),
		value: t('team.user.user_statuses.frozen'),
	},
	{
		name: t('team.user.user_statuses.blocked'),
		value: t('team.user.user_statuses.blocked'),
	},
];

const success = ref(false);
function onSubmit() {
	success.value = true;
}
</script>
