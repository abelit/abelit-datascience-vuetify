<template>
  <v-app>
    <v-navigation-drawer app class="deep-purple">
      <!-- -->
    </v-navigation-drawer>

    <v-toolbar app class="grey darken-3">
      <!-- -->
    </v-toolbar>

    <v-content class="indigo">
      <v-container fluid>
        <!-- If using vue-router -->
        <router-view></router-view>
      </v-container>
    </v-content>

    <v-footer app class="grey darken-3">
      <!-- -->
    </v-footer>
  </v-app>
</template>