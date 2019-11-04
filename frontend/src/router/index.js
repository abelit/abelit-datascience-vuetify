import Vue from "vue";
import Router from "vue-router";
import Home from "@/views/Home.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    // {
    //   path: "/",
    //   name: "home",
    //   component: Home
    // },
    // {
    //   path: "/about",
    //   name: "about",
    //   // route level code-splitting
    //   // this generates a separate chunk (about.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () =>
    //     import(/* webpackChunkName: "about" */ "@/views/About.vue")
    // },
    {
      path: "/demo",
      name: "demo",
      component: () => import("@/App.vue"),
      children: [
        {
          path: "googlekeep",
          name: "googlekeep",
          component: () => import("@/views/demo/GoogleKeep.vue")
        },
        {
          path: "center",
          name: "center",
          component: () => import("@/views/demo/Center.vue")
        },
        {
          path: "complex",
          name: "complex",
          component: () => import("@/views/demo/Complex.vue")
        },
        {
          path: "sandbox",
          name: "sandbox",
          component: () => import("@/views/demo/Sandbox.vue")
        },
        {
          path: "test",
          name: "test",
          component: () => import("@/views/demo/TestGrid.vue")
        }
      ]
    },
    {
      path: "/",
      name: "Root",
      component: () => import("@/views/layout/Layout"),
      children: [
        {
          path: "",
          name: "home",
          component: Home
        },
        {
          path: "about",
          name: "about",
          // route level code-splitting
          // this generates a separate chunk (about.[hash].js) for this route
          // which is lazy-loaded when the route is visited.
          component: () =>
            import(/* webpackChunkName: "about" */ "@/views/About.vue")
        },
      ]
    }
  ]
});