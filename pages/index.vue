<script setup lang="ts">
import { regionIndication, regionList, regions } from "~/utils/region";
import { getCustomLayer, getCustomLayerData } from "~/utils/dom";

let map;

let customLayer: any;

const selectedRegion = ref("Beijing");

const selectedRegionValue = computed(() => {
  return regionIndication[
    regions[
      selectedRegion.value as keyof typeof regions
    ] as keyof typeof regionIndication
  ];
});

const items = [
  [
    ...regionList.map((region) => ({
      label: region,
      click: () => {
        selectedRegion.value = region;
      },
    })),
  ],
];

const selectedType = ref("all");

const selectType = (type: string) => {
  selectedType.value = type;
  customLayer.updateData(getCustomLayerData(type));
};

onMounted(() => {
  map = new BMapGL.Map("map_container");
  const point = new BMapGL.Point(95, 37);
  map.centerAndZoom(point, 5);
  map.setMapStyleV2({
    styleId: "d8baf435b5ec45b2718d0a5c6946cf6b",
  });
  map.enableScrollWheelZoom(true);
  const zoomCtrl = new BMapGL.ZoomControl();
  map.addControl(zoomCtrl);

  customLayer = getCustomLayer();
  const data = getCustomLayerData("all");
  customLayer.setData(data);
  map.addCustomHtmlLayer(customLayer);
});
</script>

<template>
  <div id="background">
    <div id="map_container" class="w-full h-full"></div>
    <div class="absolute top-24 left-14 z-10 flex flex-col gap-24 select-none">
      <div>
        <h1 class="text-3xl text-black font-bold">Readiness</h1>
        <h1 class="text-3xl text-black font-bold -mt-1">Assessment</h1>
        <h2 class="text-black font-light text-2xl">
          Is your nation ready to navigate
        </h2>
        <h2 class="text-black font-light text-2xl -mt-1">AI transformation?</h2>
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
          class="w-full select-none flex flex-col pt-4 font-light text-xs bg-[rgba(255,255,255,0.9)] rounded-2xl"
          style="box-shadow: 1px 2px 5px rgba(170, 161, 206, 0.56)"
        >
          <div
            class="w-full h-10 flex flex-row gap-4 items-center px-4 rounded-md hover:bg-linear-gradient"
            :class="{ 'bg-linear-gradient': selectedType === 'all' }"
            @click="selectType('all')"
          >
            <img
              src="../assets/img/total.svg"
              class="w-3.5 flex-none"
              alt="Total score"
            />
            <div class="flex-1">Overall</div>
            <div class="flex-none">{{ selectedRegionValue.all }}</div>
          </div>
          <div
            class="w-full flex flex-col gap-1 pt-2"
            style="border-top: 1px solid #5b1cf3"
          >
            <div
              class="w-full h-10 flex flex-row gap-4 items-center px-4 rounded-md hover:bg-linear-gradient"
              :class="{ 'bg-linear-gradient': selectedType === 'economy' }"
              @click="selectType('economy')"
            >
              <img
                src="../assets/img/economy.svg"
                class="w-3.5 flex-none"
                alt="Economy"
              />
              <div class="flex-1">Economy</div>
              <div class="flex-none">{{ selectedRegionValue.economy }}</div>
            </div>
            <div
              class="w-full h-10 flex flex-row gap-4 items-center px-4 rounded-md hover:bg-linear-gradient"
              :class="{ 'bg-linear-gradient': selectedType === 'government' }"
              @click="selectType('government')"
            >
              <img
                src="../assets/img/gov.svg"
                class="w-3.5 flex-none"
                alt="Government"
              />
              <div class="flex-1">Government</div>
              <div class="flex-none">{{ selectedRegionValue.government }}</div>
            </div>

            <div
              class="w-full h-10 flex flex-row gap-4 items-center px-4 rounded-md hover:bg-linear-gradient"
              :class="{
                'bg-linear-gradient': selectedType === 'infrastructure',
              }"
              @click="selectType('infrastructure')"
            >
              <img
                src="../assets/img/human.svg"
                class="w-3.5 flex-none"
                alt="Infrastructure"
              />
              <div class="flex-1">Infrastructure</div>
              <div class="flex-none">
                {{ selectedRegionValue.infrastructure }}
              </div>
            </div>

            <div
              class="w-full h-10 flex flex-row gap-4 items-center px-4 rounded-md hover:bg-linear-gradient"
              :class="{ 'bg-linear-gradient': selectedType === 'human' }"
              @click="selectType('people')"
            >
              <img
                src="../assets/img/human.svg"
                class="w-3.5 flex-none"
                alt="People"
              />
              <div class="flex-1">People</div>
              <div class="flex-none">{{ selectedRegionValue.people }}</div>
            </div>

            <div
              class="w-full h-10 flex flex-row gap-4 items-center px-4 rounded-md hover:bg-linear-gradient"
              :class="{ 'bg-linear-gradient': selectedType === 'risk' }"
              @click="selectType('risk')"
            >
              <img
                src="../assets/img/risk.svg"
                class="w-3.5 flex-none"
                alt="Risks"
              />
              <div class="flex-1">Risks</div>
              <div class="flex-none">{{ selectedRegionValue.risk }}</div>
            </div>

            <div
              class="w-full h-10 flex flex-row gap-4 items-center px-4 rounded-md hover:bg-linear-gradient"
              :class="{ 'bg-linear-gradient': selectedType === 'environment' }"
              @click="selectType('environment')"
            >
              <img
                src="../assets/img/env.svg"
                class="w-3.5 flex-none"
                alt="Environment"
              />
              <div class="flex-1">Environment</div>
              <div class="flex-none">{{ selectedRegionValue.environment }}</div>
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
