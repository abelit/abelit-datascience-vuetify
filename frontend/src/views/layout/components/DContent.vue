<template>
  <transition name="fade" mode="out-in">
    <keep-alive :include="cachedViews">
      <v-content>
        <!-- <div  class="page-wrapper"> -->
        <router-view></router-view>
        <!-- </div> -->
        <!-- <d-footer></d-footer> -->
      </v-content>
    </keep-alive>
  </transition> 
</template>

<script>
import DFooter from "@/components/footer/DFooter";
export default {
  components: {
    DFooter
  },
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
