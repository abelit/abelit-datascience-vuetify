import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import TestVue from '@/components/TestVue'
import Ping from '@/components/Ping'
import Books from '@/components/Books'
import IndexPage from '@/components/IndexPage'
import Login from '@/components/Login'

Vue.use(Router)

export default new Router({
  // mode: 'history',
  routes: [
    {
      path: '/',
      name: 'IndexPage',
      component: IndexPage
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/helloworld',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/testvue',
      name: 'TestVue',
      component: TestVue
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping
    },
    {
      path: '/books',
      name: 'Books',
      component: Books
    }
  ]
})
