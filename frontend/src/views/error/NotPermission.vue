<template>
    <v-container fill-height  fluid  class="grey" style="height: 89vh;z-index: 0">
        <v-layout justify-center align-center>
          <v-flex text-xs-center shrink>
            <v-alert :value="true" type="warning" class="mover">
              Sorry! No permission to access this page!
            </v-alert>
          </v-flex>
        </v-layout>
      </v-container>
</template>

<script>
export default {
  data: () => ({
    display: ""
  })
}
</script>

<style scoped>
.mover {
  z-index: 0;
  animation: move 4s linear infinite alternate; 
}

@keyframes move {
  from { z-index: 0; transform: scale(1); }
  to { z-index: 4; transform: scale(2.5); }
}
</style>
