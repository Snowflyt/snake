<template>
  <div class="mx-auto w-4/5">
    <div class="mb-16 flex justify-between">
      <div class="flex w-44 justify-around">
        <img
          class=""
          src="@/assets/images/主页/u38.svg"
          style="cursor: hand"
          @click="$router.push('/shop')" />商城
        <img
          class=""
          src="@/assets/images/主页/u39.svg"
          style="cursor: hand"
          @click="$router.push('/chat')" />论坛
      </div>
      <div class="flex w-44 justify-around">
        <img
          class=""
          src="@/assets/images/主页/u34.svg"
          style="cursor: hand"
          @click="$router.push('/user-center')" />用户
        <img
          class=""
          src="@/assets/images/主页/u35.svg"
          style="cursor: hand"
          @click="$router.push('/settings')" />设置
      </div>
    </div>

    <div class="w-50 mt-5 flex flex-col items-center">
      <p class="text-5xl">Code Snake</p>
      <img src="@/assets/images/cover.png" alt="snake" />
      <div class="mt-3 flex w-1/3 flex-row space-x-6">
        <el-button
          class="h-12 w-32 rounded-md bg-red-600 text-base font-bold text-white"
          color="#dc2626"
          @click="$router.push('/battle')">
          竞技模式
        </el-button>
        <el-button
          class="h-12 w-32 rounded-md bg-blue-600 text-base font-bold text-white"
          color="#2563eb"
          @click="$router.push('/leisure')">
          休闲模式
        </el-button>
      </div>
    </div>

    <div class="mt-14 flex items-center justify-center">
      Copyright© 苏州大学蛇行者工作室出品
    </div>
  </div>
</template>
