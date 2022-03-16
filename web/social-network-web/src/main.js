import Vue from 'vue'

import 'normalize.css/normalize.css' // A modern alternative to CSS resets

import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
// import locale from 'element-ui/lib/locale/lang/en' // lang i18n

import '@/styles/index.scss' // global css

import App from './App'
import store from './store'
import router from './router'

import '@/icons' // icon
import '@/permission' // permission control

import axios from 'axios'
Vue.prototype.$axios = axios // 全局注册，使用方法为:this.$axios

/**
 * If you don't want to use mock-server
 * you want to use MockJs for mock api
 * you can execute: mockXHR()
 *
 * Currently MockJs will be used in the production environment,
 * please remove it before going online ! ! !
 */
// if (process.env.NODE_ENV === 'production') {
//   const { mockXHR } = require('../mock')
//   mockXHR()
// }

// set ElementUI lang to EN
// Vue.use(ElementUI, { locale })
// 如果想要中文版 element-ui，按如下方式声明
Vue.use(ElementUI)

Vue.config.productionTip = false

Vue.component('remote-script', {
  props: {
    src: {
      type: String,
      required: true
    }
  },
  render: function(createElement) {
    var self = this
    return createElement('script', {
      attrs: {
        type: 'text/javascript',
        src: this.src
      },
      on: {
        load: function(event) {
          self.$emit('load', event)
        },
        error: function(event) {
          self.$emit('error', event)
        },
        readystatechange: function(event) {
          if (this.readyState === 'complete') {
            self.$emit('load', event)
          }
        }
      }
    })
  }
})

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})
