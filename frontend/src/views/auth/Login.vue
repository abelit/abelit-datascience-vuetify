<template>
  <transition name="rotate-fall">
    <div class="login-container container-fluid">
      <v-card class="mx-auto" style="max-width: 500px; margin-top:15%;" color="#eaeaeaa1">
        <v-toolbar color="#01074ccf !important" cards dark flat>
          <v-icon size="36" color="#efefef">account_box</v-icon>
          <v-card-title
            class="title font-weight-regular"
            style="margin: 0 auto;"
          >{{$t('auth.USER_LOGIN')}}</v-card-title>
          <select-lang></select-lang>
        </v-toolbar>
        <v-form ref="form" v-model="form" class="pa-3 pt-4" :disabled="!form">
          <v-icon size="36" color="#efefef" style="float: left;" class="df-icon">person</v-icon>
          <v-text-field
            v-model="username"
            box
            color="deep-purple"
            :label="$t('auth.EMAIL')+'/'+$t('auth.USERNAME') "
            type="username"
            v-validate="'required'"
            :error-messages="errors.collect('username')"
            data-vv-name="username"
            required
            class="df-input"
          ></v-text-field>

          <v-icon size="36" color="#efefef" style="float: left;" class="df-icon">lock</v-icon>
          <v-text-field
            v-model="password"
            box
            color="deep-purple"
            counter="18"
            :label="$t('auth.PASSWORD')"
            style="min-height: 96px; "
            :append-icon="passwordShow ? 'visibility_off' : 'visibility'"
            :type="passwordShow ? 'text' : 'password'"
            @click:append="passwordShow = !passwordShow"
            v-validate="'required|max:18|min:3'"
            :error-messages="errors.collect('password')"
            data-vv-name="password"
            required
            @keyup.enter="submit"
          ></v-text-field>
        </v-form>
        <v-divider></v-divider>

        <v-card-actions>
          <v-btn flat class="title font-weight-regular">
            <router-link to="/user/register">{{$t('button.REGISTER')}}?</router-link>
          </v-btn>
          <v-spacer></v-spacer>
          <v-spacer></v-spacer>
          <v-btn class="title font-weight-regular" color="#01074ccf" depressed @click="submit">
            <span style="color: #efefef">{{$t('button.LOGIN')}}</span>
          </v-btn>
        </v-card-actions>
        <div class="loading-overlay" v-if="isButtonLoading">
          <v-progress-circular :size="50" color="primary" indeterminate></v-progress-circular>
          <span>{{loadingMessage}}</span>
        </div>

        <div class="loading-overlay" v-if="message">
          <span v-bind:class="[isActive ? 'activeClass' : 'errorClass']">{{message}}</span>
        </div>
      </v-card>
    </div>
  </transition>
</template>

<script>
import SelectLang from "@/components/lang/SelectLang";

export default {
  name: "Login",
  components: {
    SelectLang
  },
  data: () => ({
    passwordShow: false,
    username: undefined,
    email: undefined,
    form: false,
    isButtonLoading: false,
    loadingMessage: "",
    password: undefined,
    message: "",
    isActive: true
  }),
  methods: {
    // 等待完成表单输入验证后，然后显示登陆加载动画，这里在需要使用async与await关键字
    async submit() {
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
                // 存储token信息
                this.$store.commit("setToken", res.data);
                // 生成动态路由
                this.genRoutes();
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
    },
    genRoutes() {
      let routeList = [
        { path: "/demo/mapdemo", name: "mapdemo", component: "AmchartsDemo" },
        { path: "/demo/uidemo", name: "uidemo", component: "UIDemo" },
        { path: "/demo/trans", name: "trans", component: "TranslateDemo" }
      ];
      // 生成路由对象，使用 vue-cli开发时导入组件推荐使用import导入模块
      let routes = [];
      for (let i = 0; i < routeList.length; i++) {
        routes.push({
          path: routeList[i].path,
          name: routeList[i].name,
          component: () => import("@/components/demo/" + routeList[i].component)
        });
      }
      routes.push({
        path: "*",
        name: "404",
        component: () => import("@/views/NotFound")
      });

      // 把动态路由写入实列路由表
      for (var rt in routes) {
        this.$router.options.routes.push(routes[rt]);
      }
      // add dynamic routes 添加动态路由
      this.$router.addRoutes(routes);
      // console.log(this.$router.options.routes);

      localStorage.setItem("routeList", JSON.stringify(routeList));
    }
  }
};
</script>

<style lang="css" scoped>
.login-container {
  width: 100%;
  height: 100%;
  background-image: url("../../assets/images/auth/login_page_default.jpg");
  background-repeat: no-repeat;
  background-size: 100% 100%;
  -moz-background-size: 100% 100%;
}
.df-icon {
  position: relative;
  padding: 10px;
  background: #01074ccf;
  min-width: 50px;
  text-align: center;
}
.df-input {
  /* padding: 10px; */
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