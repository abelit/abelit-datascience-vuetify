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
              <v-list-tile-avatar >
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
          v-model="name"
          box
          color="deep-purple"
          :label="$t('auth.name')"
          type="name"
          v-validate="'required|alpha_num|max:20|min:6'"
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
            <v-select v-model="selected_department" :items="items" box :label="$t('auth.department')"  class="df-select"></v-select>
          <!-- </v-flex> -->

          <!-- <v-flex xs12 sm6 d-flex> -->
            <v-icon size="36" color="#efefef" style="float: left;" class="df-icon">assignment_ind</v-icon>
            <v-select v-model="selected_position" :items="items" box :label="$t('auth.position')" class="df-select"></v-select>
          <!-- </v-flex> -->
        </v-layout>
        <v-icon size="36" color="#efefef" class="df-icon" style="float:left">group</v-icon>
          <v-radio-group v-model="picked_gender" :mandatory="false" class="df-radio">
            <v-radio :label="$t('auth.male')" value="male"></v-radio>
            <v-radio :label="$t('auth.female')" value="female"></v-radio>
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
          :loading="isLoading"
          class="white--text title font-weight-regular"
          color="#01074ccf"
          depressed
          @click="submit"
        >{{$t('auth.register')}}</v-btn>
      </v-card-actions>
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
    isLoading: false,
    password: undefined,
    repassword: undefined,
    lang: 'zh_CN',
    langLogo: require("../../assets/images/cn.png"),
    langs: {
      zh: { lang: "zh_CN", name: "简体中文", img: require("../../assets/images/cn.png") },
      en: { lang: "en_US", name: "English", img: require("../../assets/images/us.png") }
    }
  }),
  methods: {
    submit() {
      this.$validator.validateAll();
    },
    changeLangEvent(param_lang,param_index) {
      if (param_lang != null) {
        this.lang = param_lang;
      }
      if (param_index != null) {
        this.langLogo = this.langs[param_index].img;
      }
      this.$i18n.locale = this.lang;
      this.$validator.locale = this.lang;
    }
  }
};
</script>

<style lang="css">
.login-container {
  width: 100%;
  height: 100%;
  background-image: url("../../assets/images/login/login_page_default.jpg");
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