<template class="pl-0" v-resize="onResize">
  <nav>
    <v-toolbar flat app class="grey darken-3" dark v-if="!isSmallScreen">
      <v-toolbar-side-icon v-if="!mini" @click="miniSidebar"></v-toolbar-side-icon>
      <v-toolbar-side-icon v-else style="transform: rotate(90deg)"  @click="miniSidebar"></v-toolbar-side-icon>
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
      <df-select-skin></df-select-skin>
      <v-btn icon class="indigo">
        <v-icon>account_circle</v-icon>
      </v-btn>
    </v-toolbar>
    <v-toolbar flat app class="indigo" dark v-else>
      <v-toolbar-side-icon @click.stop="toggleSidebar"></v-toolbar-side-icon>
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
      <df-select-skin></df-select-skin>
      <v-btn icon>
        <v-icon>account_circle</v-icon>
      </v-btn>
    </v-toolbar>
  </nav>
</template>


<script>
import dfTopLock from "@/components/lock/TopLock";
import dfSkinPicker from "@/components/skin/SkinPicker";
import dfSelectSkin from "@/components/skin/SelectSkin";

export default {
  components: {
    dfTopLock,
    dfSkinPicker,
    dfSelectSkin
  },
  props: ["isSmallScreen"],
  data: () => ({
    isFullSceen: false,
    mini: true,
    drawer: true,
    isSmallScreen: false
  }),
  methods: {
    toggleSidebar() {
      this.drawer = !this.drawer;
      this.mini = false;
      console.log("nav togglesidebar")
      this.$emit("toggleSidebar", {drawer: this.drawer, mini: this.mini});
      
    },
    miniSidebar() {
      this.mini = !this.mini;
      this.drawer = true;
      console.log("nav minisidevbar")

      this.$emit("miniSidebar",  {drawer: this.drawer, mini: this.mini});
    },
    initSidebar() {
      if (this.isSmallScreen) {
        this.mini = false;
        this.drawer = false;
      } else {
        this.mini = false;
        this.drawer = true;
      }
    }
  
  },
  mounted() {
    this.initSidebar();
    console.log("Nava bar oooo ");
  }
};
</script>