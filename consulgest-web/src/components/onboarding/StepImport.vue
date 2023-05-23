<template>
	<div class="w-full overflow-hidden flex flex-col items-center px-16 mt-8">
		<h1 class="text-c-dark-blue text-4xl font-semibold">
			{{ t('import_dossier.steps.data_table.title') }}
		</h1>
		<h4 class="text-c-dark-blue text-lg font-light mb-12">
			{{ t('import_dossier.steps.data_table.subtitle') }}
		</h4>
		<Form
			v-slot="{ errors }"
			:validation-schema="schema"
			class="flex flex-col w-full overflow-hidden"
			@submit="importFile"
		>
			<div class="w-2/4 m-auto flex flex-col items-start">
				<div class="flex gap-4 items-end w-full">
					<div
						class="form-control w-full relative"
						:class="{ 'opacity-25 pointer-events-none': isNewTemplate }"
					>
						<label class="label pb-1">
							<span
								class="label-text"
								:class="[
									errors.templateLibrary
										? 'text-red-500 '
										: 'text-c-light-grey',
								]"
							>
								Template Library
							</span>
						</label>
						<Field v-slot="{ field }" name="templateLibrary">
							<div class="relative">
								<Dropdown
									:label="selectedOption.name"
									v-bind="field"
									class="w-full input px-0 h-11 border-c-grey focus:outline-none focus:border-c-deep-blue text-c-dark-blue"
								>
									<DropdownItem
										v-for="option in options"
										:key="option.id"
										class="py-2 px-4 w-full"
										:value="option.name"
										@click="selectTemplate(option)"
									>
										{{ option.name }}
									</DropdownItem>
								</Dropdown>
								<div class="text-red-500 absolute -bottom-5 text-xs">
									{{ errors.templateLibrary }}
								</div>
							</div>
						</Field>
					</div>
					<div class="form-control w-full relative">
						<label class="label pb-1">
							<span
								class="label-text"
								:class="[
									errors.fileError ? 'text-red-500 ' : 'text-c-light-grey',
								]"
							>
								CSV Name*
							</span>
						</label>
						<Field v-slot="{ field }" name="fileError">
							<div class="relative">
								<input
									v-model="fileName"
									type="text"
									class="input input-bordered w-full h-11 focus:outline-none focus:border-c-deep-blue text-c-dark-blue"
									:placeholder="t('placeholder.type_here')"
									:class="[
										errors.fileError ? 'border-red-500' : 'border-c-grey',
									]"
									v-bind="field"
								/>
							</div>
						</Field>
						<div class="text-red-500 absolute -bottom-5 text-xs">
							{{ errors.fileError }}
						</div>
					</div>
					<button
						class="btn bg-c-dark-blue px-8 border-none rounded-md text-white normal-case h-[50px]"
						type="submit"
					>
						{{ t('import_dossier.steps.data_table.button.import') }}
					</button>
				</div>
				<label class="label cursor-pointer mt-4 mb-2">
					<input
						v-model="isNewTemplate"
						type="checkbox"
						class="radio rounded-md checked:bg-c-deep-blue border-c-grey h-5 w-5"
						@change="handleTemplateChange($event)"
					/>
					<span class="label-text ml-2 text-c-dark-blue">{{
						t('import_dossier.steps.data_table.save')
					}}</span>
				</label>
				<div
					class="form-control w-full relative"
					:class="{ 'opacity-25': !isNewTemplate }"
				>
					<label class="label pb-1">
						<span
							class="label-text"
							:class="[
								errors.templateName ? 'text-red-500 ' : 'text-c-light-grey',
							]"
						>
							Template Name
						</span>
					</label>
					<Field v-slot="{ field }" type="text" name="templateName">
						<input
							v-model="templateName"
							type="text"
							class="input input-bordered w-full focus:outline-none focus:border-c-deep-blue text-c-dark-blue disabled:bg-c-input-grey"
							:placeholder="t('placeholder.type_here')"
							v-bind="field"
							:disabled="!isNewTemplate"
							:class="[
								errors.templateName ? 'border-red-500' : 'border-c-grey',
							]"
						/>
					</Field>
					<div class="text-red-500 absolute -bottom-5 text-xs">
						{{ errors.templateName }}
					</div>
				</div>
			</div>
			<div class="text-right mb-2 mt-14 text-c-pink">
				Please note that this is a representation of your file to create a
				template. Please review your file to avoid mistakes
			</div>
			<div class="flex-1 overflow-auto">
				<Table :columns="columnHeader" :data="rowData" :checkbox="false">
					<template #headerList>
						<td
							v-for="(i, index) in columnHeader"
							:key="index"
							class="px-3 py-4 relative"
						>
							<Field v-slot="{ field }" as="div" name="templateHeader">
								<Dropdown
									v-bind="field"
									v-model="headerCols[index]"
									:label="String(headerCols[index])"
									class="w-full input px-0 h-11 border-c-grey focus:outline-none focus:border-c-deep-blue text-c-dark-blue"
								>
									<DropdownItem
										v-for="(option, optionIndex) in dynamicHeader"
										:key="optionIndex"
										class="py-2 px-4 w-full"
										:value="option['colonna' + (optionIndex + 1)]"
										@click="
											headerCol(option['colonna' + (optionIndex + 1)], index)
										"
										v-text="option['colonna' + (optionIndex + 1)]"
									/>
								</Dropdown>
								<div class="text-red-500 absolute -bottom-1 left-3 text-xs">
									{{ errors.templateHeader }}
								</div>
							</Field>
						</td>
					</template>
				</Table>
			</div>
		</Form>
	</div>
</template>

<script lang="ts" setup>
import { useI18n } from 'vue-i18n';
import { PropType, Ref, ref, toRaw } from 'vue';
import { onMounted } from '@vue/runtime-core';
import { Field, Form } from 'vee-validate';
import { object, string } from 'yup';
import Table from '../../components/table/table.component.vue';
import Dropdown from '../../components/dropdown/dropdown.component.vue';
import DropdownItem from '../../components/dropdown/dropdown-item.component.vue';
import { apiService } from '../../api.service';
import { useCurrentUser } from '../../composables/use-current-user';

const props = defineProps({
	uploadedFile: {
		type: Object as PropType<{ csv: object; file: string }>,
		default: null,
		required: false,
	},
});

const emit = defineEmits<{
	(e: 'next-tab'): void;
}>();

interface Option {
	name: string;
	id: number;
}
interface DynamicHeaderType {
	[key: string]: string;
}

interface HeaderColsType {
	[key: number]: string;
}

const fileData: any = toRaw(props.uploadedFile.csv);
const options = ref<Option[]>([]);
const isNewTemplate = ref(false);
const selectedOption = ref({
	name: 'Select a value',
	id: '',
	colonne_mappate: '',
});
const headerCols: Ref<HeaderColsType[]> = ref([]);
const fileName = ref('');
const templateName = ref('');
const headerName: any = fileData[0];
const dynamicHeader: Ref<DynamicHeaderType[]> = ref([]);
const currentUser = useCurrentUser();

onMounted(() => {
	getTemplateList();
	getHeaderList();
});

const columnHeader = Object.keys(headerName).map((str) => ({
	label: str,
	value: str,
}));

const rowData = fileData.map((dataItem: { [x: string]: string }) =>
	Object.keys(headerName).reduce((objectList, key) => {
		objectList[key] = dataItem[key];
		return objectList;
	}, {} as Record<string, string>),
);

const schema = object().shape({
	fileError: string().required('Please enter csv name'),
	templateName: string().when('isNewTemplate', {
		is: () => isNewTemplate.value === true,
		then: string().required('Please enter template name'),
	}),
	templateLibrary: string().when('selectedOption.value.id', {
		is: () => selectedOption.value.id === '' && isNewTemplate.value === false,
		then: string().required('Please select a template'),
	}),
});

const { t } = useI18n();

const selectTemplate = (option: any) => {
	selectedOption.value = option;
	const templateHeaders = JSON.parse(selectedOption.value.colonne_mappate);

	for (let i = 0; i < Object.keys(headerCols.value).length; i++) {
		headerCols.value[i] = templateHeaders[`colonna${i + 1}`];
	}
};

const headerCol = (option: any, i: any) => {
	headerCols.value[i] = option;
};

const handleTemplateChange = (event: Event) => {
	isNewTemplate.value = (event.target as HTMLInputElement)?.checked;
};

const getTemplateList = () => {
	apiService.get('api/template/').then((res) => (options.value = res.data));
};

const getHeaderList = () => {
	apiService.get('api/getlistheaders/').then((res) => {
		dynamicHeader.value = res.data.map((value: string, index: number) => {
			return { ['colonna' + (index + 1)]: value };
		});
		for (let i = 0; i < columnHeader.length; i++) {
			headerCols.value.push(dynamicHeader.value[0].colonna1);
		}
	});
};

const uploadFile = (templateId: string) => {
	// upload a file
	const formData = new FormData();
	formData.append('name', fileName.value);
	formData.append('file', props.uploadedFile.file);
	formData.append('id_utente', currentUser.value?.pk);
	formData.append('id_template', templateId);
	apiService.post('api/uploadfilepratiche/', formData);
};

const uploadNewFileAsTemplate = () => {
	// save a new template and uplod file
	const addTemplate = new FormData();
	addTemplate.append('name', fileName.value);
	addTemplate.append('colonne_mappate', JSON.stringify(headerCols.value));
	addTemplate.append('id_utente', currentUser.value?.pk);
	apiService
		.post('api/template/', addTemplate)
		.then((res) => uploadFile(res.data.id));
};

const importFile = () => {
	if (isNewTemplate.value) {
		uploadNewFileAsTemplate();
	} else {
		uploadFile(selectedOption.value.id);
	}
	emit('next-tab');
};
</script>
