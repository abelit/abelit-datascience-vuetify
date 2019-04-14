<template>
  <div class="example">
    <side-bar :drawer="drawer" :mini="mini"></side-bar>
    <nav-bar :drawer="drawer" @updateSidebarStatus="getSidebarStatus($event)"></nav-bar>
    <app-main></app-main>
  </div>
</template>

<script>
import AppMain from "@/views/layout/AppMain";
import NavBar from "@/views/layout/NavBar";
import SideBar from "@/views/layout/SideBar";

export default {
  name: "Layout",
  components: {
    NavBar,
    AppMain,
    SideBar
  },
  data: () => ({
    drawer: true,
    mini: false
  }),
  methods: {
    getSidebarStatus: function(getSidebarStatus) {
      this.mini = getSidebarStatus;
    }
  }
};
</script>