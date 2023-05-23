<template>
	<div>
		<div class="text-center mt-8 w-2/4 mx-auto">
			<h1 class="text-c-dark-blue text-4xl font-semibold">
				{{ t('onboarding.steps.select.title') }}
			</h1>
			<h4 class="text-c-dark-blue text-lg font-light mb-12">
				{{ t('onboarding.steps.select.description') }}
			</h4>
			<div class="flex justify-between items-center">
				<span class="text-c-dark-blue font-semibold">Supported Formats:</span>
				<div class="flex gap-4">
					<button
						class="flex items-center bg-c-grey-bg text-sm font-semibold text-c-dark px-4 py-2 rounded-lg gap-2 uppercase"
					>
						<IconBook class="h-5 w-5" />csv
					</button>
					<button
						class="items-center bg-c-grey-bg text-c-dark-blue px-4 py-2 rounded gap-2 uppercase hidden"
					>
						<IconBook class="h-5 w-5" />excel
					</button>
					<button
						class="items-center bg-c-grey-bg text-c-dark-blue px-4 py-2 rounded gap-2 uppercase hidden"
					>
						<IconBook class="h-5 w-5" />txt
					</button>
				</div>
			</div>
			<div class="mt-6">
				<label
					class="flex flex-col justify-center w-full h-auto relative py-8 px-4 transition bg-white border-2 border-c-blue border-dashed rounded-xl appearance-none cursor-pointer hover:border-c-deep-blue focus:outline-none"
					@drop="dragFile"
					@dragenter="dragFile"
				>
					<div class="relative">
						<img
							class="mx-auto"
							src="../../assets/images/file-upload.svg"
							alt="img"
						/>
					</div>
					<div
						class="flex items-center justify-center mt-4 font-normal text-c-dark-blue text-sm"
					>
						{{ t('onboarding.steps.import.drag_file') }}
						<span class="text-c-deep-blue underline ml-1">
							{{ t('onboarding.steps.import.browse') }}
						</span>
					</div>
					<input
						id="fileUpload"
						type="file"
						name="file_upload"
						accept="text/csv"
						class="absolute max-h-full max-w-full inset-0 opacity-0"
						@change="uploadFile"
					/>
				</label>
			</div>
			<div
				v-if="file"
				class="bg-c-input-grey p-2 mt-2 text-c-dark-blue rounded-lg font-semibold"
			>
				{{ file.name }}
			</div>
			<div
				v-if="error && !file"
				class="bg-c-pink bg-opacity-5 py-2 px-4 mt-8 text-c-error rounded-xl flex items-center gap-2"
			>
				<IconFile class="h-5 w-5" />{{ error }}
			</div>
		</div>
		<div class="mb-8 flex gap-8 mx-auto mt-16 w-2/4 justify-end">
			<RouterLink
				v-if="isImportPage"
				to="/dashboard"
				class="text-c-dark-blue btn btn-ghost"
			>
				{{ t('commonButtons.back_btn') }}
			</RouterLink>
			<button
				v-else
				class="text-c-dark-blue btn btn-ghost"
				@click="previousTab()"
			>
				{{ t('commonButtons.back_btn') }}
			</button>
			<button
				class="btn btn-primary border-none capitalize w-[117px] h-[50px]"
				@click="nextTab()"
			>
				{{ t('commonButtons.next_btn') }}
			</button>
		</div>
	</div>
</template>
<script lang="ts" setup>
import { useI18n } from 'vue-i18n';
import { ref, defineEmits, computed } from 'vue';
import { useRoute } from 'vue-router';
import { IconBook, IconFile } from '../../icons';
import { sheetFileToJson } from '../../utils/sheet-file-to-json';

const { t } = useI18n();
const csv = ref();
const file = ref<File | null | undefined>();
const error = ref('');
const route = useRoute();

const isImportPage = computed(() => {
	return route.path.includes('/import-dossier');
});

const emit = defineEmits<{
	(e: 'next-tab', csv: any, file: any): void;
	(e: 'previous-tab'): void;
}>();

const dragFile = (event: DragEvent) => {
	const element = event.currentTarget as HTMLLabelElement;
	element.classList.add('bg-c-grey-bg');
};

const uploadFile = async (event: Event) => {
	const input = event.target as HTMLInputElement;
	file.value = input?.files?.item(0);
	if (!file.value) return;
	try {
		csv.value = await sheetFileToJson<Record<string, string>>(file.value);
	} catch (err) {
		error.value = 'Something went wrong with the CSV file.';
	}
};

const nextTab = () => {
	if (csv.value) {
		emit('next-tab', csv, file);
	} else {
		error.value = 'Please select a CSV file';
	}
};

const previousTab = () => {
	emit('previous-tab');
};
</script>
