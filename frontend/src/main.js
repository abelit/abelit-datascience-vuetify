import Vue from "vue";
import App from "./App.vue";
import router from "@/router";
import store from "@/store";
import vuetify from './plugins/vuetify';
import '@babel/polyfill'
import 'roboto-fontface/css/roboto/roboto-fontface.css'

// import marterial icon fonts designed by google
import "material-design-icons-iconfont/dist/material-design-icons.css";

// import material design icon fonts
import "@mdi/font/css/materialdesignicons.css";

// import NProgress
import NProgress from "nprogress";
import 'nprogress/nprogress.css'

// International
import i18n from './locales';

// import Echarts
import echarts from "echarts";
Vue.prototype.$echarts = echarts;

// 导入MD5
import md5 from 'js-md5';
Vue.prototype.$md5 = md5;

Vue.config.productionTip = false;

// router gards
router.beforeEach((to, _from, next) => {
  NProgress.start();
  // store.state.appLoading = true
  console.log("before each ...")

  // // This goes through the matched routes from last to first, finding the closest route with a title.
  // // eg. if we have /some/deep/nested/route and /some, /deep, and /nested have titles, nested's will be chosen.
  // const nearestWithTitle = to.matched.slice().reverse().find(r => r.meta && r.meta.title);

  // // Find the nearest route element with meta tags.
  // const nearestWithMeta = to.matched.slice().reverse().find(r => r.meta && r.meta.metaTags);
  // const previousNearestWithMeta = _from.matched.slice().reverse().find(r => r.meta && r.meta.metaTags);

  // // If a route with a title was found, set the document (page) title to that value.
  // if (nearestWithTitle) document.title = "Data AV - " + nearestWithTitle.meta.title;

  if (store.state.lockPassword && to.path !== "/lock") {
    next({
      path: "/lock"
    });
  } else {
    // next()
    next()
  }
});

router.afterEach((_to, _from) => {
  NProgress.done();
  // store.state.appLoading = false
  console.log("after each ...")

});

new Vue({
  router,
  store,
  i18n,
  vuetify,
  render: h => h(App)
}).$mount("#app");