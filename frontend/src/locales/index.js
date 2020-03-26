import Vue from 'vue'
import VueI18n from 'vue-i18n'

// 导入Vuetify lang(typescript)
import vuetifyEnLocale from 'vuetify/src/locale/en.ts'
import vuetifyZhLocale from 'vuetify/src/locale/zh-Hans.ts'

// vue-i18n lang
import enLocale from './en_us'
import zhLocale from './zh_cn'

Vue.use(VueI18n)

const messages = {
  en_us: {
    ...enLocale,
    ...vuetifyEnLocale
  },
  zh_cn: {
    ...zhLocale,
    ...vuetifyZhLocale
  }
}

const i18n = new VueI18n({
  // set locale
  // options: en | zh | es
  locale: localStorage.getItem('lang') || 'en_us',
  // set locale messages
  messages
})

export default i18n