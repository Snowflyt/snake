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
        @click="$router.push('/setting')" />
    </div>
    <div class="">
      <div
        class="ml-28 mt-5 flex h-14 w-7/12 items-center border-2 border-gray-600">
        <img class="ml-2 h-5 w-5" src="../../assets/images/商城/u213.svg" />9999
        <img class="ml-2 h-5 w-5" src="../../assets/images/商城/u214.svg" />711
      </div>
      <div
        class="ml-28 flex w-7/12 flex-col justify-around border-2 border-gray-600 pl-8">
        <div class="mb-5 mt-8 flex w-3/5 justify-around">
          <img class="shrink-0" src="../../assets/images/商城/u217.svg" />
          <div class="h-38 w-3/5 border-2 border-gray-400">
            <div>功能：xxx</div>
            <div>价格：xxx</div>
          </div>
          <div class="flex items-end">
            <button class="rounded-lg bg-gray-200 p-1">购买</button>
          </div>
        </div>
        <div class="mb-5 flex w-3/5 justify-around">
          <img class="shrink-0" src="../../assets/images/商城/u217.svg" />
          <div class="h-38 w-3/5 border-2 border-gray-400">
            <div>功能：xxx</div>
            <div>价格：xxx</div>
          </div>
          <div class="flex items-end">
            <button class="rounded-lg bg-gray-200 p-1">购买</button>
          </div>
        </div>
        <div class="mb-5 flex w-3/5 justify-around">
          <img class="shrink-0" src="../../assets/images/商城/u217.svg" />
          <div class="h-38 w-3/5 border-2 border-gray-400">
            <div>功能：xxx</div>
            <div>价格：xxx</div>
          </div>
          <div class="flex items-end">
            <button class="rounded-lg bg-gray-200 p-1">购买</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
