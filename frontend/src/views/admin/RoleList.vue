<template>
  <v-container fluid>
    <v-toolbar flat color="white">
      <v-toolbar-title>${$t("admin.ROLE")}</v-toolbar-title>
      <v-divider class="mx-2" inset vertical></v-divider>

      <v-flex xs2>
        <v-text-field
          v-model="search"
          append-icon="search"
          :label="$t('button.SEARCH')"
          hide-details
        ></v-text-field>
      </v-flex>
      <v-spacer></v-spacer>
      <d-new-role></d-new-role>
    </v-toolbar>
    <v-data-table :headers="headers" :items="data" :search="search" class="elevation-1" :pagination.sync="paginations">
      <template v-slot:items="props">
        <td class="text-xs-left">{{ props.item.name }}</td>
        <td class="text-xs-left">{{ props.item.status }}</td>
        <td class="text-xs-left">{{ props.item.created_time }}</td>

        <td class="justify-center layout px-0">
          <v-icon small class="mr-2" @click="editItem(props.item)">edit</v-icon>
          <v-icon small @click="deleteItem(props.item)">delete</v-icon>
        </td>
      </template>
      <template v-slot:no-data>
        <v-btn color="primary" @click="initialize">Reset</v-btn>
      </template>
    </v-data-table>
  </v-container>
</template>


<script>
import DNewRole from "@/components/admin/DNewRole";

export default {
  components: {
    DNewRole
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
      { text: "状态", value: "status" },
      { text: "创建日期", value: "created_time" }
    ],
    data: [],
    editedIndex: -1
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
    this.getUserLists();
  },

  methods: {
    getUserLists() {
      this.$axios
        .get("/admin/role/list")
        .then(res => {
          this.data = res.data;
        })
        .catch(error => {
          console.log(error);
        });
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