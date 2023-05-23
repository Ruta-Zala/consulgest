<template>
	<div>
		<div class="border-b border-c-coral-blue gap-2 mb-10 p-6 flex">
			<button class="gap-2 flex items-center rounded-lg">
				<IconDropdownFilter class="w-4 h-4 text-c-dark" />
				<span class="text-c-dark text-sm">Filtered by:</span>
			</button>
			<button
				class="bg-c-linear sm:px-4 px-2 py-2.5 gap-2 flex items-center rounded-lg"
			>
				<span class="text-c-dark-blue text-sm">Debtor</span>
				<IconClose class="w-3 h-3 text-c-coral-blue" />
			</button>
		</div>
		<CardHeader title="Address book">
			<template #afterTitle>
				<div class="flex items-center gap-4 border-l border-c-coral-blue">
					<span class="badge text-white bg-c-deep-blue ml-4 px-5 h-8">03</span>
				</div>
			</template>
			<template #endTitle>
				<div class="flex gap-4 flex-wrap">
					<button
						class="px-2 py-2.5 gap-2 flex items-center rounded-lg sm:px-4"
					>
						<span class="text-c-dark-blue text-sm">Subject type</span>
						<IconDropdown class="w-3.5 h-3.5 text-c-dark-blue" />
					</button>
					<button
						class="px-2 py-2.5 gap-2 flex items-center rounded-lg sm:px-4"
					>
						<span class="text-c-dark-blue text-sm">City</span>
						<IconDropdown class="w-3.5 h-3.5 text-c-dark-blue" />
					</button>
					<button
						class="bg-c-grey-bg px-2 py-2.5 gap-2 flex items-center rounded-lg sm:px-4"
					>
						<span class="text-c-dark-blue text-sm">Type</span>
						<span class="text-white bg-c-deep-blue w-6 h-5 text-xs badge"
							>2</span
						>
						<IconDropdown class="w-3.5 h-3.5 text-c-dark-blue" />
					</button>
				</div>
			</template>
		</CardHeader>
		<div class="flex flex-col flex-1 mt-6">
			<div class="flex w-full pb-12 overflow-x-auto overflow-y-hidden">
				<Table
					:columns="columns"
					:data="data"
					:page="page"
					:page-size="pageSize"
					:menu="true"
					:header-menu="true"
				>
					<template #menu>
						<Dropdown
							:arrow-drop-down="false"
							:icon="IconDots"
							position="right"
						>
							<DropdownItem
								v-for="link in links"
								:key="link.href"
								:href="link.href"
							>
								<RouterLink v-slot="{ isActive, navigate }" :to="link.href">
									<a
										class="flex items-center text-sm text-c-dark-blue gap-2 px-4 py-3 hover:bg-c-ghost-white"
										:href="link.href"
										:class="isActive ? 'bg-c-ghost-white' : 'bg-transparent'"
										@click="navigate"
									>
										<component :is="link.icon" class="w-4 h-4" />
										{{ link.label }}
									</a>
								</RouterLink>
							</DropdownItem>
						</Dropdown>
					</template>
					<template #headerMenu>
						<div class="dropdown dropdown-end">
							<label tabindex="0" class="block cursor-pointer text-c-deep-blue">
								<IconPlus class="w-4"></IconPlus>
							</label>
							<div
								tabindex="0"
								class="dropdown-content shadow bg-base-100 rounded-box px-6 py-4 whitespace-nowrap w-80 text-left"
							>
								<span class="font-normal">{{ t('extra_field.title') }}</span>
								<div
									v-for="(headerData, index) in totalColumn"
									:key="index"
									class="mt-2 p-3 border border-c-grey rounded-md"
								>
									<div class="form-control p-0">
										<label class="cursor-pointer label justify-start p-0">
											<input
												type="checkbox"
												:name="headerData.label"
												:value="headerData.value"
												:disabled="
													['name', 'phone', 'email'].includes(headerData.value)
												"
												class="checkbox checkbox-success border-c-grey"
												checked
												@change="(e) => tableColumnsFilter(e)"
											/>
											<span class="font-normal ml-3">{{
												headerData.label
											}}</span>
										</label>
									</div>
								</div>
							</div>
						</div>
					</template>
				</Table>
			</div>
			<div class="text-end">
				<Pagination v-model="page" :total="totalPage.length" />
			</div>
		</div>
	</div>
</template>

<script lang="ts" setup>
import { ref, shallowRef } from 'vue';
import { useI18n } from 'vue-i18n';
import {
	IconDropdownFilter,
	IconDropdown,
	IconClose,
	IconDots,
	IconPlus,
	IconEdit,
	IconEmail,
	IconUser,
} from '../../../icons';
import { chunk } from '../../../utils/chunk';
import NameCell from '../components/name-cell.component.vue';
import CardHeader from './../../../components/card/card-header/card-header.component.vue';
import Table from './../../../components/table/table.component.vue';
import Pagination from './../../../components/pagination/pagination.component.vue';
import Dropdown from './../../../components/dropdown/dropdown.component.vue';
import DropdownItem from './../../../components/dropdown/dropdown-item.component.vue';

const { t } = useI18n();
const data = [
	{
		name: `Hugo Paulo`,
		status: 'Active',
		phone: '0000000000',
		email: 'hugo.paolo@email.com',
		role: 'Controller',
		profile: 'Esattore Esterno',
	},
];

const totalColumn = [
	{
		label: 'Name',
		value: 'name',
		Cell: NameCell,
	},
	{
		label: 'Phone',
		value: 'phone',
	},
	{
		label: 'Email',
		value: 'email',
	},
	{
		label: 'Role',
		value: 'role',
	},
	{
		label: 'Profile',
		value: 'profile',
	},
];

const columns = shallowRef(totalColumn);
const pageSize = 6;
const page = ref(0);
const totalPage = chunk(data, pageSize);

function tableColumnsFilter(e: any) {
	if (!e.target.checked) {
		columns.value = columns.value.filter((item: any) => {
			return item.value !== e.target.value;
		});
	} else {
		columns.value.push({
			label: e.target.name,
			value: e.target.value,
		});
	}
}
const links = [
	{
		href: '/dossiers/address-book',
		label: t('menu.link_first'),
		icon: IconEdit,
	},
	{
		href: '/dossiers/address-book',
		label: t('menu.link_second'),
		icon: IconEmail,
	},
	{
		href: '/dossiers/address-book',
		label: t('menu.link_third'),
		icon: IconUser,
	},
];
</script>
