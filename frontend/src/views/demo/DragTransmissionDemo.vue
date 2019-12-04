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
          v-for="(item,idx) in list1"
          :key="idx"
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
        v-model="list"
        v-bind="dragOptions"
        @start="drag = true"
        @end="drag = false"
      >
       <!-- <transition-group type="transition" :name="!drag ? 'flip-list' : null"> -->
        <div
          class="list-group-item"
          v-for="(item,idx) in list2"
          :key="idx"
        >
          {{ item.name }}
        </div>
       <!-- </transition-group> -->
      </draggable>
      <v-btn @click="save">save</v-btn>
    </div>
  </div>
</template>

<script>
import draggable from "vuedraggable";
const message = [
"John",
"Joao",
"Jean",
"Gerard",
"Juan",
"Edgard",
// "Johnson"
];

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
      ],
      list: message.map((name, index) => {
        return { name, id: index + 1 };
      }),
      drag: false
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
  },
  computed: {
    dragOptions() {
      return {
        animation: 200,
        group: "forgroup",
        disabled: false,
        ghostClass: "ghost"
      };
    }
  }
};
</script>
<style>
.button {
  margin-top: 35px;
}
.flip-list-move {
  transition: transform 0.5s;
}
.no-move {
  transition: transform 0s;
}
.ghost {
  opacity: 0.5;
  background: #c8ebfb;
}
.list-group {
  min-height: 20px;
}
.list-group-item {
  cursor: move;
}
.list-group-item i {
  cursor: pointer;
}
</style>