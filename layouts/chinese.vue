<script setup lang="ts">
const selectedNavItem = ref(0);

const clickNavItem = (index: number) => {
  selectedNavItem.value = index;
};
</script>

<template>
  <div class="w-full h-full">
    <div
      class="w-full h-16 bg-white py-2.5 px-14 flex flex-row justify-between items-center"
      style="border-bottom: 1px solid #5b1cf3"
    >
      <img class="h-full" src="/logo.svg" alt="Qing&Long" />
      <div class="flex flex-row items-center gap-12">
        <div class="h-full flex flex-row gap-6 items-center select-none">
          <NuxtLink
            to="/zh"
            class="nav-item"
            :class="{
              'font-medium underline': selectedNavItem === 0,
              'font-light': selectedNavItem !== 0,
            }"
            @click="clickNavItem(0)"
            >条件</NuxtLink
          >
          <NuxtLink
            to="/zh/evaluation"
            class="nav-item"
            :class="{
              'font-medium underline': selectedNavItem === 1,
              'font-light': selectedNavItem !== 1,
            }"
            @click="clickNavItem(1)"
            >预测</NuxtLink
          >
          <NuxtLink
            id="strategy-item"
            to="/zh/strategy"
            class="nav-item"
            :class="{
              'font-medium underline': selectedNavItem === 2,
              'font-light': selectedNavItem !== 2,
            }"
            @click="clickNavItem(2)"
            >战略</NuxtLink
          >
          <NuxtLink
            id="about-item"
            to="/zh/about"
            class="nav-item"
            :class="{
              'font-medium underline': selectedNavItem === 3,
              'font-light': selectedNavItem !== 3,
            }"
            @click="clickNavItem(3)"
            >关于</NuxtLink
          >
        </div>
        <a
          href="https://github.com/DataVizU/AISustainabilityCompass"
          target="_blank"
        >
          <img src="../assets/img/github.svg" class="w-6" alt="Github" />
        </a>
      </div>
    </div>
    <slot />
  </div>
</template>

<style scoped>
.nav-item {
  @apply w-24 hover:font-medium text-center;
}

#about-item {
  @apply w-14;
}

#strategy-item {
  @apply w-20;
}
</style>
