<template>
  <v-app-bar app dense clipped-left elevation=1>
    <!-- <v-progress-linear
      :active="loading"
      :indeterminate="loading"
      absolute
      top
    ></v-progress-linear>-->
    <v-app-bar-nav-icon @click.stop="setDrawer" />
    <v-avatar size="36px" tile class="hidden-md-and-down">
      <img
        :src="require('@/assets/images/logo/data_science.svg')"
        alt="Data Analysis & Visualization"
      />
    </v-avatar>
    <span class="title ml-3 mr-5 hidden-md-and-down">
      DATA&nbsp;
      <span class="font-weight-light text--testabelit">ANALYSIS</span>
    </span>
    <!-- <v-text-field solo-inverted flat hide-details label="Search" prepend-inner-icon="search" /> -->

    <v-spacer />
    <!-- <d-question-help></d-question-help> -->
    <d-fullscreen></d-fullscreen>
    <d-top-lock></d-top-lock>
    <d-notification></d-notification>
    <d-lang-picker></d-lang-picker>
    <d-user-info></d-user-info>
    <!-- <v-switch v-model="$vuetify.theme.dark" primary label="Dark" /> -->
  </v-app-bar>
</template>


<script>
//Vue兄弟组件使用bus总线设置全局事件通信
// import dataBus from "@/dataBus.js";

//导入语言设置组件
import DLangPicker from "@/components/lang/DLangPicker";
import DQuestionHelp from "@/components/support/DQuestionHelp";
import DTopLock from "@/components/lock/DTopLock";
import DNotification from "@/components/notification/DNotification";
import DUserInfo from "@/components/user/DUserInfo";
import DFullscreen from "@/components/fullscreen/DFullscreen";

import { mapGetters } from "vuex";

export default {
  components: {
    DLangPicker,
    DQuestionHelp,
    DTopLock,
    DNotification,
    DUserInfo,
    DFullscreen
  },
  data: () => ({
    drawer: true
    // loading: true
  }),
  methods: {
    setDrawer() {
      window.getApp.$emit("APP_DRAWER_TOGGLED");
      this.drawer = !this.drawer;
    }
  },
  computed: {
    // ...mapGetters({
    //   loading: 'getAppLoading'
    // })
  },
  created() {
    console.log("created ...");
  },
  mounted() {
    console.log("mounted ...");
  }
};
</script>