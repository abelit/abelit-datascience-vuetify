<template>
  <div id="app">
    <radial-menu
      style="margin: auto; margin-top: 300px; background-color: white"
      :itemSize="50"
      :radius="120"
      :angle-restriction="180">
        <radial-menu-item
          v-for="(item, index) in items"
          :key="index"
          style="background-color: white"
          @click="() => handleClick(item)">
          <!-- <a href="http://localhost:8080/#/helloworld"><span>{{item}}</span></a> -->
          <!-- <span v-if="item  === 'baidu'"><router-link to="/books">{{ index }} {{ item }} </router-link> </span>
          <span v-else><router-link to="/helloworld">{{ index }} {{ item }} </router-link></span> -->
          <router-link v-bind:to="item">{{ index }}</router-link>
        </radial-menu-item>
      </radial-menu>
      <div style="color: rgba(0,0,0,0.6); margin-top: 16px;">{{ lastClicked }}</div>
  </div>
</template>

<script>
import { RadialMenu, RadialMenuItem } from 'vue-radial-menu'
// var aa = '<router-link to="/testvue"><a>testvue</a></router-link>'
export default {
  name: 'TestRadialMenu',
  components: {
    RadialMenu,
    RadialMenuItem
  },
  data () {
    return {
      // 在开发中，这里可以从数据库里面提取最近使用的模块
      // items: ['foo', 'bar', 'hello', 'world', 'more', 'items', 'baidu'],
      items: {'foo': '/test/', 'bar': '/test/', 'hello': '/test/helloworld', 'world': '/test/', 'more': '/test/testvue', 'books': '/test/books'},
      lastClicked: 'click on something!'
    }
  },
  methods: {
    handleClick (item) {
      this.lastClicked = item
    }
  }
}
</script>
