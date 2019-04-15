<template>
  <v-layout wrap>
    <v-navigation-drawer v-model="drawer" :mini-variant="mini" dark app :class="color_sidebar">
      <v-list class="pa-1 darken-3" :class="color_sidebar">
        <v-list-tile avatar tag="div">
          <v-list-tile-avatar>
            <img src="../../../../static/logo.png">
          </v-list-tile-avatar>

          <v-list-tile-content>
            <v-list-tile-title class="font-weight-bold text-uppercase">Data Visualiztion</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>

      <v-list class="pt-0" :class="color_sidebar" dense>
        <v-divider class="my-0"></v-divider>
        <v-list-group value="true" prepend-icon="dashboard" v-if="!mini">
          <template v-slot:activator>
            <v-list-tile @click.stop>
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
                <v-btn flat dark v-on="on">
                  <v-icon>dashboard</v-icon>
                </v-btn>
              </template>
              <v-list class>
                <v-list-tile
                  v-for="(item, index) in dashboards"
                  :key="index"
                  @click.stop
                  router
                  :to="item.path"
                  avatar
                >
                  <v-list-tile-action-avatar class="mr-1" :class="color_sidebar">
                    <v-icon>{{item.icon}}</v-icon>
                  </v-list-tile-action-avatar>
                  <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                </v-list-tile>
              </v-list>
            </v-menu>
          </v-list-tile-action>
        </v-list-tile>

        <v-list-group value="true" prepend-icon="assessment" v-if="!mini">
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
                <v-btn flat dark v-on="on">
                  <v-icon>assessment</v-icon>
                </v-btn>
              </template>
              <v-list class>
                <v-list-tile
                  v-for="(item, index) in reports"
                  :key="index"
                  @click.stop
                  router
                  :to="item.path"
                  avatar
                >
                  <v-list-tile-action-avatar class="mr-1" :class="color_sidebar">
                    <v-icon>{{item.icon}}</v-icon>
                  </v-list-tile-action-avatar>
                  <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                </v-list-tile>
              </v-list>
            </v-menu>
          </v-list-tile-action>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
  </v-layout>
</template>


<script>
export default {
  name: "SideBar",
  props: ["mini", "drawer"],
  data() {
    return {
      // drawer: true,
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
      // mini: false,
      // right: null
      color_sidebar: ""
    };
  },
  mounted() {
    this.color_sidebar = JSON.parse(this.$store.getters.skin).class;
  }
  // watch: {
  //   color_sidebar: () => {
  //     this.color_sidebar = JSON.parse(this.$store.getters.skin).class;
  //   }
  // }
};
</script>