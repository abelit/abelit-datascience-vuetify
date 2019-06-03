<template>
  <v-app>
    <v-navigation-drawer app class="deep-purple">
      <!-- -->
    </v-navigation-drawer>

    <v-toolbar app class="grey darken-3">
      <!-- -->
    </v-toolbar>

    <v-content>
    <v-container fill-height class="red" fluid>
        <v-layout justify-center align-center>
          <v-flex shrink>
            <p>dfadfa</p>
          </v-flex>
        </v-layout>
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