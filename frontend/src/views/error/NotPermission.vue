<template>
  <v-container fill-height fluid text-xs-center align-content-center style="height: 89vh">
    <v-layout justify-center align-center row wrap>
      <v-flex shrink xs-12>
        <v-alert :value="true" type="warning" class="mover">{{ $t("content.UNAUTHORIZED") }}</v-alert>
      </v-flex>
    </v-layout>
    <v-layout justify-center align-center class="d-permission-page">
      <v-flex shrink></v-flex>
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
  max-width: 80vw;
}

@keyframes move {
  from {
    z-index: 1;
    transform: scale(1);
  }
  to {
    z-index: 3;
    transform: scale(1.15);
  }
}

.d-permission-page {
  position: fixed;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  -webkit-filter: blur(1px);
  filter: blur(1px);
  animation: bgcolor-move 4s linear infinite alternate;
}

@keyframes bgcolor-move {
  from {
    -webkit-filter: blur(1px);
    filter: blur(1px);
    background-color: #4942427c;
  }
  to {
    -webkit-filter: blur(10px);
    filter: blur(10px);
    background-color: #242121c4;
  }
}
</style>
