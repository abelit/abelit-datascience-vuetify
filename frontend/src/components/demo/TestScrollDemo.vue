<template>
  <div>
    <v-layout column justify-center align-center>
      <v-subheader>Offset Top</v-subheader>
      {{ offsetTop }}
    </v-layout>
    <v-container
      id="scroll-target"
      style="max-height: 800px"
      class="scroll-y"
    >
      <v-layout
        column 
        align-center
        justify-center
        style="height: 1000px"
      >
      </v-layout>
    </v-container>
      <!-- <v-fab-transition>
    <v-btn fab="fab" small dark="dark" fixed="fixed" bottom="bottom" right="right" color="red"  v-show="fab" @click="toTop"  v-scroll:#scroll-target="onScroll">
      <v-icon>keyboard_arrow_up</v-icon>
    </v-btn>
  </v-fab-transition> -->
  <app-fab></app-fab>
  </div>
</template>


<script>
import AppFab from "@/views/layout/components/AppFab";
  export default {
    data: () => ({
      offsetTop: 0,
      fab: false
    }),
    components: {
      AppFab
    },
    methods: {
      onScroll (e) {
        this.offsetTop = e.target.scrollTop
          if (typeof window === 'undefined') return;

      const top = this.offsetTop|| window.pageYOffset ||
        document.documentElement.offsetTop ||
        0;

      console.log("top:" + top)
      this.fab = top > 200;
      },
       toTop () {
      this.$router.push({ hash: '' });
      this.$vuetify.goTo(0);
    }
    },
  }
</script>