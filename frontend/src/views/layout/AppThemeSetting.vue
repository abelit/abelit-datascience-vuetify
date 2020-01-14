<template>
  <div>
    <v-navigation-drawer
      v-model="rightDrawer"
      app
      fixed
      right
      temporary
      hide-overlay
      max-width="160"
    >
      <v-app-bar dense>
        <v-icon class="ml-2">settings</v-icon>
        <span class="title ml-1">{{$vuetify.lang.t("$vuetify.setting.settings")}}</span>
      </v-app-bar>
      <v-container class="pt-0">
        <v-row align="center" justify="center">
          <v-col cols="12">
            <v-color-picker></v-color-picker>
          </v-col>
        </v-row>
        <v-divider></v-divider>
        <v-row>
          <v-col cols="12" class="py-0">
            <v-switch
              v-model="dark"
              hide-details
              class="ma-2"
              :label="$vuetify.lang.t('$vuetify.theme.dark')"
              @change="updateDarkStatus"
            ></v-switch>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" class="py-0">
            <v-switch
              v-model="tag"
              hide-details
              class="ma-2"
              :label="$vuetify.lang.t('$vuetify.theme.enableTag')"
              @change="updateTagStatus"
            ></v-switch>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" class="py-0">
            <v-switch
              v-model="footer"
              hide-details
              class="ma-2"
              :label="$vuetify.lang.t('$vuetify.theme.enableFooter')"
              @change="updateFooterStatus"
            ></v-switch>
          </v-col>
        </v-row>
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
import { mapState } from "vuex";
export default {
  data: () => ({
    rightDrawer: false,
    dark: false,
    tag: true,
    footer: true
  }),
  mounted() {
    this.tag = (this.isTag == 'true' ? true : false)
    this.footer = (this.isFooter == 'true' ? true : false)
    this.dark = (this.isDark == 'true' ? true : false)
    this.$vuetify.theme.dark = (this.isDark == 'true' ? true : false);
  },
  watch: {
    dark(value) {
      this.$vuetify.theme.dark = this.dark
    }
  },
  methods: {
    updateTagStatus() {
      // 使用同步方法提交
      this.$store.dispatch("setTag", this.tag)
      console.log("isTag: " + this.isTag)
      console.log(typeof(this.isTag))
    },
    updateDarkStatus() {
      // 使用同步方法提交
      this.$store.dispatch("setDark", this.dark);
      console.log("isDark: " + this.isDark)
      console.log(typeof(this.isDark))
    },
    updateFooterStatus() {
      // 使用同步方法提交
      this.$store.dispatch("setFooter", this.footer);
    },
  },
  computed: {
    ...mapState(["isTag","isDark","isFooter"])
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