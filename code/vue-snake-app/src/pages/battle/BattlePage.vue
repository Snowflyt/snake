<template>
  <div class="mx-auto w-4/5">
    <div class="mb-14 flex">
      <img
        class=""
        src="../../assets/images/设置/u243.svg"
        style="cursor: hand"
        @click="$router.go(-1)" />
    </div>
    <div class="ml-42 flex justify-around">
      <div class="left flex flex-col items-center">
        <img class="mb-5" src="../../assets/images/排位赛/u152.svg" />
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
        <img class="w-124 mb-10 h-80" src="../../assets/images/cover.png" />
        <div class="mb-8 flex w-96 items-center justify-around">
          <div
            class="flex items-center justify-center rounded-xl bg-gray-300 p-2"
            @click="$router.push('/game')">
            单人排位
          </div>
          <div
            class="flex items-center justify-center rounded-xl bg-gray-300 p-2">
            多人组队
          </div>
          <div
            class="flex items-center justify-center rounded-xl bg-gray-300 p-2">
            蛇王榜
          </div>
        </div>
        <div
          class="flex items-center justify-around rounded-xl bg-gradient-to-r from-red-600 to-blue-600 p-2 font-semibold">
          <div class="flex items-center justify-center">当前段位排位奖励：</div>
          <div class="flex items-center justify-center">
            <img
              class="ml-2 h-5 w-5"
              src="../../assets/images/商城/u213.svg" />100蛇币
            <img
              class="ml-2 h-5 w-5"
              src="../../assets/images/商城/u214.svg" />7蛇钻
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
