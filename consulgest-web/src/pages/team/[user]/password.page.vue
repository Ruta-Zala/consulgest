<template>
	<div class="w-full">
		<h3 class="text-[22px] text-c-dark-blue font-medium mb-4">
			{{ t('team.password.header_text') }}
		</h3>
		<Form v-slot="{ errors }" :validation-schema="schema" @submit="onSubmit">
			<div class="flex flex-col lg:flex-row">
				<div class="w-full">
					<div class="flex-1 relative mb-4">
						<label class="label pb-1 text-sm w-fit">
							<span
								class="label-text"
								:class="[
									errors.oldPassword ? 'text-red-500 ' : 'text-c-dark-blue',
								]"
							>
								{{ t('team.password.form.old_password') }}
							</span>
						</label>
						<Field v-slot="{ field }" type="text" name="oldPassword">
							<div class="relative">
								<input
									type="text"
									class="input w-full input-bordered text-c-dark-blue focus:outline-none focus:border-c-deep-blue"
									:placeholder="t('placeholder.type_here')"
									:class="[
										errors.oldPassword
											? 'border-red-500'
											: 'border-c-input-grey',
									]"
									v-bind="field"
								/>
							</div>
						</Field>
						<div class="text-red-500 absolute -bottom-5 text-xs">
							{{ errors.oldPassword }}
						</div>
					</div>
					<div class="flex-1 relative mb-4">
						<label class="label pb-1 text-sm w-fit">
							<span
								class="label-text"
								:class="[
									errors.newPassword ? 'text-red-500 ' : 'text-c-dark-blue',
								]"
							>
								{{ t('team.password.form.new_password') }}
							</span>
						</label>
						<Field v-slot="{ field }" type="text" name="newPassword">
							<div class="relative">
								<input
									type="text"
									class="input w-full input-bordered text-c-dark-blue focus:outline-none focus:border-c-deep-blue"
									:placeholder="t('placeholder.type_here')"
									:class="[
										errors.newPassword
											? 'border-red-500'
											: 'border-c-input-grey',
									]"
									v-bind="field"
								/>
							</div>
						</Field>
						<div class="text-red-500 absolute -bottom-5 text-xs">
							{{ errors.newPassword }}
						</div>
					</div>
				</div>
			</div>
			<div class="mt-16 text-right w-full">
				<a
					class="btn btn-link mr-8 text-sm font-normal text-c-dark-blue capitalize"
				>
					{{ t('team.password.form.cancel') }}
				</a>
				<button
					type="submit"
					class="btn btn-primary font-semibold bg-c-dark-blue capitalize"
				>
					{{ t('team.password.form.change_password') }}
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

const { t } = useI18n();

const schema = object().shape({
	oldPassword: string().required(
		t('team.password.form.error_messages.old_password_required'),
	),
	newPassword: string()
		.required(t('team.password.form.error_messages.new_password_required'))
		.length(10, t('team.password.form.error_messages.new_password_length')),
});

const success = ref(false);
function onSubmit() {
	success.value = true;
}
</script>
