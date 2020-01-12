<template>
  <v-container fluid class="mt-0 ml-0 pa-0">
        <v-toolbar dense height="32" class="pl-1">
          <v-chip-group show-arrows class="pa-0" v-if="chip">
            <v-chip
              v-if="chip"
              class="mr-1 my-0"
              close
              to="/"
              color="orange"
              label
              outlined
              small
              @click:close="chip = false"
              @contextmenu.prevent.native="openMenu(tag,$event)"
            >Complete</v-chip>
            <v-chip
              v-if="chip"
              class="mr-1 my-0"
              close
              to="/"
              color="orange"
              label
              outlined
              small
              @click:close="chip = false"
              @contextmenu.prevent.native="openMenu(tag,$event)"
            >Complete</v-chip>
            <v-chip
              v-if="chip"
              class="mr-1 my-0"
              close
              to="/"
              color="orange"
              label
              outlined
              small
              @click:close="chip = false"
              @contextmenu.prevent.native="openMenu(tag,$event)"
            >Complete</v-chip>
          </v-chip-group>
        </v-toolbar>
        <!-- <v-divider></v-divider> -->
        <ul v-show="visible" :style="{left:left+'px',top:top+'px'}" class="contextmenu">
          <li>Refresh</li>
          <li>Close</li>
          <li>Close Others</li>
          <li>Close All</li>
        </ul>
  </v-container>
</template>

<script>
export default {
  data: function() {
    return {
      chip: true,
      visible: false,
      top: 0,
      left: 0,
      selectedTag: {},
      affixTags: []
    };
  },
  methods: {
    openMenu(tag, e) {
      const menuMinWidth = 105;
      const offsetLeft = this.$el.getBoundingClientRect().left; // container margin left
      const offsetWidth = this.$el.offsetWidth; // container width
      const maxLeft = offsetWidth - menuMinWidth; // left boundary
      const left = e.clientX - offsetLeft + 15; // 15: margin right
      if (left > maxLeft) {
        this.left = maxLeft;
      } else {
        this.left = left;
      }
      this.top = e.clientY;
      this.visible = true;
      this.selectedTag = tag;
    },
    closeMenu() {
      this.visible = false;
    }
  },
  watch: {
    visible(value) {
      if (value) {
        document.body.addEventListener("click", this.closeMenu);
      } else {
        document.body.removeEventListener("click", this.closeMenu);
      }
    }
  }
};
</script>

<style lang="scss">
.contextmenu {
  margin: 0;
  background: #fff;
  z-index: 3000;
  position: absolute;
  list-style-type: none;
  padding: 5px 0;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 400;
  color: #333;
  box-shadow: 2px 2px 3px 0 rgba(0, 0, 0, 0.3);
  li {
    margin: 0;
    padding: 0px 5px;
    cursor: pointer;
    &:hover {
      background: #eee;
    }
  }
}
.v-toolbar__content {
    padding-left: 0px;
}
</style>