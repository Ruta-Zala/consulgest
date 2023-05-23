<template>
	<div
		class="relative border border-c-input-grey rounded-xl w-full flex flex-col bg-white shadow-sm"
	>
		<CardBadge :percentage="percentage" :title="title" />
		<div class="p-4">
			<div class="gap-3 my-4 flex flex-col items-center justify-center">
				<Avatar alt="image" :src="profileImage" size="w-20 h-20" />
				<div class="flex flex-col">
					<span class="text-lg text-c-dark font-medium">{{ name }}</span>
					<div
						class="text-c-dark-blue flex justify-center items-center mt-2 text-sm gap-2"
					>
						<IconBook class="h-6 w-6" />
						<span>{{ bookName }}</span>
					</div>
				</div>
			</div>
			<div class="flex flex-col gap-2">
				<div
					class="text-c-dark-blue relative px-4 py-2 border rounded-lg border-c-vivid-green overflow-hidden"
				>
					<IconBackgroundGradient
						class="absolute right-0 bottom-0 h-16 text-c-vivid-green"
					/>
					<div class="flex-1 text-sm text-c-dark-blue mb-1 font-normal">
						First instalment
					</div>
					<div class="text-c-dark-blue flex items-center text-lg font-medium">
						1.000,00 €
						<span
							class="ml-4 text-sm text-c-deep-blue bg-c-grey-bg py-1.5 px-3 rounded-3xl inline-block font-semibold"
							>+-300€</span
						>
					</div>
				</div>
				<div
					class="text-c-dark-blue relative px-4 py-2 border rounded-lg border-c-deep-blue overflow-hidden"
				>
					<IconBackgroundGradient
						class="absolute right-0 bottom-0 h-16 text-c-deep-blue"
					/>
					<div class="flex-1 text-sm text-c-dark-blue mb-1">
						Average per instalment
					</div>
					<div class="text-c-dark-blue flex items-center text-lg font-medium">
						500,00 €
						<span class="ml-1 text-sm text-c-dark font-normal">/ montly</span>
					</div>
				</div>
				<div
					class="text-c-dark-blue border border-c-grey-input flex items-center rounded-md flex-1 py-2 px-4 text-sm"
				>
					<IconChartBar class="h-5 w-5 mr-4" />
					<div class="flex-1">Difficulty</div>
					<div class="text-c-dark font-semibold">{{ difficultyLevel }}</div>
				</div>
				<div
					class="text-c-dark-blue text-sm bg-c-grey-bg rounded-md flex items-center flex-1 py-3 px-4"
				>
					<div
						v-if="collectionType === 'phone'"
						class="flex-1 flex items-center"
					>
						<IconPhone class="h-4 w-4 mr-4" />
						<span>Phone call</span>
					</div>
					<div v-else class="flex-1 flex items-center">
						<IconEmail class="h-4 w-4 mr-4" />
						<span>Email collection</span>
					</div>
					<div class="text-c-deep-blue font-semibold">
						{{ collectionPercentage }}%
					</div>
				</div>
			</div>
			<div class="gap-4 flex items-center mt-4">
				<Avatar alt="image" :src="collectorImage" size="w-11 h-11" />
				<div class="flex flex-col">
					<span class="text-sm text-c-deep-blue">Suggested Collector</span>
					<span class="text-c-dark">{{ collectorName }}</span>
				</div>
			</div>
		</div>
	</div>
</template>

<script lang="ts" setup>
import CardBadge from '../card-badge/card-badge.component.vue';
import Avatar from '../avatar/avatar.component.vue';
import {
	IconPhone,
	IconBook,
	IconChartBar,
	IconBackgroundGradient,
	IconEmail,
} from '../../icons';

defineProps({
	percentage: { type: Number, required: true },
	title: { type: String, required: true },
	profileImage: { type: String, required: true },
	name: { type: String, required: true },
	bookName: { type: String, required: true },
	difficultyLevel: { type: String, required: true },
	collectionType: { type: String, required: true },
	collectionPercentage: { type: Number, required: true },
	collectorName: { type: String, required: true },
	collectorImage: { type: String, required: true },
});
</script>
