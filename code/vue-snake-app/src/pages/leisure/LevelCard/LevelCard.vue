<script setup lang="ts">
defineProps<{
  level: string;
}>();
</script>

<template>
  <div class="box flex flex-col items-center justify-center">
    <div
      class="flex h-28 w-28 items-center justify-center border-2 border-black text-5xl">
      {{ level }}
    </div>
    <div class="mt-3 flex space-x-1">
      <img class="h-8 w-8" src="@/assets/images/休闲模式/u48.svg" />
      <img class="h-8 w-8" src="@/assets/images/休闲模式/u49.svg" />
      <img class="h-8 w-8" src="@/assets/images/休闲模式/u49.svg" />
    </div>
  </div>
</template>
