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
    <template v-slot:activator="{ on }">
      <div v-on="on">
        <v-tooltip bottom>
          <template v-slot:activator="{ on }">
            <v-btn dark icon v-on="on">
              <v-icon>camera</v-icon>
            </v-btn>
          </template>
          <span>Theme</span>
        </v-tooltip>
      </div>
    </template>

    <v-card>
      <v-container grid-list-xl>
        <v-layout wrap>
          <v-flex xs12>
            <div class="text-xs-center body-2 text-uppercase sidebar-filter">Toolbar Filters</div>

            <v-layout justify-center>
              <v-avatar
                v-for="c in btncolors"
                :key="c"
                :class="[c === tbcolor?'color-tb-active color-tb-' + c:'color-tb-'+c]"
                size="23"
                @click="setToolbarColor(c)"
              />
            </v-layout>
            <v-divider class="mt-3"/>
          </v-flex>

 <v-flex xs12>
            <div class="text-xs-center body-2 text-uppercase sidebar-filter">Sidebar Filters</div>

            <v-layout justify-center>
              <v-avatar
                v-for="c in btncolors"
                :key="c"
                :class="[c === btncolor?'color-btn-active color-btn-' + c:'color-btn-'+c]"
                size="23"
                @click="setSidebarButtonColor(c)"
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
              @click.native="setSidebarImageNew(img)"
            />
          </v-flex>
          <v-flex v-for="c in colors" :key="c" xs3>
            <v-img
              :class="[c === color?'image-active color-' + c:'color-'+c]"
              height="120"
              @click.native="setSidebarColorNew(c)"
            />
          </v-flex>
        </v-layout>
      </v-container>
    </v-card>
  </v-menu>
</template>

<script>
// Utilities
import { mapState, mapActions } from "vuex";
export default {
  data: () => ({
    btncolors: ["deep-purple", "green", "cyan", "orange", "red"],
    images: [
      "https://demos.creative-tim.com/vue-material-dashboard/img/sidebar-1.23832d31.jpg",
      "https://demos.creative-tim.com/vue-material-dashboard/img/sidebar-2.32103624.jpg",
      "https://demos.creative-tim.com/vue-material-dashboard/img/sidebar-3.3a54f533.jpg",
      "https://demos.creative-tim.com/vue-material-dashboard/img/sidebar-4.3b7e38ed.jpg",
    ],
    colors: [
      "deep-purple",
      "orange",
      "grey-darken-3",
      "cyan"
    ]
  }),

  computed: {
    ...mapState(["color", "image","btncolor"])
  },

  methods: {
    ...mapActions(["setSidebarImage", "setSidebarButtonColor", "setSidebarColor", "setToolbarColor"]),
    setSidebarImageNew(val) {
      this.setSidebarColor("");
      this.setSidebarImage(val);
    },
    setSidebarColorNew(val) {
      this.setSidebarImage("");
      this.setSidebarColor(val);
    }
  }
};
</script>

<style lang="scss" scoped>
@import "@/assets/styles/index.scss";
.v-avatar,
.v-responsive {
  cursor: pointer;
}
</style>
