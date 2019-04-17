<template>
  <v-navigation-drawer v-model="drawer" :mini-variant.sync="mini" hide-overlay stateless>
    <v-img src="image" height="100%">
      <v-toolbar flat class="transparent">
        <v-list class="pa-0">
          <v-list-tile avatar>
            <v-list-tile-avatar>
              <img src="https://randomuser.me/api/portraits/men/85.jpg">
            </v-list-tile-avatar>

            <v-list-tile-content>
              <v-list-tile-title>John Leider</v-list-tile-title>
            </v-list-tile-content>

            <v-list-tile-action>
              <v-btn icon @click.stop="mini = !mini">
                <v-icon>chevron_left</v-icon>
              </v-btn>
            </v-list-tile-action>
          </v-list-tile>
        </v-list>
      </v-toolbar>

      <v-list class="pt-0" dense>
        <v-divider></v-divider>

        <v-list-tile v-for="item in items" :key="item.title" @click>
          <v-list-tile-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>

          <v-list-tile-content>
            <v-list-tile-title>{{ item.title }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>

      <v-list>
        <v-list-group value="true">
          <template v-slot:activator>
            <v-list-tile>
              <v-list-tile-action>
                <v-icon>account_circle</v-icon>
              </v-list-tile-action>
              <v-list-tile-content><v-list-tile-title>Users</v-list-tile-title></v-list-tile-content>
            </v-list-tile>
          </template>
          <v-list-group no-action sub-group value="true">
            <template v-slot:activator>
              <v-list-tile>
                <v-list-tile-title>Admin</v-list-tile-title>
              </v-list-tile>
            </template>

            <v-list-tile v-for="(admin, i) in admins" :key="i" @click>
                <v-list-tile-action>
                <v-icon v-text="admin[1]"></v-icon>
              </v-list-tile-action>
              <v-list-tile-title v-text="admin[0]"></v-list-tile-title>
              
            </v-list-tile>
          </v-list-group>
        </v-list-group>


        <v-menu offset-x dark min-width="200">
                <template v-slot:activator="{ on }">
                  <v-btn flat dark v-on="on" >
                    <v-icon>dashboard</v-icon>
                  </v-btn>
                </template>
                <v-list class="grey darken-1">
                  <v-list-tile
                    v-for="(item, index) in items"
                    :key="index"
                    @click
                    router
                    :to="item.path"
                    avatar
                  >
                    <v-list-tile-action-avatar class="mr-1">
                      <v-icon>{{item.icon}}</v-icon>
                    </v-list-tile-action-avatar>
                    <v-list-tile-title>{{ item.title }}</v-list-tile-title>
                  </v-list-tile>
                </v-list>
              </v-menu>
      </v-list>
    </v-img>
  </v-navigation-drawer>
</template>



<script>
export default {
  data() {
    return {
      drawer: true,
      items: [
        { title: "Home", icon: "dashboard" },
        { title: "About", icon: "question_answer" }
      ],
      mini: true,
      right: null,
      image:
        "https://demos.creative-tim.com/vue-material-dashboard/img/sidebar-3.3a54f533.jpg",
      admins: [["Management", "people_outline"], ["Settings", "settings"]]
    };
  }
};
</script>