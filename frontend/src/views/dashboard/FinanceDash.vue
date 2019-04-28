<template>
  <v-container fluid style="height: 900px">
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
export default {
  name: "Report",
  components: {
    TableDemo,
    TableTwoDemo,
    TableOneDemo,
    TableThreeDemo
  }
};
</script>
