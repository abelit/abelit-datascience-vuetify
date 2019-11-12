<template>
  <v-tooltip bottom>
    <template v-slot:activator="{ on }">
      <v-btn icon v-on="on" @click="handleFullscreen">
        <v-icon>{{ isFullscreen?'fullscreen_exit':'fullscreen'}}</v-icon>
      </v-btn>
    </template>
    <span>{{ isFullscreen?$vuetify.lang.t("$vuetify.tooltip.exitFullscreen"):$vuetify.lang.t("$vuetify.tooltip.fullscreen") }}</span>
  </v-tooltip>
</template>


<script>
import util from "@/util";

export default {
  data: () => ({
    isFullscreen: false
  }),
  methods: {
    handleFullscreen() {
      util.toggleFullscreen();
      this.isFullscreen = !this.isFullscreen;
      this.$store.dispatch("setFullscreen", this.isFullscreen);
    },
    /**
     * 是否全屏并按键ESC键的方法
     */
      checkFullscreen() {
      // document.fullscreenEnabled
      var isFullscreen =
        window.fullScreen ||
        document.webkitIsFullScreen ||
        document.msFullscreenEnabled;
      // to fix : false || undefined == undefined
      if (isFullscreen === undefined) {
        isFullscreen = false;
      }
      return isFullscreen;
    }
  },
  mounted() {
    window.onresize = () => {
      // 全屏下监控是否按键了ESC
      if (!this.checkFullscreen()) {
        // 全屏下按键esc后要执行的动作
        this.isFullscreen = false;
      }
      // Vuex异步调用，实际执行的是actions中的方法
      this.$store.dispatch("setFullscreen", this.isFullscreen);
    };
  }
};
</script>