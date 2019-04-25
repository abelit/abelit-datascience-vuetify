<template>
  <v-layout wrap>
    <v-navigation-drawer
      v-model="getDrawerStatus"
      :mini-variant="mini"
      dark
      app
      :class="sidebarColor"
      stateless
    >
      <v-img :src="image" height="100%">
        <v-toolbar flat class="transparent">
          <v-list class="pa-1 darken-3" :class="sidebarColor">
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

        <v-list class="pt-0" :class="sidebarColor" dense :color="sidebarColor">
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
              :active-class="color"
            >
              <v-list-tile-action>
                <v-icon v-text="dash.icon"></v-icon>
              </v-list-tile-action>
              <v-list-tile-title v-text="dash.title"></v-list-tile-title>
            </v-list-tile>
          </v-list-group>
        <v-list-tile v-else>
            <v-list-tile-action>
              <v-menu offset-x dark min-width="200" nudge-left="15">
                <template v-slot:activator="{ on }">
                  <div v-on="on">
                    <v-tooltip right nudge-left="10">
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
                    @click=""
                    router
                    :to="item.path"
                    avatar
                  >
                    <v-list-tile-action class="mr-1" :class="sidebarColor">
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
            >
              <v-list-tile-action>
                <v-icon v-text="dash.icon"></v-icon>
              </v-list-tile-action>
              <v-list-tile-title v-text="dash.title"></v-list-tile-title>
            </v-list-tile>
          </v-list-group>

          <v-list-tile v-else>
            <v-list-tile-action>
              <v-menu offset-x dark min-width="200">
                <template v-slot:activator="{ on }">
                  <v-btn flat dark v-on="on" right>
                    <v-icon>assessment</v-icon>
                  </v-btn>
                </template>
                <v-list class>
                  <v-list-tile
                    v-for="(item, index) in reports"
                    :key="index"
                    @click=""
                    router
                    :to="item.path"
                    avatar
                  >
                    <v-list-tile-action class="mr-1" :class="sidebarColor">
                      <v-icon>{{item.icon}}</v-icon>
                    </v-list-tile-action>
                    <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                  </v-list-tile>
                </v-list>
              </v-menu>
            </v-list-tile-action>
          </v-list-tile>
        </v-list>
      </v-img>
    </v-navigation-drawer>
  </v-layout>
</template>

<script>
import { mapActions, mapState } from "vuex";

const newLocal=false;
export default {
  name: "SideBar",
  data() {
    return {
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
        { title: "Sale", icon: "add_shopping_cart", path: "/dashboard/sale" }
      ],
      reports: [
        {
          title: "Finance",
          icon: "account_balance",
          path: "/report/finance"
        },
        { title: "Sale", icon: "add_shopping_cart", path: "/report/sale" }
      ],
      sidebarColor: "",
      iamge:
        "https://demos.creative-tim.com/vue-material-dashboard/img/sidebar-3.3a54f533.jpg",
      logo: "./static/datascience_logo.png",
      value: false
    };
  },
  methods: {
    ...mapActions(["setDrawer"])
  },
  computed: {
    ...mapState(["color", "image", "mini", "drawer", "isSmallScreen"]),
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