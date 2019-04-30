<template>
  <v-footer dark height="auto" app insert>
    <v-card class="flex" flat tile>
      <v-card-actions class="justify-center"  :class="[tbcolor==='grey'?tbcolor+' darken-3':tbcolor]">
        &copy;2019 &nbsp; — &nbsp;
        <strong>Data Visualization & Analyzation</strong>
      </v-card-actions>
    </v-card>
  </v-footer>
</template>


<script>
import { mapState } from 'vuex';
export default {
  data: () => ({
  }),
  computed: {
    ...mapState(["tbcolor"])
  }
};
</script>