<template>
  <v-form>
    <v-container>
      <!-- <v-row>
        <v-col cols="12" sm="4">
          <v-text-field v-model="message" outlined type="text" dense>
            <span style="width: 50px;padding-top:10px" slot="prepend">姓名:</span>
          </v-text-field>
        </v-col>
        <v-col cols="12" sm="4">
          <v-text-field v-model="message" outlined type="text" dense>
            <span style="width: 50px;padding-top:10px" slot="prepend">密码:</span>
          </v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" sm="4">
          <v-text-field v-model="message" outlined type="text" dense>
            <template v-slot:append-outer>
              <v-btn class="primary" style="height: 40px">查询</v-btn>
            </template>
          </v-text-field>
        </v-col>
        <v-col cols="12" sm="4">
          <v-text-field v-model="message" outlined type="text" dense>
            <template v-slot:append-outer>
              <v-btn class="primary" style="height: 40px">查询</v-btn>
            </template>
          </v-text-field>
        </v-col>
        <v-col cols="12" sm="4">
          <v-text-field v-model="message" outlined type="text" dense>
            <template v-slot:append-outer>
              <v-btn class="primary" style="height: 40px">查询</v-btn>
            </template>
          </v-text-field>
        </v-col>
      </v-row>

      <v-row>
        <v-col cols="12" sm="4">
          <v-text-field v-model="message" outlined type="text" dense>
            <template v-slot:prepend>
              <span style="height: 40px;width: 50px;text-align:center;padding-top:10px">查询</span>
            </template>
          </v-text-field>
        </v-col>
        <v-col cols="12" sm="6">
          <v-text-field v-model="message" outlined type="text" dense>
            <template v-slot:prepend>
              <span style="height: 40px;width: 50px;text-align:center;padding-top:10px">查询</span>
            </template>
          </v-text-field>
        </v-col>
        <v-col cols="12" sm="2">
          <v-text-field v-model="message" outlined type="text" dense>
            <template v-slot:prepend>
              <span style="height: 40px;width: 50px;text-align:center;padding-top:10px">查询</span>
            </template>
          </v-text-field>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <v-card>
            <v-tabs dark background-color="teal darken-3" show-arrows>
              <v-tabs-slider color="teal lighten-3"></v-tabs-slider>

              <v-tab v-for="i in 30" :key="i" :href="'#tab-' + i">Item {{ i }}</v-tab>
            </v-tabs>
          </v-card>
        </v-col>
      </v-row> -->
      <v-row>
        <v-col>
          <div class="text-center">
            <v-chip-group show-arrows style="vertical-align: middle">
              <span
                style="border: 1px orange  solid; height: 32px;line-height: 30px;z-index: 2000;background-color: green"
                v-if="chip1"
                class="mx-1"
              >
                <v-chip
                  class="ma-0 pa-0 py-1"
                  tag
                  :to="url"
                  style="background-opacity:.5"
                  @click:close="closeChip"
                  @contextmenu.prevent.native="openMenu(tag,$event)"
                >Remove</v-chip>
                <span style="z-index: 2000" @click="chip1 = false">
                  <v-icon small fab>close</v-icon>
                </span>
              </span>
              <span
                style="border: 1px orange  solid;border-radius: 3px; height:32px;line-height: 30px; text-align:center"
                v-if="chip1"
              >
                <span to="/" class="ma-1" @contextmenu.prevent.native="openMenu(tag,$event)">page</span>
                <span style="z-index: 2000" @click="chip1 = false" class="ma-1">
                  <v-icon small>close</v-icon>
                </span>
              </span>

              <v-chip
                tag
                v-if="chip2"
                class="ma-1"
                close
                :to="url"
                color="red"
                text-color="white"
                @click:close="closeChip"
                style="z-index: 2000"
                @contextmenu.prevent.native="openMenu(tag,$event)"
              >Remove</v-chip>

              <v-chip
                tag
                v-if="chip3"
                class="ma-1"
                close
                :to="url"
                color="green"
                outlined
                @click:close="chip3 = false"
                
              >Success</v-chip>

              <v-chip
                v-if="chip4"
                class="ma-1"
                close
                :to="url"
                color="orange"
                label
                outlined
                @click:close="chip4 = false"
                @contextmenu.prevent.native="openMenu(tag,$event)"
              >Complete</v-chip>
              <v-chip
                tag
                v-if="chip1"
                class="ma-1"
                :to="url"
                close
                @click(close).prevent.stop="chip1 = false"
                @contextmenu.prevent.native="openMenu(tag,$event)"
              >Closable</v-chip>

              <router-link
                ref="tag"
                :to="url"
                tag="span"
                class="tags-view-item"
                style="border: 1px orange  solid;border-radius: 3px; height:32px;line-height: 30px; text-align:center"
                v-if="chip1"
              >
                ceshi
                <span @click.prevent.stop="chip1 = false" class="ma-1">
                  <v-icon small>close</v-icon>
                </span>
              </router-link>
            </v-chip-group>
          </div>
          <ul
            v-show="visible"
            :style="{left:left+'px',top:top+'px'}"
            class="contextmenuaa"
            slot="mytag"
          >
            <li>Refresh</li>
            <li>Close</li>
            <li>Close Others</li>
            <li>Close All</li>
          </ul>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>


<script>
export default {
  data: () => ({
    message: "Hey!",
    loading: false,
    chip1: true,
    chip2: true,
    chip3: true,
    chip4: true,
    visible: false,
    top: 0,
    left: 0,
    selectedTag: {},
    affixTags: [],
    url: "/"
  }),

  methods: {
    closeChip() {
      console.log("hi");
      this.url = "#";
      console.log(this.$router);
      alert("hi");

      this.chip2 = false;
      return;
    },
    clickMe() {
      this.loading = true;
      this.message = "Wait for it...";
      setTimeout(() => {
        this.loading = false;
        this.message = "You've clicked me!";
      }, 2000);
    },
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
  },
  mounted() {
    console.log("v-chip mounted");
  }
};
</script>

<style lang="scss">
.v-chip__content {
  // background-color: #fff;
}
.v-input__append-outer {
  margin: 0 0 !important;
}
.v-input__prepend-outer {
  margin: 0 0 !important;
}
.contextmenuaa {
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
    padding: 7px 16px;
    cursor: pointer;
    &:hover {
      background: #eee;
    }
  }
}
</style>