import Vue from 'vue';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';
import VueI18n from 'vue-i18n';
import '@mdi/font/css/materialdesignicons.css';

Vue.use(Vuetify);
Vue.use(VueI18n)

// 导入Vuetify lang(typescript)
import vuetifyEnLocale from 'vuetify/src/locale/en.ts'
import vuetifyZhLocale from 'vuetify/src/locale/zh-Hans.ts'

// 导入自定义翻译文件
import zhLocale from '@/i18n/vuetify/zh_cn.ts';
import enLocale from '@/i18n/vuetify/en_us.ts';

// 整合vuetify lang和Vue-i18n
const messages = {
  en: {
    ...enLocale,
    ...vuetifyEnLocale
  },
  zh: {
    ...zhLocale,
    ...vuetifyZhLocale
  },
}

// 设置语言
const i18n = new VueI18n({
  // set locale
  // options: en | zh | es
  locale: 'en',
  // set locale messages
  messages
})

export default new Vuetify({
  theme: {
    options: {
      customProperties: true,
    },
    dark: false,

    // 设置主题
    themes: {
      // light: {
      //   primary: '#ee44aa',
      //   secondary: '#424242',
      //   accent: '#82B1FF',
      //   error: '#FF5252',
      //   info: '#2196F3',
      //   success: '#4CAF50',
      //   warning: '#FFC107'
      // },
      // dark: {
      //   primary: "#2196F3",
      //   secondary: "#424242",
      //   accent: "#FF4081",
      //   error: "#FF5252",
      //   info: "#2196F3",
      //   success: "#4CAF50",
      //   warning: "#FB8C00"
      // }
    },
  },

  // 设置默认图标
  icons: {
    iconfont: 'mdi', // default - only for display purposes
  },

  // 设置语言
  lang: {
    t: (key, ...params) => i18n.t(key, params)
  },
});