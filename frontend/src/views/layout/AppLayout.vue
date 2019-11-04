<template>
  <v-app id="inspire">
    <app-toolbar></app-toolbar>
    <app-navigation-drawer></app-navigation-drawer>
    <v-content>
      <router-view></router-view>
    </v-content>
    <app-footer></app-footer>
  </v-app>
</template>

<script>
import AppToolbar from "@/views/layout/AppToolbar";
import AppNavigationDrawer from "@/views/layout/AppNavigationDrawer";
import AppFooter from "@/views/layout/AppFooter";

export default {
  components: {
    AppToolbar,
    AppNavigationDrawer,
    AppFooter
  }
};
</script>