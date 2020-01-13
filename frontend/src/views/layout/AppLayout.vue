<template>
  <v-app id="app-content-page">
    <!-- <vue-perfect-scrollbar id="app-content-page--scroll" :settings="scrollSettings"> -->
    <app-toolbar></app-toolbar>
    <app-navigation-drawer></app-navigation-drawer>
    <v-content>
        <app-tag></app-tag>
      <router-view></router-view>
    </v-content>
    <app-theme-setting></app-theme-setting>
    <app-footer></app-footer>
    <!-- </vue-perfect-scrollbar> -->
  </v-app>
</template>

<script>
import { mapState } from "vuex";
import AppToolbar from "@/views/layout/AppToolbar";
import AppNavigationDrawer from "@/views/layout/AppNavigationDrawer";
import AppFooter from "@/views/layout/AppFooter";
import AppThemeSetting from "@/views/layout/AppThemeSetting";
import AppTag from "@/views/layout/AppTag";

import VuePerfectScrollbar from "vue-perfect-scrollbar";

export default {
  components: {
    AppToolbar,
    AppNavigationDrawer,
    AppFooter,
    VuePerfectScrollbar,
    AppThemeSetting,
    AppTag
  },
  data: () => ({
    scrollSettings: {
      // maxScrollbarLength: 160
    }
  }),
  created() {
    window.getApp = this;
  }
  // computed: {
  //   ...mapState(["isTag"])
  // }
};
</script>


<style lang="scss">
#app-content-page {
  overflow: hidden;

  #app-content-page--scroll {
    height: 100vh;
    overflow: auto;
  }
}
</style>