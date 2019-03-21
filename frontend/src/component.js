export default {
  // login: require('login/index').default, // 同步的方式
  // login: () => import('login/index') // 异步的方式
  PageDemo: () => import("@/components/demo/PageDemo.vue"),
  UIDemo: () => import("@/components/demo/UIDemo.vue"),
  AmchartsDemo: () => import("@/components/demo/AmchartsDemo.vue"),
  FullscreenDemo: () => import("@/components/demo/FullscreenDemo.vue"),
  D3Demo: () => import("@/components/demo/D3Demo.vue"),
  TestVue: () => import("@/components/demo/TestVue.vue"),
  TranslateDemo: () => import("@/components/demo/TranslateDemo"),
  FormDemo: () => import("@/components/demo/FormDemo"),
  TestPath: () => import("@/components/demo/TestPath"),
  TestVuex: () => import("@/components/demo/TestVuex")
};
