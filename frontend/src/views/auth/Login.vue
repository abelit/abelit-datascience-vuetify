<template>
  <v-app id="login" class="primary">
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4 lg4>
            <v-card class="elevation-1 pa-3">
              <v-card-title class="pa-0">
                <v-spacer></v-spacer>
                <d-lang-picker></d-lang-picker>
              </v-card-title>
              <v-card-text>
                <div class="layout column align-center">
                  <img
                    :src="logo"
                    alt="Data Analysis"
                    width="120"
                    height="120"
                  >
                  <h3 class="flex primary--text mt-2 mb-4">DATA ANALYSIS</h3>
                </div>
                <v-form>
                  <v-text-field
                    v-model="username"
                    prepend-inner-icon="person"
                    color="deep-purple"
                    :label="$t('auth.EMAIL')+'/'+$t('auth.USERNAME') "
                    type="username"
                    v-validate="'required'"
                    :error-messages="errors.collect('username')"
                    data-vv-name="username"
                    required
                  ></v-text-field>
                  <v-text-field
                    v-model="password"
                    prepend-inner-icon="lock"
                    color="deep-purple"
                    counter="18"
                    :label="$t('auth.PASSWORD')"
                    style="min-height: 96px; "
                    :append-icon="isDisplayPassword ? 'visibility_off' : 'visibility'"
                    :type="isDisplayPassword ? 'text' : 'password'"
                    @click:append="isDisplayPassword = !isDisplayPassword"
                    v-validate="'required|max:18|min:3'"
                    :error-messages="errors.collect('password')"
                    data-vv-name="password"
                    required
                    @keyup.enter="handleLogin"
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-divider></v-divider>
              <v-card-actions>
                <v-btn flat color="primary">
                  <router-link to="/user/register">{{$t('button.REGISTER')}}?</router-link>
                </v-btn>
                <v-spacer></v-spacer>
                <v-btn block color="primary" @click="handleLogin" class="font-weight-regular">{{$t('button.LOGIN')}}</v-btn>
              </v-card-actions>
              <div class="loading-overlay" v-if="isButtonLoading">
                <v-progress-circular :size="50" color="primary" indeterminate></v-progress-circular>
                <span>{{loadingMessage}}</span>
              </div>

              <div class="loading-overlay" v-if="message">
                <span v-bind:class="[isActive ? 'activeClass' : 'errorClass']">{{message}}</span>
              </div>
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
  name: "Login",
  components: {
    DLangPicker
  },
  data: () => ({
    logo: "/static/images/logo/DataScience.svg",
    isDisplayPassword: false,
    username: undefined,
    email: undefined,
    isButtonLoading: false,
    loadingMessage: "",
    password: undefined,
    message: "",
    isActive: true
  }),
  methods: {
    // 等待完成表单输入验证后，然后显示登陆加载动画，这里在需要使用async与await关键字
    async handleLogin() {
      await this.$validator.validateAll();
      if (this.$validator.errors.all().length === 0) {
        this.isButtonLoading = true;
        this.loadingMessage = this.$t("message.LOGINING");
        setTimeout(() => {
          this.isButtonLoading = false;
          this.$axios
            .post("/auth/login", {
              username: this.username,
              password: this.password
            })
            .then(res => {
              // console.log(res.data);
              // console.log(res.status);
              this.message = this.$t("message.SUCCESS_LOGIN");
              this.isActive = true;
              setTimeout(() => {
                this.message = "";
                // 异步调用store中action下setToken方法存储token信息
                this.$store.dispatch("setToken", res.data);
                // 生成动态路由
                // 跳转上一请求页面或主页
                this.$router.push(this.$router.currentRoute.query.url || "/");
              }, 2000);
            })
            .catch(error => {
              // console.log(error.data);
              // console.log(error.status);
              // 接收后台返回错误状态，401表示登录用户授权错误，可能是用户名或密码不匹配造成的
              this.isActive = false;
              if (error.status === 401) {
                this.message = this.$t("message.ERROR_LOGIN");
              } else {
                this.message = this.$t("message.ERROR_INTERNAL");
              }
              setTimeout(() => {
                this.message = "";
              }, 2000);
            });
        }, 2000);
      }
    }
  },
  computed: {
    ...mapState(["toolbarColor"])
  }
};
</script>

<style scoped lang="css">
/* .login-container {
  background-image: url("/static/images/page/background001.jpg");
  background-repeat: no-repeat;
} */
#login {
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
