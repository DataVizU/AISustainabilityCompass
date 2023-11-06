<script setup lang="ts">
import { regionList } from "~/utils/region";
import { ModelInfo } from "~/utils/model";

const selectedRegion = ref("All");

const items = [
  [
    {
      label: "All",
      click: () => {
        selectedRegion.value = "All";
      },
    },
    ...regionList.map((region) => ({
      label: region,
      click: () => {
        selectedRegion.value = region;
      },
    })),
  ],
];
</script>

<template>
  <div id="background">
    <div id="map_container" class="w-full h-full"></div>
    <div class="absolute top-24 left-14 z-10 flex flex-col gap-24 select-none">
      <div>
        <h1 class="text-3xl text-black font-bold">Deployment</h1>
        <h1 class="text-3xl text-black font-bold -mt-1">Forecasting</h1>
        <h2 class="text-black font-light text-2xl">
          What would happen to your region
        </h2>
        <h2 class="text-black font-light text-2xl -mt-1">
          after deploying large language models?
        </h2>
      </div>
      <div class="w-64 flex flex-col gap-10 font-light">
        <UDropdown
          :items="items"
          :popper="{ placement: 'bottom-start' }"
          class="mt-8 w-full h-12"
          :ui="{
            width: 'w-64',
            height: 'h-32',
            item: {
              base: 'hover:bg-linear-gradient',
            },
          }"
        >
          <UButton
            color="white"
            :label="selectedRegion"
            trailing-icon="i-heroicons-chevron-down-20-solid"
            class="w-full justify-between h-12 border-none"
            style="box-shadow: 1px 2px 5px rgba(170, 161, 206, 0.56)"
          />
        </UDropdown>
        <div
          class="w-full h-80 font-light text-xs bg-[rgba(255,255,255,0.9)] rounded-2xl flex flex-col"
          style="box-shadow: 1px 2px 5px rgba(170, 161, 206, 0.56)"
        >
          <div
            class="w-full h-8 flex items-center px-3 text-base model-card-title-bg-linear-gradient rounded-t-2xl text-white"
          >
            Model
          </div>
          <div
            class="w-full h-full p-2 bg-[#DFDAF4] overflow-y-auto rounded-b-2xl"
          >
            <div class="w-full flex flex-col gap-2">
              <ModelCard
                v-for="modelRecord in ModelInfo"
                :key="`${modelRecord.model}-${modelRecord.size}`"
                :name="modelRecord.model"
                :arc="modelRecord.arc"
                :average="modelRecord.average"
                :hellaswag="modelRecord.hellaswag"
                :mmlu="modelRecord.mmlu"
                :truthfulqa="modelRecord.truthfulqa"
                :memory="modelRecord.memory"
                :throughput="modelRecord.throughput"
                :energy="modelRecord.energy"
                :size="modelRecord.size"
              ></ModelCard>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
#background::before {
  content: "";
  position: absolute;
  top: 4rem;
  left: 0;
  width: 200%;
  height: calc(200% - 8rem);
  background-image: linear-gradient(to right, #6440f547 1px, transparent 1px),
    linear-gradient(to bottom, #6440f547 1px, transparent 1px);
  background-size: 134px 134px;
  transform: scale(0.5);
  transform-origin: 0 0;
}
#background {
  height: calc(100% - 4rem);
  width: 100%;
  margin: 0;
  overflow: hidden;
}
</style>
