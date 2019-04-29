<template class="pl-0">
  <nav>
    <v-toolbar flat app :class="[tbcolor==='grey'?tbcolor+' darken-3':tbcolor]" dark v-if="!isSmallScreen" absolute fixed>
      <!-- 根据mini值显示icon的样式，正常与旋转90° -->
      <v-toolbar-side-icon v-if="!mini" @click="miniSidebar"></v-toolbar-side-icon>
      <v-toolbar-side-icon v-else style="transform: rotate(90deg)" @click="miniSidebar"></v-toolbar-side-icon>
      <v-spacer></v-spacer>
      <d-help-question></d-help-question>
      <d-lang-picker></d-lang-picker>
      <d-screen-display></d-screen-display>
      <d-app-lock></d-app-lock>

      <d-skin-picker></d-skin-picker>

      <v-tooltip bottom>
        <template v-slot:activator="{ on }">
          <v-btn icon v-on="on">
            <v-icon>account_circle</v-icon>
          </v-btn>
        </template>
        <span>{{$t("tooltip.USER_PROFILE")}}</span>
      </v-tooltip>
    </v-toolbar>
    <!-- 当屏幕为小屏时，显示这里的工具条 -->
    <v-toolbar flat app class="indigo" dark v-else :class="tbcolor">
      <v-toolbar-side-icon @click="toggleSidebar"></v-toolbar-side-icon>
      <v-spacer></v-spacer>
      <d-help-question></d-help-question>
      <d-lang-picker></d-lang-picker>
      <d-screen-display></d-screen-display>
      <d-app-lock></d-app-lock>

      <d-skin-picker></d-skin-picker>
      <v-tooltip bottom>
        <template v-slot:activator="{ on }">
          <v-btn icon v-on="on">
            <v-icon>account_circle</v-icon>
          </v-btn>
        </template>
        <span>{{$t("tooltip.USER_PROFILE")}}</span>
      </v-tooltip>
    </v-toolbar>
  </nav>
</template>


<script>
import DAppLock from "@/components/lock/DAppLock";
import DSkinPicker from "@/components/skin/DSkinPicker";
import DScreenDisplay from "@/components/fullscreen/DScreenDisplay";
import DLangPicker from "@/components/lang/DLangPicker";
import DHelpQuestion from "@/components/support/DHelpQuestion";

import { mapActions, mapState } from "vuex";

export default {
  components: {
    DAppLock,
    DSkinPicker,
    DScreenDisplay,
    DLangPicker,
    DHelpQuestion
  },
  data: () => ({
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
    ...mapState(["isSmallScreen", "tbcolor"])
  },
  mounted() {
    console.log("NavBar mount ....");
  }
};
</script>