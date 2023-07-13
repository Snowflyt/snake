<script setup lang="ts">
import { onMounted, ref, watch } from 'vue';

import CodeEditor from '@/components/CodeEditor';

const roomId = ref('');
const code = ref('');

const canvas = ref<HTMLCanvasElement | null>(null);
const ctx = ref<CanvasRenderingContext2D | null>(null);
const timeInterval = ref<number | null>(null);

const colors = ref([
  '#000000',
  '#FF0000',
  '#00FF00',
  '#0000FF',
  '#FFFF00',
  '#FF00FF',
  '#00FFFF',
]);

const snake = [
  [2, 3],
  [2, 4],
  [2, 5],
  [3, 5],
  [4, 5],
  [4, 4],
  [5, 4],
  [5, 5],
];
const gridWidth = 10;
const gapWidth = 5;

onMounted(() => {
  canvas.value = document.querySelector('#canvas1') as HTMLCanvasElement;
  ctx.value = canvas.value.getContext('2d');
});

const drawSnake = () => {
  if (!ctx.value) return;

  ctx.value.fillStyle = colors.value[0];
  console.log('herl');
  for (let i = 0; i < snake.length; i++) {
    var temp = gerGridLeftUp(snake[i]);
    ctx.value.fillRect(temp[0], temp[1], gridWidth, gridWidth);
  }
};

const refreshAllTheTime = () => {
  timeInterval.value = setInterval(() => {
    drawSnake();
  }, 1000);
};
const gerGridLeftUp = (g: number[]) => {
  return [g[0] * (gridWidth + gapWidth), g[1] * (gridWidth + gapWidth)];
};

const stopFreshing = () => {
  if (timeInterval.value) clearInterval(timeInterval.value);
};

watch(
  () => code.value,
  (code) => {
    console.log('start sending');
    console.log(code);
    console.log('stop sending');
  },
);
</script>

<template>
  <div
    class="absolute flex h-[100%] w-[100%] flex-wrap content-center items-center justify-center border-2 border-black">
    <el-container class="h-[100%]">
      <el-header class="h-[20%]">
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
          <button class="text-2xl font-bold" @click="$router.go(-1)">
            返回
          </button>
          <button class="text-2xl font-bold" @click="$router.push('/setting')">
            设置
          </button>
        </div>
        <div class="w-100 flex h-[30%] flex-row justify-center">
          <b class="text-2xl font-bold">房间号:</b>
          <input v-model="roomId" class="border-2 border-black" type="text" />
        </div>
      </el-header>
      <el-main class="h-[65%] bg-slate-300">
        <div>
          <p class="relative left-[17%] inline">对战区</p>
          <p class="relative left-[70%] inline">代码区</p>
        </div>
        <div class="w-100 flex h-[100%] flex-row justify-between bg-slate-100">
          <canvas
            id="canvas1"
            class="h-[400] w-[45%] border-2 border-black"></canvas>

          <div class="w-[45%]">
            <CodeEditor v-model="code" />
          </div>
        </div>
      </el-main>
      <el-footer>
        <div class="flex justify-center">
          <el-button class="" @click="refreshAllTheTime">submit</el-button>
          <el-button class="" @click="stopFreshing">clear</el-button>
        </div>
      </el-footer>
    </el-container>
  </div>
</template>
