<template>
	<table class="w-full">
		<thead class="sticky top-0 z-10">
			<tr class="h-[45px] bg-c-grey-bg text-c-dark-blue">
				<th v-if="checkbox" class="rounded-l-lg px-3">
					<label for="" class="flex items-center justify-center">
						<input type="checkbox" class="w-[18px] h-[18px] rounded checkbox" />
					</label>
				</th>
				<th
					v-for="(field, index) in columns"
					:key="index"
					class="px-3 cursor-pointer"
					@click="sortList(field.value)"
				>
					<div class="flex items-center gap-3 text-sm font-normal">
						{{ field.label }}
						<IconFilter class="h-2 w-2 text-c-polo-blue" />
					</div>
				</th>
				<th class="rounded-r-lg px-3">
					<div v-if="headerMenu" class="flex item-center justify-center">
						<slot name="headerMenu"></slot>
					</div>
				</th>
			</tr>
		</thead>
		<tbody>
			<tr>
				<slot name="headerList"> </slot>
			</tr>
			<tr
				v-for="(item, index) in sortedData"
				:key="index"
				class="h-[55px] border-solid border-b border-c-coral-blue text-c-dark-blue cursor-pointer"
				@click="emit('row-click', item)"
			>
				<td v-if="checkbox" class="px-3">
					<label for="" class="flex items-center justify-center">
						<input type="checkbox" class="w-[18px] h-[18px] rounded checkbox" />
					</label>
				</td>
				<td v-for="field in columns" :key="field.value" class="px-3">
					<component
						:is="field.Cell ?? DefaultCell"
						:value="item[field.value]"
						:row="item"
					/>
				</td>
				<td class="px-3">
					<div v-if="menu">
						<slot name="menu"></slot>
					</div>
				</td>
			</tr>
		</tbody>
	</table>
</template>

<script setup lang="ts">
import { computed, ref, PropType, type Component } from 'vue';
import { IconFilter } from '../../icons/index';
import { chunk } from '../../utils/chunk';

type DefaultCellProps = { value: unknown; row: unknown };
const DefaultCell = ({ value }: DefaultCellProps) => {
	return value;
};

const emit = defineEmits<{
	// TODO: this is not how it should be done
	(e: 'row-click', value: unknown): void;
}>();

const props = defineProps({
	data: {
		type: Array as PropType<Array<Record<string, unknown>>>,
		required: true,
	},
	columns: {
		type: Array as PropType<
			Array<{ label: string; value: string; Cell?: Component }>
		>,
		required: true,
	},
	page: {
		type: Number,
		default: 0,
	},
	pageSize: {
		type: Number,
		default: Infinity,
	},
	menu: {
		type: Boolean,
		default: false,
	},
	headerMenu: {
		type: Boolean,
		default: false,
	},
	checkbox: {
		type: Boolean,
		default: true,
	},
});

const sortBy = ref<string | undefined>();

function asc<T>(x: T, y: T) {
	return x < y ? -1 : 1;
}
function desc<T>(x: T, y: T) {
	return x > y ? -1 : 1;
}
const sortAscendent = ref(true);
const sortingDirection = computed(() => (sortAscendent.value ? asc : desc));

const sortedData = computed(() => {
	const chunks = chunk(props.data, props.pageSize);
	const data = chunks[props.page];
	const by = sortBy.value;

	// No sorting is defined
	if (by === undefined) return data;

	// Sort
	return data.sort((x, y) => sortingDirection.value(x[by], y[by]));
});

function sortList(by: string) {
	sortAscendent.value = sortBy.value === by ? !sortAscendent.value : true;
	sortBy.value = by;
}
</script>
