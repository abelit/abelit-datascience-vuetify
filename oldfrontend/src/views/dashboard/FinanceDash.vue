<template>
  <v-container grid-list-xl fluid>
    <!-- <not-permission></not-permission> -->
    <v-layout>
     <h1>Finance Dashboard</h1>
        <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon class="text--secondary">refresh</v-icon>
      </v-btn>
    </v-layout>
    <v-layout row wrap>
      <v-flex>
        <table-demo></table-demo>
        <table-two-demo></table-two-demo>
        <table-one-demo></table-one-demo>
        <table-three-demo></table-three-demo>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import TableDemo from "@/components/tables/TableDemo";
import TableTwoDemo from "@/components/tables/TableTwoDemo";
import TableOneDemo from "@/components/tables/TableOneDemo";
import TableThreeDemo from "@/components/tables/TableThreeDemo";
import NotPermission from "@/views/error/NotPermission";
import { mapState } from "vuex";

export default {
  name: "Report",
  data: () => ({}),
  components: {
    TableDemo,
    TableTwoDemo,
    TableOneDemo,
    TableThreeDemo,
    NotPermission
  },
  computed: {
    ...mapState(["windowSize"])
  },
  mounted() {}
};
</script>


<style lang="stylus">
.setting-fab {
  top: 50% !important;
  right: 0;
  border-radius: 0;
}

.page-wrapper {
  min-height: calc(100vh - 64px - 50px - 81px);
}
</style>
