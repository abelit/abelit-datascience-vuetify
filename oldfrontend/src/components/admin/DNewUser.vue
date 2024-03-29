<template>
  <v-dialog v-model="cdialog" max-width="500">
    <template v-slot:activator="{ on }">
      <div v-on="on">
        <v-tooltip bottom>
          <template v-slot:activator="{ on }">
            <v-btn color="primary" dark class="mb-2" v-on="on" icon flat>
              <v-icon>playlist_add</v-icon>
            </v-btn>
          </template>
          <span>{{ $t('button.newUser') }}</span>
        </v-tooltip>
      </div>
    </template>
    <v-flex xs-12 sm-6 md-4 lg-1>
      <v-toolbar dark color="primary">
        <v-toolbar-title>{{  formTitle()  }}</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn icon dark @click="cdialog = false">
          <v-icon>close</v-icon>
        </v-btn>
      </v-toolbar>
      <v-card class="px-3">
        <v-card-title class="headline lighten-2" color="blue-grey darken-2" primary-title></v-card-title>
        <v-card-text class="pa-0">
          <v-form class="pa-3">
            <v-layout wrap align-center>
              <v-flex xs12 sm6>
                <v-text-field
                  v-model.trim="editedItem.username"
                  :disabled="editedIndex===-1?false:true"
                  prepend-inner-icon="person"
                  color="deep-purple"
                  :label="$t('auth.USERNAME')"
                  type="username"
                  v-validate="'required|alpha_num|max:20|min:6'"
                  :error-messages="pdialog?'':errors.collect('username')+usernameMessage"
                  data-vv-name="username"
                  required
                  class="mx-1"
                  @focus="checkUsername"
                  @blur="checkUsername"
                ></v-text-field>
              </v-flex>
              <v-flex xs12 sm6>
                <v-text-field
                  v-model.trim="editedItem.name"
                  prepend-inner-icon="person"
                  color="deep-purple"
                  :label="$t('auth.NAME')"
                  type="name"
                  v-validate="'required|max:20|min:2'"
                  :error-messages="errors.collect('name')"
                  data-vv-name="name"
                  required
                  class="mx-1"
                ></v-text-field>
              </v-flex>
            </v-layout>

            <v-layout wrap algin-center>
              <v-flex xs12 sm6>
                <v-text-field
                  v-model.trim="editedItem.email"
                  :disabled="editedIndex===-1?false:true"
                  prepend-inner-icon="email"
                  color="deep-purple"
                  :label="$t('auth.EMAIL')"
                  type="email"
                  v-validate="'required|email'"
                  :error-messages="errors.collect('email') + emailMessage"
                  data-vv-name="email"
                  required
                  class="mx-1"
                  @focus="checkEmail"
                  @blur="checkEmail"
                ></v-text-field>
              </v-flex>
              <v-flex xs12 sm6>
                <v-select
                  prepend-inner-icon="people"
                  v-model="editedItem.selected_gender"
                  v-validate="'required'"
                  :error-messages="errors.collect('gender')"
                  :items="genders"
                  item-text="name"
                  item-value="code"
                  :label="$t('auth.GENDER')"
                  data-vv-name="gender"
                  required
                  class="mx-1"
                ></v-select>
              </v-flex>
            </v-layout>

            <v-layout wrap align-center>
              <v-flex xs12 sm12>
                <v-text-field
                  v-model.trim="editedItem.password"
                  prepend-inner-icon="lock"
                  color="deep-purple"
                  counter="16"
                  :label="$t('auth.PASSWORD')"
                  :append-icon="isDisplayPassword ? 'visibility_off' : 'visibility'"
                  :type="isDisplayPassword ? 'text' : 'password'"
                  @click:append="isDisplayPassword = !isDisplayPassword"
                  v-validate="editedIndex===-1?'required|max:16|min:6':''"
                  :error-messages="errors.collect('password')"
                  data-vv-name="password"
                  ref="password"
                  required
                  class="mx-1"
                ></v-text-field>
              </v-flex>
            </v-layout>

            <v-layout wrap align-center>
              <v-flex xs12 sm6>
                <v-select
                  prepend-inner-icon="work"
                  v-model="editedItem.selected_department"
                  v-validate="'required'"
                  :error-messages="errors.collect('department')"
                  :items="departments"
                  item-text="name"
                  item-value="id"
                  :label="$t('auth.DEPARTMENT')"
                  class="mx-1"
                  data-vv-name="department"
                  required
                ></v-select>
              </v-flex>

              <v-flex xs12 sm6>
                <v-select
                  prepend-inner-icon="assignment_ind"
                  v-model="editedItem.selected_position"
                  v-validate="'required'"
                  :error-messages="errors.collect('position')"
                  :items="positions"
                  item-text="name"
                  item-value="id"
                  :label="$t('auth.POSITION')"
                  class="mx-1"
                  data-vv-name="position"
                  required
                ></v-select>
              </v-flex>
            </v-layout>

            <v-layout row wrap align-center>
              <v-flex xs12 sm12>
                <v-combobox
                  prepend-inner-icon="security"
                  v-model="editedItem.selected_role"
                  :items="roles"
                  :label="$t('admin.ROLE')"
                  item-text="name"
                  item-value="id"
                  class="mx-1"
                  multiple
                  chips
                  hide-details
                ></v-combobox>
              </v-flex>
            </v-layout>
            <v-layout row wrap align-center>
              <v-flex xs12 sm6>
                <v-checkbox
                  class="mx-1"
                  v-model="editedItem.status"
                  :label="$t('button.enable')"
                  data-vv-name="status"
                  hide-details
                ></v-checkbox>
              </v-flex>
            </v-layout>
          </v-form>
        </v-card-text>
        <!-- <v-divider></v-divider> -->
        <v-card-actions class="pb-3">
          <v-spacer></v-spacer>
          <v-btn color="primary" @click="cdialog = false" dark>
            <span class="font-weight-bold">{{$t("button.CANCEL") }}</span>
          </v-btn>
          <v-btn color="primary" @click="editedIndex===-1?handleNewUser():updateUser()" dark>
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
</template>


<script>
import { mapState } from "vuex";

export default {
  props: ["pdialog", "editedItem", "editedIndex"],
  data: () => ({
    isDisplayPassword: false,
    // username: undefined,
    // name: undefined,
    // email: undefined,
    isButtonLoading: false,
    message: "",
    loadingMessage: "",
    usernameMessage: "",
    emailMessage: "",
    // password: undefined,
    // selected_department: undefined,
    // selected_position: undefined,
    // selected_gender: undefined,
    // selected_role: undefined,
    departments: [],
    positions: [],
    roles: [],
    isActive: false,
    // status: false,
    cdialog: false
  }),
  methods: {
    // 等待完成表单输入验证后，然后显示登陆加载动画，这里在需要使用async与await关键字
    async handleNewUser() {
      // console.log(typeof this.editedItem.selected_gender)
      // console.log(this.editedItem)
      // console.log(this.$validator)
      // this.$validator.reset()
      // console.log(this.$validator)
      await this.$validator.validateAll();
      // 如果用户输入的所有内容没有错误信息，然后发起后台请求
      if (this.$validator.errors.all().length === 0) {
        this.isButtonLoading = true;
        this.loadingMessage = this.$t("message.LOADING");
        setTimeout(() => {
          this.isButtonLoading = false;
          this.$axios
            .post("/admin/user/add", {
              username: this.editedItem.username,
              name: this.editedItem.name,
              email: this.editedItem.email,
              password: this.editedItem.password,
              selected_department: this.editedItem.selected_department,
              selected_position: this.editedItem.selected_position,
              selected_gender: this.editedItem.selected_gender,
              status: this.editedItem.status ? 1 : 0,
              role: this.editedItem.selected_role
            })
            .then(() => {
              this.isActive = true;
              this.message = this.$t("message.SUCCESS_REGISTER");
              setTimeout(() => {
                this.message = "";
                // 跳转上一请求页面或主页
                this.cdialog = false;
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
    // 更新用户信息
    async updateUser() {
      // console.log(this.editedItem.selected_gender instanceof Object)
      // console.log(this.editedItem)
      await this.$validator.validateAll();
      // 如果用户输入的所有内容没有错误信息，然后发起后台请求
      if (this.$validator.errors.all().length === 0) {
        this.isButtonLoading = true;
        this.loadingMessage = this.$t("message.LOADING");
        setTimeout(() => {
          this.isButtonLoading = false;
          this.$axios
            .post("/admin/user/update", {
              username: this.editedItem.username,
              name: this.editedItem.name,
              email: this.editedItem.email,
              password: this.editedItem.password,
              selected_department: (this.editedItem.selected_department instanceof Object)?this.editedItem.selected_department.id:this.editedItem.selected_department,
              selected_position: (this.editedItem.selected_position instanceof Object)?this.editedItem.selected_position.id:this.editedItem.selected_position,
              selected_gender: (this.editedItem.selected_gender instanceof Object)?this.editedItem.selected_gender.code:this.editedItem.selected_gender,
              status: this.editedItem.status ? 1 : 0,
              role: this.editedItem.selected_role
            })
            .then(() => {
              this.isActive = true;
              this.message = this.$t("message.updateSuccessfully");
              setTimeout(() => {
                this.message = "";
                // 跳转上一请求页面或主页
                this.cdialog = false;
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
    getDepartment() {
      this.$axios
        .get("/api/group")
        .then(res => {
          // console.log(res.data)
          for (var i = 0; i < res.data.length; i++) {
            this.departments.push({
              id: res.data[i].id,
              name: res.data[i].name
            });
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    getPosition() {
      this.$axios
        .get("/api/position")
        .then(res => {
          // console.log(res.data)
          for (var i = 0; i < res.data.length; i++) {
            this.positions.push({
              id: res.data[i].id,
              name: res.data[i].name
            });
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    getRole() {
      this.$axios
        .get("/api/role")
        .then(res => {
          // console.log(res.data)
          for (var i = 0; i < res.data.length; i++) {
            this.roles.push({
              id: res.data[i].id,
              name: res.data[i].name
            });
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    checkUsername() {
      this.$axios
        .get("/api/checkusername", {
          params: {
            username: this.editedItem.username
          }
        })
        .then(() => {
          this.usernameMessage = "";
        })
        .catch(error => {
          if (error.status === 700) {
            this.usernameMessage = this.$t("api.USERNAME_EXIST");
          } else {
            this.usernameMessage = "";
          }
        });
    },
    checkEmail() {
      this.$axios
        .get("/api/checkemail", {
          params: {
            email: this.editedItem.email
          }
        })
        .then(() => {
          this.emailMessage = "";
        })
        .catch(error => {
          if (error.status === 700) {
            this.emailMessage = this.$t("api.EMAIL_EXIST");
          } else {
            this.emailMessage = "";
          }
        });
    },
    clear() {
      this.usernameMessage = "";
      this.emailMessage = "";
      this.$validator.reset();
    },
    formTitle() {
      return (this.editedIndex===-1) ? this.$t('button.newUser') : this.$t('button.editUser');
    }
  },
  mounted() {
    this.getDepartment();
    this.getPosition();
    this.getRole();
  },
  computed: {
    genders: function() {
      return [
        {
          name: this.$t("auth.MALE"),
          code: 1
        },
        {
          name: this.$t("auth.FEMALE"),
          code: 0
        }
      ];
    }
  },
  watch: {
    // 监听父组件pdialog的值
    pdialog(val) {
      console.log("pdialog: "+val);
      if (val) {
        this.clear()
        this.cdialog = true;
      }
    },
    // 监听子组件cdialog的值
    cdialog(val) {
      if (!val) {
        this.$emit("pChangeDialog");
      }
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