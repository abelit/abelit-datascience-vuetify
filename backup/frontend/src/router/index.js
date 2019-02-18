import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/tests/HelloWorld'
import TestVue from '@/components/tests/TestVue'
import Ping from '@/components/tests/Ping'
import Books from '@/components/tests/Books'
import IndexPage from '@/components/tests/IndexPage'
import Login from '@/components/tests/Login'
import TestRadialMenu from '@/components/tests/TestRadialMenu'
import DatePicker from '@/components/tests/TestDatePicker'
import TestChineseDate from '@/components/tests/TestChineseDate'
import TestDatePickerLocal from '@/components/tests/TestDatePickerLocal'
import TestEcharts from '@/components/tests/TestEcharts'
import HelloEcharts from '@/components/tests/HelloEcharts'
import HelloAmcharts from '@/components/tests/HelloAmcharts'
import HelloMap from '@/components/tests/HelloMap'
import TestEchartsMap from '@/components/tests/TestEchartsMap'
import TestD3 from '@/components/tests/TestD3'
import TestVuetify from '@/components/tests/TestVuetify'

Vue.use(Router)

export default new Router({
  // mode: 'history',
  routes: [
    {
      path: '/test/',
      name: 'IndexPage',
      component: IndexPage
    },
    {
      path: '/test/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/test/helloworld',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/test/testvue',
      name: 'TestVue',
      component: TestVue
    },
    {
      path: '/test/testradialmenu',
      name: 'TestRadialMenu',
      component: TestRadialMenu
    },
    {
      path: '/test/datepicker',
      name: 'DatePicker',
      component: DatePicker
    },
    {
      path: '/test/testlocaldatepicker',
      name: 'TestDatePickerLocal',
      component: TestDatePickerLocal
    },
    {
      path: '/test/testchinesedate',
      name: 'TestChineseDate',
      component: TestChineseDate
    },
    {
      path: '/test/ping',
      name: 'Ping',
      component: Ping
    },
    {
      path: '/test/books',
      name: 'Books',
      component: Books
    },
    {
      path: '/test/echarts',
      name: 'TestEcharts',
      component: TestEcharts
    },
    {
      path: '/test/helloecharts',
      name: 'HelloEcharts',
      component: HelloEcharts
    },
    {
      path: '/test/amcharts',
      name: 'HelloAmcharts',
      component: HelloAmcharts
    },
    {
      path: '/test/hellomap',
      name: 'HelloMap',
      component: HelloMap
    },
    {
      path: '/test/testechartsmap',
      name: 'TestEchartsMap',
      component: TestEchartsMap
    },
    {
      path: '/test/testd3',
      name: 'TestD3',
      component: TestD3
    },
    {
      path: '/test/testvuetify',
      name: 'TestVuetify',
      component: TestVuetify
    }
  ]
})
