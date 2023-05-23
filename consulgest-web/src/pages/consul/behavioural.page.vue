<template>
	<div class="flex gap-6 flex-col">
		<div class="flex flex-col gap-2">
			<span class="text-c-dark">Prediction portfolio:</span>
			<div class="flex flex-col gap-8 items-center md:flex-row">
				<button
					class="px-4 py-2 rounded-md w-full gap-2 flex flex-row items-center justify-between text-c-dark-blue bg-c-ghost-white"
				>
					<span>All banks/lots</span>
					<span>
						<IconDropdown class="w-3 h-3" />
					</span>
				</button>
				<div
					class="flex gap-4 border border-c-input-grey rounded-md px-4 py-3 text-c-dark"
				>
					<span>Dossiers:</span>
					<span class="font-semibold">1000</span>
				</div>
				<button class="whitespace-nowrap">View bank details</button>
			</div>
		</div>
		<hr class="border-c-grey" />
		<div class="flex flex-col gap-6">
			<div class="flex flex-col justify-between lg:flex-row">
				<div class="flex items-center text-c-dark-blue gap-2">
					<IconCpu class="h-8 w-8" />
					<div class="text-lg font-medium">Best success rate dossiers</div>
					<span
						class="bg-c-deep-blue text-white h-6 flex justify-center items-center w-9 text-sm rounded-3xl"
						>40</span
					>
				</div>
				<div class="flex gap-2 items-center">
					<div class="flex gap-2 items-center">
						<div
							class="cursor-pointer border border-current text-c-input-grey rounded-full w-8 h-8 flex items-center justify-center"
						>
							<IconArrowAlt class="h-4 w-4 rotate-180" />
						</div>
						<div
							class="cursor-pointer border border-current text-c-dark-blue rounded-full w-8 h-8 flex items-center justify-center"
						>
							<IconArrowAlt class="h-4 w-4" />
						</div>
					</div>
					<Dropdown label="Ascending">
						<DropdownItem>
							<span>Ascending</span>
						</DropdownItem>
					</Dropdown>
				</div>
			</div>
			<div class="grid grid-cols-1 gap-6 lg:grid-cols-2 xl:grid-cols-5">
				<div v-for="i in 4" :key="i">
					<UserCard
						:percentage="20"
						title="positive closure"
						profile-image="https://picsum.photos/72/72"
						name="Josh Anderson Smith"
						book-name="CRV - RB1 RB001"
						difficulty-level="Easy"
						collection-type="phone"
						:collection-percentage="20"
						collector-name="Hanna Martin"
						collector-image="https://picsum.photos/42/42"
					/>
				</div>
			</div>
		</div>
		<div>
			<div class="flex flex-col justify-between lg:flex-row gap-3">
				<div class="flex items-center text-c-dark-blue gap-2">
					<IconCpu class="h-8 w-8" />
					<div class="text-lg font-medium">Closure success rate list</div>
				</div>
				<div class="flex gap-4 items-center">
					<Dropdown label="Sucess rate" class="rounded-md">
						<DropdownItem>
							<span class="text-c-success">Sucess rate</span>
						</DropdownItem>
					</Dropdown>
					<Dropdown label="All actions" class="rounded-md">
						<DropdownItem>
							<span class="text-c-success">All actions</span>
						</DropdownItem>
					</Dropdown>
					<Dropdown label="Dificulty level" class="rounded-md">
						<DropdownItem>
							<span class="text-c-success">Dificulty level</span>
						</DropdownItem>
					</Dropdown>
				</div>
			</div>
			<div class="flex my-4 w-full overflow-auto pb-4">
				<Table
					:columns="columns"
					:data="data"
					:page="page"
					:page-size="pageSize"
				/>
			</div>
			<div class="text-end">
				<Pagination
					v-model="page"
					:total="totalPage.length"
					class="rounded-xl"
				/>
			</div>
		</div>
	</div>
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { IconCpu, IconArrowAlt, IconDropdown } from '../../icons';
import UserCard from '../../components/user-card/user-card.component.vue';
import Pagination from '../../components/pagination/pagination.component.vue';
import Table from '../../components/table/table.component.vue';
import { chunk } from '../../utils/chunk';
import Dropdown from '../../components/dropdown/dropdown.component.vue';
import DropdownItem from '../../components/dropdown/dropdown-item.component.vue';

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
const columns = [
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
const pageSize = 2;
const totalPage = chunk(data, pageSize);
</script>
