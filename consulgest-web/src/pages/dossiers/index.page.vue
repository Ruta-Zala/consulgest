<template>
	<div class="flex flex-col flex-1">
		<div class="flex w-full overflow-auto pb-12">
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
import { useRouter } from 'vue-router';
import Table from '../../components/table/table.component.vue';
import Pagination from '../../components/pagination/pagination.component.vue';
import { chunk } from '../../utils/chunk';
import Dropdown from '../../components/dropdown/dropdown.component.vue';
import DropdownItem from '../../components/dropdown/dropdown-item.component.vue';
import { IconDots, IconEdit, IconEmail, IconPlus, IconUser } from '../../icons';

const { t } = useI18n();
const page = ref(0);
const data = [
	{
		id: '1',
		dossier_name: 'CRV - RB1 RB001',
		n_d_g: '4349',
		debtor: 'Louis Adjanohoun',
		position: 'Phone Col.',
		statistical_taking: '60%',
	},
	{
		id: '2',
		dossier_name: 'CRV - RB1 RB003',
		n_d_g: '9439',
		debtor: 'aouis Adjanohoun',
		position: 'dPhone Col.',
		statistical_taking: '20%',
	},
	{
		id: '3',
		dossier_name: 'CRV - RB1 RB0043',
		n_d_g: '1349',
		debtor: 'vouis Adjanohoun',
		position: 'zPhone Col.',
		statistical_taking: '40%',
	},
	{
		id: '4',
		dossier_name: 'CRV - RB1 RB003',
		n_d_g: '9439',
		debtor: 'aouis Adjanohoun',
		position: 'dPhone Col.',
		statistical_taking: '20%',
	},
	{
		id: '5',
		dossier_name: 'CRV - RB1 RB0043',
		n_d_g: '1349',
		debtor: 'vouis Adjanohoun',
		position: 'zPhone Col.',
		statistical_taking: '40%',
	},
	{
		id: '6',
		dossier_name: 'CRV - RB1 RB003',
		n_d_g: '9439',
		debtor: 'aouis Adjanohoun',
		position: 'dPhone Col.',
		statistical_taking: '20%',
	},
	{
		id: '7',
		dossier_name: 'CRV - RB1 RB0043',
		n_d_g: '1349',
		debtor: 'vouis Adjanohoun',
		position: 'zPhone Col.',
		statistical_taking: '40%',
	},
	{
		id: '8',
		dossier_name: 'CRV - RB1 RB001',
		n_d_g: '4349',
		debtor: 'Louis Adjanohoun',
		position: 'Phone Col.',
		statistical_taking: '60%',
	},
];
const totalColumn = [
	{
		label: 'id',
		value: 'id',
	},
	{
		label: 'Dossier Name',
		value: 'dossier_name',
	},
	{
		label: 'N.D.G',
		value: 'n_d_g',
	},
	{
		label: 'Debtor',
		value: 'debtor',
	},
	{
		label: 'Position',
		value: 'position',
	},
	{
		label: 'Statistical Taking',
		value: 'statistical_taking',
	},
];
const columns = shallowRef(totalColumn);
const pageSize = 6;
const totalPage = chunk(data, pageSize);
const router = useRouter();
const emit = defineEmits(['update:dossierId']);

const updateRoute = (dossierId: number) => {
	return router.push({
		name: 'dossiers-overview',
		path: `dossiers/${dossierId}/overview`,
		params: {
			dossierId,
		},
	});
};

async function rowClick(item: { id: number }) {
	await updateRoute(item.id);
	emit('update:dossierId', item.id);
}

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
