<template>
  <v-container fluid>
    <v-row>
      <v-col cols="4" md="3">
        <vuedraggable
          class="dragArea list-group"
          :list="formStyleList"
          :group="{ name: 'people', pull: 'clone', put: false }"
          :clone="cloneDog"
        >
         <v-btn v-for="(item,index) in formStyleList" x-large color="success" dark block :key="item.id" left>
           <v-icon left>{{item.icon}}</v-icon> {{item.name}}
         </v-btn>
          <!-- <v-text-field v-model="message" label="Outlined" outlined clearable key="1"></v-text-field> -->
          <!-- <v-file-input label="File input"></v-file-input>
          <v-textarea
            outlined
            name="input-7-4"
            label="Outlined textarea"
            value="The Woodman set to work at once, and so sharp was his axe that the tree was soon chopped nearly through."
          ></v-textarea>
          <v-btn @click="addForm">add form</v-btn> -->
        </vuedraggable>
      </v-col>
      <v-col cols="8" md="9">
        <vuedraggable class="dragArea list-group" :list="list" v-for="(item,index) in list" group="people">
          <v-text-field

            v-model="formData[item.model]"
            :key="index"
            :label="item.label"
            outlined
            clearable
            v-if="item.type==0"
          ></v-text-field>
          <v-select
            v-model="formData[item.model]"
            :key="index"
            :label="item.label"
          outlined
          v-else-if="item.type==1"
        ></v-select>
          <v-file-input 
            v-model="formData[item.model]"
            :key="index"
            :label="item.label" v-else-if="item.type==2"></v-file-input>
          <v-textarea
            v-model="formData[item.model]"
            :key="index"
            :label="item.label"
          auto-grow
          outlined
          rows="5"
          row-height="15"
          v-else-if="item.type==3"
        ></v-textarea>
        </vuedraggable>
        <v-btn @click="save">Save</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>


<script>
import vuedraggable from "vuedraggable";

let globalId = 0;

export default {
  components: {
    vuedraggable
  },
  data() {
    return {
      formData: {},
      formStyleList: [
        {id: 0, name: "Text Field", icon:"mdi-format-text",type:"text_field"},
        {id: 1, name: "Selects", icon:"mdi-select",type:"select_field"},
        {id: 2, name: "File Inputs", icon:"mdi-paperclip",type:"file_field"},
        {id: 3, name: "Text Area", icon:"mdi-card-text",type:"text_area"},
      ],
      list: [],
      dragging: false,
      message: "",

    };
  },
  methods: {
    // addForm() {
    //   this.list.push({
    //     id: this.id,
    //     model: "message" + this.id,
    //     label: "text" + this.id
    //   });
    //   this.id++;
    // },
    removeForm(idx) {
      this.list.splice(idx, 1);
    },
    save() {
      // console.log(this.formData["message4"]);
      console.log(this.formData["message3"]);
      console.log(this.list);
    },
    cloneDog({ id }) {
      // console.log(this.list)
      console.log(id)
      this.list.push({
        id: globalId,
        model: "message" + globalId,
        label: "text" + globalId,
        type: id
      });
      globalId++;
      console.log(this.list)
    }
  }
};
</script>