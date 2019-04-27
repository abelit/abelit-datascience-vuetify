<template>
  <v-container grid-list-xl fluid>
    <h1>Finance Dashboard</h1>
    <table-demo></table-demo>
    <table-two-demo></table-two-demo>
    <table-one-demo></table-one-demo>
  </v-container>
</template>

<script>
import TableDemo from "@/components/tables/TableDemo";
import TableTwoDemo from "@/components/tables/TableTwoDemo";
import TableOneDemo from "@/components/tables/TableOneDemo";
export default {
  name: "Report",
  components: {
    TableDemo,
    TableTwoDemo,
    TableOneDemo
  }
};
</script>