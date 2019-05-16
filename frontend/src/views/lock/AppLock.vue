<template>
  <v-container fluid style="height: 100vh" pa-0 align-center align-content-center>
    <v-img :src="backgroundImage" height="100%" width="100%">
      <v-layout justify-center row style="padding-top: 40vh">
        <v-flex xs6 sm3 md2 lg-2>
          <!-- <h4 class="pb-1">{{ $t("content.SCREEN_PASSWORD") }}</h4>   -->
          <v-text-field
            solo
            v-model="password"
            :label="$t('auth.PASSWORD')"
            type="password"
            v-validate="'required|max:18|min:3'"
            :error-messages="errors.collect('password') + message"
            data-vv-name="password"
            required
            @keyup.enter.native="handleLogin"
          ></v-text-field>
        </v-flex>
        <v-flex xs3 sm1 md1 lg-1>
          <v-btn-toggle
            v-model="toggle_exclusive"
            :class="toolbarColor"
            dark
            style="height: 49px;"
            class="pt-2 mr-0 pr-0"
          >
            <v-tooltip bottom>
              <template  v-slot:activator="{ on }">
                <v-btn depressed flat @click="handleLogin" class="mx-1" v-on="on">
                  <v-icon dark>lock_open</v-icon>
                </v-btn>
              </template>
              <span>{{ $t("button.LOGIN") }}</span>
            </v-tooltip>
            <v-tooltip bottom>
              <template  v-slot:activator="{ on }">
                <v-btn depressed flat @click="handleLogout" class="mx-1" v-on="on">
                  <v-icon dark>exit_to_app</v-icon>
                </v-btn>
              </template>
              <span>{{ $t("button.EXIT") }}</span>
            </v-tooltip>
          </v-btn-toggle>
        </v-flex>
      </v-layout>
    </v-img>
  </v-container>
</template>


<script>
import { mapState } from "vuex";
export default {
  data: () => ({
    password: undefined,
    toggle_exclusive: 2,
    message: "",
    backgroundImage: require("@/assets/images/auth/LockBackground.png")
  }),
  methods: {
    async handleLogin() {
      // console.log(this.$validator.errors.all());
      await this.$validator.validateAll();
      if (this.$validator.errors.all().length === 0) {
        if (this.password !== this.lockPassword) {
          // this.password = ''
          this.message = this.$t("message.ERROR_UNLOCK");
          setTimeout(() => {
            this.message = "";
          }, 1000);
          return;
        }
        setTimeout(() => {
          this.$store.commit("CLEAR_LOCK");
          this.$router.push(
            this.$router.currentRoute.query.url || "/dashboard"
          );
        }, 1000);
      }
    },
    handleLogout() {
      this.$store.dispatch("logOut").then(() => {
        this.$router.push({ path: "/user/login" });
      });
    }
  },
  computed: {
    ...mapState(["toolbarColor", "lockPassword"])
  }
};
</script>