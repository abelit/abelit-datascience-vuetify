import Vue from 'vue'
import VueI18n from 'vue-i18n'

// element-ui lang
import elementEnLocale from 'element-ui/lib/locale/lang/en' 
import elementZhLocale from 'element-ui/lib/locale/lang/zh-CN'

// vue-i18n lang
import enLocale from './en'
import zhLocale from './zh'

Vue.use(VueI18n)

const messages = {
  en: {
    ...enLocale,
    ...elementEnLocale
  },
  zh: {
    ...zhLocale,
    ...elementZhLocale
  }
}

const i18n = new VueI18n({
  // set locale
  // options: en | zh | es
  locale: localStorage.getItem('lang') || 'zh',
  // set locale messages
  messages
})

export default i18n