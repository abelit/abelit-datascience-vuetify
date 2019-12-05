<template>
  <v-container fluid class="pa-0 ma-0">
    <v-img :src="backgroundImage" height="100vh" width="100%">
      <v-row align="center" justify="center" style="height: 100%"  no-getters>
        <v-col cols="8" sm="4">
          <v-form :lazy-validation="lazy" ref="form" v-model="valid">
              <v-text-field
                v-model="password"
                :label="$vuetify.lang.t('$vuetify.form.password')"
                type="password"
                prepend-inner-icon="lock"
                outlined
                required
                dense
                solo
                flat
                :rules="rules($vuetify.lang.t('$vuetify.form.password'),24)"
                :error-messages="errorMessage"
              >
              <template v-slot:append-outer>
                <v-btn-toggle>
                  <v-tooltip bottom>
                    <template v-slot:activator="{ on }">
                      <v-btn @click="handleLogin" height="41" dense v-on="on">
                        <v-icon dark>lock_open</v-icon>
                      </v-btn>
                    </template>
                    <span>{{ $vuetify.lang.t('$vuetify.tooltip.unlock') }}</span>
                  </v-tooltip>

                  <v-tooltip bottom>
                    <template v-slot:activator="{ on }">
                      <v-btn @click="handleLogout" height="41" dense v-on="on">
                        <v-icon dark>exit_to_app</v-icon>
                      </v-btn>
                    </template>
                    <span>{{ $vuetify.lang.t('$vuetify.tooltip.logout') }}</span>
                  </v-tooltip>
                </v-btn-toggle>
                <!-- <v-btn @click="handleLogin" height="40" dense v-on="on">
                        <v-icon dark>lock_open</v-icon>
                      </v-btn> -->
              </template>
              </v-text-field>
                
          </v-form>
        </v-col>
      </v-row>
    </v-img>
  </v-container>
</template>
<!--<template>
  <v-container fluid class="pa-0 ma-0">
    <v-img :src="backgroundImage" height="100vh" width="100%">
      <v-row align="center" justify="center" style="height: 100%" class="px-5">
        <v-col cols="8" sm="4">
          <v-form :lazy-validation="lazy" ref="form" v-model="valid">
            <v-input>
              <v-text-field
                v-model="password"
                :label="$vuetify.lang.t('$vuetify.form.password')"
                type="password"
                prepend-inner-icon="lock"
                outlined
                required
                dense
                solo
                :rules="rules($vuetify.lang.t('$vuetify.form.password'),24)"
                :error-messages="errorMessage"
              ></v-text-field>
              <v-input>
                <v-btn-toggle>
                  <v-tooltip bottom>
                    <template v-slot:activator="{ on }">
                      <v-btn @click="handleLogin" height="40" dense v-on="on">
                        <v-icon dark>lock_open</v-icon>
                      </v-btn>
                    </template>
                    <span>{{ $vuetify.lang.t('$vuetify.tooltip.unlock') }}</span>
                  </v-tooltip>

                  <v-tooltip bottom>
                    <template v-slot:activator="{ on }">
                      <v-btn @click="handleLogout" height="40" dense v-on="on">
                        <v-icon dark>exit_to_app</v-icon>
                      </v-btn>
                    </template>
                    <span>{{ $vuetify.lang.t('$vuetify.tooltip.logout') }}</span>
                  </v-tooltip>
                </v-btn-toggle>
              </v-input>
            </v-input>
          </v-form>
        </v-col>
      </v-row>
    </v-img>
  </v-container>
</template>-->


<!-- <template>
  <v-container fluid class="pa-0 ma-0">
    <v-img :src="backgroundImage" height="100vh" width="100%">
      <v-row align="center" justify="center" style="height: 100%" class="px-5">
        <v-col cols="12" sm="6">
          <v-form :lazy-validation="lazy" ref="form" v-model="valid">
            <v-row no-gutters justify="center">
              <v-col cols="8" sm="4" class="pl-4">
                <v-text-field
                  v-model="password"
                  :label="$vuetify.lang.t('$vuetify.form.password')"
                  type="password"
                  prepend-inner-icon="lock"
                  outlined
                  required
                  dense
                  solo
                  :rules="rules($vuetify.lang.t('$vuetify.form.password'),24)"
                  :error-messages="errorMessage"
                ></v-text-field>
              </v-col>
              <v-col :cols="$vuetify.breakpoint.xsOnly?4:4" sm="2">
                <v-btn-toggle>
                  <v-tooltip bottom>
                    <template v-slot:activator="{ on }">
                      <v-btn @click="handleLogin" height="40" dense v-on="on">
                        <v-icon dark>lock_open</v-icon>
                      </v-btn>
                    </template>
                    <span>{{ $vuetify.lang.t('$vuetify.tooltip.unlock') }}</span>
                  </v-tooltip>

                  <v-tooltip bottom>
                    <template v-slot:activator="{ on }">
                      <v-btn @click="handleLogout" height="40" dense v-on="on">
                        <v-icon dark>exit_to_app</v-icon>
                      </v-btn>
                    </template>
                    <span>{{ $vuetify.lang.t('$vuetify.tooltip.logout') }}</span>
                  </v-tooltip>
                </v-btn-toggle>
              </v-col>
            </v-row>
          </v-form>
        </v-col>
      </v-row>
    </v-img>
  </v-container>
</template> -->


<script>
import { mapState } from "vuex";

export default {
  data: () => ({
    password: null,
    errorMessage: null,
    lazy: false,
    valid: true,
    backgroundImage: require("@/assets/images/auth/lock_page.png")
  }),
  methods: {
    async handleLogin() {
      await this.$refs.form.validate();
      if (this.$refs.form.validate()) {
        if (this.$md5(this.password) !== this.lockPassword) {
          // this.password = ''
          this.errorMessage = this.$vuetify.lang.t(
            "$vuetify.form.errorPassword"
          );
          setTimeout(() => {
            this.errorMessage = null;
          }, 1000);
          return;
        }
        setTimeout(() => {
          // 清除lockPassword
          this.$store.commit("setLockPassword", "");
          this.$router.push(this.$router.currentRoute.query.url || "/");
        }, 1000);
      }
    },
    handleLogout() {
      // Vuex通过dispatch实现异步，实际执行的是actions中的方法
      this.$store.dispatch("logout").then(() => {
        this.$store.commit("setLockPassword", "");
        // 跳转到指定页面
        this.$router.push({ path: "/" });
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
    ...mapState(["lockPassword"])
  }
};
</script>


<style lang="scss">
 .v-input__append-outer {
    margin: 0 !important
  }
</style>