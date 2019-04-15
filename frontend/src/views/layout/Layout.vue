<template>
  <div class="pl-4">
    <side-bar :drawer="drawer" :mini="mini"></side-bar>
    <nav-bar
      :drawer="drawer"
      @updateSidebarToggle="getSidebarToggleStatus($event)"
      @updateSidebarOpen="getSidebarOpenStatus($event)"
    ></nav-bar>
    <app-main></app-main>
  </div>
</template>

<script>
import AppMain from "@/views/layout/components/AppMain";
import NavBar from "@/views/layout/components/NavBar";
import SideBar from "@/views/layout/components/SideBar";

export default {
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
    getSidebarToggleStatus: function(getSidebarToggleStatus) {
      this.mini = getSidebarToggleStatus;
    },
    getSidebarOpenStatus: function(getSidebarOpenStatus) {
      this.drawer = getSidebarOpenStatus;
    }
  }
};
</script>