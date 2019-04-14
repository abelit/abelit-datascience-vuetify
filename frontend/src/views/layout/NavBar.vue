<template>
  <nav>
    <v-toolbar flat app class="primary" dark>
      <v-toolbar-side-icon v-if="!isSidebarOpened" @click="updateSidebarStatus"></v-toolbar-side-icon>
      <v-toolbar-side-icon v-else @click="updateSidebarStatus">
        <v-icon>view_column</v-icon>
      </v-toolbar-side-icon>

      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>contact_support</v-icon>
      </v-btn>
      <v-btn icon @click="toggle">
        <v-icon>fullscreen</v-icon>
      </v-btn>
      <top-lock></top-lock>
      <v-btn icon>
        <v-icon>camera</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>account_box</v-icon>
      </v-btn>
    </v-toolbar>
  </nav>
</template>


<script>
import TopLock from "@/components/lock/TopLock";
import fullscreen from "vue-fullscreen";

import Vue from "vue";
Vue.use(fullscreen);

export default {
  components: {
    TopLock
  },
  data: () => ({
    isSidebarOpened: false,
    fullscreen: false
  }),
  methods: {
    updateSidebarStatus() {
      this.isSidebarOpened = !this.isSidebarOpened;
      this.$emit("updateSidebarStatus", this.isSidebarOpened);
    },
    toggle() {
      this.$fullscreen.toggle(this.$el.querySelector(".example"), {
        wrap: false,
        callback: this.fullscreenChange
      });
    },
    fullscreenChange(fullscreen) {
      this.fullscreen = fullscreen;
    }
  }
};
</script>