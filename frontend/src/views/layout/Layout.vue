<template >
  <div v-resize="onResize">
    <d-side-bar></d-side-bar>
    <d-nav-bar></d-nav-bar>
    <d-app-main></d-app-main>
    <!-- <d-footer></d-footer> -->
  </div>
</template>

<script>
import DAppMain from "@/views/layout/components/DAppMain";
import DNavBar from "@/views/layout/components/DNavBar";
import DSideBar from "@/views/layout/components/DSideBar";
import DFooter from "@/components/footer/DFooter";

import { mapActions } from "vuex";

export default {
  components: {
    DNavBar,
    DAppMain,
    DSideBar,
    DFooter
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

      console.log("layout smallscreen: " + this.isSmallScreen);
      console.log(
        "layout store smallscreen: " + this.$store.state.isSmallScreen
      );

      // 当屏幕尺寸在大小两个值变化时，设置vuex中mini,drawer的值
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

      // 设置vuex中isSmallScreen的值
      this.setSmallScreen(this.isSmallScreen);

      console.log("layout store mini: " + this.$store.state.mini);
      console.log("layout store drawer: " + this.$store.state.drawer);
    },
    // 根据屏幕大小设置mini, drawer的值
    initValue() {
      if (!this.isSmallScreen) {
        this.setDrawer(true);
        this.setMini(false);
      } else {
        this.setMini(false);
        this.setDrawer(false);
      }
    }
  },
  mounted() {
    console.log("hah" + this.isSmallScreen);
    // Init mini, drawer in store
    this.initValue();
  }
};
</script>