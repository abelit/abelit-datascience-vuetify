<template>
  <div>
    <v-navigation-drawer v-model="rightDrawer"  app fixed right temporary hide-overlay max-width="160">
      <v-app-bar  dense>
        <v-icon>settings</v-icon>
        <span class="title ml-3">{{$vuetify.lang.t("$vuetify.setting.settings")}}</span>
      </v-app-bar>
     <v-container class="pt-0">
         <v-row align="center" justify="center">
         <v-col cols="12">
             <v-color-picker ></v-color-picker>
         </v-col>
     </v-row>
     <v-divider></v-divider>
     </v-container>

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
    rightDrawer: true
  }),
  method: {}
};
</script>

<style lang="scss">
.setting-fab {
  top: 50% !important;
  right: 0;
  border-radius: 0;
}
</style>