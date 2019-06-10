<template>
  <v-container fluid class="d-content-fullscreen">
    <v-layout row wrap>
      <v-flex lg12>
        <v-card>
          <v-toolbar flat color="white">
            <v-flex xs4>
              <v-text-field
                flat
                solo
                prepend-icon="search"
                :placeholder="$t('admin.typeSomething')"
                v-model="search"
                hide-details
              ></v-text-field>
            </v-flex>
            <v-spacer></v-spacer>
            <d-refresh :pMethod="getPositions"></d-refresh>
            <d-new-position></d-new-position>
          </v-toolbar>
          <v-card-text class="pa-0">
            <v-data-table
              :headers="headers"
              :items="data"
              :search="search"
              class="elevation-1"
              :pagination.sync="paginations"
              :loading="isLoading"
            >
              <template v-slot:items="props">
                <td class="text-xs-left">{{ props.item.name }}</td>
                <td class="text-xs-left">{{ props.item.enname }}</td>
                <td class="text-xs-left">{{ props.item.description }}</td>
                <td class="text-xs-left">{{ props.item.status }}</td>
                <td class="text-xs-left">{{ props.item.created_time }}</td>

                <td>
                  <v-icon small class="mr-2" color="primary" @click="editItem(props.item)">edit</v-icon>
                  <v-icon small color="error" @click="deleteItem(props.item)">delete</v-icon>
                </td>
              </template>
              <template v-slot:no-data>
                <span>{{$t("message.noData")}}</span>
              </template>
              <template v-slot:no-results>
                <v-alert
                  :value="true"
                  color="error"
                  icon="warning"
                >{{ $t("admin.noRecordFound") }}</v-alert>
              </template>
            </v-data-table>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>


<script>
import DNewPosition from "@/components/admin/DNewPosition";
import DRefresh from "@/components/widgets/tool/DRefresh";

export default {
  components: {
    DNewPosition,
    DRefresh
  },
  data: () => ({
    search: "",
    dialog: false,
    paginations: {
      descending: true,
      rowsPerPage: 15
    },
    headers: [
      { text: "名称", value: "name" },
      { text: "英文名称", value: "enname" },
      { text: "描述信息", value: "description" },
      { text: "状态", value: "status" },
      { text: "创建日期", value: "created_time" },
      { text: "操作", value: "Action" }
    ],
    data: [],
    editedIndex: -1,
    isLoading: false
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Item" : "Edit Item";
    }
  },

  watch: {
    dialog(val) {
      val || this.close();
    }
  },

  created() {
    this.getPositions();
  },

  methods: {
    getPositions() {
      this.isLoading = true;
      setTimeout(() => {
        this.$axios
        .get("/api/position")
        .then(res => {
          this.data = res.data;
        })
        .catch(error => {
          console.log(error);
        });
        this.isLoading = false;
      }, 1500);
      
    },

    editItem(item) {
      this.editedIndex = this.data.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      const index = this.data.indexOf(item);
      confirm("Are you sure you want to delete this item?") &&
        this.data.splice(index, 1);
    },

    close() {
      this.dialog = false;
      setTimeout(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      }, 300);
    },

    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.data[this.editedIndex], this.editedItem);
      } else {
        this.data.push(this.editedItem);
      }
      this.close();
    }
  }
};
</script>