<template>
  <v-app id="inspire">
    <v-content>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="4">
            <v-row class="mb-6 title">
              <v-col align="center">
                <v-img
                  :src="require('@/assets/images/logo/data_science.svg')"
                  width="60"
                  height="70"
                  class="mb-6"
                ></v-img>
                <span>Sign in to Data Analysis</span>
              </v-col>
            </v-row>
            <v-card class="elevation-3" outlined>
              <v-toolbar color="primary" flat>
                <v-toolbar-title>User Login</v-toolbar-title>
                <v-spacer />
              </v-toolbar>
              <v-card-text>
                <v-form class="pt-5">
                  <v-text-field
                    label="Login"
                    name="login"
                    prepend-inner-icon="person"
                    type="text"
                    outlined
                    dense
                  />

                  <v-text-field
                    id="password"
                    label="Password"
                    name="password"
                    prepend-inner-icon="lock"
                    type="password"
                    outlined
                    dense
                  />
                </v-form>
              </v-card-text>
              <v-card-actions class="px-4 pb-6">
                <router-link to="/">
                  <span>
                  Forget Password?
                </span>
                </router-link>
                <v-spacer />
                <v-btn color="primary">Login</v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {
  props: {
    source: String
  }
};
</script>