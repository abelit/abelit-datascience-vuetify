<template >
  <div v-resize="onResize">
    <d-drawer v-if="!isFullScreen"></d-drawer>
    <d-toolbar v-if="!isFullScreen"></d-toolbar>
    <d-content></d-content>
    <d-footer v-if="!isFullScreen"></d-footer>
  </div>
</template>

<script>
import DContent from "@/views/layout/components/DContent";
import DToolbar from "@/views/layout/components/DToolbar";
import DDrawer from "@/views/layout/components/DDrawer";
import DFooter from "@/components/footer/DFooter";
import DSkinPicker from "@/components/skin/DSkinPicker";

import { mapActions, mapState } from "vuex";

export default {
  components: {
    DToolbar,
    DContent,
    DDrawer,
    DFooter,
    DSkinPicker
  },
  data: () => ({
    drawer: false,
    mini: false,
    responseSize: 991,
    isSmallScreen: false,
    isFullScreen: false
  }),
  methods: {
    ...mapActions(["setDrawer", "setMini", "setSmallScreen", "setWindowSize"]),
    onResize() {
      let windowSize = {
        windowHeight: window.innerHeight,
        windowWidth: window.innerWidth
      };
      this.setWindowSize(windowSize);
      // console.log(windowSize);
      if (window.innerWidth < this.responseSize) {
        this.isSmallScreen = true;
      } else {
        this.isSmallScreen = false;
      }

      // console.log("layout smallscreen: " + this.isSmallScreen);
      // console.log(
      //   "layout store smallscreen: " + this.$store.state.isSmallScreen
      // );

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

      // console.log("layout store mini: " + this.$store.state.mini);
      // console.log("layout store drawer: " + this.$store.state.drawer);
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
    // console.log("hah" + this.isSmallScreen);
    // Init mini, drawer in store
    this.initValue();
    // console.log(this.$store.state.isFullScreen);
  },
  computed: {
  //  ...mapState(["isFullScreen"])
  }
};
</script>




