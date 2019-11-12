<template>
  <v-tooltip bottom>
    <template v-slot:activator="{ on }">
      <v-btn icon v-on="on" @click="handleFullscreen">
        <v-icon>{{ isFullscreen?'fullscreen_exit':'fullscreen'}}</v-icon>
      </v-btn>
    </template>
    <span>{{ $vuetify.lang.t("$vuetify.tooltip.fullscreen") }}</span>
  </v-tooltip>
</template>


<script>
// import Util from "@/util";
// import { mapState } from "vuex";
// export default {
//   data: () => ({
//     isFullscreen: false
//   }),
//   methods: {
//     handleFullscreen() {
//       Util.toggleFullScreen();
//       this.isFullscreen = !this.isFullscreen;
//       this.$store.dispatch("setFullscreen", this.isFullscreen);
//     },
//     /**
//      * 是否全屏并按键ESC键的方法
//      */
//     checkFullscreen() {
//       // document.fullscreenEnabled
//       var isFullscreen =
//         window.fullScreen ||
//         document.webkitisFullscreen ||
//         document.msFullscreenEnabled;
//       // to fix : false || undefined == undefined
//       if (isFullscreen === undefined) {
//         isFullscreen = false;
//       }
//       return isFullscreen;
//     }
//   },
//   computed: {},
//   mounted() {
//     window.onresize = () => {
//       // 全屏下监控是否按键了ESC
//       if (!this.checkFullscreen()) {
//         // 全屏下按键esc后要执行的动作
//         this.isFullscreen = false;
//       }
//       this.$store.dispatch("setFullscreen", this.isFullscreen);
//     };
//   }
// };
</script>