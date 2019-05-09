<template>
  <v-tooltip bottom>
    <template v-slot:activator="{ on }">
      <v-btn icon v-on="on" @click="handleFullScreen">
        <v-icon>{{ isFullScreen?'fullscreen_exit':'fullscreen'}}</v-icon>
      </v-btn>
    </template>
    <span>{{ isFullScreen?$t("tooltip.FULLSCREEN_EXIT"):$t("tooltip.FULLSCREEN_ENTER") }}</span>
  </v-tooltip>
</template>


<script>
import Utils from "@/utils";
import { mapState } from "vuex";
export default {
  data: () => ({
    isFullScreen: false
  }),
  methods: {
    handleFullScreen() {
      Utils.toggleFullScreen();
      this.isFullScreen = !this.isFullScreen;
      this.$store.dispatch("setFullScreen", this.isFullScreen);
      console.log("esc...");
    },
    /**
     * 是否全屏并按键ESC键的方法
     */
    checkFullScreen() {
      // document.fullscreenEnabled
      var isFullScreen =
        window.fullScreen ||
        document.webkitIsFullScreen ||
        document.msFullscreenEnabled;
      // console.log(document.fullscreenEnabled)
      // console.log(window.fullScreen)
      // console.log(document.webkitIsFullScreen)
      // console.log(document.msFullscreenEnabled)
      // to fix : false || undefined == undefined
      if (isFullScreen === undefined) {
        isFullScreen = false;
      }
      return isFullScreen;
    }
  },
  computed: {},
  mounted() {
    window.onresize = () => {
      // console.log("hello ....")
      // 全屏下监控是否按键了ESC
      if (!this.checkFullScreen()) {
        // 全屏下按键esc后要执行的动作
        this.isFullScreen = false;
      }
      // console.log(this.isFullScreen)
      this.$store.dispatch("setFullScreen", this.isFullScreen);
    };
  }
};
</script>