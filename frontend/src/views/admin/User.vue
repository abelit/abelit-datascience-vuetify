<template>
  <v-container fluid class="d-content-fullscreen">
    <v-layout row wrap >
      <v-flex sm12>
        <v-btn color="primary" @click="toggleFullscreen">fullscreen</v-btn>
      </v-flex>
      <v-flex lg12 >
        <v-card>
          <v-toolbar flat color="white">
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
            <d-refresh :pMethod="getUsers"></d-refresh>
            <d-new-user></d-new-user>
          </v-toolbar>
          <v-divider></v-divider>
          <v-card-text class="pa-0">
            <v-data-table
              :headers="result.headers"
              :search="search"
              :items="result.items"
              :rows-per-page-items="[10,25,50,{text:'All','value':-1}]"
              class="elevation-1"
              item-key="name"
              select-all
              v-model="result.selected"
            >
              <template v-slot:items="props">
                <td class="pr-0">
                  <v-checkbox primary hide-details v-model="props.selected"></v-checkbox>
                </td>
                <td>{{ props.item.username }}</td>
                <td class="text-xs-left">{{ props.item.name }}</td>
                <td class="text-xs-left">{{ props.item.email }}</td>
                <td class="text-xs-left">{{ props.item.gender }}</td>
                <td class="text-xs-left">{{ props.item.group }}</td>
                <td class="text-xs-left">{{ props.item.position }}</td>
                <td class="text-xs-left">{{ props.item.role }}</td>
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
import DNewUser from "@/components/admin/DNewUser";
import DRefresh from "@/components/widgets/tool/DRefresh";

export default {
  components: {
    DNewUser,
    DRefresh
  },
  data: () => ({
    search: "",
    dialog: false,
    paginations: {
      descending: true,
      rowsPerPage: 15
    },
    result: {
      selected: [],
      headers: [
        {
          text: "用户名",
          align: "left",
          sortable: false,
          value: "user"
        },
        { text: "姓名", value: "name" },
        { text: "邮箱", value: "email" },
        { text: "性别", value: "gender" },
        { text: "部门", value: "group" },
        { text: "职位", value: "position", sortable: false },
        { text: "角色", value: "role" },
        { text: "状态", value: "status" },
        { text: "创建日期", value: "created_time" },
        { text: "操作", value: "action" }
      ],
      items: []
    },
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
    this.getUsers();
  },

  methods: {
    getUsers() {
      this.$axios
        .get("/admin/user/list")
        .then(res => {
          this.result.items = res.data;
        })
        .catch(error => {
          console.log(error);
        });
    },

    editItem(item) {
      this.editedIndex = this.result.items.indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      const index = this.result.items.indexOf(item);
      confirm("Are you sure you want to delete this item?") &&
        this.result.items.splice(index, 1);
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
        Object.assign(this.result.items[this.editedIndex], this.editedItem);
      } else {
        this.result.items.push(this.editedItem);
      }
      this.close();
    },
    toggleFullscreen () {
      this.$fullscreen.toggle(this.$el.querySelector('.d-content-fullscreen'),{
        wrap: false,
        callback: this.fullscreenChange
      })
    },
    fullscreenChange (fullscreen) {
      this.fullscreen = fullscreen;
    }
  }
};
</script>


<style lang="scss" rel="stylesheet/scss" scoped>
  .wrapper {
    position: relative;
    height: 400px;
    .chart-container {
      height: 100%;
      width: 100%;
    }
    .btn-map-fullscreen {
      position: absolute;
      right: 10px;
      bottom: 10px;
      width: 36px;
      height: 36px;
      padding: 0;
      font-size: 36px;
      line-height: 36px;
      text-align: center;
      outline: none;
    }
    &.fullscreen {
      display: flex;
      justify-content: center;
      align-items: center;
      .chart-container {
        height: 60%;
        width: 60%;
      }
      .btn-map-fullscreen {
        left: 10px;
        top: 10px;
        right: auto;
        bottom: auto;
      }
    }
  }
</style>