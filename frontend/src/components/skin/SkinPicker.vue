<template>
  <v-menu offset-y max-width="200" nudge-bottom="20" return-value="hello">
    <template v-slot:activator="{ on }">
      <v-btn dark v-on="on" icon>
        <v-icon>camera</v-icon>
      </v-btn>
    </template>
    <v-list color="primary">
      <v-list-tile
        v-for="(item, index) in items"
        :key="index"
        :data-id="item.title"
        @click="getSkin(dataId)"
      >
        <v-card :class="item.class" class="mr-3">
          <v-card-text :data-id="item.title" @click="getSkin(dataId)"></v-card-text>
        </v-card>
        <v-list-tile-title :data-id="item.title" @click="getSkin(dataId)">{{ item.title }}</v-list-tile-title>
      </v-list-tile>
    </v-list>
  </v-menu>
</template>


<script>
export default {
  name: "dfSkinPicker",
  data: () => ({
    items: [
      { title: "Black", color: "#000000", class: "black" },
      { title: "Grey", color: "#9E9E9E", class: "grey" },
      { title: "Indigo", color: "#3F51B5", class: "indigo" },
      { title: "Light Blue", clolor: "#03A9F4", class: "light-blue" },
      { title: "Teal", color: "#009688", class: "teal" },
      { title: "Blue", color: "#2196F3", class: "blue" },
      { title: "Deep Purple", color: "#673AB7", class: "deep-purple" }
    ],
    lvalue: ""
  }),
  mounted() {
    console.log("hi");
  },
  methods: {
    getSkin(e) {
      console.log("hello");
      var target = event.target;
      var dataid = e;
      console.log(target);
      console.log(target.getAttribute("data-id"));
    }
  }
};
</script>