<template>
  <div class="mx-auto w-4/5">
    <div class="mb-14 flex">
      <img
        class=""
        src="../../assets/images/设置/u243.svg"
        style="cursor: hand"
        @click="
          () => {
            $router.go(-1);
          }
        " />
    </div>
    <div class="mb-8 flex justify-around">
      <span class="k">背景音乐:</span>
      <el-slider v-model="value2" class="w-1/2"></el-slider>
    </div>
    <div class="mb-8 flex justify-around">
      <span class="demonstration">游戏音效:</span>
      <el-slider v-model="value2" class="w-1/2"></el-slider>
    </div>
    <div class="mb-8 ml-32 flex">
      <!-- <el-dropdown class="">
                <el-button type="primary">
                    选择编程语言<i class="text-xs"></i>
                </el-button>
                <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item>c/c++</el-dropdown-item>
                    <el-dropdown-item>java</el-dropdown-item>
                    <el-dropdown-item>python</el-dropdown-item>
                    <el-dropdown-item>javascript</el-dropdown-item>
                    <el-dropdown-item>go</el-dropdown-item>
                </el-dropdown-menu>
            </el-dropdown> -->
      <span class="mr-56">选择编程语言:</span>
      <el-radio v-model="radio" label="1">c/c++</el-radio>
      <el-radio v-model="radio" label="2">java</el-radio>
      <el-radio v-model="radio" label="3">javascript</el-radio>
      <el-radio v-model="radio" label="4">go</el-radio>
    </div>
    <div class="ml-32 flex">
      <span class="mr-64">代码提示:</span>
      <el-radio v-model="radio" label="1">开</el-radio>
      <el-radio v-model="radio" label="2">关</el-radio>
    </div>
  </div>
</template>

<script setup lang="ts">
const value2 = 50;
const radio = '1';
</script>
