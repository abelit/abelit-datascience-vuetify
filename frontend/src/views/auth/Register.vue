<template>
  <v-app id="register" class="primary">
    <v-content>
      <v-container fill-height fluid class="login-container">
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4 lg4>
            <v-card class="elevation-1 pa-3">
              <v-card-title class="pa-0">
                <v-spacer></v-spacer>
                <d-lang-picker></d-lang-picker>
              </v-card-title>
              <v-card-text>
                <div class="layout column align-center">
                  <img :src="logo" alt="Data Analysis" width="120" height="120">
                  <h3 class="flex primary--text mt-2 mb-4">DATA ANALYSIS</h3>
                </div>
                <v-form class="pa-3">
                  <v-layout wrap align-center>
                    <v-flex xs12 sm6>
                      <v-text-field
                        v-model.trim="username"
                        prepend-inner-icon="person"
                        color="deep-purple"
                        :label="$t('auth.USERNAME')"
                        type="username"
                        v-validate="'required|alpha_num|max:20|min:6'"
                        :error-messages="errors.collect('username')+usernameMessage"
                        data-vv-name="username"
                        required
                        class="mx-1"
                        @focus="checkUsername"
                        @blur="checkUsername"
                      ></v-text-field>
                    </v-flex>
                    <v-flex xs12 sm6>
                      <v-text-field
                        v-model.trim="name"
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
                        v-model.trim="email"
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
                        v-model="selected_gender"
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
                    <v-flex xs12 sm6>
                      <v-text-field
                        v-model.trim="password"
                        prepend-inner-icon="lock"
                        color="deep-purple"
                        counter="18"
                        :label="$t('auth.PASSWORD')"
                        style="min-height: 96px; "
                        :append-icon="isDisplayPassword ? 'visibility_off' : 'visibility'"
                        :type="isDisplayPassword ? 'text' : 'password'"
                        @click:append="isDisplayPassword = !isDisplayPassword"
                        v-validate="'required|max:18|min:8'"
                        :error-messages="errors.collect('password')"
                        data-vv-name="password"
                        ref="password"
                        required
                        class="mx-1"
                      ></v-text-field>
                    </v-flex>
                    <v-flex xs12 sm6>
                      <v-text-field
                        v-model.trim="repassword"
                        prepend-inner-icon="lock"
                        color="deep-purple"
                        counter="18"
                        :label="$t('auth.REPASSWORD')"
                        style="min-height: 96px; "
                        :append-icon="isDisplayPassword ? 'visibility_off' : 'visibility'"
                        :type="isDisplayPassword ? 'text' : 'password'"
                        @click:append="isDisplayPassword = !isDisplayPassword"
                        v-validate="'required|confirmed:password'"
                        :error-messages="errors.collect('repassword')"
                        data-vv-name="repassword"
                        required
                        class="mx-1"
                      ></v-text-field>
                    </v-flex>
                  </v-layout>

                  <v-layout wrap align-center>
                    <v-flex xs12 sm6>
                      <v-select
                        prepend-inner-icon="work"
                        v-model="selected_department"
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
                        v-model="selected_position"
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
                </v-form>
                <v-divider></v-divider>

                <v-card-actions>
                  <v-btn flat  @click="$refs.forauth.reset()">
                    <router-link to="/user/login">{{$t('button.LOGIN')}}?</router-link>
                  </v-btn>
                  <v-spacer></v-spacer>
                  <v-btn
                    block
                    color="primary"
                    @click="hanldeRegister"
                    class="font-weight-regular"
                  >{{$t('button.REGISTER')}}</v-btn>
                </v-card-actions>
                <div class="loading-overlay" v-if="isButtonLoading">
                  <v-progress-circular :size="50" color="primary" indeterminate></v-progress-circular>
                  <span>{{loadingMessage}}</span>
                </div>
                <div class="loading-overlay" v-if="message">
                  <span :class="[isActive ? 'activeClass' : 'errorClass']">{{message}}</span>
                </div>
              </v-card-text>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import DLangPicker from "@/components/widgets/lang/DLangPicker";

import { mapState } from "vuex";

export default {
  name: "Register",
  components: {
    DLangPicker
  },
  data: () => ({
    logo: "/static/images/logo/DataScience.svg",
    isDisplayPassword: false,
    username: undefined,
    name: undefined,
    email: undefined,
    isButtonLoading: false,
    message: "",
    loadingMessage: "",
    usernameMessage: "",
    emailMessage: "",
    password: undefined,
    repassword: undefined,
    selected_department: undefined,
    selected_position: undefined,
    selected_gender: undefined,
    departments: [],
    positions: [],
    isActive: false
  }),
  methods: {
    // 等待完成表单输入验证后，然后显示登陆加载动画，这里在需要使用async与await关键字
    async hanldeRegister() {
      await this.$validator.validateAll();
      // 如果用户输入的所有内容没有错误信息，然后发起后台请求
      if (this.$validator.errors.all().length === 0) {
        this.isButtonLoading = true;
        this.loadingMessage = this.$t("message.LOADING");
        setTimeout(() => {
          this.isButtonLoading = false;
          console.log(this.selected_gender);
          this.$axios
            .post("/auth/register", {
              username: this.username,
              name: this.name,
              email: this.email,
              password: this.password,
              selected_department: this.selected_department,
              selected_position: this.selected_position,
              selected_gender: this.selected_gender
            })
            .then(() => {
              this.isActive = true;
              this.message = this.$t("message.SUCCESS_REGISTER");
              setTimeout(() => {
                this.message = "";
                // 跳转上一请求页面或主页
                this.$router.push(
                  this.$router.currentRoute.query.url || "/user/login"
                );
              }, 2000);
            })
            .catch(() => {
              this.isActive = false;
              this.message = this.$t("message.ERROR_REGISTER");
              setTimeout(() => {
                this.message = "";
              }, 2000);
            });
        }, 2000);
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
    checkUsername() {
      this.$axios
        .get("/api/checkusername", {
          params: {
            username: this.username
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
            email: this.email
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
      this.name = "";
      this.email = "";
      this.select = null;
      this.checkbox = null;
      this.$validator.reset();
    }
  },
  mounted() {
    this.getDepartment();
    this.getPosition();
    console.log(this.selected_gender);
  },
  computed: {
    ...mapState(["toolbarColor"]),
    genders: function() {
      return [
        {
          name: this.$t("auth.MALE"),
          code: "1"
        },
        {
          name: this.$t("auth.FEMALE"),
          code: "0"
        }
      ];
    }
  }
};
</script>

<style lang="css" scoped>
/* .login-container {
  background-image: url("/static/images/page/background001.jpg");
  background-repeat: no-repeat;
} */
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