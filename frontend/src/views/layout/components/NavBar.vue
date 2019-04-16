<template class="pl-0">
  <nav>
    <v-toolbar flat app class="grey darken-3" dark v-if="device !== 'small'"  >
      <v-toolbar-side-icon v-if="!mini" @click="updateSidebarToggle"></v-toolbar-side-icon>
      <v-toolbar-side-icon v-else @click="updateSidebarToggle" style="transform: rotate(90deg)"></v-toolbar-side-icon>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>contact_support</v-icon>
      </v-btn>
      <v-btn icon v-if="!isFullSceen">
        <v-icon>fullscreen</v-icon>
      </v-btn>
      <v-btn icon v-else>
        <v-icon>fullscreen_exit</v-icon>
      </v-btn>
      <df-top-lock></df-top-lock>
      <df-skin-picker></df-skin-picker>
      <v-btn icon class="indigo">
        <v-icon>account_circle</v-icon>
      </v-btn>
    </v-toolbar>
    <v-toolbar flat app class="grey  darken-3" dark v-else>
      <v-toolbar-side-icon @click="updateSidebarOpen"></v-toolbar-side-icon>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>contact_support</v-icon>
      </v-btn>
      <v-btn icon v-if="!isFullSceen">
        <v-icon>fullscreen</v-icon>
      </v-btn>
      <v-btn icon v-else>
        <v-icon>fullscreen_exit</v-icon>
      </v-btn>
      <df-top-lock></df-top-lock>
      <df-skin-picker></df-skin-picker>
      <v-btn icon>
        <v-icon>account_circle</v-icon>
      </v-btn>
    </v-toolbar>
  </nav>
</template>


<script>
import dfTopLock from "@/components/lock/TopLock";
import dfSkinPicker from "@/components/skin/SkinPicker";

export default {
  props: ["device"],
  components: {
    dfTopLock,
    dfSkinPicker
  },
  data: () => ({
    drawer: true,
    mini: false,
    isFullSceen: false
  }),
  methods: {
    updateSidebarOpen() {
      this.drawer = !this.drawer;
      this.mini = true;
      this.$emit("updateSidebarOpenA", {
        drawer: this.drawer,
        mini: this.mini
      });
    },
    updateSidebarToggle() {
      this.mini = !this.mini;
      this.$emit("updateSidebarToggle", this.mini);
    }
  }
};
</script>