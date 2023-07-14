<script setup lang="ts">
import LevelCard from './LevelCard';
</script>

<template>
  <div class="mx-auto w-4/5">
    <div class="flex justify-between">
      <img
        class="hover:cursor-pointer"
        src="@/assets/images/论坛/u185.svg"
        @click="$router.go(-1)" />
      <img
        class="hover:cursor-pointer"
        src="@/assets/images/论坛/u206.svg"
        @click="$router.push('/settings')" />
    </div>

    <div class="mt-16 flex flex-col">
      <div class="mb-16 flex justify-between">
        <LevelCard level="1" />
        <LevelCard level="2" />
        <LevelCard level="3" />
        <LevelCard level="4" />
        <LevelCard level="5" />
      </div>
      <div class="mb-16 flex justify-between">
        <LevelCard level="6" />
        <LevelCard level="7" />
        <LevelCard level="8" />
        <LevelCard level="9" />
        <LevelCard level="10" />
      </div>

      <div class="flex justify-around">
        <img
          class="h-8 w-8 hover:cursor-pointer"
          src="@/assets/images/休闲模式/u148.svg" />
        <img
          class="h-8 w-8 hover:cursor-pointer"
          src="@/assets/images/休闲模式/u149.svg" />
      </div>
    </div>
  </div>
</template>
