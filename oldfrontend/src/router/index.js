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
  
  // This goes through the matched routes from last to first, finding the closest route with a title.
  // eg. if we have /some/deep/nested/route and /some, /deep, and /nested have titles, nested's will be chosen.
  const nearestWithTitle = to.matched.slice().reverse().find(r => r.meta && r.meta.title);

  // Find the nearest route element with meta tags.
  const nearestWithMeta = to.matched.slice().reverse().find(r => r.meta && r.meta.metaTags);
  const previousNearestWithMeta = _from.matched.slice().reverse().find(r => r.meta && r.meta.metaTags);

  // If a route with a title was found, set the document (page) title to that value.
  if (nearestWithTitle) document.title = "Data AV - " + nearestWithTitle.meta.title;

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
