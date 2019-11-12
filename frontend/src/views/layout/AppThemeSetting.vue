<template>
  <div>
    <v-navigation-drawer v-model="rightDrawer" fixed right temporary hide-overlay>
      <v-app-bar fixed dense>
        <v-icon>settings</v-icon>
        <span class="title ml-3">{{$vuetify.lang.t("$vuetify.setting.settings")}}</span>
      </v-app-bar>
    </v-navigation-drawer>
    <v-btn
      small
      fab
      falt
      fixed
      top="top"
      right="right"
      class="setting-fab"
      color="primary"
      @click="rightDrawer = true"
    >
      <v-icon>settings</v-icon>
    </v-btn>
  </div>
</template>

<script>
export default {
  data: () => ({
    rightDrawer: false
  }),
  method: {
  }
};
</script>

<style lang="scss">
.setting-fab {
  top: 50% !important;
  right: 0;
  border-radius: 0;
}
</style>