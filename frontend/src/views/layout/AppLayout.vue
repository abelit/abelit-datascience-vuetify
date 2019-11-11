<template>
  <v-app id="app-content-page">
    <vue-perfect-scrollbar id="app-content-page--scroll" :settings="scrollSettings">
      <app-toolbar></app-toolbar>
      <app-navigation-drawer></app-navigation-drawer>

      <v-content>
        <router-view></router-view>
      </v-content>

      <app-footer></app-footer>
    </vue-perfect-scrollbar>
  </v-app>
</template>

<script>
import AppToolbar from "@/views/layout/AppToolbar";
import AppNavigationDrawer from "@/views/layout/AppNavigationDrawer";
import AppFooter from "@/views/layout/AppFooter";

import VuePerfectScrollbar from "vue-perfect-scrollbar";

export default {
  components: {
    AppToolbar,
    AppNavigationDrawer,
    AppFooter,
    VuePerfectScrollbar
  },
  data: () => ({
    scrollSettings: {
      // maxScrollbarLength: 160
    }
  }),
  created() {
    window.getApp = this;
  }
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