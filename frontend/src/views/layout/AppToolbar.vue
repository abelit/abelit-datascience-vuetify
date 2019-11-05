<template>
  <v-app-bar app dense clipped-left>
    <v-app-bar-nav-icon @click.stop="setDrawer" />
    <v-avatar size="36px" tile class="hidden-sm-and-down">
    <img :src="require('@/assets/images/logo/data_science.svg')" alt="Data Analysis & Visualization" />
    </v-avatar>
    <span class="title ml-3 mr-5 hidden-sm-and-down">
      DATA&nbsp;
      <span class="font-weight-light">ANALYSIS</span>
    </span>
    <!-- <v-text-field solo-inverted flat hide-details label="Search" prepend-inner-icon="search" /> -->

    <v-spacer />
      <d-lang-picker></d-lang-picker>
      <!-- <v-switch v-model="$vuetify.theme.dark" primary label="Dark" /> -->
  </v-app-bar>
</template>


<script>
//Vue兄弟组件使用bus总线设置全局事件通信
// import dataBus from "@/dataBus.js";

//导入语言设置组件
import DLangPicker from "@/components/lang/DLangPicker";

export default {
  components: {
    DLangPicker
  },
  data: () => ({
    drawer: true
  }),
  methods: {
    setDrawer() {
      window.getApp.$emit('APP_DRAWER_TOGGLED');
      this.drawer = !this.drawer;
    }
  }
};
</script>