import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import PageDemo from "./components/PageDemo.vue";
import UIDemo from "@/components/UIDemo.vue";
import AmchartsDemo from "@/components/AmchartsDemo.vue";

import FullscreenDemo from "@/components/FullscreenDemo.vue";

import D3Demo from "@/components/D3Demo.vue";
import TestVue from "@/components/TestVue.vue";

import TranslateDemo from "@/components/TranslateDemo";

import FormDemo from "@/components/FormDemo";

import Login from "./views/Login.vue";

Vue.use(Router);

export default new Router({
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
        import( /* webpackChunkName: "about" */ "./views/About.vue")
    },
    {
      path: "/demo",
      name: "demo",
      component: PageDemo
    },
    {
      path: "/uidemo",
      name: "uidemo",
      component: UIDemo
    },
    {
      path: "/fullscreen",
      name: "fullscreen",
      component: FullscreenDemo
    },
    {
      path: "/mapdemo",
      name: "mapdemo",
      component: AmchartsDemo
    },
    {
      path: "/d3demo",
      name: "d3demo",
      component: D3Demo
    },
    {
      path: "/testvue",
      name: "testvue",
      component: TestVue
    },
    {
      path: "/trans",
      name: "trans",
      component: TranslateDemo
    },
    {
      path: "/form",
      name: "form",
      component: FormDemo
    }, {
      path: "/login",
      name: "login",
      component: Login
    }
  ]
});