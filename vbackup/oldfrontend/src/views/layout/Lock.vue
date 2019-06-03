<template>
  <v-container fill-height fluid style="height: 100vh" pa-0 align-center align-content-center>
    <v-img :src="backgroundImage" height="100%" width="100%">
      <v-layout align-center justify-center fill-height row wrap>
        <div style="max-width: 300px;">
          <div class="pb-2">
            <h4>锁屏密码</h4>
          </div>
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
            class="float: left"
          ></v-text-field>
          <v-btn-toggle v-model="toggle_exclusive" class="d-icon-group" :class="toolbarColor" dark>
            <v-btn depressed flat @click="handleLogin" >
              <v-icon dark>lock_open</v-icon>
            </v-btn>
            <v-btn depressed flat @click="handleLogout">
              <v-icon dark>exit_to_app</v-icon>
            </v-btn>
          </v-btn-toggle>
        </div>
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
    backgroundImage: require('@/assets/images/auth/LockBackground.png')
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
          this.passwdError = false
        }, 1000)
        return
      }      setTimeout(() => {
        this.$store.commit('CLEAR_LOCK')
        this.$router.push(this.$router.currentRoute.query.url || "/dashboard")
      }, 1000)
      }
    },
    handleLogout() {
        this.$store.dispatch('logOut').then(() => {
          this.$router.push({ path: '/user/login' })
        })
    },
  },
  computed: {
    ...mapState(["toolbarColor", "lockPassword"])
  }
};
</script>


<style lang="scss" scoped>
.d-icon-group {
  padding: 6px;
}
</style>
