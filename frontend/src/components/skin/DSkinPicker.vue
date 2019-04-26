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
import { mapState, mapActions } from "vuex";
export default {
  data: () => ({
    colors: ["primary", "info", "success", "warning", "danger"],
    images: [
      "https://demos.creative-tim.com/vue-material-dashboard/img/sidebar-1.23832d31.jpg",
      "https://demos.creative-tim.com/vue-material-dashboard/img/sidebar-2.32103624.jpg",
      "https://demos.creative-tim.com/vue-material-dashboard/img/sidebar-3.3a54f533.jpg",
      "https://demos.creative-tim.com/vue-material-dashboard/img/sidebar-4.3b7e38ed.jpg"
    ]
  }),

  computed: {
    ...mapState(["color", "image"])
  },

  methods: {
    ...mapActions(["setSidebarImage", "setSidebarColor"])
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


<style lang="scss" scoped>
// .v-avatar,
// .v-responsive {
//   cursor: pointer
// }

// $red-500: #f44336 !default;
// $red: $red-500 !default;

// $purple-500: #9c27b0 !default;
// $purple: $purple-500 !default;

// $cyan-500: #00bcd4 !default;
// $cyan: $cyan-500 !default;

// $green-500: #4caf50 !default;
// $green: $green-500 !default;

// $orange-500: #ff9800 !default;
// $orange: $orange-500 !default;
// $black: #000000;
// $white: #ffffff;

// //  Brand Colors
// $brand-primary:                    $purple !default;
// $brand-success:                    $green !default;
// $brand-danger:                     $red !default;
// $brand-warning:                    $orange !default;
// $brand-info:                       $cyan !default;

// $font-size-small:                   12px !default;
// $border-radius-dropdown:            10px !default;
// $font-weight-bolder:                500 !default;
// $black-color:                       #495057 !default;
// $padding-small:                     10px !default;
// $box-shadow-general:                0 2px 5px 0 rgba($black, .26);

// @mixin fixed-plugin-colors($color-name, $color) {
//   &.color-#{$color-name}{
//     background-color: $color;
//   }
// }

// .v-menu__content {
//   border-radius: $border-radius-dropdown;
//   box-shadow: $box-shadow-general;

//   .sidebar-filter {
//     height: 30px;
//     line-height: 25px;
//     font-size: $font-size-small !important;
//     font-weight: $font-weight-bolder + 100;
//     color: $black-color;
//   }

//   .v-responsive {
//     max-height: 100px;
//     border-radius: $border-radius-dropdown;
//     max-width: 50px;
//     margin: 0 auto;
//   }

//   .container.grid-list-xl .layout .flex {
//     padding: $padding-small - 5;
//   }

//   .v-avatar,
//   .v-responsive {
//     border: 3px solid $white;
//     transition: all .34s;

//     &:not(:last-child) {
//       margin-right: 5px;
//     }

//     &.image-active,
//     &.color-active {
//       border-color: $brand-info;
//     }
//   }

//   .v-avatar {
//     @include fixed-plugin-colors('primary', $brand-primary);
//     @include fixed-plugin-colors('info', $brand-info);
//     @include fixed-plugin-colors('danger', $brand-danger);
//     @include fixed-plugin-colors('warning', $brand-warning);
//     @include fixed-plugin-colors('success', $brand-success);
//   }
// }
</style>
