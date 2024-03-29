import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import TestVue from "./components/TestVue.vue";
import TestAvstar from "./components/TestAvstar.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/home",
      name: "home",
      component: Home
    },
    {
      path: "/about",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () =>
        import(/* webpackChunkName: "about" */ "./views/About.vue")
    },
    {
      path: "/testvue",
      name: "testvue",
      component: TestVue
    },
    {
      path: "/testav",
      name: "testav",
      component: TestAvstar
    },
  ]
});
