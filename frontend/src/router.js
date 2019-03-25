import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";

// Demo
import PageDemo from "./components/demo/PageDemo.vue";
import UIDemo from "@/components/demo/UIDemo.vue";
import AmchartsDemo from "@/components/demo/AmchartsDemo.vue";
import FullscreenDemo from "@/components/demo/FullscreenDemo.vue";
import D3Demo from "@/components/demo/D3Demo.vue";
import TestVue from "@/components/demo/TestVue.vue";
import TranslateDemo from "@/components/demo/TranslateDemo";
import FormDemo from "@/components/demo/FormDemo";
import TestPath from "@/components/demo/TestPath";
import TestVuex from "@/components/demo/TestVuex";

// Dev
import Login from "./views/auth/Login.vue";
import Register from "./views/auth/Register.vue";
import NotFound from "@/views/NotFound";
// import auth from "./helpers/auth.js";

Vue.use(Router);

const router = new Router({
  // mode: "history",
  base: process.env.BASE_URL,
  routes: [{
      path: "/",
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
        import( /* webpackChunkName: "about" */ "./views/About.vue"),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: "/demo",
      name: "demo",
      component: PageDemo
    },
    {
      path: "/demo/vuex",
      name: "vuex",
      component: TestVuex
    },
    // {
    //   path: "/demo/uidemo",
    //   name: "uidemo",
    //   component: UIDemo
    // },
    {
      path: "/demo/fullscreen",
      name: "fullscreen",
      component: FullscreenDemo
    },
    // {
    //   path: "/demo/mapdemo",
    //   name: "mapdemo",
    //   component: AmchartsDemo
    // },

    {
      path: "/demo/testvue",
      name: "testvue",
      component: TestVue
    },
    // {
    //   path: "/demo/trans",
    //   name: "trans",
    //   component: TranslateDemo
    // },
    {
      path: "/demo/form",
      name: "form",
      component: FormDemo,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: "/demo/testpath",
      name: "testpath",
      component: TestPath
    },
    {
      path: "/user/login",
      name: "login",
      component: Login
    },
    {
      path: "/user/register",
      name: "register",
      component: Register
    },
    // {
    //   path: '*',
    //   name: "404",
    //   component: NotFound
    // }
  ]
});

export default router;
