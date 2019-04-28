<template>
<div id="app">
  <v-app id="inspire">
    <v-navigation-drawer
      fixed
      v-model="drawer"
      app
    >
      <v-list dense>
        <v-list-tile @click="">
          <v-list-tile-action>
            <v-icon>home</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Home</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile @click="">
          <v-list-tile-action>
            <v-icon>contact_mail</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Contact</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-toolbar color="indigo" dark fixed app>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>Application</v-toolbar-title>
    </v-toolbar>
    <v-content>
      <v-container fluid fill-height class="scroll-y">
        <v-layout
          justify-center
          align-center
        >
          <v-flex text-xs-center>
            <v-tooltip left>
              <v-btn icon large :href="source" target="_blank" slot="activator">
                <v-icon large>code</v-icon>
              </v-btn>
              <span>Source</span>
            </v-tooltip>
          </v-flex>

          <v-flex  text-xs-center>  
                  <table-demo></table-demo>
    <table-two-demo></table-two-demo>
    <table-one-demo></table-one-demo>
    <table-three-demo></table-three-demo>
          </v-flex>
        </v-layout>

  
      </v-container>
    </v-content>
    <v-footer color="indigo" app inset absolute>
      <span class="white--text">&copy; 2017</span>
    </v-footer>
  </v-app>
</div>
</template>


<script>
import TableDemo from "@/components/tables/TableDemo";
import TableTwoDemo from "@/components/tables/TableTwoDemo";
import TableOneDemo from "@/components/tables/TableOneDemo";
import TableThreeDemo from "@/components/tables/TableThreeDemo";
export default {
  components: {
    TableDemo,
    TableTwoDemo,
    TableOneDemo,
    TableThreeDemo
  },
  
data: () => ({
    drawer: null
  })
}
</script>