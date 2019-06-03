  <template>
  <v-layout row class="align-center layout px-4 pt-2 app--page-header">
    <div class="page-header-left">
      <h3 class="pr-3">{{generateTitle(title)}}</h3>
    </div>
    <v-breadcrumbs divider="-" :items="breadcrumbs"></v-breadcrumbs>
    <v-spacer></v-spacer>
    <div class="page-header-right">
      <v-btn icon class="mx-0">
        <v-icon class="text--secondary">refresh</v-icon>
      </v-btn>
    </div>
    <v-btn icon @click="toggleParentMethod" class="mx-0">
      <v-icon class="text--secondary">fullscreen</v-icon>
    </v-btn>
    <v-btn icon v-on="on" class="mx-0">
      <v-icon class="text--secondary">more_vert</v-icon>
    </v-btn>
  </v-layout>
</template>

<script>
import menu from "@/api/menu";
import { generateTitle } from "@/util/i18n";

export default {
  data() {
    return {
      title: ""
    };
  },
  methods: {
    generateTitle,
    toggleParentMethod() {
      this.$emit("toggleFullscreen");
    }
  },
  computed: {
    breadcrumbs: function() {
      let breadcrumbs = [];
      menu.forEach(item => {
        if (item.items) {
          let child = item.items.find(i => {
            return i.component === this.$route.name;
          });
          if (child) {
            breadcrumbs.push(item.title);
            breadcrumbs.push(child.title);
            this.title = child.title;
          }
        } else {
          if (item.name === this.$route.name) {
            this.title = item.title;
            breadcrumbs.push(item.title);
          }
        }
      });
      return breadcrumbs;
    }
  },
  mounted () {
  }
};
</script>
