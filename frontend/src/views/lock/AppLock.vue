<template>
  <v-container fluid class="pa-0 ma-0">
    <v-img :src="backgroundImage" height="100vh" width="100%">
      <v-row align="center" justify="center" style="height: 100%" class="px-5">
        <v-col cols="12" sm="6">
          <v-form :lazy-validation="lazy" ref="form" v-model="valid">
            <v-row no-gutters justify="center" >
              <v-col cols="8"  sm="4" class="pl-4">
                <v-text-field
                  v-model="password"
                  :label="$vuetify.lang.t('$vuetify.form.password')"
                  prepend-inner-icon="lock"
                  outlined
                  required
                  dense
                  solo
                  :rules="rules($vuetify.lang.t('$vuetify.form.password'),12)"
                ></v-text-field>
              </v-col>
              <v-col :cols="$vuetify.breakpoint.xsOnly?4:4" sm="2">
                <v-btn-toggle mandatory multiple v-model="value">
                  <v-tooltip bottom>
                    <template v-slot:activator="{ on }">
                      <v-btn @click="handleLogin" height="40" dense v-on="on">
                        <v-icon dark>lock_open</v-icon>
                      </v-btn>
                    </template>
                    <span>lock open</span>
                  </v-tooltip>

                  <v-tooltip bottom>
                    <template v-slot:activator="{ on }">
                      <v-btn @click="handleLogin" height="40" dense v-on="on">
                        <v-icon dark>exit_to_app</v-icon>
                      </v-btn>
                    </template>
                    <span>exit app</span>
                  </v-tooltip>
                </v-btn-toggle>
              </v-col>
            </v-row>
          </v-form>
        </v-col>
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
      await this.$refs.form.validate();
      if (his.$refs.form.validate()) {
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
    },
    rules(filed, length) {
      return [
        v => !!v || filed + this.$vuetify.lang.t("$vuetify.rules.isRequired"),
        v =>
          (v && v.length <= length) ||
          this.$vuetify.lang.t("$vuetify.rules.max") +
            length +
            this.$vuetify.lang.t("$vuetify.rules.character")
      ];
    }
  },
  computed: {
    ...mapState(["toolbarColor", "lockPassword"])
  }
};
</script>