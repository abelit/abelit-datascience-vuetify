<template>
  <div class="pl-4" v-resize="onResize">
    <side-bar :drawer="drawer" :isSmallScreen="isSmallScreen" :mini="mini"></side-bar>
    <nav-bar
      :drawer="drawer"
      :isSmallScreen="isSmallScreen"
      :mini="mini"
      @toggleSidebar="getToggleStatus($event)"
      @miniSidebar="getOpenStatus($event)"
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
    drawer: false,
    mini: false,
    responseSize: 991,
    isSmallScreen: false
  }),
  methods: {
    getToggleStatus: function(event) {
      this.drawer = event.drawer;
      this.mini = event.mini;
      console.log("layout gettogglestatus");
    },
    getOpenStatus: function(event) {
      this.drawer = event.drawer;
      this.mini = event.mini;
      console.log("layout getopenstatus");
    },
    onResize() {
      if (window.innerWidth < this.responseSize) {
        this.isSmallScreen = true;
        this.mini = false;
        this.drawer = false;
      } else {
        this.isSmallScreen = false;
        this.mini = false;
        this.drawer = true;
      }
      console.log("layout " + window.innerWidth);
      console.log("layout isSmallScreen: " + this.isSmallScreen);
    }
  },
  mounted() {
    console.log("layout mount");
    // this.onResize();
  }
};
</script>