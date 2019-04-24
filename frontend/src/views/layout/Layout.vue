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

import { mapActions } from "vuex";

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
    ...mapActions(["setDrawer", "setMini", "setSmallScreen"]),
    onResize() {
      if (window.innerWidth < this.responseSize) {
        this.isSmallScreen = true;
      } else {
        this.isSmallScreen = false;
      }

      console.log("layout smallscreen: "+this.isSmallScreen)
      console.log("layout store smallscreen: "+this.$store.state.isSmallScreen)

      if (
        this.isSmallScreen != this.$store.state.isSmallScreen &&
        this.isSmallScreen
      ) {
        this.setMini(false);
        this.setDrawer(false);
      }

      if (
        this.isSmallScreen != this.$store.state.isSmallScreen &&
        !this.isSmallScreen 
      ) {
        this.setMini(false);
        this.setDrawer(true);
      }

      this.setSmallScreen(this.isSmallScreen);

      console.log("layout store mini: "+this.$store.state.mini)
      console.log("layout store drawer: "+this.$store.state.drawer)
    },
    initValue() {
      if (!this.isSmallScreen) {
      this.setDrawer(true)
      this.setMini(false)
    } else {
      this.setMini(false)
      this.setDrawer(false)
    }
    }
  },
  mounted() {
    console.log("hah"+this.isSmallScreen)
    // Init mini, drawer in store
    this.initValue();
  }
};
</script>