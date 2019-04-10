<template>
  <div class="login-container container-fluid">
    <v-card class="mx-auto" style="max-width: 500px; margin-top:5%;" color="#eaeaeaa1">
      <v-toolbar color="#01074ccf !important" cards dark flat>
        <v-icon size="36" color="#efefef">account_box</v-icon>
        <v-card-title
          class="title font-weight-regular"
          style="margin: 0 auto;"
        >{{$t('auth.USER_REGISTER')}}</v-card-title>

        <v-menu offset-y>
          <template v-slot:activator="{ on }">
            <v-btn color="transparent" v-on="on" flat>
              <img :src="langLogo" alt>
            </v-btn>
          </template>
          <v-list>
            <v-list-tile v-for="(lang, index) in langs" :key="index">
              <v-list-tile-avatar>
                <v-avatar size="32px" tile @click="changeLang(lang.lang,index)">
                  <img :src="lang.img">
                </v-avatar>
              </v-list-tile-avatar>
              <v-list-tile-title @click="changeLang(lang.lang)">{{ lang.name }}</v-list-tile-title>
            </v-list-tile>
          </v-list>
        </v-menu>
      </v-toolbar>
      <v-form ref="form" v-model="form" class="pa-3 pt-4">
        <v-icon size="36" color="#efefef" style="float: left;" class="df-icon">person</v-icon>
        <v-text-field
          v-model="username"
          box
          color="deep-purple"
          :label="$t('auth.USERNAME')"
          type="username"
          v-validate="'required|alpha_num|max:20|min:6'"
          :error-messages="errors.collect('username')+usernameMessage"
          data-vv-name="username"
          required
          class="df-input"
          @focus="checkUsername"
          @blur="checkUsername"
        ></v-text-field>
        <v-icon size="36" color="#efefef" style="float: left;" class="df-icon">person</v-icon>
        <v-text-field
          v-model="name"
          box
          color="deep-purple"
          :label="$t('auth.NAME')"
          type="name"
          v-validate="'required|max:20|min:2'"
          :error-messages="errors.collect('name')"
          data-vv-name="name"
          required
          class="df-input"
        ></v-text-field>

        <v-icon size="36" color="#efefef" style="float: left;" class="df-icon">email</v-icon>
        <v-text-field
          v-model="email"
          box
          color="deep-purple"
          :label="$t('auth.EMAIL')"
          type="email"
          v-validate="'required|email'"
          :error-messages="errors.collect('email') + emailMessage"
          data-vv-name="email"
          required
          class="df-input"
          @focus="checkEmail"
          @blur="checkEmail"
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
          v-validate="'required|max:18|min:8'"
          :error-messages="errors.collect('password')"
          data-vv-name="password"
          ref="password"
          required
        ></v-text-field>
        <v-icon size="36" color="#efefef" style="float: left;" class="df-icon">lock</v-icon>
        <v-text-field
          v-model="repassword"
          box
          color="deep-purple"
          counter="18"
          :label="$t('auth.REPASSWORD')"
          style="min-height: 96px; "
          :append-icon="passwordShow ? 'visibility_off' : 'visibility'"
          :type="passwordShow ? 'text' : 'password'"
          @click:append="passwordShow = !passwordShow"
          v-validate="'required|confirmed:password'"
          :error-messages="errors.collect('repassword')"
          data-vv-name="repassword"
          required
        ></v-text-field>
        <v-layout wrap align-center>
          <!-- <v-flex xs12 sm6 d-flex> -->
          <v-icon size="36" color="#efefef" style="float: left;" class="df-icon">work</v-icon>
          <v-select
            v-model="selected_department"
            v-validate="'required'"
            :error-messages="errors.collect('department')"
            :items="departments"
            item-text="name"
            item-value="id"
            box
            :label="$t('auth.DEPARTMENT')"
            class="df-select"
            data-vv-name="department"
            required
          ></v-select>
          <!-- </v-flex> -->

          <!-- <v-flex xs12 sm6 d-flex> -->
          <v-icon size="36" color="#efefef" style="float: left;" class="df-icon">assignment_ind</v-icon>
          <v-select
            v-model="selected_position"
            v-validate="'required'"
            :error-messages="errors.collect('position')"
            :items="positions"
            item-text="name"
            item-value="id"
            box
            :label="$t('auth.POSITION')"
            class="df-select"
            data-vv-name="position"
            required
          ></v-select>
          <!-- </v-flex> -->
        </v-layout>
        <v-icon size="36" color="#efefef" class="df-icon" style="float:left">group</v-icon>
        <v-radio-group
          v-model="picked_gender"
          v-validate="'required'"
          :error-messages="errors.collect('gender')"
          :mandatory="false"
          class="df-radio"
          data-vv-name="gender"
          required
        >
          <v-radio :label="$t('auth.MALE')" value="1"></v-radio>
          <v-radio :label="$t('auth.FEMALE')" value="0"></v-radio>
        </v-radio-group>
      </v-form>
      <v-divider></v-divider>

      <v-card-actions>
        <v-btn flat class="title font-weight-regular" @click="$refs.forauth.reset()">
          <router-link to="/user/login">{{$t('button.LOGIN')}}?</router-link>
        </v-btn>
        <v-spacer></v-spacer>
        <v-spacer></v-spacer>
        <v-btn
          :disabled="!form"
          class="title font-weight-regular"
          color="#01074ccf"
          depressed
          @click="submit"
        >{{$t('button.REGISTER')}}</v-btn>
      </v-card-actions>
      <div class="loading-overlay" v-if="isButtonLoading">
        <v-progress-circular :size="50" color="primary" indeterminate></v-progress-circular>
        <span>{{loadingMessage}}</span>
      </div>

      <div class="loading-overlay" v-if="message">
        <span v-bind:class="[isActive?'activeClass':'errorClass']">{{message}}</span>
      </div>
    </v-card>
  </div>
</template>

<script>
export default {
  data: () => ({
    passwordShow: false,
    username: undefined,
    name: undefined,
    email: undefined,
    form: false,
    isButtonLoading: false,
    message: "",
    loadingMessage: "",
    usernameMessage: "",
    emailMessage: "",
    password: undefined,
    repassword: undefined,
    selected_department: undefined,
    selected_position: undefined,
    picked_gender: undefined,
    departments: [],
    positions: [],
    isActive: false,
    lang: "zh_CN",
    langLogo: require("../../assets/images/auth/cn.png"),
    langs: {
      zh: {
        lang: "zh_CN",
        name: "简体中文",
        img: require("../../assets/images/auth/cn.png")
      },
      en: {
        lang: "en_US",
        name: "English",
        img: require("../../assets/images/auth/us.png")
      }
    }
  }),
  methods: {
    // 等待完成表单输入验证后，然后显示登陆加载动画，这里在需要使用async与await关键字
    async submit() {
      await this.$validator.validateAll();
      // 如果用户输入的所有内容没有错误信息，然后发起后台请求
      if (this.$validator.errors.all().length === 0) {
        this.isButtonLoading = true;
        this.loadingMessage = this.$t("message.LOADING");
        setTimeout(() => {
          this.isButtonLoading = false;
          this.$axios
            .post("/auth/register", {
              username: this.username,
              name: this.name,
              email: this.email,
              password: this.password,
              selected_department: this.selected_department,
              selected_position: this.selected_position,
              picked_gender: this.picked_gender
            })
            .then(res => {
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
            .catch(error => {
              this.isActive = false;
              this.message = this.$t("message.ERROR_REGISTER");
              setTimeout(() => {
                this.message = "";
              }, 2000);
            });
        }, 2000);
      }
    },
    changeLang(param_lang, param_index) {
      if (param_lang != null) {
        this.lang = param_lang;
      }
      if (param_index != null) {
        this.langLogo = this.langs[param_index].img;
      }
      this.$i18n.locale = this.lang;
      this.$validator.locale = this.lang;
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
  margin-bottom: auto;
  margin-left: 5px;
}

.df-input {
  padding: 10px;
}
.df-select {
  width: 20px;
}
.df-radio {
  margin-top: 0px;
  padding-top: 0px;
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