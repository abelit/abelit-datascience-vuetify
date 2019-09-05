<template>
  <v-footer height="auto" class="white app--footer">
    <v-card class="flex" flat tile>
      <v-card-actions class="justify-center primary--text">
        &copy; {{ new Date().getFullYear() }} &nbsp; — &nbsp;
        <strong>Data Visualization & Analyzation</strong>
      </v-card-actions>
    </v-card>
  </v-footer>
</template>


<script>
// import { mapState } from 'vuex';
export default {
  data: () => ({})
  // computed: {
  //   ...mapState(["toolbarColor"])
  // }
};
</script>


<style>
/* .d-footer {
  margin-left: 260px;
} */
</style>
