<template>
  <v-layout wrap>
    <v-navigation-drawer v-model="drawer" :mini-variant="mini" dark app>
      <v-list class="pa-1">
        <!-- <v-list-tile v-if="mini" @click.stop="mini = !mini">
          <v-list-tile-action>
            <v-icon>chevron_right</v-icon>
          </v-list-tile-action>
        </v-list-tile>-->

        <v-list-tile avatar tag="div">
          <v-list-tile-avatar>
            <img src="../../../static/logo.png">
          </v-list-tile-avatar>

          <v-list-tile-content>
            <v-list-tile-title>数据视野</v-list-tile-title>
          </v-list-tile-content>

          <!-- <v-list-tile-action>
            <v-btn icon @click.stop="mini = !mini">
              <v-icon>chevron_left</v-icon>
            </v-btn>
          </v-list-tile-action>-->
        </v-list-tile>
      </v-list>

      <!-- <v-list class="pt-0" dense>
        <v-divider light></v-divider>
        <v-list-tile v-for="item in items" :key="item.title" @click>
          <v-list-tile-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>

          <v-list-tile-content>
            <v-list-tile-title>{{ item.title }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>-->

      <v-list class="pt-0" dense>
        <!-- <v-divider light></v-divider> -->
        <v-list-group value="true" prepend-icon="dashboard">
          <template v-slot:activator>
            <v-list-tile @click>
              <v-list-tile-content>
                <v-list-tile-title>Dashboard</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
            <v-menu offset-x v-if="mini">
              <template v-slot:activator="{ on }">
                <v-btn color="primary" dark v-on="on">Dropdown</v-btn>
              </template>
              <v-list right>
                <v-list-tile v-for="(item, index) in items" :key="index" @click>
                  <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                </v-list-tile>
              </v-list>
            </v-menu>
          </template>

          <div v-if="!mini">
            <v-list-tile
              class="pl-5"
              v-for="dash in dashboards"
              :key="dash.title"
              @click
              router
              :to="dash.path"
            >
              <v-list-tile-action>
                <v-icon v-text="dash.icon"></v-icon>
              </v-list-tile-action>
              <v-list-tile-title v-text="dash.title"></v-list-tile-title>
            </v-list-tile>
          </div>
        </v-list-group>

        <v-list-group value="true" prepend-icon="assessment">
          <template v-slot:activator>
            <v-list-tile @click>
              <v-list-tile-content>
                <v-list-tile-title>Report</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </template>
          <v-list-tile
            class="pl-5"
            v-for="dash in reports"
            :key="dash.title"
            @click
            router
            :to="dash.path"
          >
            <v-list-tile-action>
              <v-icon v-text="dash.icon"></v-icon>
            </v-list-tile-action>
            <v-list-tile-title v-text="dash.title"></v-list-tile-title>
          </v-list-tile>
        </v-list-group>
      </v-list>
    </v-navigation-drawer>
  </v-layout>
</template>


<script>
export default {
  props: ["mini"],
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
      ]
      // mini: false,
      // right: null
    };
  }
};
</script>