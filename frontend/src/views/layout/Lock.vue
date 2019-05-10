<template>
  <v-container fill-height fluid style="height: 100vh" pa-0 align-center align-content-center>
    <v-img :src="require('@/assets/images/auth/lockLogin.png')" height="100%" width="100%">
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
            :error-messages="errors.collect('password')"
            data-vv-name="password"
            required
            @keyup.enter.native="handleLogin"
            class="float: left"
          ></v-text-field>
          <v-btn-toggle v-model="toggle_exclusive" class="d-icon-group" :class="btncolor" dark>
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
    toggle_exclusive: 2
  }),
  methods: {
     async handleLogin() {
      console.log(this.password);
      console.log(this.lockPassword);
      await this.$validator.validateAll();
      if (this.password !== this.lockPassword) {
        this.password = ''
        this.$message({
          message: '解锁密码错误,请重新输入',
          type: 'error'
        })
        this.passwdError = true
        setTimeout(() => {
          this.passwdError = false
        }, 1000)
        return
      }
      this.pass = true
      setTimeout(() => {
        this.$store.commit('CLEAR_LOCK')
        this.$router.push('/dashboard')
      }, 1000)
    },
    handleLogout() {
      this.$confirm('是否退出系统, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$store.dispatch('LogOut').then(() => {
          this.$router.push({ path: '/login' })
        })
      }).catch(() => {
        return false
      })
    },
  },
  computed: {
    ...mapState(["btncolor", "lockPassword"])
  }
};
</script>


<style lang="scss" scoped>
.d-icon-group {
  padding: 6px;
}
</style>
