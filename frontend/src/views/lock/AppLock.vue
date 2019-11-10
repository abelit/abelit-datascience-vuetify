<template>
  <v-container fluid class="pa-0 ma-0">
    <v-img :src="backgroundImage" height="100vh" width="100%">
      <v-row :align="alignment" :justify="justify" style="height: 100%">
        <v-col :cols="$vuetify.breakpoint.mdAndUp?4:6">
          <v-form :lazy-validation="lazy" ref="form" v-model="valid">
            <v-row  :justify="justify">
              <v-col cols="9" class="pr-0">
                <v-text-field
                  v-model="password"
                  :label="$vuetify.lang.t('$vuetify.form.password')"
                  prepend-inner-icon="lock"
                  outlined
                  required
                  dense
                  solo
                ></v-text-field>
                
              </v-col>
              <v-col cols="3" class="pl-0">
                <v-card width="64">
                  <v-btn flat @click="handleLogin" height="40" dense>
                  <v-icon dark>lock_open</v-icon>
                </v-btn>
                </v-card>
              </v-col>
            </v-row>
          </v-form>
        </v-col>
        <!-- <v-col cols="1" class="pl-0">
         <v-btn flat @click="handleLogin" width="36">
                  <v-icon dark>lock_open</v-icon>
                </v-btn>
        </v-col>-->
      </v-row>
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
    backgroundImage: require("@/assets/images/auth/lock_page.png"),
    alignment: "center",
    justify: "center"
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