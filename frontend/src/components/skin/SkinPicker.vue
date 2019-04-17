<template>
  <v-menu offset-y max-width="200" nudge-bottom="20">
    <template v-slot:activator="{ on }">
      <v-btn dark v-on="on" icon>
        <v-icon>camera</v-icon>
      </v-btn>
    </template>
    <v-list color="primary">
      <v-list-tile v-for="(item, index) in items" :key="index" @click="getSkin(item)">
        <v-card :class="item.class" class="mr-3">
          <v-card-text></v-card-text>
        </v-card>
        <v-list-tile-title>{{ item.title }}</v-list-tile-title>
      </v-list-tile>
    </v-list>
  </v-menu>
</template>


<script>
export default {
  props: [""],
  data: () => ({
    items: [
      { title: "Black", color: "#000000", class: "black" },
      { title: "Grey", color: "#9E9E9E", class: "grey" },
      { title: "Grey Darken", color: "#424242", class: "grey darken-3" },
      { title: "Indigo", color: "#3F51B5", class: "indigo" },
      { title: "Light Blue", clolor: "#03A9F4", class: "light-blue" },
      { title: "Teal", color: "#009688", class: "teal" },
      { title: "Blue", color: "#2196F3", class: "blue" },
      { title: "Deep Purple", color: "#673AB7", class: "deep-purple" }
    ]
  }),
  methods: {
    getSkin(value) {
      this.$store.dispatch("setSkin", value);
      console.log(this.$store.getters.skin.class);
    }
  }
};
</script>