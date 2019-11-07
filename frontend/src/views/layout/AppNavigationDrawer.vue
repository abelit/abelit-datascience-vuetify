<template>
  <v-navigation-drawer v-model="drawer" app clipped class="pr-0">
    <v-app-bar dense class="hidden-lg-and-up">
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
    <v-divider dark class="my-0" />
    <v-list dense>
      <v-list-item v-for="item in items" :key="item.text" link>
        <v-list-item-action>
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
  </v-navigation-drawer>
</template>

<script>
//Vue兄弟组件使用bus总线设置全局事件通信
// import dataBus from "@/dataBus.js";
export default {
  data: () => ({
    drawer: null,
    items: [
      { icon: "trending_up", text: "Most Popular" },
      { icon: "subscriptions", text: "Subscriptions" },
      { icon: "history", text: "History" },
      { icon: "featured_play_list", text: "Playlists" },
      { icon: "watch_later", text: "Watch Later" },
      { icon: "navigate_next", text: "Navigate Next" },
      { icon: "md-star_half", text: "Start Half" },
      { icon: "mdi-compass-outline", text: "Compass Outline" },

      { icon: "trending_up", text: "Most Popular" },
      { icon: "subscriptions", text: "Subscriptions" },
      { icon: "history", text: "History" },
      { icon: "featured_play_list", text: "Playlists" },
      { icon: "watch_later", text: "Watch Later" },
      { icon: "navigate_next", text: "Navigate Next" },
      { icon: "md-star_half", text: "Start Half" },
      { icon: "mdi-compass-outline", text: "Compass Outline" },

      { icon: "trending_up", text: "Most Popular" },
      { icon: "subscriptions", text: "Subscriptions" },
      { icon: "history", text: "History" },
      { icon: "featured_play_list", text: "Playlists" },
      { icon: "watch_later", text: "Watch Later" },
      { icon: "navigate_next", text: "Navigate Next" },
      { icon: "md-star_half", text: "Start Half" },
      { icon: "mdi-compass-outline", text: "Compass Outline" }
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


<style>
#keep .v-navigation-drawer__border {
  display: none;
}
</style>