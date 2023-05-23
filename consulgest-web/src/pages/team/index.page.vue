<template>
	<div class="flex flex-col flex-1">
		<div class="flex w-full pb-12">
			<Table
				:columns="columns"
				:data="data"
				:page="page"
				:page-size="pageSize"
				:menu="true"
				:header-menu="true"
				@row-click="rowClick"
			>
				<template #menu>
					<Dropdown :arrow-drop-down="false" :icon="IconDots" position="right">
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
										<span class="font-normal ml-3">{{ headerData.label }}</span>
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
</template>

<script lang="ts" setup>
import { useI18n } from 'vue-i18n';
import { ref, shallowRef } from 'vue';
import Table from '../../components/table/table.component.vue';
import Pagination from '../../components/pagination/pagination.component.vue';
import { chunk } from '../../utils/chunk';
import Dropdown from '../../components/dropdown/dropdown.component.vue';
import DropdownItem from '../../components/dropdown/dropdown-item.component.vue';
import { IconEdit, IconEmail, IconUser, IconDots, IconPlus } from '../../icons';
import { router } from '../../router';
import NameCell from './components/name-cell.component.vue';

const data = [
	{
		name: `Hugo Paulo`,
		status: 'Active',
		phone: '0000000000',
		email: 'hugo.paolo@email.com',
		role: 'Controller',
		profile: 'Esattore Esterno',
		last_access: 'Today',
		created_on: '01/10/2022',
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
	{
		label: 'Last Access',
		value: 'last_access',
	},
	{
		label: 'Created on',
		value: 'created_on',
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

const { t } = useI18n();

const links = [
	{ href: '/team/user', label: t('menu.link_first'), icon: IconEdit },
	{ href: '/dashboard', label: t('menu.link_second'), icon: IconEmail },
	{ href: '/dashboard', label: t('menu.link_third'), icon: IconUser },
];

function rowClick() {
	router.push('/team/user');
}
</script>
