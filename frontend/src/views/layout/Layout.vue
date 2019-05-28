<template>
  <div id="appRoot">
    <template v-if="!$route.meta.public">
      <v-app id="inspire" class="app">
        <app-drawer class="app--drawer"></app-drawer>
        <app-toolbar class="app--toolbar"></app-toolbar>
        <v-content>
          <!-- Page Header -->
          <app-page-header v-if="$route.meta.breadcrumb" @toggleFullscreen="toggleFullscreen"></app-page-header>
          <!-- <div class="d-content-fullscreen scroll-y"> -->
            <div class="page-wrapper">
              <router-view></router-view>
            <!-- </div> -->
          </div>
          <!-- App Footer -->
          <app-footer></app-footer>
        </v-content>

        <!-- Go to top -->
        <app-fab></app-fab>
        <!-- theme setting -->
        <v-btn
          small
          fab
          dark
          falt
          fixed
          top="top"
          right="right"
          class="setting-fab"
          color="red"
          @click="openThemeSettings"
        >
          <v-icon>camera</v-icon>
        </v-btn>
        <v-navigation-drawer
          class="setting-drawer"
          temporary
          right
          v-model="rightDrawer"
          hide-overlay
          fixed
        >
          <app-theme-settings></app-theme-settings>
        </v-navigation-drawer>
      </v-app>
    </template>
    <template v-else>
      <transition>
        <keep-alive>
          <router-view :key="$route.fullpath"></router-view>
        </keep-alive>
      </transition>
    </template>
    <v-snackbar :timeout="3000" bottom right :color="snackbar.color" v-model="snackbar.show">
      {{ snackbar.text }}
      <v-btn dark flat @click.native="snackbar.show = false" icon>
        <v-icon>close</v-icon>
      </v-btn>
    </v-snackbar>
  </div>
</template>
<script>
import AppDrawer from "@/views/layout/components/AppDrawer";
import AppToolbar from "@/views/layout/components/AppToolbar";
import AppFooter from "@/views/layout/components/AppFooter";
import AppFab from "@/views/layout/components/AppFab";
import AppPageHeader from "@/views/layout/components/AppPageHeader";
import AppThemeSettings from "@/views/layout/components/AppThemeSettings";
import AppEvents from "@/event";
export default {
  components: {
    AppDrawer,
    AppToolbar,
    AppFooter,
    AppFab,
    AppPageHeader,
    AppThemeSettings
  },
  data: () => ({
    expanded: true,
    rightDrawer: false,
    snackbar: {
      show: false,
      text: "",
      color: ""
    },
    fullscreen: false
  }),

  computed: {},

  created() {
    AppEvents.forEach(item => {
      this.$on(item.name, item.callback);
    });
    window.getApp = this;
  },
  methods: {
    openThemeSettings() {
      this.$vuetify.goTo(0);
      this.rightDrawer = !this.rightDrawer;
    },
    toggleFullscreen() {
      this.$fullscreen.toggle(this.$el.querySelector(".d-content-fullscreen"), {
        wrap: false,
        callback: this.fullscreenChange
      });
    },
    fullscreenChange(fullscreen) {
      this.fullscreen = fullscreen;
    }
  }
};
</script>


<style lang="stylus" scoped>
.setting-fab {
  top: 50% !important;
  right: 0;
  border-radius: 0;
}

.page-wrapper {
  min-height: calc(100vh - 64px - 50px - 81px);
}
// .d-content-fullscreen {
//   overflow: hidden;
// }
</style>
