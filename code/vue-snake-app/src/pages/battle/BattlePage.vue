<template>
  <div class="mx-auto w-4/5">
    <div class="mb-14 flex">
      <img
        class="hover:cursor-pointer"
        src="@/assets/images/设置/u243.svg"
        @click="$router.go(-1)" />
    </div>

    <div class="ml-42 flex justify-around space-x-8 border-gray-300 pl-8">
      <div class="left mt-16 flex flex-col items-center">
        <img class="mb-5 h-64 w-64" src="@/assets/images/排位赛/u152.svg" />
        <div
          class="mb-3 flex items-center justify-center rounded-xl bg-gray-300 p-2">
          当前段位：倔强青铜
        </div>
        <div
          class="mb-3 flex items-center justify-center rounded-xl bg-gray-300 p-2">
          胜点：0
        </div>
        <div
          class="mb-3 flex items-center justify-center rounded-xl bg-gray-300 p-2">
          超过了99%的玩家
        </div>
      </div>

      <div class="right flex flex-col items-center">
        <div class="mt-5">
          <img
            class="w-124 mb-10 h-80 border-2 border-gray-300"
            src="@/assets/images/cover.png" />
        </div>
        <div class="mb-8 flex w-96 items-center justify-around">
          <el-button
            class="h-10 w-28 rounded-lg bg-blue-600 text-base font-bold text-white"
            color="#2563eb"
            @click="$router.push('/game')">
            单人排位
          </el-button>
          <el-button
            class="h-10 w-28 rounded-lg bg-red-600 text-base font-bold text-white"
            color="#dc2626">
            多人组队
          </el-button>
          <el-button
            class="h-10 w-28 rounded-lg bg-gray-600 text-base font-bold text-white"
            color="#6b7280">
            蛇王榜
          </el-button>
        </div>
        <div
          class="flex items-center justify-around rounded-xl bg-gradient-to-r from-red-600 to-blue-600 p-2 font-semibold">
          <div class="flex items-center justify-center">当前段位排位奖励：</div>
          <div class="flex items-center justify-center">
            <img
              class="ml-2 h-5 w-5"
              src="@/assets/images/商城/u213.svg" />100蛇币
            <img
              class="ml-2 h-5 w-5"
              src="@/assets/images/商城/u214.svg" />7蛇钻
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
