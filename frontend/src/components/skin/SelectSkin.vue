<template>
  <v-menu
    :close-on-content-click="false"
    bottom
    left
    min-width="300"
    max-width="300"
    nudge-bottom="20"
    offset-y
    transition="slide-y-transition"
  >
    <v-btn slot="activator" class="elevation-0"  dark  icon app >
      <v-icon>camera</v-icon>
    </v-btn>
    <v-card>
      <v-container grid-list-xl>
        <v-layout wrap>
          <v-flex xs12>
            <div class="text-xs-center body-2 text-uppercase sidebar-filter">Sidebar Filters</div>

            <v-layout justify-center>
              <v-avatar
                v-for="c in colors"
                :key="c"
                :class="[c === color?'color-active color-' + c:'color-'+c]"
                size="23"
                @click="setSidebarColor(c)"
              />
            </v-layout>
            <v-divider class="mt-3"/>
          </v-flex>
          <v-flex xs12>
            <div class="text-xs-center body-2 text-uppercase sidebar-filter">Images</div>
          </v-flex>
          <v-flex v-for="img in images" :key="img" xs3>
            <v-img
              :class="[image === img ? 'image-active' : '']"
              :src="img"
              height="120"
              @click.native="setSidebarImage(img)"
            />
          </v-flex>
        </v-layout>
      </v-container>
    </v-card>
  </v-menu>
</template>

<script>
// Utilities
import { mapMutations, mapState, mapActions } from "vuex";
export default {
  data: () => ({
    colors: [
      'primary',
      'info',
      'success',
      'warning',
      'danger',
      'test'
    ],
    images: [
      'https://demos.creative-tim.com/vue-material-dashboard/img/sidebar-1.23832d31.jpg',
      'https://demos.creative-tim.com/vue-material-dashboard/img/sidebar-2.32103624.jpg',
      'https://demos.creative-tim.com/vue-material-dashboard/img/sidebar-3.3a54f533.jpg',
      'https://demos.creative-tim.com/vue-material-dashboard/img/sidebar-4.3b7e38ed.jpg'
    ]
  }),


  computed: {
    ...mapState(["color","image"]),
  },

  methods: {
    ...mapActions(["setSidebarImage","setSidebarColor"])
  }
};
</script>

<style lang="scss" scoped>
@import '@/styles/index.scss';
.v-avatar,
.v-responsive {
  cursor: pointer;
}
</style>