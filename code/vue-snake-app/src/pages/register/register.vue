<template>
    <div class="w-4/5 mx-auto">
        <div class="flex justify-center mb-7">
            <img class="" src="../../assets/images/注册/u24.svg" />
        </div>
        <div class="flex justify-center mb-3 font-bold text-2xl">用户注册</div>
        <el-form-item label="请输入您的手机号：">
            <el-input v-model="username"></el-input>
        </el-form-item>
        <el-form-item class="mr-4" label="请输入验证码：">
            <el-input v-model="pwd"></el-input>
        </el-form-item>
        <div class="flex justify-center">
            <button class="bg-black p-4 rounded-md w-32 text-white">注册</button>
        </div>
    </div>
</template> 

<script lang="ts">
export default {
    data() {
        return {
            username: '',
            pwd: ''
        }
    }
}
</script>