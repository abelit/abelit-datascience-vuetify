// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
// import './assets/bootstrap/css/bootstrap.css'
// import './assets/render/jquery-3.3.1.js'
// import './assets/bootstrap/js/bootstrap.js'
import 'bootstrap/dist/css/bootstrap.css'
import 'jquery/dist/jquery.js'
import 'bootstrap/dist/js/bootstrap.js'

Vue.config.productionTip = false
/* eslint-disable no-new */
new Vue({
  // mode: 'history',
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
