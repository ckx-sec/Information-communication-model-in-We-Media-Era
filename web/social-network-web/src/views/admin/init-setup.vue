<template>
  <div class="app-container">
    <el-form ref="form" :model="form" label-width="140px">
      <el-form-item label="计算轮数">
        <el-input-number
          v-model="num"
          @change="handleChange"
          :min="1"
          :max="10"
          label="计算轮数"
        ></el-input-number>
      </el-form-item>
      <el-form-item label="初始字符串" label-width="140px">
        <el-input type="textarea" v-model="form.desc"></el-input>
      </el-form-item>
      <el-form-item label="传播阈值">
        <el-input-number
          v-model="num_percent"
          @change="handleChange"
          :min="1"
          :max="100"
          label="传播阈值"
        ></el-input-number>
        （%）
      </el-form-item>
      <el-form-item label="blogger层挑选阈值" label-width="140px">
        <el-input-number
          v-model="num_blogger"
          @change="handleChange"
          :min="1"
          :max="10000"
          label="传播阈值"
        ></el-input-number>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">保存</el-button>
        <el-button>取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import waves from "@/directive/waves"; // waves directive
import { parseTime } from "@/utils";
import jsCookie from "js-cookie";

export default {
  name: "InitSetup",
  data() {
    return {
      num: 6,
      num_percent: 60,
      num_blogger: 1580,
      form: {
        name: "",
        region: "",
        date1: "",
        date2: "",
        delivery: false,
        type: [],
        resource: "",
        desc: "",
      },
    };
  },
  watch: {},
  mounted() {
  },
  created() {
  },
  methods: {
    handleChange(value) {
      console.log(value);
    },
    onSubmit() {
      console.log("submit!");
      this.$router.push("/")
    },
  },
};
</script>
