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
          path: "grid",
          name: "grid",
          component: () => import("@/views/demo/Grid.vue")
        },
        {
          path: "contact",
          name: "contact",
          component: () => import("@/views/demo/GoogleContact.vue")
        },
        {
          path: "drag",
          name: "drag",
          component: () => import("@/views/demo/DragDemo.vue")
        },
        {
          path: "dynamicgrid",
          name: "dynamicgrid",
          component: () => import("@/views/demo/DynamicGrid.vue")
        },
        {
          path: "gridorder",
          name: "gridorder",
          component: () => import("@/views/demo/GridOrder.vue")
        },
        {
          path: "eq/1",
          name: "eq1",
          component: () => import("@/views/demo/EqDemo.vue")
        },
        {
          path: "eq/2",
          name: "eq2",
          component: () => import("@/views/demo/EqTwo.vue")
        }
      ]
    },
    {
      path: "/",
      name: "Root",
      component: () => import("@/views/layout/AppLayout"),
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
        {
          path: "form",
          name: "form",
          // route level code-splitting
          // this generates a separate chunk (about.[hash].js) for this route
          // which is lazy-loaded when the route is visited.
          component: () =>
            import(
              /* webpackChunkName: "about" */ "@/views/form/AppMakeForm.vue"
            )
        }
      ]
    },
    {
      path: "/lock",
      name: "Lock",
      component: () => import("@/views/lock/AppLock")
    },
    {
      path: "/login",
      name: "Login",
      component: () => import("@/views/user/AppLogin")
    }
  ]
});
