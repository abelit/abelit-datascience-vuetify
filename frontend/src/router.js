import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import PageDemo from "./components/PageDemo.vue";
import UIDemo from "@/components/UIDemo.vue";
import AmchartsDemo from "@/components/AmchartsDemo.vue";

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
      path: "/mapdemo",
      name: "mapdemo",
      component: AmchartsDemo
    }
  ]
});