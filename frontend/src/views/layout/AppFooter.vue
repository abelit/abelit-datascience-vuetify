<template>
  <v-footer
    app
    :inset="inset"
    max-height="48px"
    dense
    class="font-weight-medium"
    color="primary lighten-1"
    v-if="(typeof(isFooter) == 'string' && isFooter == 'true') || (typeof(isFooter) != 'string' && isFooter)?true:false"
  >
    <v-row align="center" justify="center">
      &copy; {{ new Date().getFullYear() }} &nbsp; — &nbsp;
      <strong>Data Visualization & Analyzation</strong>
    </v-row>
  </v-footer>
</template>

<script>
import { mapState } from "vuex";
export default {
  data: () => ({
    inset: true
  }),
  computed: {
    ...mapState(["isFooter"])
  }
};
</script>