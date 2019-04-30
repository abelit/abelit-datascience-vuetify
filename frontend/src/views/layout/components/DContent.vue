<template>
  <!-- <section class="app-main"> -->
  <transition name="fade" mode="out-in">
    <keep-alive :include="cachedViews">
      <v-content>
        <div  class="page-wrapper">
        <router-view :key="key"></router-view>
        </div>
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


<style lang="stylus">
  .setting-fab 
    top:50%!important; 
    right:0;
    border-radius:0  
  .page-wrapper
    min-height:calc(100vh - 64px - 50px - 81px );  

</style>
