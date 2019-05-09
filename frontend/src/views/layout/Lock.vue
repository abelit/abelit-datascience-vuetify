<template>
  <v-container fluid style="height: 100vh" pa-0>
    <v-img :src="require('@/assets/images/auth/login_page_default.jpg')" height="100%" width="100%">
      <v-layout align-center justify-center fill-height >
        <v-flex  xs12 sm6 >
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
            prepend-inner-icon="lock"
            height="3"
            required
          ></v-text-field>
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