<template >
  <div class="pl-4" v-resize="onResize">
    <side-bar></side-bar>
    <nav-bar></nav-bar>
    <app-main></app-main>
    <df-footer></df-footer>
  </div>
</template>

<script>
import AppMain from "@/views/layout/components/AppMain";
import NavBar from "@/views/layout/components/NavBar";
import SideBar from "@/views/layout/components/SideBar";
import dfFooter from "@/components/footer/Footer";

import {mapActions} from "vuex";

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
    ...mapActions(["setDrawer","setMini","setSmallScreen"]),
    onResize() {
      if (window.innerWidth < this.responseSize) {
        this.isSmallScreen = true;
        // this.mini = false;
        // this.drawer = false;
      } else {
        this.isSmallScreen = false;
        // this.mini = false;
        // this.drawer = true;
      }
      
      // 把当前的mini和drawer值保存到store中
      // this.setDrawer(this.drawer);
      // this.setMini(this.mini);
      this.setSmallScreen(this.isSmallScreen);

      console.log("layout state: "+this.$store.state.isSmallScreen)

    }
  },
  mounted() {
    // this.onResize()
    console.log("layout mount");
  }
};
</script>