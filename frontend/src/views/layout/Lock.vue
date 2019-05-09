<template>
  <v-container fill-height fluid style="height: 100vh" pa-0>
    <v-img :src="require('@/assets/images/auth/login_page_default.jpg')" height="100%" width="100%">
      <v-layout align-center justify-center fill-height text-xs-center>
        <v-flex xs12 sm6 row wrap>
          <v-text-field
            v-model="password"
            outline
            :label="$t('auth.PASSWORD')"
            :append-icon="passwordDisplay ? 'visibility_off' : 'visibility'"
            :type="passwordDisplay ? 'text' : 'password'"
            @click:append="passwordDisplay = !passwordDisplay"
            v-validate="'required|max:18|min:3'"
            :error-messages="errors.collect('password')"
            data-vv-name="password"
            height="3"
            required
            style="width: 300px"
          ></v-text-field>
          <v-btn-toggle>
            <v-btn color="secondary" flat>
              <v-icon>lock_open</v-icon>
            </v-btn>
            <v-btn color="secondary" flat>
              <v-icon>exit_to_app</v-icon>
            </v-btn>
          </v-btn-toggle>
        </v-flex>
        <v-flex xs12 sm6 class="py-2">
          <p>No Options Selected</p>
          <v-btn-toggle v-model="toggle_none">
            <v-btn flat>
              <v-icon>format_align_left</v-icon>
            </v-btn>
            <v-btn flat>
              <v-icon>format_align_center</v-icon>
            </v-btn>
            <v-btn flat>
              <v-icon>format_align_right</v-icon>
            </v-btn>
            <v-btn flat>
              <v-icon>format_align_justify</v-icon>
            </v-btn>
          </v-btn-toggle>
        </v-flex>
      </v-layout>
    </v-img>
  </v-container>
</template>


<script>
export default {
  data: () => ({
    dialog: false,
    passwordDisplay: false,
    password: undefined
  }),
  methods: {
    async submit() {
      await this.$validator.validateAll();
    }
  }
};
</script>