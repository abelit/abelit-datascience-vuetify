<template>
     <div id="app">
  <v-app id="inspire">
    <v-navigation-drawer
      app
      fixed
      permanent
      right
      v-model="drawer"
      width="420"
      class="pb-0"
    >
      <div class="panel">
        <header>
          <div class="header-slot">
            <h1>Header</h1>
            <v-btn icon>
              <v-icon color="primary">close</v-icon>
            </v-btn>
          </div>
        </header>
        <section>
          <h2>Content</h2>
          <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Magnam cumque doloribus cum praesentium illo distinctio quos vero aspernatur? Laudantium itaque, a cupiditate culpa corrupti dolores? Officiis inventore adipisci blanditiis recusandae!</p>
          <p>
            <img src="http://placeholder.pics/svg/300x300" alt="Placeholder">
          </p>
          <h3>More content</h3>
          <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Magnam cumque doloribus cum praesentium illo distinctio quos vero aspernatur? Laudantium itaque, a cupiditate culpa corrupti dolores? Officiis inventore adipisci blanditiis recusandae!</p>
          <p>
            <img src="http://placeholder.pics/svg/300x300" alt="Placeholder">
          </p>
          <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Magnam cumque doloribus cum praesentium illo distinctio quos vero aspernatur? Laudantium itaque, a cupiditate culpa corrupti dolores? Officiis inventore adipisci blanditiis recusandae!</p>
        </section>
        <footer>
          <div class="footer-slot">
            <div>
              <v-btn flat color="primary">Close</v-btn>
            </div>
            <div>
              <v-btn color="primary">Save</v-btn>
            </div>
          </div>
        </footer>
      </div>
    </v-navigation-drawer>
    <v-toolbar color="cyan" dark fixed app>
      <v-spacer></v-spacer>
      <v-toolbar-title>Application</v-toolbar-title>
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
    </v-toolbar>
    <v-content>
      <v-container fluid fill-height>
        <v-layout justify-center align-center>
          <v-tooltip right>
            <v-btn icon large :href="source" target="_blank" slot="activator">
              <v-icon large>code</v-icon>
            </v-btn>
          </v-tooltip>
        </v-layout>
      </v-container>
    </v-content>
    <v-footer color="cyan" app>
      <v-spacer></v-spacer>
      <span class="white--text">&copy; 2017</span>
    </v-footer>
  </v-app>
</div>   

</template>


<script>
export default {
     data: () => ({
    //
  })
}
</script>


<style lang="stylus">
    .navigation-drawer
        z-index 5
        .panel
            width: 100%
            height: 100%
            display: flex
            flex-direction: column
            flex-wrap: nowrap
            header
                border-bottom 1px solid rgba(0, 0, 0, .16)
                flex-shrink: 0
            section
                flex-grow: 1
                overflow-y: auto
                min-height: 2em
            footer
                border-top 1px solid rgba(0, 0, 0, .16)
                flex-shrink: 0
            header, section, footer
                padding 16px 24px
            .header-slot, .footer-slot
                align-items: center
                display: flex
                justify-content: space-between
            h1, .btn
                margin: 0
</style>