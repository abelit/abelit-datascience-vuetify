<template>
  <v-app>
    <v-navigation-drawer app class="deep-purple">
      <!-- -->
    </v-navigation-drawer>

    <v-toolbar app class="grey darken-3">
      <!-- -->
    </v-toolbar>

    <v-content>
      <v-container fluid>
          <!-- If using vue-router -->
        <h1>Finance Dashboard</h1>
        <table-demo></table-demo>
        <table-two-demo></table-two-demo>
        <table-one-demo></table-one-demo>
        <router-view></router-view>
      </v-container>
    </v-content>

    <v-footer app class="grey darken-3">
      <!-- -->
    </v-footer>
  </v-app>
</template>



<script>
import TableDemo from "@/components/tables/TableDemo";
import TableTwoDemo from "@/components/tables/TableTwoDemo";
import TableOneDemo from "@/components/tables/TableOneDemo";
export default {
  components: {
    TableDemo,
    TableOneDemo,
    TableTwoDemo
  }
};
</script>