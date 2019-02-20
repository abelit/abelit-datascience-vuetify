import Vue from "vue";
import './plugins/vuetify'
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "bootstrap/dist/css/bootstrap.css";
import "jquery/dist/jquery.js";
import "bootstrap/dist/js/bootstrap.js";

import echarts from "echarts";
Vue.prototype.$echarts = echarts;

import axios from "axios";
axios.defaults.baseURL = "http://localhost:5000";
Vue.prototype.$axios = axios;

import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";
Vue.use(ElementUI);

import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'

Vue.use(VueMaterial)

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");