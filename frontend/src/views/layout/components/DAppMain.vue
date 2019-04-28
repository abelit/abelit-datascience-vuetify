<template>
  <!-- <section class="app-main"> -->
  <transition name="fade" mode="out-in">
  <keep-alive :include="cachedViews">
  <v-content> 
    
      <router-view :key="key"></router-view>
    
  </v-content>
  </keep-alive>
  </transition>
  <!-- </section> -->
</template>

<script>
export default {
  name: "AppMain",
  data() {
    return {
      cachedViews: "",
      key: ""
    };
  }
};
</script>


<style>
/* .container {
  overflow: auto;
  height: 100%;
} */
</style>
