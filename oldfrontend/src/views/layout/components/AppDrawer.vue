<template>
  <v-navigation-drawer
    id="appDrawer"
    :mini-variant.sync="mini"
    fixed
    :dark="computeTheme"
    app
    v-model="drawer"
    width="260"
  >
    <v-toolbar
      :color="$vuetify.theme.primary==='#9e9e9e'?'primary'+' darken-3':'primary darken-1'"
      dark
      @click="$router.push('/')"
    >
      <img v-bind:src="computeLogo" height="50" alt="Data Analysis & Visualization">
      <v-toolbar-title class="ml-0 pl-2">
        <span class="hidden-sm-and-down">DATA ANALYSIS</span>
        <!-- <span>{{ generateTitle("userManagement") }}</span> -->
      </v-toolbar-title>
    </v-toolbar>
    <vue-perfect-scrollbar class="drawer-menu--scroll" :settings="scrollSettings">
      <v-list dense expand>
        <v-list-tile class="pt-3 hidden-sm-and-up">
          <v-list-tile-content>
            <v-text-field append-icon="search" label="Search"></v-text-field>
          </v-list-tile-content>
        </v-list-tile>
        <template v-for="(item, i) in menus">
          <!--group with subitems-->
          <v-list-group
            v-if="item.items"
            :key="item.name"
            :group="item.group"
            :prepend-icon="item.icon"
            no-action="no-action"
          >
            <v-list-tile slot="activator" ripple="ripple">
              <v-list-tile-content>
                <v-list-tile-title>{{ generateTitle(item.title) }}</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
            <template v-for="(subItem, i) in item.items">
              <!--sub group-->
              <v-list-group
                v-if="subItem.items"
                :key="subItem.name"
                :group="subItem.group"
                sub-group="sub-group"
              >
                <v-list-tile slot="activator" ripple="ripple">
                  <v-list-tile-content>
                    <v-list-tile-title>{{ generateTitle(subItem.title) }}</v-list-tile-title>
                  </v-list-tile-content>
                </v-list-tile>
                <v-list-tile
                  v-for="(grand, i) in subItem.children"
                  :key="i"
                  :to="genChildTarget(item, grand)"
                  :href="grand.href"
                  ripple="ripple"
                >
                  <v-list-tile-content>
                    <v-list-tile-title>{{ generateTitle(grand.title) }}</v-list-tile-title>
                  </v-list-tile-content>
                </v-list-tile>
              </v-list-group>
              <!--child item-->
              <v-list-tile
                v-else
                :key="i"
                :to="genChildTarget(item, subItem)"
                :href="subItem.href"
                :disabled="subItem.disabled"
                :target="subItem.target"
                ripple="ripple"
              >
                <v-list-tile-content>
                  <v-list-tile-title>
                    <span>{{ generateTitle(subItem.title) }}</span>
                  </v-list-tile-title>
                </v-list-tile-content>
                <v-list-tile-action v-if="subItem.action">
                  <v-icon :class="[subItem.actionClass || 'success--text']">{{ subItem.action }}</v-icon>
                </v-list-tile-action>
              </v-list-tile>
            </template>
          </v-list-group>
          <v-subheader v-else-if="item.header" :key="i">{{ generateTitle(item.header) }}</v-subheader>
          <v-divider v-else-if="item.divider" :key="i"></v-divider>
          <!--top-level link-->
          <v-list-tile
            v-else
            :to="!item.href ? { name: item.name } : null"
            :href="item.href"
            ripple="ripple"
            :disabled="item.disabled"
            :target="item.target"
            rel="noopener"
            :key="item.name"
          >
            <v-list-tile-action v-if="item.icon">
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>{{ generateTitle(item.title) }}</v-list-tile-title>
            </v-list-tile-content>
            <v-list-tile-action v-if="item.subAction">
              <v-icon class="success--text">{{ item.subAction }}</v-icon>
            </v-list-tile-action>
          </v-list-tile>
        </template>
      </v-list>
    </vue-perfect-scrollbar>
  </v-navigation-drawer>
</template>
<script>
import menu from "@/api/menu";
import VuePerfectScrollbar from "vue-perfect-scrollbar";
import { generateTitle } from "@/util/i18n";

export default {
  name: "app-drawer",
  components: {
    VuePerfectScrollbar
  },
  props: {
    expanded: {
      type: Boolean,
      default: true
    }
  },
  data: () => ({
    mini: false,
    drawer: true,
    menus: menu,
    scrollSettings: {
      maxScrollbarLength: 160
    }
  }),
  computed: {
    computeGroupActive() {
      return true;
    },
    computeLogo() {
      return "/static/images/logo/DataScience.svg";
    },

    sideToolbarColor() {
      return this.$vuetify.options.extra.sideNav;
    },
    computeTheme() {
      return this.$store.state.sidebarTheme === "dark";
    }
  },
  created() {
    window.getApp.$on("APP_DRAWER_TOGGLED", () => {
      this.drawer = !this.drawer;
    });
  },

  methods: {
    genChildTarget(item, subItem) {
      if (subItem.href) return;
      if (subItem.component) {
        return {
          name: subItem.component
        };
      }
      return { name: `${item.group}/${subItem.name}` };
    },
    generateTitle
  },
  mounted() {
    // console.log("drawer vuetify-dark: " + this.$vuetify.dark);
    // console.log(this.menus)
  }
};
</script>


<style lang="stylus">
// @import '../../node_modules/vuetify/src/stylus/settings/_elevations.styl';
#appDrawer {
  overflow: hidden;

  .drawer-menu--scroll {
    height: calc(100vh - 48px);
    overflow: auto;
  }
}
</style>
