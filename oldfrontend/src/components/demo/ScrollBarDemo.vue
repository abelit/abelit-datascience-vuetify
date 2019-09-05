<template>
  <vue-perfect-scrollbar class="drawer-menu--scroll" v-once :settings="scrollSettings">
  <v-container grid-list-xs fluid>
       <v-layout row wrap>
           <v-flex lg3 sm6 xs12>
            <img src="/static/creative_process/01.jpeg" height="720" width="1280" alt>
    <img src="/static/creative_process/01.jpeg" height="720" width="1280" alt>
    <img src="/static/creative_process/01.jpeg" height="720" width="1280" alt>
    <img src="/static/creative_process/01.jpeg" height="720" width="1280" alt>
    <img src="/static/creative_process/01.jpeg" height="720" width="1280" alt>
    <img src="/static/creative_process/01.jpeg" height="720" width="1280" alt>
    <img src="/static/creative_process/01.jpeg" height="720" width="1280" alt>
           </v-flex>
       </v-layout>
  </v-container>
  </vue-perfect-scrollbar>
</template>
 
<script>
import VuePerfectScrollbar from "vue-perfect-scrollbar";

export default {
  components: {
    VuePerfectScrollbar
  },
  name: "app",
  data() {
    return {
      settings: {
        maxScrollbarLength: 160
      }
    };
  },
  methods: {
    scrollHanle(evt) {
      console.log(evt);
    }
  }
};
</script> 
<style lang="scss">
// .drawer-menu--scroll {
//   position: relative;
//   margin: auto;
//   width: 400px;
//   height: 300px;
// }
</style> 
 
<style>
.drawer-menu--scroll {
  height: calc(100vh - 48px);
  overflow: auto;
}
</style>
