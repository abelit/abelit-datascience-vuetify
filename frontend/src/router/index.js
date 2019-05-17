/* eslint-disable no-unused-vars */
import Vue from "vue";
import Router from "vue-router";
import paths from "./paths";
import NProgress from "nprogress";
import "nprogress/nprogress.css";
import store from "../store";

Vue.use(Router);
const router = new Router({
  base: "/",
  mode: "hash",
  linkActiveClass: "active",
  routes: paths
});
// router gards
router.beforeEach((to, _from, next) => {
  NProgress.start();
  if (store.state.isLock && to.path !== "/lock") {
    next({
      path: "/lock"
    });
  } else {
    // next()
    if (to.matched.some(record => record.meta.requireAuth)) {
      if (localStorage.getItem("token")) {
        next();
      } else {
        next({
          path: "/user/login",
          query: {
            url: to.fullPath
          }
        });
      }
    } else {
      next();
    }
  }
});

router.afterEach((to, from) => {
  NProgress.done();
});

export default router;
