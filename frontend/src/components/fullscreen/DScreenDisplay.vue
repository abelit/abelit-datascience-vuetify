<template>
  <v-tooltip bottom>
    <template v-slot:activator="{ on }">
      <v-btn icon v-if="!isFullScreen" v-on="on">
        <v-icon>fullscreen</v-icon>
      </v-btn>
      <v-btn icon v-else v-on="on">
        <v-icon>fullscreen_exit</v-icon>
      </v-btn>
    </template>
    <span v-if="!isFullScreen">{{ $t("tooltip.FULLSCREEN_ENTER") }}</span>
    <span v-else>{{ $t("tooltip.FULLSCREEN_EXIT") }}</span>
  </v-tooltip>
</template>


<script>
export default {
  data: () => ({
    isFullScreen: false
  })
};
</script>