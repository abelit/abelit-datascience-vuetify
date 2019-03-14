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

// Dev
import Login from "./views/auth/Login.vue";
import Register from "./views/auth/Register.vue";
// import auth from "./helpers/auth.js";

Vue.use(Router);

// function requireAuth(to, from, next) {
//   if (!auth.loggedIn()) {
//     next({
//       path: "/user/login",
//       query: {
//         redirect: to.fullPath
//       }
//     });
//   } else {
//     next();
//   }
// }

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
      path: "/demo/uidemo",
      name: "uidemo",
      component: UIDemo
    },
    {
      path: "/demo/fullscreen",
      name: "fullscreen",
      component: FullscreenDemo
    },
    {
      path: "/demo/mapdemo",
      name: "mapdemo",
      component: AmchartsDemo
    },
    {
      path: "/demo/d3demo",
      name: "d3demo",
      component: D3Demo
    },
    {
      path: "/demo/testvue",
      name: "testvue",
      component: TestVue
    },
    {
      path: "/demo/trans",
      name: "trans",
      component: TranslateDemo
    },
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
    }
  ]
});

// // 拦截所有路由
// router.beforeEach((to, from, next) => {
//   // redirect to login page if not logged in and trying to access a restricted page
//   const publicPages = ["/user/login"];
//   const authRequired = !publicPages.includes(to.path);
//   const loggedIn = localStorage.getItem("user");

//   if (authRequired && !loggedIn) {
//     return next("/user/login");
//   }

//   next();
// });

// let entryUrl = "/about";

router.beforeEach(async (to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (localStorage.token) {
      return next()
    }
    next({path:'/user/login',query:{url: to.fullPath} });
  } else {
    next();
  }
});

export default router;