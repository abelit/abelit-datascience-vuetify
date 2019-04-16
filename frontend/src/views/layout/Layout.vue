<template>
  <div class="pl-4">
    <side-bar :drawer="drawer" :mini="mini"></side-bar>
    <nav-bar
      :device="device"
      @updateSidebarToggle="getSidebarToggleStatus($event)"
      @updateSidebarOpen="getSidebarOpenStatus($event)"
      @updateSidebarOpenA="getSidebarOpenStatus($event)"
    ></nav-bar>
    <app-main></app-main>
    <df-footer></df-footer>
  </div>
</template>

<script>
import AppMain from "@/views/layout/components/AppMain";
import NavBar from "@/views/layout/components/NavBar";
import SideBar from "@/views/layout/components/SideBar";
import dfFooter from "@/components/footer/Footer";

export default {
  components: {
    NavBar,
    AppMain,
    SideBar,
    dfFooter
  },
  data: () => ({
    drawer: true,
    mini: false,
    device: "smal0l"
  }),
  methods: {
    getSidebarToggleStatus: function(getSidebarToggleStatus) {
      this.mini = getSidebarToggleStatus;
    },
    getSidebarOpenStatus: function(getSidebarOpenStatus) {
      this.drawer = getSidebarOpenStatus.drawer;
      this.mini = getSidebarOpenStatus.mini;
    },
    getMini() {
      if (this.device === "small") {
        this.mini = true;
      } else {
        this.mini = false;
      }
    }
  },
  mounted() {
    this.getMini();
  }
};
</script>