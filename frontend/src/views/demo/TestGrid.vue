<template>
  <!-- v2.0 -->
  <v-container>
    <v-row>
      <v-col xs12 md6>
        <v-row class="ma-n3">
          <v-col xs12 md6>
            <v-sheet class="pa-3">v-col</v-sheet>
          </v-col>

          <v-col xs12 md6>
            <v-sheet class="pa-3">v-col</v-sheet>
          </v-col>
        </v-row>
      </v-col>

      <v-col xs12 md6>
        <v-sheet class="pa-3">v-col</v-sheet>
      </v-col>

      <v-col cols="12">
        <v-row class="ma-n3">
          <v-col cols="12" md="4">
            <v-row class="ma-n3">
              <v-col cols="12" md="6">
                <v-sheet class="pa-3">v-col-a</v-sheet>
              </v-col>

              <v-col cols="12" md="6">
                <v-sheet class="pa-3">v-col-b</v-sheet>
              </v-col>
            </v-row>
          </v-col>

          <v-col cols="12" md="8">
            <v-row class="ma-n3">
              <v-col cols="12" md="6">
                <v-sheet class="pa-3">v-col-c</v-sheet>
              </v-col>

              <v-col cols="12" md="6">
                <v-sheet class="pa-3">v-col-d</v-sheet>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
    <v-row>
      <v-col xs12 md6>
        <v-sheet class="pa-3">v-col-new1</v-sheet>
      </v-col>
      <v-col xs12 md6>
        <v-row class="ma-n3">
          <v-col xs12 md6>
            <v-sheet class="pa-3">v-col-new2</v-sheet>
          </v-col>
           <v-col xs12 md6>
            <v-sheet class="pa-3">v-col-new3</v-sheet>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    //
  })
};
</script>


<style>
.v-sheet {
  background-color: aqua !important;
}
</style>