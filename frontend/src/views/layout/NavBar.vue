<template class="pl-0">
  <nav>
    <v-toolbar flat app  dark>
      <v-toolbar-side-icon v-if="!isSidebarToggle" @click="updateSidebarToggle"></v-toolbar-side-icon>
      <v-toolbar-side-icon v-else @click="updateSidebarToggle">
        <v-icon>view_column</v-icon>
      </v-toolbar-side-icon>

      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>contact_support</v-icon>
      </v-btn>
      <v-btn icon @click="updateSidebarOpen">
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
    isSidebarOpen: true,
    isSidebarToggle: false,
    fullscreen: false
    
  }),
  methods: {
    updateSidebarOpen() {
      this.isSidebarOpen = !this.isSidebarOpen;
      this.$emit("updateSidebarOpen", this.isSidebarOpen);
      this.toggle();
       console.log("fullscrenn o ooo");
    },
    updateSidebarToggle() {
      this.isSidebarToggle = !this.isSidebarToggle;
      this.$emit("updateSidebarToggle", this.isSidebarToggle);
    },
    toggle() {
      console.log("before full scrren oooo");
      this.$fullscreen.toggle(this.$el.querySelector(".content"), {
        wrap: false,
        callback: this.fullscreen = !this.fullscreen
      });
    }
  }
};
</script>