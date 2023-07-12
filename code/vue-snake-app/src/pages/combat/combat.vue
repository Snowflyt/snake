<template>
  <div
    class="absolute flex h-[100%] w-[100%] flex-wrap content-center items-center justify-center border-2 border-black">
    <el-container class="h-[100%]">
      <el-header class="h-[30%]">
        <div class="w-100 flex flex-row justify-between">
          <img
            id="u226_img"
            class="inline"
            src="../../assets/images/对战/u226.svg" />

          <img
            id="u227_img"
            class="inline"
            src="../../assets/images/对战/u227.svg" />
        </div>
        <div class="w-100 flex flex-row justify-between">
          <b>返回</b>
          <b>设置</b>
        </div>
        <div class="w-100 flex flex-row justify-center">
          <b>房间号:</b>
          <input v-model="RoomID" />
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
