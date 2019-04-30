<template>
  <v-layout wrap>
    <v-navigation-drawer
      id="appDrawer"
      v-model="getDrawerStatus"
      :mini-variant.sync="mini"
      dark
      app
      :class="[color==='grey'?color+' darken-3': color]"
      width="260"
    >
      <v-img :src="image" height="100%">
        <v-toolbar flat class="mb-0 darken-3" :class="tbcolor">
          <v-list class="pa-1 darken-3">
            <v-list-tile avatar tag="div">
              <v-list-tile-avatar>
                <img :src="logo">
              </v-list-tile-avatar>

              <v-list-tile-content>
                <v-list-tile-title class="font-weight-bold text-uppercase">Data Visualiztion</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list>
        </v-toolbar>

        <vue-perfect-scrollbar class="drawer-menu--scroll" :settings="scrollSettings">
          <v-list class="pt-0 d-list" dense expand>
            <v-divider class="my-0"></v-divider>
            <v-list-group prepend-icon="dashboard" v-if="!mini">
              <template v-slot:activator>
                <v-list-tile>
                  <v-list-tile-content>
                    <v-list-tile-title>Dashboard</v-list-tile-title>
                  </v-list-tile-content>
                </v-list-tile>
              </template>
              <v-list-tile
                class="pl-5"
                v-for="dash in dashboards"
                :key="dash.title"
                @click.stop
                router
                :to="dash.path"
                :active-class="[btncolor==='grey'?btncolor+' darken-3': btncolor]"
              >
                <v-list-tile-action>
                  <v-icon v-text="dash.icon"></v-icon>
                </v-list-tile-action>
                <v-list-tile-title v-text="dash.title"></v-list-tile-title>
              </v-list-tile>
            </v-list-group>
            <v-list-tile v-else>
              <v-list-tile-action>
                <v-menu
                  offset-x
                  dark
                  min-width="200"
                  nudge-left="20"
                  allow-overflow
                  max-height="60%"
                >
                  <template v-slot:activator="{ on }">
                    <div v-on="on">
                      <v-tooltip right nudge-left="15">
                        <template v-slot:activator="{ on }">
                          <v-btn flat dark v-on="on" right>
                            <v-icon>dashboard</v-icon>
                          </v-btn>
                        </template>
                        <span>Dashboard</span>
                      </v-tooltip>
                    </div>
                  </template>

                  <v-list class>
                    <v-list-tile
                      v-for="(item, index) in dashboards"
                      :key="index"
                      @click
                      router
                      :to="item.path"
                      avatar
                    >
                      <v-list-tile-action class="mr-1">
                        <v-icon>{{item.icon}}</v-icon>
                      </v-list-tile-action>
                      <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                    </v-list-tile>
                  </v-list>
                </v-menu>
              </v-list-tile-action>
            </v-list-tile>

            <v-list-group :value="value" prepend-icon="assessment" v-if="!mini">
              <template v-slot:activator>
                <v-list-tile>
                  <v-list-tile-content>
                    <v-list-tile-title>Report</v-list-tile-title>
                  </v-list-tile-content>
                </v-list-tile>
              </template>
              <v-list-tile
                class="pl-5"
                v-for="dash in reports"
                :key="dash.title"
                router
                :to="dash.path"
                :active-class="btncolor"
              >
                <v-list-tile-action>
                  <v-icon v-text="dash.icon"></v-icon>
                </v-list-tile-action>
                <v-list-tile-title v-text="dash.title"></v-list-tile-title>
              </v-list-tile>
            </v-list-group>

            <v-list-tile v-else>
              <v-list-tile-action>
                <v-menu offset-x dark min-width="200" allow-overflow max-height="600">
                  <template v-slot:activator="{ on }">
                    <v-btn flat dark v-on="on" right>
                      <v-icon>assessment</v-icon>
                    </v-btn>
                  </template>
                  <v-list class>
                    <v-list-tile
                      v-for="(item, index) in reports"
                      :key="index"
                      @click
                      router
                      :to="item.path"
                      avatar
                    >
                      <v-list-tile-action class="mr-1">
                        <v-icon>{{item.icon}}</v-icon>
                      </v-list-tile-action>
                      <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                    </v-list-tile>
                  </v-list>
                </v-menu>
              </v-list-tile-action>
            </v-list-tile>
          </v-list>
        </vue-perfect-scrollbar>
      </v-img>
    </v-navigation-drawer>
  </v-layout>
</template>

<script>
import { mapActions, mapState } from "vuex";
import VuePerfectScrollbar from "vue-perfect-scrollbar";

const newLocal = false;
export default {
  name: "SideBar",
  components: {
    VuePerfectScrollbar
  },
  props: {
    expanded: {
      type: Boolean,
      default: true
    }
  },
  data() {
    return {
      scrollSettings: {
        maxScrollbarLength: 160
      },
      items: [
        { title: "Dashboard", icon: "dashboard", path: "/dashboard" },
        { title: "Report", icon: "assessment", path: "/report" }
      ],
      dashboards: [
        { title: "Home", icon: "home", path: "/dashboard/main" },
        {
          title: "Finance",
          icon: "account_balance",
          path: "/dashboard/finance"
        },
        { title: "Sale", icon: "add_shopping_cart", path: "/dashboard/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/dashboard/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/dashboard/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/dashboard/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/dashboard/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/dashboard/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/dashboard/sale" }
      ],
      reports: [
        {
          title: "Finance",
          icon: "account_balance",
          path: "/report/finance"
        },
        { title: "Sale", icon: "add_shopping_cart", path: "/report/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/report/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/report/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/report/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/report/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/report/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/report/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/report/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/report/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/report/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/report/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/report/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/report/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/report/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/report/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/report/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/report/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/report/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/report/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/report/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/report/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/report/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/report/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/report/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/report/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/report/sale" },
        { title: "Sale", icon: "add_shopping_cart", path: "/report/sale" }
      ],
      logo: "./static/datascience_logo.png",
      value: false
    };
  },
  methods: {
    ...mapActions(["setDrawer"])
  },
  computed: {
    ...mapState([
      "color",
      "btncolor",
      "image",
      "mini",
      "drawer",
      "isSmallScreen",
      "tbcolor"
    ]),
    getDrawerStatus: {
      get() {
        console.log(
          "sidebar  compute store isSmallScreen: " +
            this.$store.state.isSmallScreen
        );
        console.log(
          "sidebar drawer compute store mini: " + this.$store.state.mini
        );
        console.log(
          "sidebar drawer compute store drawer: " + this.$store.state.drawer
        );
        console.log("sidebar drawer compute: " + this.drawer);
        return this.drawer;
      },
      set(val) {
        console.log("sidebar getdrawerstatus set method: " + val);
        this.setDrawer(val);
      }
    }
  },
  mounted() {
    console.log(
      "sidebar mount store issamllscreen: " + this.$store.state.isSmallScreen
    );

    console.log("sidebar mount store mini: " + this.$store.state.mini);
    console.log("sidebar mount store drawer: " + this.$store.state.drawer);
  }
};
</script>


<style lang="scss" scoped>
// @import "@/assets/styles/index.scss";
$sidebar-bg: #29292927;
.d-list,
.v-toolbar {
  background: $sidebar-bg;
}
</style>


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