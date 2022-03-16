<template>
  <div class="login-container">
    <el-card class="login-card" shadow="always">
      <!-- <div v-for="o in 4" :key="o" class="text item">
        {{ '列表内容 ' + o }}
      </div> -->

      <el-form
        ref="loginForm"
        :model="loginForm"
        :rules="loginRules"
        class=""
        auto-complete="on"
        label-position="left"
      >
        <div class="title-container">
          <h3 class="title">登录</h3>
        </div>

        <el-form-item prop="username">
          <span class="svg-container">
            <svg-icon icon-class="user" />
          </span>
          <el-input
            ref="username"
            v-model="loginForm.username"
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
            v-model="loginForm.password"
            :type="passwordType"
            placeholder="密码"
            name="password"
            tabindex="2"
            auto-complete="on"
            @keyup.enter.native="handleLogin"
          />
          <span class="show-pwd" @click="showPwd">
            <svg-icon
              :icon-class="passwordType === 'password' ? 'eye' : 'eye-open'"
            />
          </span>
        </el-form-item>

        <div style="text-align: right">
          <el-link
            :loading="loading"
            type="primary"
            style="align: left"
            @click.native.prevent="handleRegister"
          >点我注册</el-link>
        </div>
        <div>
          <el-button
            :loading="loading"
            type="primary"
            style="width: 100%; margin-bottom:15%; margin-top:5%"
            @click.native.prevent="handleLogin"
          >登录</el-button>
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
import Cookie from 'js-cookie'
import { Message } from 'element-ui'
// import { setRouterByType } from '@/router'

export default {
  name: 'Login',
  data() {
    const validateUsername = (rule, value, callback) => {
      callback()
    }
    const validatePassword = (rule, value, callback) => {
      callback()
    }

    return {
      loginForm: {
        username: 'admin',
        password: 'admin'
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
    handleRegister() {
      this.$router.push({ path: '/register' })
    },
    handleLogin() {
      this.loading = true
      this.$axios.post('/api/user/login', this.loginForm).then(r => {
        this.loading = false
        console.log(r)
        if (r.data.data === 0) {
          Cookie.set('userId', r.data.userId)
          Cookie.set('username', r.data.username)
          Cookie.set('type', r.data.type)
          this.$router.push({ path: this.redirect || '/' })
        } else if (r.data.data === -2) {
          Message.error('表单未填写完整')
        } else if (r.data.data === -1) {
          Message.error('用户名或密码错误')
        }
      })

      // this.$axios({
      //   // baseUrl: '',
      //   method: 'get',
      //   url: '/api/baidu'
      // }).then(r => {
      //   console.log(r + 'ok')
      // })

      // this.$refs.loginForm.validate((valid) => {
      //   if (valid) {
      //     this.loading = true
      //     this.$store
      //       .dispatch('user/login', this.loginForm)
      //       .then(() => {
      //         this.$router.push({ path: this.redirect || '/' })
      //         this.loading = false
      //       })
      //       .catch(() => {
      //         this.loading = false
      //       })
      //   } else {
      //     console.log('error submit!!')
      //     return false
      //   }
      // })
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
