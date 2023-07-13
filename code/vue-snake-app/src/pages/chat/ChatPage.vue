<template>
  <div class="mx-auto w-4/5">
    <div class="flex justify-between">
      <img
        class=""
        src="../../assets/images/论坛/u185.svg"
        style="cursor: hand"
        @click="$router.go(-1)" />
      <img
        class=""
        src="../../assets/images/论坛/u206.svg"
        style="cursor: hand"
        @click="$router.push('/settings')" />
    </div>
    <div class="ml-80 mt-5">
      <div class="flex">
        <h3>热议话题</h3>
        <img class="ml-2 h-5 w-5" src="../../assets/images/论坛/u187.svg" />
      </div>
      <div class="ml-36 mt-3 flex flex-col justify-around">
        <div class="mb-5 flex w-3/5 justify-around">
          <img class="shrink-0" src="../../assets/images/论坛/u190.svg" />
          <div class="h-38 w-3/5 border-2 border-gray-400"></div>
          <div class="flex items-end">
            <img
              class="mr-2 h-5 w-5 md:shrink-0"
              src="../../assets/images/论坛/u188.svg" />
            <img
              class="h-5 w-5 md:shrink-0"
              src="../../assets/images/论坛/u189.svg" />
          </div>
        </div>
        <div class="mb-5 flex w-3/5 justify-around">
          <img class="shrink-0" src="../../assets/images/论坛/u190.svg" />
          <div class="h-38 w-3/5 border-2 border-gray-400"></div>
          <div class="flex items-end">
            <img
              class="mr-2 h-5 w-5 md:shrink-0"
              src="../../assets/images/论坛/u188.svg" />
            <img
              class="h-5 w-5 md:shrink-0"
              src="../../assets/images/论坛/u189.svg" />
          </div>
        </div>
        <div class="mb-5 flex w-3/5 justify-around">
          <img class="shrink-0" src="../../assets/images/论坛/u190.svg" />
          <div class="h-38 w-3/5 border-2 border-gray-400"></div>
          <div class="flex items-end">
            <img
              class="mr-2 h-5 w-5 md:shrink-0"
              src="../../assets/images/论坛/u188.svg" />
            <img
              class="h-5 w-5 md:shrink-0"
              src="../../assets/images/论坛/u189.svg" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
