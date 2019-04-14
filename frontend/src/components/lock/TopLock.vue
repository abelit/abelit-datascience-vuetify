<template>
  <v-dialog v-model="dialog" max-width="500px">
    <template v-slot:activator="{ on }">
      <v-btn icon dark v-on="on">
        <v-icon>lock</v-icon>
      </v-btn>
    </template>
    <v-card>
      <v-card-title
        style="padding: 10px 5px 10px 20px;"
        class="headline lighten-2"
        color="blue-grey darken-2"
        primary-title
      >
        <span>{{ $t("admin.SCREEN_LOCK_PASSWORD_SET") }}</span>
        <v-spacer></v-spacer>
        <v-btn icon dark @click="dialog = false">
          <v-icon color="dark">close</v-icon>
        </v-btn>
      </v-card-title>

      <v-text-field
        v-model="password"
        style="margin: 25px 20px 25px 20px"
        outline
        :label="$t('auth.PASSWORD')"
        :append-icon="passwordShow ? 'visibility_off' : 'visibility'"
        :type="passwordShow ? 'text' : 'password'"
        @click:append="passwordShow = !passwordShow"
        v-validate="'required|max:18|min:3'"
        :error-messages="errors.collect('password') + groupMessage"
        data-vv-name="password"
        prepend-inner-icon="lock"
        height="3"
        required
      ></v-text-field>
      <v-divider></v-divider>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          style="margin-right: 13px;"
          color="primary"
          @click="dialog = false"
        >{{$t("button.CONFIRM") }}</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>



<script>
export default {
  data: () => ({
    dialog: false,
    passwordShow: false,
    password: undefined
  })
};
</script>