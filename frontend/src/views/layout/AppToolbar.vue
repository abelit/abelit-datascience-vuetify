<template>
  <v-app-bar app clipped-left>
    <v-app-bar-nav-icon @click="setDrawer" />
    <span class="title ml-3 mr-5">
      Google&nbsp;
      <span class="font-weight-light">Keep</span>
    </span>
    <!-- <v-text-field solo-inverted flat hide-details label="Search" prepend-inner-icon="search" /> -->

    <v-spacer />
      <d-lang-picker></d-lang-picker>
      <!-- <v-switch v-model="$vuetify.theme.dark" primary label="Dark" /> -->
  </v-app-bar>
</template>


<script>
//Vue兄弟组件使用bus总线设置全局事件通信
import dataBus from "@/dataBus.js";

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
      this.drawer = !this.drawer;
      dataBus.$emit("getDrawer", this.drawer);
      // console.log(this.drawer);
    }
  }
};
</script>