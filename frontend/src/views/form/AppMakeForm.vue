<template>
  <v-container fluid class="pt-0">
    <v-row justify="center">
      <v-col cols="4" md="3" sm="2" xs="2" v-if="!$vuetify.breakpoint.mdAndDown">
        <v-card outlined class="mx-auto" max-height="100%" dense>
          <v-card-title class="py-2">
            <v-icon large left>ballot</v-icon>
            <span class="title font-weight-light">Form Category</span>
          </v-card-title>
          <v-divider></v-divider>
          <vue-perfect-scrollbar>
            <v-card-text :style="$vuetify.breakpoint.mdAndDown?'height:40vh':'height:76vh'">
              <vuedraggable
                class="dragArea list-group"
                :list="formStyleList"
                :group="{ name: 'formgroup', pull: 'clone', put: false }"
                :clone="cloneDog"
              >
                <v-btn
                  v-for="item in formStyleList"
                  x-large
                  color="primary lighten-1"
                  dark
                  block
                  :key="item.id"
                  left
                  class="text-left"
                >
                  <v-icon left>{{item.icon}}</v-icon>
                  {{item.name}}
                </v-btn>
              </vuedraggable>
            </v-card-text>
          </vue-perfect-scrollbar>
        </v-card>
      </v-col>
      <v-col cols="$vuetify.breakpoint.mdAndDown?12:8" md="9" sm="10" xs="10" class="pl-0">
        <v-card outlined>
          <v-card-title class="py-2">
            <v-icon large left>description</v-icon>
            <span class="title font-weight-light">Form Design Zone</span>

            <v-spacer></v-spacer>
            <v-btn icon>
              <v-icon>mdi-settings</v-icon>
            </v-btn>
          </v-card-title>
          <v-divider></v-divider>
          <vue-perfect-scrollbar>
            <v-card-text :style="$vuetify.breakpoint.mdAndDown?'height:43vh':'height:70vh'">
              <v-container fluid>
                <v-row justify="center" dense>
                  <v-col cols="12">
                    <v-card>
                      <v-card-title class="justify-center">
                        <vuedraggable
                          class="dragArea list-group"
                          :list="list"
                          group="formgroup"
                          v-bind="dragOptions"
                          @start="drag = true"
                          @end="drag = false"
                        >
                          <div v-for="item in list" :key="item.id">
                            <span class="title font-weight-light" v-if="item.type==4">Table1</span>
                            <v-btn icon color="teal" style="height: 40px" v-if="item.type==4">
                              <v-icon>mdi-format-list-bulleted-square</v-icon>
                            </v-btn>
                            <v-btn
                              icon
                              color="teal"
                              style="height: 40px"
                              @click="removeItem(list, item)"
                              v-if="item.type==4"
                            >
                              <v-icon>close</v-icon>
                            </v-btn>
                          </div>
                        </vuedraggable>
                      </v-card-title>
                      <v-card-text>
                        <v-form>
                          <vuedraggable
                            class="dragArea list-group"
                            :list="list"
                            group="formgroup"
                            v-bind="dragOptions"
                            @start="drag = true"
                            @end="drag = false"
                          >
                            <v-row justify="center" v-if="list.length==0"> 
                              <span>Drag Form components Here ...</span>
                            </v-row>
                            <div v-for="item in list" :key="item.id" >
                              <v-text-field
                                v-model="formData[item.model]"
                                :label="item.label"
                                outlined
                                dense
                                clearable
                                v-if="item.type==0"
                              >
                                <template v-slot:append-outer>
                                  <v-btn icon color="teal" style="height: 40px">
                                    <v-icon>mdi-format-list-bulleted-square</v-icon>
                                  </v-btn>
                                  <v-btn
                                    icon
                                    color="teal"
                                    style="height: 40px"
                                    @click="removeItem(list,item)"
                                  >
                                    <v-icon>close</v-icon>
                                  </v-btn>
                                </template>
                              </v-text-field>
                              <v-select
                                v-model="formData[item.model]"
                                :label="item.label"
                                outlined
                                dense
                                v-else-if="item.type==1"
                              >
                                <template v-slot:append-outer>
                                  <v-btn icon color="teal" style="height: 40px">
                                    <v-icon>mdi-format-list-bulleted-square</v-icon>
                                  </v-btn>
                                  <v-btn
                                    icon
                                    color="teal"
                                    style="height: 40px"
                                    @click="removeItem(list,item)"
                                  >
                                    <v-icon>close</v-icon>
                                  </v-btn>
                                </template>
                              </v-select>
                              <v-file-input
                                v-model="formData[item.model]"
                                :label="item.label"
                                outlined
                                dense
                                v-else-if="item.type==2"
                              >
                                <template v-slot:append-outer>
                                  <v-btn icon color="teal" style="height: 40px">
                                    <v-icon>mdi-format-list-bulleted-square</v-icon>
                                  </v-btn>
                                  <v-btn
                                    icon
                                    color="teal"
                                    style="height: 40px"
                                    @click="removeItem(list,item)"
                                  >
                                    <v-icon>close</v-icon>
                                  </v-btn>
                                </template>
                              </v-file-input>
                              <v-textarea
                                v-model="formData[item.model]"
                                :key="item.id"
                                :label="item.label"
                                auto-grow
                                outlined
                                rows="10"
                                row-height="10"
                                v-else-if="item.type==3"
                              >
                                <template v-slot:append-outer>
                                  <v-btn icon color="teal" style="height: 40px">
                                    <v-icon>mdi-format-list-bulleted-square</v-icon>
                                  </v-btn>
                                  <v-btn
                                    icon
                                    color="teal"
                                    style="height: 40px"
                                    @click="removeItem(list, item)"
                                  >
                                    <v-icon>close</v-icon>
                                  </v-btn>
                                </template>
                              </v-textarea>
                            </div>
                          </vuedraggable>
                        </v-form>
                      </v-card-text>
                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <vuedraggable
                          class="dragArea list-group"
                          :list="list"
                          group="formgroup"
                          v-bind="dragOptions"
                          @start="drag = true"
                          @end="drag = false"
                        >
                          <div v-for="item in list" :key="item.id">
                            <v-btn v-if="item.type==5">cancel</v-btn>
                            <v-btn v-if="item.type==5">save</v-btn>
                            <v-btn icon color="teal" style="height: 40px" v-if="item.type==5">
                              <v-icon>mdi-format-list-bulleted-square</v-icon>
                            </v-btn>
                            <v-btn
                              icon
                              color="teal"
                              style="height: 40px"
                              @click="removeItem(list, item)"
                              v-if="item.type==5"
                            >
                              <v-icon>close</v-icon>
                            </v-btn>
                          </div>
                        </vuedraggable>
                      </v-card-actions>
                    </v-card>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>
          </vue-perfect-scrollbar>
          <v-divider></v-divider>

          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn @click="clear">Clear</v-btn>
            <v-btn @click="save">Save</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
    <v-row justify="center" v-if="$vuetify.breakpoint.mdAndDown">
      <v-col>
        <div class="text-center">
          <v-btn fab color="cyan accent-2" @click="dialog = !dialog">
            <v-icon>mdi-plus</v-icon>
          </v-btn>
        </div>

        <v-dialog v-model="dialog" max-width="500px">
          <v-card>
            <v-card-title class="py-2">Form Style</v-card-title>
            <v-card-text class="pt-5">
              <vuedraggable
                class="dragArea list-group"
                :list="formStyleList"
                :group="{ name: 'formgroup', pull: 'clone', put: false }"
                :clone="cloneDog"
              >
                <v-btn
                  v-for="item in formStyleList"
                  x-large
                  color="primary"
                  dark
                  block
                  :key="item.id"
                  left
                  @click.stop="addForm(item.id)"
                >
                  <v-icon left>{{item.icon}}</v-icon>
                  {{item.name}}
                </v-btn>
              </vuedraggable>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn text color="primary" @click.stop="dialog = false">Finish</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-col>
    </v-row>
  </v-container>
</template>


<script>
import vuedraggable from "vuedraggable";
import VuePerfectScrollbar from "vue-perfect-scrollbar";

let globalId = 0;

export default {
  components: {
    vuedraggable,
    VuePerfectScrollbar
  },
  order: 3,
  data() {
    return {
      formData: {},
      formStyleList: [
        {
          id: 0,
          name: "Text Field",
          icon: "mdi-format-text",
          type: "text_field"
        },
        { id: 1, name: "Selects", icon: "mdi-select", type: "select_field" },
        {
          id: 2,
          name: "File Inputs",
          icon: "mdi-paperclip",
          type: "file_field"
        },
        { id: 3, name: "Text Area", icon: "mdi-card-text", type: "text_area" },
        { id: 4, name: "Title", icon: "table_chart", type: "table_title" },
        {
          id: 5,
          name: "Button",
          icon: "radio_button_checked",
          type: "submit_button"
        }
      ],
      list: [],
      dragging: false,
      message: "",
      dialog: false,
      scrollSettings: {}
    };
  },
  methods: {
    addForm(id) {
      // console.log(id);
      var addList = {
        id: globalId,
        model: "message" + globalId,
        label: "text" + globalId,
        type: id
      };
      this.list.push(addList);
      globalId++;
    },
    save() {
      // console.log(this.formData["message4"]);
      // console.log(this.formData["message0"]);
      console.log(this.list);
    },
    clear() {
      this.list = [];
      globalId = 0;
    },
    removeItem(arr, item) {
      console.log(arr);
      var num = arr.length;
      for (var i = 0; i < num; i++) {
        if (arr[0] != item) {
          arr.push(arr.shift());
        } else {
          arr.shift();
        }
      }
      console.log(arr);
      return arr;
    },
    cloneDog({ id }) {
      // console.log(this.list)
      // console.log(id);
      var addList = {
        id: globalId,
        model: "message" + globalId,
        label: "text" + globalId,
        type: id
      };

      globalId++;
      return addList;
      // console.log(this.list);
    }
  },
  computed: {
    dragOptions() {
      return {
        animation: 200,
        group: "description",
        disabled: false,
        ghostClass: "ghost"
      };
    }
  }
};
</script>


<style lang="scss">
#app-content-page {
  overflow: hidden;

  #app-content-page--scroll {
    height: 100%;
    overflow: auto;
  }
}
.v-input__append-outer {
  margin: 0 !important;
}
</style>