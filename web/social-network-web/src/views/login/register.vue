<template>
  <div class="login-container">
    <el-card class="login-card" shadow="always">

      <el-form
        ref="registerForm"
        :model="registerForm"
        :rules="loginRules"
        class=""
        auto-complete="on"
        label-position="left"
      >
        <div class="title-container">
          <h3 class="title">注册</h3>
        </div>

        <el-form-item prop="username">
          <span class="svg-container">
            <svg-icon icon-class="user" />
          </span>
          <el-input
            ref="username"
            v-model="registerForm.username"
            placeholder="用户名"
            name="username"
            type="text"
            tabindex="1"
            auto-complete="on"
          />
        </el-form-item>

        <el-form-item prop="password">
          <span class="svg-container">
            <svg-icon icon-class="password" />
          </span>
          <el-input
            :key="passwordType"
            ref="password"
            v-model="registerForm.password"
            :type="passwordType"
            placeholder="密码"
            name="password"
            tabindex="2"
            auto-complete="on"
          />
          <span class="show-pwd" @click="showPwd">
            <svg-icon
              :icon-class="passwordType === 'password' ? 'eye' : 'eye-open'"
            />
          </span>
        </el-form-item>

        <el-form-item prop="name">
          <span class="svg-container">
            <i class="el-icon-user" />
          </span>
          <el-input
            ref="name"
            v-model="registerForm.name"
            placeholder="姓名"
            name="name"
            type="text"
            tabindex="3"
            auto-complete="on"
          />
        </el-form-item>

        <el-form-item prop="contact">
          <span class="svg-container">
            <!-- <svg-icon icon-class="phone" /> -->
            <i class="el-icon-phone" />
          </span>
          <el-input
            ref="contact"
            v-model="registerForm.contact"
            placeholder="联系方式"
            name="contact"
            type="text"
            tabindex="4"
            auto-complete="on"
          />
        </el-form-item>
        <div style="text-align: right">
          <el-link
            :loading="loading"
            type="primary"
            style="align: left"
            @click.native.prevent="handleBack"
          >点我返回登录</el-link>
        </div>
        <div>
          <el-button
            :loading="loading"
            type="primary"
            style="width: 100%; margin-bottom:5%; margin-top:5%"
            @click.native.prevent="handleRegister"
          >注册</el-button>
        </div>

      <!-- <div class="tips">
        <span style="margin-right:20px;">username: admin</span>
        <span> password: any</span>
      </div> -->
      </el-form>
    </el-card>
  </div>
</template>

<script>
// import { validUsername } from '@/utils/validate'
import { Message } from 'element-ui'

export default {
  name: 'Register',
  data() {
    const validateUsername = (rule, value, callback) => {
      callback()
    }
    const validatePassword = (rule, value, callback) => {
      callback()
    }

    return {
      registerForm: {
        username: '',
        password: '',
        name: '',
        contact: '',
      },
      loginRules: {
        username: [
          { required: true, trigger: 'blur', validator: validateUsername }
        ],
        password: [
          { required: true, trigger: 'blur', validator: validatePassword }
        ]
      },
      loading: false,
      passwordType: 'password',
      redirect: undefined
    }
  },
  watch: {
    $route: {
      handler: function(route) {
        this.redirect = route.query && route.query.redirect
      },
      immediate: true
    }
  },
  methods: {
    showPwd() {
      if (this.passwordType === 'password') {
        this.passwordType = ''
      } else {
        this.passwordType = 'password'
      }
      this.$nextTick(() => {
        this.$refs.password.focus()
      })
    },
    handleBack() {
      this.$router.push({ path: '/login' })
    },
    handleRegister() {
      this.$axios.post('/api/user/add', this.registerForm).then(r => {
        if (r.data === -2) {
          Message.error('表单未填写完整')
        } else if (r.data === -1) {
          Message.error('用户名重复')
        } else if (r.data === 0) {
          this.$router.push({ path: this.redirect || '/login' })
        }
      })
    }
  }
}
</script>

<style lang="scss">
/* 修复input 背景不协调 和光标变色 */
/* Detail see https://github.com/PanJiaChen/vue-element-admin/pull/927 */

$bg: #575656;
$light_gray: #fff;
$cursor: #fff;

@supports (-webkit-mask: none) and (not (cater-color: $cursor)) {
  .login-container .el-input input {
    color: $cursor;
  }
}

/* reset element-ui css */
.login-container {
  .el-input {
    display: inline-block;
    height: 47px;
    width: 85%;

    input {
      background: transparent;
      border: 0px;
      -webkit-appearance: none;
      border-radius: 0px;
      padding: 12px 5px 12px 15px;
      color: $light_gray;
      height: 47px;
      caret-color: $cursor;

      &:-webkit-autofill {
        box-shadow: 0 0 0px 1000px #4e4d4d inset !important;
        -webkit-text-fill-color: $cursor !important;
      }
    }
  }

  .el-form-item {
    border: 1px solid rgba(255, 255, 255, 0.1);
    background: rgba(0, 0, 0, 0.1);
    border-radius: 5px;
    color: #454545;
  }
}
</style>

<style lang="scss" scoped>
// $bg: #2f3031;
$bg: #383838;
$bg_light: #575656;
$dark_gray: #889aa4;
$light_gray: #eee;

.login-container {
  min-height: 100%;
  width: 100%;
  background-color: $bg;
  overflow: hidden;
  display:flex;
  justify-content:center; //水平居中
  align-items:center; //垂直居中

  .login-card {
    border-color: $bg_light;
    background-color: $bg_light;
    position: relative;
    width: 520px;
    max-width: 100%;
    padding: 10px 10px 0;
    overflow: hidden;
  }

  .tips {
    font-size: 14px;
    color: #fff;
    margin-bottom: 10px;

    span {
      &:first-of-type {
        margin-right: 16px;
      }
    }
  }

  .svg-container {
    padding: 6px 5px 6px 15px;
    color: $dark_gray;
    vertical-align: middle;
    width: 30px;
    display: inline-block;
  }

  .title-container {
    position: relative;

    .title {
      font-size: 26px;
      color: $light_gray;
      margin: 0px auto 40px auto;
      text-align: center;
      font-weight: bold;
    }
  }

  .show-pwd {
    position: absolute;
    right: 10px;
    top: 7px;
    font-size: 16px;
    color: $dark_gray;
    cursor: pointer;
    user-select: none;
  }
}
</style>
