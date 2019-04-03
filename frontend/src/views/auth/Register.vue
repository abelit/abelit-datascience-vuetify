<template>
  <div class="login-container container-fluid">
    <v-card class="mx-auto" style="max-width: 500px; margin-top:5%;" color="#eaeaeaa1">
      <v-toolbar color="#01074ccf !important" cards dark flat>
        <v-icon size="36" color="#efefef">account_box</v-icon>
        <v-card-title
          class="title font-weight-regular"
          style="margin: 0 auto;"
        >{{$t('auth.registerPage')}}</v-card-title>

        <v-menu offset-y>
          <template v-slot:activator="{ on }">
            <v-btn color="transparent" v-on="on" flat>
              <img :src="langLogo" alt>
            </v-btn>
          </template>
          <v-list>
            <v-list-tile v-for="(lang, index) in langs" :key="index">
              <v-list-tile-avatar>
                <v-avatar size="32px" tile @click="changeLangEvent(lang.lang,index)">
                  <img :src="lang.img">
                </v-avatar>
              </v-list-tile-avatar>
              <v-list-tile-title @click="changeLangEvent(lang.lang)">{{ lang.name }}</v-list-tile-title>
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
          :label="$t('auth.username')"
          type="username"
          v-validate="'required|alpha_num|max:20|min:6'"
          :error-messages="errors.collect('username')+checkUsername"
          data-vv-name="username"
          required
          class="df-input"
          @focus="checkUser"
          @blur="checkUser"
        ></v-text-field>
        <v-icon size="36" color="#efefef" style="float: left;" class="df-icon">person</v-icon>
        <v-text-field
          v-model="name"
          box
          color="deep-purple"
          :label="$t('auth.name')"
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
          :label="$t('auth.email')"
          type="email"
          v-validate="'required|email'"
          :error-messages="errors.collect('email')"
          data-vv-name="email"
          required
          class="df-input"
        ></v-text-field>

        <v-icon size="36" color="#efefef" style="float: left;" class="df-icon">lock</v-icon>
        <v-text-field
          v-model="password"
          box
          color="deep-purple"
          counter="18"
          :label="$t('auth.password')"
          style="min-height: 96px; "
          :append-icon="showPassword ? 'visibility_off' : 'visibility'"
          :type="showPassword ? 'text' : 'password'"
          @click:append="showPassword = !showPassword"
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
          :label="$t('auth.repassword')"
          style="min-height: 96px; "
          :append-icon="showPassword ? 'visibility_off' : 'visibility'"
          :type="showPassword ? 'text' : 'password'"
          @click:append="showPassword = !showPassword"
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
            :label="$t('auth.department')"
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
            :label="$t('auth.position')"
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
          <v-radio :label="$t('auth.male')" value="1"></v-radio>
          <v-radio :label="$t('auth.female')" value="0"></v-radio>
        </v-radio-group>
      </v-form>
      <v-divider></v-divider>

      <v-card-actions>
        <v-btn flat class="title font-weight-regular" @click="$refs.forauth.reset()">
          <router-link to="/user/login">{{$t('auth.login')}}?</router-link>
        </v-btn>
        <v-spacer></v-spacer>
        <v-spacer></v-spacer>
        <v-btn
          :disabled="!form"
          class="white--text title font-weight-regular"
          color="#01074ccf"
          depressed
          @click="submit"
        >{{$t('auth.register')}}</v-btn>
      </v-card-actions>
      <div class="loading-overlay" v-if="isBtnLoading">
        <v-progress-circular :size="50" color="primary" indeterminate></v-progress-circular>
        <span>{{btnLoadingText}}</span>
      </div>

      <div class="loading-overlay" v-if="ResiterError">
        <span style="color:red;font-size:18px;">{{ResiterError}}</span>
      </div>
    </v-card>
  </div>
</template>

<script>
export default {
  data: () => ({
    showPassword: false,
    username: undefined,
    name: undefined,
    email: undefined,
    form: false,
    isBtnLoading: false,
    ResiterError: undefined,
    checkUsername: "",
    checkEmail: "",
    password: undefined,
    repassword: undefined,
    selected_department: undefined,
    selected_position: undefined,
    picked_gender: undefined,
    departments: [],
    positions: [],
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

      if (this.$validator.errors.all().length === 0) {
        this.isBtnLoading = true;
        setTimeout(() => {
          this.isBtnLoading = false;
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
              // 跳转上一请求页面或主页
              console.log(res.data);
              if (res.data === 600) {
                this.checkUsername = "用户已存在";
              }
              if (res.data === 500) {
                this.ResiterError = this.$t("auth.registerError");
                setTimeout(() => {
                  this.ResiterError = false;
                }, 2000);
              }
              if (res.data === 200) {
                this.$router.push(this.$router.currentRoute.query.url || "/");
              }
            })
            .catch(error => {
              console.log(error);
              this.loginError = this.$t("auth.loginError");
              setTimeout(() => {
                this.loginError = false;
              }, 2000);
            });
        }, 2000);
      }
    },
    changeLangEvent(param_lang, param_index) {
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
          console.log(this.departments);
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
    checkUser(){
       this.$axios
        .get("/auth/checkuser", {
          params: {
            username: this.username
          }
        })
        .then(res => {
          if (res.data === 600) {
            this.checkUsername = "用户已存在";
          } else {
            this.checkUsername = "";
          }
        })
        .catch(error => {
          console.log(error);
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
  },
  watch: {
    username: function() {
      // this.checkUsername = ''
      // this.checkUser();
    }
  }
};
</script>

<style lang="css">
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
</style>