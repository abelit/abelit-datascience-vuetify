<template>
  <v-container fluid>
    <v-row>
      <v-col cols="4" md="3">
        <v-text-field v-model="message" label="Outlined" outlined clearable></v-text-field>
        <v-file-input label="File input"></v-file-input>
        <v-textarea
          outlined
          name="input-7-4"
          label="Outlined textarea"
          value="The Woodman set to work at once, and so sharp was his axe that the tree was soon chopped nearly through."
        ></v-textarea>
        <v-btn @click="addForm">add form</v-btn>
      </v-col>
      <v-col cols="8" md="9">
        <vuedraggable :list="list" class="list-group">
          <v-text-field v-for="(item,index) in list" v-model="formData[item.model]" :key="index" :label="item.label" outlined clearable></v-text-field>
        </vuedraggable>
        <v-btn @click="save">Save</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>


<script>
import vuedraggable from "vuedraggable";

export default {
  components: {
    vuedraggable
  },
  data() {
    return {
      formData: {},
      list: [
        // {id: 0, model: "message0", label: "text0"},
        // {id: 1, model: "message1", label: "text1"},
      ],
      dragging: false,
      message: "",
      id: 0
    };
  },
  methods: {
    addForm() {
      this.list.push({id: this.id, model: "message"+this.id, label: "text"+this.id});
      this.id ++;
    },
    removeForm(idx) {
      this.list.splice(idx, 1);
    },
    save() {
      console.log(this.formData["message4"])
      console.log(this.formData["message8"])
      console.log(this.list)
    }
  }
};
</script>