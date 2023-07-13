<template>
  <div class="mx-auto w-4/5">
    <div class="flex justify-between">
      <div class="flex w-44 justify-around">
        <img
          class=""
          src="../../assets/images/主页/u38.svg"
          style="cursor: hand"
          @click="$router.push('/shop')" />商城
        <img
          class=""
          src="../../assets/images/主页/u39.svg"
          style="cursor: hand"
          @click="$router.push('/chat')" />论坛
      </div>
      <div class="flex w-44 justify-around">
        <img
          class=""
          src="../../assets/images/主页/u34.svg"
          style="cursor: hand"
          @click="$router.push('/user-center')" />用户
        <img
          class=""
          src="../../assets/images/主页/u35.svg"
          style="cursor: hand"
          @click="$router.push('/setting')" />设置
      </div>
    </div>
    <div class="w-50 mt-5">
      <div class="flex justify-center">
        <p class="text-5xl">Code Snake</p>
      </div>
      <div class="flex justify-center">
        <img src="../../assets/images/cover.png" alt="snake" />
      </div>
      <div class="ml-96 mt-3 flex w-1/3 justify-between">
        <button
          class="w-32 rounded-md bg-red-600 p-4"
          @click="$router.push('/battle')">
          竞技模式
        </button>
        <button
          class="w-32 rounded-md bg-blue-600 p-4"
          @click="$router.push('/leisure')">
          休闲模式
        </button>
      </div>
    </div>
    <div class="mt-14 flex justify-center">
      Copyright<img
        class="inline-block"
        src="../../assets/images/主页/u44.svg" />苏州大学蛇行者工作室出品
    </div>
  </div>
</template>
