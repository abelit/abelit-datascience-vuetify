import Vue from "vue";
import Router from "vue-router";

// Demo
// import PageDemo from "./components/demo/PageDemo.vue";
// import UIDemo from "@/components/demo/UIDemo.vue";
// import AmchartsDemo from "@/components/demo/AmchartsDemo.vue";
// import FullscreenDemo from "@/components/demo/FullscreenDemo.vue";
// import D3Demo from "@/components/demo/D3Demo.vue";
// import TestVue from "@/components/demo/TestVue.vue";
// import TranslateDemo from "@/components/demo/TranslateDemo";
// import FormDemo from "@/components/demo/FormDemo";
// import TestPath from "@/components/demo/TestPath";
// import TestVuex from "@/components/demo/TestVuex";
// import PMenuDemo from "@/components/demo/PMenuDemo";
// import AddGroup from "@/components/demo/AddGroup";
// import AddPosition from "@/components/demo/AddPosition";
// import AddUser from "@/components/demo/AddUser";

// Dev
import Home from "./views/Home.vue";
import Login from "./views/auth/Login.vue";
import Register from "./views/auth/Register.vue";
import Layout from "@/views/layout/Layout";

// import NotFound from "@/views/NotFound";

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
      path: "/layout",
      name: "layout",
      component: Layout
    },
    {
      path: "/dashboard",
      name: "dashboard",
      redirect: "/dashboard/main",
      component: Layout,
      children: [{
          path: "main",
          component: () => import("@/views/dashboard/MainDash")
        },
        {
          path: "finance",
          component: () => import("@/views/dashboard/FinanceDash.vue")
        },
        {
          path: "sale",
          component: () => import("@/views/dashboard/SaleDash.vue")
        }
      ]
    },
    {
      path: "/report",
      name: "report",
      component: Layout,
      redirect: "/report/finance",
      children: [{
          path: "finance",
          name: "finance_report",
          component: () => import("@/views/report/FinanceReport")
        },
        {
          path: "sale",
          name: "sale_report",
          component: () => import("@/views/report/SaleReport")
        }
      ]
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
      path: "/user/login",
      name: "login",
      component: Login
    },
    {
      path: "/user/register",
      name: "register",
      component: Register
    },
    {
      path: "/admin",
      name: "admin",
      component: () => import("@/views/admin")
    },
    {
      path: "/admin/dialog",
      name: "dialog",
      component: () => import("@/components/admin/AddGroup")
    },

    // {
    //   path: '*',
    //   name: "404",
    //   component: NotFound
    // }
    // {
    //   path: "/demo",
    //   name: "demo",
    //   component: PageDemo,
    //   children: [{
    //     path: "menu",
    //     name: "menu",
    //     component: PMenuDemo
    //   }]
    // },
    // {
    //   path: "/addgroup",
    //   name: "addgroup",
    //   component: AddGroup
    // },
    // {
    //   path: "/addposition",
    //   name: "addposition",
    //   component: AddPosition
    // },
    // {
    //   path: "/adduser",
    //   name: "adduser",
    //   component: AddUser
    // },
    // {
    //   path: "/demo/vuex",
    //   name: "vuex",
    //   component: TestVuex
    // }, {
    //   path: "/demo/uidemo",
    //   name: "uidemo",
    //   component: UIDemo
    // }, {
    //   path: "/demo/fullscreen",
    //   name: "fullscreen",
    //   component: FullscreenDemo
    // }, {
    //   path: "/demo/mapdemo",
    //   name: "mapdemo",
    //   component: AmchartsDemo
    // },

    // {
    //   path: "/demo/testvue",
    //   name: "testvue",
    //   component: TestVue
    // }, {
    //   path: "/demo/trans",
    //   name: "trans",
    //   component: TranslateDemo
    // }, {
    //   path: "/demo/form",
    //   name: "form",
    //   component: FormDemo,
    //   meta: {
    //     requiresAuth: true
    //   }
    // }, {
    //   path: "/demo/testpath",
    //   name: "testpath",
    //   component: TestPath
    // },
    // {
    //   path: "/cdemo",
    //   name: "cdemo",
    //   component: () => import("@/views/CDemo"),
    //   children: [{
    //       path: "cd1",
    //       name: "cd1",
    //       component: () => import("@/views/CDa.vue")
    //     },
    //     {
    //       path: "cd2",
    //       name: "cd2",
    //       component: () => import("@/views/CDb.vue")
    //     }
    //   ]
    // },
    // {
    //   path: "/cd1",
    //   name: "cd1",
    //   component: () => import("@/views/CDa.vue")
    // },
    // {
    //   path: "/cd2",
    //   name: "cd2",
    //   component: () => import("@/views/CDb.vue")
    // },
    {
      path: "/demo/vueres",
      name: "vueres",
      component: () => import("@/components/demo/VueResponseDemo.vue")
    },
    {
      path: "/demo/vueprop",
      name: "vueprop",
      component: () => import("@/components/demo/VuePropDemo")
    },
    {
      path: "/demo/vueslot",
      name: "vueslot",
      component: () => import("@/components/demo/VueSlotDemo")
    },
    {
      path: "/demo/vuex",
      name: "vuex",
      component: () => import("@/components/demo/VuexDemo")
    },
    {
      path: "/demo/vuetifygrid",
      name: "vuetifygrid",
      component: () => import("@/components/demo/VuetifyGridDemo")
    }
  ]
});

export default router;