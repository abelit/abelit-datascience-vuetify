<template>
    <v-footer dark height="auto" app>
    <v-card class="flex" flat tile>
      <v-card-actions class="grey darken-3 justify-center">
        &copy;2019 &nbsp; — &nbsp;
        <strong>Data Visualization & Analyzation</strong>
      </v-card-actions>
    </v-card>
  </v-footer>
</template>



<script>
export default {
  data: () => ({
    icons: [
      "fab fa-facebook",
      "fab fa-twitter",
      "fab fa-google-plus",
      "fab fa-linkedin",
      "fab fa-instagram"
    ]
  })
};
</script>