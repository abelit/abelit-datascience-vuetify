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

import VueMaterial from 'vue-material';
import 'vue-material/dist/vue-material.min.css';
import 'vue-material/dist/theme/default.css';
Vue.use(VueMaterial);

import VueI18n from 'vue-i18n';

Vue.use(VueI18n);

Vue.config.productionTip = false;

const i18n = new VueI18n({
  locale: 'zh_CN', // 语言标识
  messages: {
    'zh_CN': require('./common/lang/zh'), // 中文语言包
    'en_US': require('./common/lang/en') // 英文语言包
  }
});


import VeeValidate from 'vee-validate';
import zh from 'vee-validate/dist/locale/zh_CN';
import en from 'vee-validate/dist/locale/en';

Vue.use(VeeValidate, {
  i18n,
  i18nRootKey: 'validation',
  dictionary: {
    en_US: en,
    zh_CN: zh
  }
});

new Vue({
  i18n,
  router,
  store,
  render: h => h(App)
}).$mount("#app");
