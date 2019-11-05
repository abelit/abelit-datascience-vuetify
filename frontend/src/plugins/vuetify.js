import Vue from 'vue';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';

Vue.use(Vuetify);

// 导入Vuetify自带翻译文件(javascript)
// import zh_cn from 'vuetify/es5/locale/zh-Hans';
// import en_us from 'vuetify/es5/locale/en';
// import ja from 'vuetify/es5/locale/ja';

// 导入自定义翻译文件
import zh_cn from '@/i18n/vuetify/zh_cn.ts';
import en_us from '@/i18n/vuetify/en_us.ts';


export default new Vuetify({
  theme: {
    options: {
      customProperties: true,
    },
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
    },
  },
  icons: {
    iconfont: 'mdi',
  },
  lang: {
    locales: {
      zh_cn,
      en_us
    },
    current: 'zh_cn'
  },
});