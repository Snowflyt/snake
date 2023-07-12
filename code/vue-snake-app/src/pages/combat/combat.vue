<template>
  <div
    class="absolute flex h-[100%] w-[100%] flex-wrap content-center items-center justify-center border-2 border-black">
    <el-container class="h-[100%]">
      <el-header class="h-[30%]">
        <div class="w-100 flex h-[30%] flex-row justify-between">
          <img
            id="u226_img"
            class="inline h-[80%]"
            src="../../assets/images/对战/u226.svg" />

          <img
            id="u227_img"
            class="inline"
            src="../../assets/images/对战/u227.svg" />
        </div>
        <div class="w-100 flex flex-row justify-between">
          <button
            class="text-2xl font-bold"
            @click="
              () => {
                $router.push('/userCenter');
              }
            ">
            返回
          </button>
          <button class="text-2xl font-bold">设置</button>
        </div>
        <div class="w-100 flex h-[30%] flex-row justify-center">
          <b class="text-5xl font-bold">房间号:</b>
          <input v-model="RoomID" class="border-2 border-black" type="text" />
        </div>
      </el-header>
      <el-main class="h-[60%] bg-slate-300">
        <div class="w-100 flex flex-row justify-between">
          <img class="inline" src="../../assets/images/对战/u228.svg" />
        </div>
      </el-main>
      <el-footer>
        <div class="flex justify-center">
          <el-button class="">submit</el-button>
          <el-button class="">clear</el-button>
        </div>
      </el-footer>
    </el-container>
  </div>
</template>

<script></script>
