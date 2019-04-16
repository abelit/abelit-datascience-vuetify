<template>
  <div class="pl-4">
    <side-bar :drawer="drawer" :mini="mini" :onResize="onResize"></side-bar>
    <nav-bar
      :isMobile="isMobile"
      @updateSidebarToggle="getSidebarToggleStatus($event)"
      @updateSidebarOpen="getSidebarOpenStatus($event)"
    ></nav-bar>
    <app-main></app-main>
    <df-footer></df-footer>
  </div>
</template>

<script>
import AppMain from "@/views/layout/components/AppMain";
import NavBar from "@/views/layout/components/NavBar";
import SideBar from "@/views/layout/components/SideBar";
import dfFooter from "@/components/footer/Footer";

export default {
  components: {
    NavBar,
    AppMain,
    SideBar,
    dfFooter
  },
  data: () => ({
    drawer: true,
    mini: false,
    isMobile: undefined
  }),
  methods: {
    getSidebarToggleStatus: function(event) {
      this.mini = event;
    },
    getSidebarOpenStatus: function(event) {
      this.drawer = event.drawer;
      this.mini = event.mini;
    },
    // getMini() {
    //   if (window.innerWidth <= 991) {
    //     this.isMobile = "small";
    //     this.mini = true;
    //   } else {
    //     this.mini = false;
    //   }
    // },
    onResize() {
      this.isMobile = window.innerWidth < 600;
    }
  },
  mounted() {
    // this.getMini();

    this.onResize();
    window.addEventListener("resize", this.onResize, { passive: true });
  },
  beforeDestroy() {
    if (typeof window !== "undefined") {
      window.removeEventListener("resize", this.onResize, { passive: true });
    }
  }
};
</script>