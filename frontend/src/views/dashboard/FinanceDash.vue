<template>
  <v-container fluid :style="'height: '+ (windowSize.windowHeight-60) +'px'" class="scroll-y">
    <v-flex>
      <h1>Finance Dashboard</h1>
      <table-demo></table-demo>
      <table-two-demo></table-two-demo>
      <table-one-demo></table-one-demo>
      <table-three-demo></table-three-demo>
    </v-flex>
  </v-container>
</template>

<script>
import TableDemo from "@/components/tables/TableDemo";
import TableTwoDemo from "@/components/tables/TableTwoDemo";
import TableOneDemo from "@/components/tables/TableOneDemo";
import TableThreeDemo from "@/components/tables/TableThreeDemo";
import {mapState} from "vuex";

export default {
  name: "Report",
  data: () => ({
  }),
  components: {
    TableDemo,
    TableTwoDemo,
    TableOneDemo,
    TableThreeDemo
  },
  computed: {
    ...mapState(["windowSize"]),
  },
  mounted() {
    
  }
};
</script>
