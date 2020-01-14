<template>
  <v-navigation-drawer v-model="drawer" app clipped class="pr-0" id="app-drawer">
    <!-- <v-toolbar app absolute dense v-if="$vuetify.breakpoint.mdAndDown" width="256">
      <v-avatar size="36px" tile>
        <img
          :src="require('@/assets/images/logo/data_science.svg')"
          alt="Data Analysis & Visualization"
        />
      </v-avatar>
      <span class="title ml-3">
        DATA&nbsp;
        <span class="font-weight-light">ANALYSIS</span>
      </span>
    </v-toolbar>-->
    <v-app-bar fixed dense v-if="$vuetify.breakpoint.mdAndDown">
      <v-avatar size="36px" tile>
        <img
          :src="require('@/assets/images/logo/data_science.svg')"
          alt="Data Analysis & Visualization"
        />
      </v-avatar>
      <span class="title ml-3">
        DATA&nbsp;
        <span class="font-weight-light">ANALYSIS</span>
      </span>
    </v-app-bar>
    <!-- <v-divider dark class="my-0" /> -->
    <vue-perfect-scrollbar class="drawer-menu--scroll" :settings="scrollSettings">
      <v-list  dense class="pt-0" v-if="$vuetify.breakpoint.mdAndDown">
        <v-list-item></v-list-item>
      </v-list>
      <v-list dense class="pt-0">
        <v-list-item v-for="item in items" :key="item.text" link :to="item.link">
          <v-list-item-action class="mr-5">
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>{{ item.text }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-subheader class="mt-4 grey--text text--darken-1">SUBSCRIPTIONS</v-subheader>

        <v-list-item class="mt-4" link>
          <v-list-item-action>
            <v-icon color="grey darken-1">mdi-plus-circle-outline</v-icon>
          </v-list-item-action>
          <v-list-item-title class="grey--text text--darken-1">Browse Channels</v-list-item-title>
        </v-list-item>
        <v-list-item link>
          <v-list-item-action>
            <v-icon color="grey darken-1">mdi-settings</v-icon>
          </v-list-item-action>
          <v-list-item-title class="grey--text text--darken-1">Manage Subscriptions</v-list-item-title>
        </v-list-item>
      </v-list>
    </vue-perfect-scrollbar>
  </v-navigation-drawer>
</template>

<script>
//Vue兄弟组件使用bus总线设置全局事件通信
// import dataBus from "@/dataBus.js";

import VuePerfectScrollbar from "vue-perfect-scrollbar";

export default {
  components: {
    VuePerfectScrollbar
  },
  data: () => ({
    drawer: null,
    scrollSettings: {
      // maxScrollbarLength: 160
    },
    items: [
      { icon: "mdi-file-document-box-plus-outline", text: "FromGenerate", link: "/form"},
      { icon: "mdi-dev-to", text: "Development Path", link: "/admin/path"},
      { icon: "mdi-table", text: "Table Demo", link:"/" },
      { icon: "subscriptions", text: "Subscriptions", link:"/1" },
      { icon: "history", text: "History", link:"/2" },
      { icon: "featured_play_list", text: "Playlists", link:"/3" },
      { icon: "watch_later", text: "Watch Later", link:"/4" },
      { icon: "navigate_next", text: "Navigate Next", link:"/5" },
      { icon: "mdi-compass-outline", text: "Compass Outline", link:"/6" }
    ]
  }),
  created() {
    window.getApp.$on("APP_DRAWER_TOGGLED", () => {
      this.drawer = !this.drawer;
    });
    //中屏及以下大小隐藏Navigation Drawer
    if (this.$vuetify.breakpoint.mdAndDown) {
      this.drawer = false;
    }
    // console.log(this.$vuetify.breakpoint.smAndDown);
  }
};
</script>


<style lang="scss">
#keep .v-navigation-drawer__border {
  display: none;
}
#app-drawer {
  overflow: hidden;

  .drawer-menu--scroll {
    height: calc(100vh - 48px);
    overflow: auto;
  }
}
</style>