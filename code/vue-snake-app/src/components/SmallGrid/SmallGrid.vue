<template>
  <div class="PassPic">
    <div
      class="flex h-[70%] content-center items-center justify-center border-2 border-black">
      <div>
        {{ number }}
      </div>
      <div>
        <el-rate v-model="value1" :color="color" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      size: 'large',
      number: 8,
      value1: null,
      color: null,
    };
  },
};
</script>
