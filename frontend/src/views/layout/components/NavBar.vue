<template class="pl-0">
  <nav>
    <v-toolbar flat app class="grey darken-3" dark v-if="!isSmallScreen">
      <v-toolbar-side-icon v-if="!mini" @click="miniSidebar"></v-toolbar-side-icon>
      <v-toolbar-side-icon v-else style="transform: rotate(90deg)" @click="miniSidebar"></v-toolbar-side-icon>
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
      <df-select-skin></df-select-skin>
      <v-btn icon class="indigo">
        <v-icon>account_circle</v-icon>
      </v-btn>
    </v-toolbar>
    <!-- 当屏幕为小屏时，显示这里的工具条 -->
    <v-toolbar flat app class="indigo" dark v-else>
      <v-toolbar-side-icon @click="toggleSidebar"></v-toolbar-side-icon>
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
      <df-select-skin></df-select-skin>
      <v-btn icon>
        <v-icon>account_circle</v-icon>
      </v-btn>
    </v-toolbar>
  </nav>
</template>


<script>
import dfTopLock from "@/components/lock/TopLock";
import dfSelectSkin from "@/components/skin/SelectSkin";
import { mapActions, mapState } from "vuex";

export default {
  components: {
    dfTopLock,
    dfSelectSkin
  },
  data: () => ({
    isFullSceen: false,
    mini: false,
    drawer: false
  }),
  methods: {
    ...mapActions(["setDrawer", "setMini"]),
    miniSidebar() {
      console.log("navbar 3: " + this.mini);
      this.mini = !this.mini;
      this.setMini(this.mini);
      console.log("navbar 4: " + this.mini);
    },
    toggleSidebar() {
      console.log("navbar 1: " + this.drawer);
      this.drawer = !this.drawer;
      this.setDrawer(this.drawer);
      console.log("navbar 2: " + this.drawer);
    }
  },
  computed: {
    ...mapState(["isSmallScreen"])
  },
  mounted() {
    console.log("NavBar mount ....")
  }
};
</script>