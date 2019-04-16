<template class="pl-0">
  <nav>
    <v-toolbar flat app class="indigo" dark>
      <v-toolbar-side-icon v-if="!isSidebarToggle" @click="updateSidebarToggle"></v-toolbar-side-icon>
      <v-toolbar-side-icon v-else @click="updateSidebarToggle" style="transform: rotate(90deg)"></v-toolbar-side-icon>

      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>contact_support</v-icon>
      </v-btn>
      <v-btn icon @click="updateSidebarOpen" v-if="isSidebarOpen">
        <v-icon>fullscreen</v-icon>
      </v-btn>
      <v-btn icon @click="updateSidebarOpen" v-else>
        <v-icon>fullscreen_exit</v-icon>
      </v-btn>
      <df-top-lock></df-top-lock>
      <df-skin-picker></df-skin-picker>
      <v-btn icon>
        <v-icon>account_box</v-icon>
      </v-btn>
    </v-toolbar>
  </nav>
</template>


<script>
import dfTopLock from "@/components/lock/TopLock";
import dfSkinPicker from "@/components/skin/SkinPicker";

export default {
  components: {
    dfTopLock,
    dfSkinPicker
  },
  data: () => ({
    isSidebarOpen: true,
    isSidebarToggle: false,
  }),
  methods: {
    updateSidebarOpen() {
      this.isSidebarOpen = !this.isSidebarOpen;
      this.$emit("updateSidebarOpen", this.isSidebarOpen);
    },
    updateSidebarToggle() {
      this.isSidebarToggle = !this.isSidebarToggle;
      this.$emit("updateSidebarToggle", this.isSidebarToggle);
    }
  }
};
</script>