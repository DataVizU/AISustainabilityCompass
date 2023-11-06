<script setup lang="ts">
import * as echarts from "echarts";
import { Buffer } from "unenv/runtime/node/buffer/_buffer";
import poolSize = Buffer.poolSize;

const props = defineProps({
  name: {
    type: String,
    required: true,
  },
  average: {
    type: Number,
    required: true,
  },
  size: {
    type: Number,
    required: true,
  },
  arc: {
    type: Number,
    required: true,
  },
  hellaswag: {
    type: Number,
    required: true,
  },
  mmlu: {
    type: Number,
    required: true,
  },
  truthfulqa: {
    type: Number,
    required: true,
  },
  memory: {
    type: Number,
    required: true,
  },
  throughput: {
    type: Number,
    required: true,
  },
  energy: {
    type: Number,
    required: true,
  },
});

onMounted(() => {
  const dom = document.getElementById(
    `radar-chart-${props.name}-${props.size}`,
  );
  const myChart = echarts.init(dom, null, {
    renderer: "canvas",
    useDirtyRect: false,
  });

  const option = {
    color: ["#5B1CF3"],
    legend: {},
    radar: [
      {
        indicator: [
          { text: "arc", max: 100 },
          { text: "hellaswag", max: 100 },
          { text: "mmlu", max: 100 },
          { text: "truthfulqa", max: 100 },
          { text: "memory", max: 60000 },
          { text: "throughput", max: 100 },
          { text: "energy", max: 800000 },
        ],
        radius: 50,
        startAngle: 90,
        splitNumber: 4,
        shape: "circle",
        splitArea: {
          areaStyle: {
            color: ["#00000000", "#00000000", "#00000000", "#00000000"],
            shadowColor: "rgba(0, 0, 0, 0)",
            shadowBlur: 10,
          },
        },
        axisLine: {
          lineStyle: {
            color: "rgba(211, 253, 250, 0)",
          },
        },
        splitLine: {
          lineStyle: {
            color: "rgba(211, 253, 250, 0)",
          },
        },
      },
    ],
    series: [
      {
        type: "radar",
        emphasis: {
          lineStyle: {
            width: 10,
          },
        },
        data: [
          {
            value: [
              props.arc,
              props.hellaswag,
              props.mmlu,
              props.truthfulqa,
              props.memory,
              props.throughput,
              props.energy,
            ],
            label: {
              show: true,
              formatter: function (params: { value: number }) {
                return params.value;
              },
            },
          },
        ],
      },
    ],
  };
  if (option && typeof option === "object") {
    myChart.setOption(option);
  }
  window.addEventListener(
    "resize",
    () => {
      setTimeout(() => {
        myChart && myChart.resize();
      }, 100);
    },
    false,
  );
});
</script>

<template>
  <div class="w-full h-36 bg-white rounded-xl flex flex-row pr-2">
    <div class="h-full w-24 pt-10 pb-8 flex flex-col">
      <div class="w-full h-full model-card-info">
        <div
          class="h-1/3 flex justify-center items-center text-white"
          style="
            background: linear-gradient(
              to right,
              #7689fb 0,
              #7a9afc 80%,
              #7fadfd 100%
            );
          "
        >
          {{ props.name.toUpperCase() }}
        </div>
        <div class="h-2/3 flex justify-center items-center text-lg">
          {{ props.size }} B
        </div>
      </div>
    </div>
    <div class="w-full h-full py-4 pl-14 pr-0.5 flex">
      <div
        :id="`radar-chart-${props.name}-${props.size}`"
        class="h-full flex-1"
        style="
          background-size: 100% 100%;
          background: url(https://r2-img.datavizu.app/radar-back.svg) no-repeat;
        "
      ></div>
    </div>
  </div>
</template>

<style scoped>
.model-card-info {
  border-width: 1px;
  border-style: solid;
  border-image: linear-gradient(60deg, #7689fb 0, #7a9afc 80%, #7fadfd 100%) 1;
}
</style>
