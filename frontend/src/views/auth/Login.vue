<template>
  <div class="login-container container-fluid">
    <v-card class="mx-auto" style="max-width: 500px; margin-top:15%;" color="#eaeaeaa1">
      <v-toolbar color="#01074ccf !important" cards dark flat>
        <v-icon size="36" color="#efefef">account_box</v-icon>
        <v-card-title
          class="title font-weight-regular"
          style="margin: 0 auto;"
        >{{$t('auth.loginPage')}}</v-card-title>
        <v-menu offset-y>
          <template v-slot:activator="{ on }">
            <v-btn color="transparent" v-on="on" flat>
              <img :src="require('@/assets/images/auth/'+langLogo)" alt>
            </v-btn>
          </template>
          <v-list>
            <v-list-tile v-for="(lang, index) in langs" :key="index">
              <v-list-tile-avatar>
                <v-avatar size="32px" tile @click="changeLangEvent(lang.lang,index)">
                  <!-- <img :src="lang.img"> -->
                  <img :src="require('@/assets/images/auth/'+lang.img)" alt="lang">
                </v-avatar>
              </v-list-tile-avatar>
              <v-list-tile-title @click="changeLangEvent(lang.lang)">{{ lang.name }}</v-list-tile-title>
            </v-list-tile>
          </v-list>
        </v-menu>
      </v-toolbar>
      <v-form ref="form" v-model="form" class="pa-3 pt-4" :disabled="!form">
        <v-icon size="36" color="#efefef" style="float: left;" class="df-icon">person</v-icon>
        <v-text-field
          v-model="name"
          box
          color="deep-purple"
          :label="$t('auth.email')+'/'+$t('auth.name') "
          type="name"
          v-validate="'required'"
          :error-messages="errors.collect('name')"
          data-vv-name="name"
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
          v-validate="'required|max:18|min:3'"
          :error-messages="errors.collect('password')"
          data-vv-name="password"
          required
        ></v-text-field>
      </v-form>
      <v-divider></v-divider>

      <v-card-actions>
        <v-btn flat class="title font-weight-regular">
          <router-link to="/user/register">{{$t('auth.register')}}?</router-link>
        </v-btn>
        <v-spacer></v-spacer>
        <v-spacer></v-spacer>
        <v-btn
          class="white--text title font-weight-regular"
          color="#01074ccf"
          depressed
          @click="submit"
        >{{$t('auth.login')}}</v-btn>
      </v-card-actions>
      <div class="loading-overlay" v-if="isBtnLoading">
        <v-progress-circular :size="50" color="primary" indeterminate></v-progress-circular>
        <span>{{btnLoadingText}}</span>
      </div>

      <div class="loading-overlay" v-if="loginError">
        <span style="color:red;font-size:18px;">{{loginError}}</span>
      </div>
    </v-card>
  </div>
</template>

<script>
export default {
  data: () => ({
    showPassword: false,
    name: undefined,
    email: undefined,
    form: false,
    isBtnLoading: false,
    password: undefined,
    lang: "zh_CN",
    langLogo: 'cn.png',
    langs: {
      zh: {
        lang: "zh_CN",
        name: "简体中文",
        img: 'cn.png',
      },
      en: {
        lang: "en_US",
        name: "English",
        img: "us.png",
      }
    },
    loginError: ''
  }),
  methods: {
    async submit() {
      // 等待完成表单输入验证后，然后显示登陆加载动画，这里在需要使用async与await关键字
      await this.$validator.validateAll();
      if (this.$validator.errors.all().length === 0) {
        this.isBtnLoading = true;
        setTimeout(() => {
          this.isBtnLoading = false;
          this.$axios
          .post("/login", {
            name: this.name,
            password: this.password
          })
          .then(res => {
            // 存储token信息
            this.$store.commit("setToken", res.data);
            console.log(res.data);
            console.log(this.$store.state.token);
            // if (this.$router.currentRoute.query.url) {
            //   this.$router.push(this.$router.currentRoute.query.url);
            // } else {
            //   this.$router.push('/');
            // }
            // 跳转上一请求页面或主页
            this.$router.push(this.$router.currentRoute.query.url || '/');
          })
          .catch(error => {
            // eslint-disable-next-line
            console.error(error.data);
            this.loginError = this.$t('auth.loginError');
            setTimeout(() => {
              this.loginError = false;
            }, 2000);
          });
        }, 2000);
        
      }
    },
    clear() {
      this.name = "";
      this.email = "";
      this.select = null;
      this.checkbox = null;
      this.$validator.reset();
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
    }
  },
  computed: {
    // function to add loading text form submit button
    btnLoadingText() {
      if (this.isBtnLoading) {
        return this.$t("auth.loginLoadingText");
      } else {
        return "";
      }
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
}
.df-input {
  padding: 10px;
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
</style>