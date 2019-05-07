<template>
  <v-container fill-height fluid style="height: 89vh">
    <v-layout justify-center align-center>
      <v-flex text-xs-center shrink>
        <v-alert
          :value="true"
          type="warning"
          class="mover"
        >Sorry! No permission to access this page!</v-alert>
      </v-flex>
    </v-layout>
    <v-layout justify-center align-center class="d-forbidden-page">
      <v-flex text-xs-center shrink></v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    display: ""
  })
};
</script>

<style scoped>
.mover {
  z-index: 1;
  animation: move 4s linear infinite alternate;
}

@keyframes move {
  from {
    z-index: 1;
    transform: scale(1);
  }
  to {
    z-index: 3;
    transform: scale(1.5);
  }
}

.d-forbidden-page {
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  -webkit-filter: blur(1px);
  filter: blur(1px);
  animation: testmove 4s linear infinite alternate;
}

@keyframes testmove {
  from {
    -webkit-filter: blur(1px);
    filter: blur(1px);
    background-color: #49424231;
  }
  to {
    -webkit-filter: blur(5px);
    filter: blur(5px);
    background-color: #242121c4;
  }
}
</style>
