<template>
    <div>
        <img class="" src="../../assets/images/注册/u24.svg" />
        <el-form label-width="100px">
            <el-form-item label="请输入您的手机号：">
                <el-input v-model="username"></el-input>
            </el-form-item>
            <el-form-item label="请输入验证码：">
                <el-input v-model="pwd"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="primary">注册</el-button>
            </el-form-item>
        </el-form>
    </div>
</template> 

<script setup lang="ts">
const username = '';
const pwd = '';
</script>