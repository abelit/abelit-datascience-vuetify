<template>
  <div class="row">
    <div class="col-3">
      <h3>Draggable 1</h3>
      <draggable
        class="dragArea list-group"
        :list="list1"
        :group="{ name: 'formgroup', pull: 'clone', put: false }"
      >
        <div
          class="list-group-item"
          v-for="item in list1"
          :key="item.name"
        >
          {{ item.name }}
        </div>
      </draggable>
    </div>

    <div class="col-3">
      <h3>Draggable 2</h3>
      <draggable
        class="dragArea list-group"
        :list="list2"
        group="formgroup"
      >
        <div
          class="list-group-item"
          v-for="item in list2"
          :key="item.name"
        >
          {{ item.name }}
        </div>
      </draggable>
      <v-btn @click="save">save</v-btn>
    </div>
  </div>
</template>

<script>
import draggable from "vuedraggable";
export default {
  // name: "clone",
  // display: "Clone",
  // order: 2,
  components: {
    draggable
  },
  data() {
    return {
      list1: [
        { name: "John", id: 1 },
        { name: "Joao", id: 2 },
        { name: "Jean", id: 3 },
        { name: "Gerard", id: 4 }
      ],
      list2: [
        // { name: "Juan", id: 5 },
        // { name: "Edgard", id: 6 },
        // { name: "Johnson", id: 7 }
      ]
    };
  },
  methods: {
    // log: function(evt) {
    //   window.console.log(evt);
    // },
    save(){
      console.log(this.list2);
      var i;
      for (i in this.list2) {
        console.log(i);
        console.log(this.list2[i].name)
      }
    }
  }
};
</script>
<style scoped></style>