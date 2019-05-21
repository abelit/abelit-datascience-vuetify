<template>
  <v-toolbar
    :color="$vuetify.theme.primary==='#9e9e9e'?'primary'+' darken-3':'primary'"
    fixed
    dark
    app
    >
    <v-toolbar-title class="ml-0 pl-0">
    </v-toolbar-title>
      <v-toolbar-side-icon  @click.stop="handleDrawerToggle"></v-toolbar-side-icon>
      <v-spacer></v-spacer>
      <v-flex xs4>
        <v-text-field
        append-icon="search"
        label="Search"
        class="hidden-sm-and-down"
        color="primary darken-4"
        >
      </v-text-field>
      </v-flex>
      <v-spacer></v-spacer>
      <d-help-question></d-help-question>
      <d-lang-picker></d-lang-picker>
      <d-full-screen></d-full-screen>
      <d-top-lock></d-top-lock>
      <v-menu offset-y origin="center center" class="elelvation-1" :nudge-bottom="14" transition="scale-transition">
        <v-btn icon flat slot="activator">
        <v-badge color="red" overlap>
          <span slot="badge">3</span>
          <v-icon medium>notifications</v-icon>
        </v-badge>
        </v-btn>
        <notification-list></notification-list>
      </v-menu>
      <v-menu offset-y origin="center center" :nudge-bottom="10" transition="scale-transition">
        <v-btn icon large flat slot="activator">
          <v-avatar size="30px">
            <img src="/static/avatar/man_4.jpg" alt="Michael Wang"/>
          </v-avatar>
          <!-- <v-icon> account_circle </v-icon> -->
        </v-btn>
        <v-list class="pa-0">
          <v-list-tile v-for="(item,index) in items" :to="!item.href ? { name: item.name } : null" :href="item.href" @click="item.click" ripple="ripple" :disabled="item.disabled" :target="item.target" rel="noopener" :key="index">
            <v-list-tile-action v-if="item.icon">
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>{{ item.title }}</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
      </v-menu>
  </v-toolbar>
</template>
<script>
import NotificationList from '@/components/widgets/list/NotificationList';
import DHelpQuestion from "@/components/widgets/support/DHelpQuestion";
import DLangPicker from "@/components/widgets/lang/DLangPicker";
import DFullScreen from "@/components/widgets/fullscreen/DFullScreen";
import DTopLock from "@/components/widgets/lock/DTopLock";

import Util from '@/util';
export default {
  name: 'app-toolbar',
  components: {
    NotificationList,
    DHelpQuestion,
    DLangPicker,
    DFullScreen,
    DTopLock
  },
  data: () => ({
    drawer: true,
    items: [
      {
        icon: 'account_circle',
        href: '#',
        title: 'Profile',
        click: (e) => {
          console.log(e);
        }
      },
      {
        icon: 'settings',
        href: '#',
        title: 'Settings',
        click: (e) => {
          console.log(e);
        }
      },
      {
        icon: 'exit_to_app',
        href: '#',
        title: 'Logout',
        click: (e) => {
          window.getApp.$emit('APP_LOGOUT');
        }
      }
    ],
  }),
  computed: {
    toolbarColor () {
      return this.$vuetify.options.extra.mainNav;
    }
  },
  methods: {
    handleDrawerToggle () {
      window.getApp.$emit('APP_DRAWER_TOGGLED');
      this.drawer = !this.drawer;
    }
  }
};
</script>
