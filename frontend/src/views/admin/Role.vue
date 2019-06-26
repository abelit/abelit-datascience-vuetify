<template>
  <v-container fluid>
    <v-layout row wrap>
      <v-flex lg12>
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
            <d-refresh :pMethod="getRoles"></d-refresh>
            <v-dialog v-model="dialog" max-width="500">
              <template v-slot:activator="{ on }">
                <div v-on="on">
                  <v-tooltip bottom>
                    <template v-slot:activator="{ on }">
                      <v-btn color="primary" dark class="mb-2" v-on="on" icon flat>
                        <v-icon>playlist_add</v-icon>
                      </v-btn>
                    </template>
                    <span>{{ $t("button.NEW_ROLE") }}</span>
                  </v-tooltip>
                </div>
              </template>
              <v-flex xs-12 sm-6 md-4 lg-1>
                <v-toolbar dark color="primary">
                  <v-toolbar-title> {{  formTitle  }} </v-toolbar-title>
                  <v-spacer></v-spacer>
                  <v-btn icon dark @click="dialog = false">
                    <v-icon>close</v-icon>
                  </v-btn>
                </v-toolbar>
                <v-card class="px-3">
                  <v-card-title class="headline lighten-2" color="blue-grey darken-2" primary-title></v-card-title>
                  <v-card-text class="pa-0">
                    <v-form class="pa-3">
                      <v-layout row wrap align-center>
                        <v-flex xs12 sm12>
                          <v-text-field
                            v-model.trim="editedItem.name"
                            prepend-inner-icon="verified_user"
                            color="deep-purple"
                            :label="$t('admin.ROLE_NAME')"
                            type="name"
                            v-validate="'required|max:20|min:2'"
                            :error-messages="errors.collect('name')"
                            data-vv-name="name"
                            required
                            class="mx-1"
                            :disabled="editedIndex===-1?false:true"
                          ></v-text-field>
                        </v-flex>
                      </v-layout>
                      <v-layout row wrap align-center>
                        <v-flex xs12 sm12>
                          <v-text-field
                            v-model.trim="editedItem.enname"
                            prepend-inner-icon="verified_user"
                            color="deep-purple"
                            :label="$t('admin.ENNAME')"
                            type="enname"
                            v-validate="'required|max:20|min:2'"
                            :error-messages="errors.collect('enname')"
                            data-vv-name="enname"
                            required
                            class="mx-1"
                            :disabled="editedIndex===-1?false:true"
                          ></v-text-field>
                        </v-flex>
                      </v-layout>
                      <v-layout row wrap align-center>
                        <v-flex xs12 sm6>
                          <v-checkbox
                            class="mx-1"
                            v-model="editedItem.status"
                            :label="$t('button.enable')"
                            data-vv-name="status"
                          ></v-checkbox>
                        </v-flex>
                      </v-layout>
                    </v-form>
                  </v-card-text>
                  <!-- <v-divider></v-divider> -->
                  <v-card-actions class="pb-3">
                    <v-spacer></v-spacer>
                    <v-btn color="primary" @click="dialog = false" dark>
                      <span class="font-weight-bold">{{$t("button.CANCEL") }}</span>
                    </v-btn>
                    <v-btn color="primary" @click="editedIndex===-1?handNewRole():updateRole()" dark>
                      <span class="font-weight-bold">{{$t("button.CONFIRM") }}</span>
                    </v-btn>
                  </v-card-actions>
                  <div class="loading-overlay" v-if="isButtonLoading">
                    <v-progress-circular :size="50" color="primary" indeterminate></v-progress-circular>
                    <span>{{loadingMessage}}</span>
                  </div>
                  <div class="loading-overlay" v-if="message">
                    <span :class="[isActive ? 'activeClass' : 'errorClass']">{{message}}</span>
                  </div>
                </v-card>
              </v-flex>
            </v-dialog>
          </v-toolbar>
          <v-card-text class="pa-0">
            <v-data-table
              :headers="headers"
              :items="items"
              :search="search"
              class="elevation-1"
              :pagination.sync="paginations"
              select-all
              v-model="selected"
              item-key="name"
            >
              <template v-slot:items="props">
                <td class="pr-0">
                  <v-checkbox primary hide-details v-model="props.selected"></v-checkbox>
                </td>
                <td class="text-xs-left">{{ props.item.name }}</td>
                <td class="text-xs-left">{{ props.item.enname }}</td>
                <td class="text-xs-left"><v-chip
                        :color="props.item.status===1?'primary':''"
                      >{{ (props.item.status===1)?$t("button.enabled"):$t("button.disabled") }}</v-chip></td>
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
                <v-alert :value="true" color="error" icon="warning">{{ $t("admin.noRecordFound") }}</v-alert>
              </template>
            </v-data-table>
          </v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>


<script>
import DRefresh from "@/components/widgets/tool/DRefresh";

export default {
  components: {
    DRefresh
  },
  data: () => ({
    isButtonLoading: false,
    message: "",
    loadingMessage: "",
    isActive: false,
    dialog: false,
    search: "",
    paginations: {
      descending: true,
      rowsPerPage: 15
    },
    selected: [],
    headers: [
      { text: "名称", value: "name" },
      { text: "英文名称", value: "en_name" },
      { text: "状态", value: "status" },
      { text: "创建日期", value: "created_time" },
      { text: "操作", value: "Action" }
    ],
    items: [],
    editedIndex: -1,
    editedItem: {
      name: "",
      enname: "",
      status: false
    },
    defaultItem: {
      name: "",
      enname: "",
      status: false
    }
  }),

  computed: {
    formTitle() {
     return (this.editedIndex===-1) ? this.$t('button.newRole') : this.$t('button.editRole');
    }
  },
  watch: {
    dialog(val) {
      val || this.close();
      this.getRoles;
    }
  },
  created() {
    this.getRoles();
  },

  methods: {
    // 等待完成表单输入验证后，然后显示登陆加载动画，这里在需要使用async与await关键字
    async handNewRole() {
      await this.$validator.validateAll();
      // 如果用户输入的所有内容没有错误信息，然后发起后台请求
      if (this.$validator.errors.all().length === 0) {
        this.isButtonLoading = true;
        this.loadingMessage = this.$t("message.LOADING");
        setTimeout(() => {
          this.isButtonLoading = false;
          this.$axios
            .post("/admin/role/add", {
              name: this.editedItem.name,
              enname: this.editedItem.enname,
              status: this.editedItem.status ? 1 : 0
            })
            .then(() => {
              this.isActive = true;
              this.message = this.$t("message.SUCCESS_REGISTER");
              setTimeout(() => {
                this.message = "";
                // 跳转上一请求页面或主页
                this.dialog = false;
              }, 1000);
            })
            .catch(() => {
              this.isActive = false;
              this.message = this.$t("message.ERROR_REGISTER");
              setTimeout(() => {
                this.message = "";
              }, 1000);
            });
        }, 1000);
      }
    },
    getRoles() {
      this.$axios
        .get("/admin/role/list")
        .then(res => {
          this.items = res.data;
        })
        .catch(error => {
          console.log(error);
        });
    },
    deleteRole(item) {
      console.log(item)
      this.$axios
        .post("/admin/role/delete", {
          name: item.name
        })
        .then(() => {
          this.isActive = true;
          this.message = this.$t("message.SUCCESS_REGISTER");
          setTimeout(() => {
            this.message = "";
            // 跳转上一请求页面或主页
          }, 1000);
        })
        .catch(() => {
          this.isActive = false;
          this.message = this.$t("message.ERROR_REGISTER");
          setTimeout(() => {
            this.message = "";
          }, 1000);
        });
    },
      // 跟新角色信息
    async updateRole() {
      await this.$validator.validateAll();
      // 如果用户输入的所有内容没有错误信息，然后发起后台请求
      if (this.$validator.errors.all().length === 0) {
        this.isButtonLoading = true;
        this.loadingMessage = this.$t("message.LOADING");
        setTimeout(() => {
          this.isButtonLoading = false;
          this.$axios
            .post("/admin/role/update", {
              name: this.editedItem.name,
              status: this.editedItem.status ? 1 : 0
            })
            .then(() => {
              this.isActive = true;
              this.message = this.$t("message.updateSuccessfully");
              setTimeout(() => {
                this.message = "";
                // 跳转上一请求页面或主页
                this.dialog = false;
              }, 1000);
            })
            .catch(() => {
              this.isActive = false;
              this.message = this.$t("message.updateFailed");
              setTimeout(() => {
                this.message = "";
              }, 1000);
            });
        }, 1000);
      }
    },
    editItem(item) {
      // 通过JSON.stringify和JSON.parse完全复制对象
      let _item = JSON.parse(JSON.stringify(item));

      _item.status = item.status === 1 ? true : false;
      this.editedIndex = this.items.indexOf(item);
      this.editedItem = Object.assign({}, _item);
      this.dialog = true;
    },

    deleteItem(item) {
      const index = this.items.indexOf(item);
      confirm(this.$t("message.deleteDataTip")) && this.deleteRole(item);
      this.items.splice(index, 1)
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
        Object.assign(this.items[this.editedIndex], this.editedItem);
      } else {
        this.items.push(this.editedItem);
      }
      this.close();
    }
  }
};
</script>


<style lang="css" scoped>
#register {
  height: 50%;
  width: 100%;
  position: absolute;
  top: 0;
  left: 0;
  content: "";
  z-index: 0;
}

.loading-overlay {
  z-index: 10;
  top: 0;
  left: 0;
  right: 0;
  position: absolute;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.9);
  display: flex;
  align-items: center;
  justify-content: center;
}
.activeClass {
  color: green;
  font-size: 18px;
}
.errorClass {
  color: red;
  font-size: 18px;
}
</style>