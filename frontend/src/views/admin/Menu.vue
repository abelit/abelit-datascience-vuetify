<template>
<div>
  <v-container grid-list-xl fluid id="scroll-target" class="scroll-y d-content-fullscreen">
    <v-layout row wrap>
      <v-flex lg12>
        <v-card>
          <v-toolbar flat color="white">
            <!-- <v-toolbar-title>{{$t("admin.ROLE_LIST")}}</v-toolbar-title>
            <v-divider class="mx-2" inset vertical></v-divider> -->

            <v-flex xs2>
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
            <d-refresh :pMethod="getMenus"></d-refresh>
            <d-new-menu></d-new-menu>
          </v-toolbar>
          <v-card-text class="pa-0">
            <v-data-table
              :headers="headers"
              :items="data"
              :search="search"
              class="elevation-1"
              :pagination.sync="paginations"
            >
              <template v-slot:items="props">
                <td class="text-xs-left">{{ props.item.id }}</td>
                <td class="text-xs-left">{{ props.item.name }}</td>
                <td class="text-xs-left">{{ props.item.enname }}</td>
                <td class="text-xs-left">{{ props.item.fid }}</td>
                <td class="text-xs-left">{{ props.item.url }}</td>
                <td class="text-xs-left">{{ props.item.component }}</td>
                <td class="text-xs-left">{{ props.item.icon }}</td>
                <td class="text-xs-left">{{ props.item.status }}</td>
                <td class="text-xs-left">{{ props.item.type }}</td>
                <td class="text-xs-left">{{ props.item.order }}</td>
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
</div>
</template>


<script>
import DNewMenu from "@/components/admin/DNewMenu";
import DRefresh from "@/components/widgets/tool/DRefresh";

export default {
  components: {
    DNewMenu,
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
      { text: "编号", value: "id" },
      { text: "名称", value: "name" },
      { text: "英文名称", value: "enname" },
      { text: "父编号", value: "id" },
      { text: "地址", value: "id" },
      { text: "组件", value: "id" },
      { text: "图标", value: "id" },
      { text: "状态", value: "id" },
      { text: "类型", value: "description" },
      { text: "排序", value: "status" },
      { text: "创建日期", value: "created_time" },
      { text: "操作", value: "Action" }
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
    this.getMenus();
  },

  methods: {
    getMenus() {
      this.$axios
        .get("/api/menu")
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
