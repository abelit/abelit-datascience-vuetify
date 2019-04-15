<template>
  <v-dialog v-model="dialog" max-width="500px">
    <template v-slot:activator="{ on }">
      <v-btn icon dark v-on="on">
        <v-icon>lock</v-icon>
      </v-btn>
    </template>
    <v-toolbar color="indigo" dark>
      <v-toolbar-title>{{ $t("admin.SCREEN_LOCK_PASSWORD_SET") }}</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-btn icon dark @click="dialog = false">
        <v-icon>close</v-icon>
      </v-btn>
    </v-toolbar>
    <v-card>
      <v-card-title class="headline lighten-2" color="blue-grey darken-2" primary-title></v-card-title>
      <v-card-text>
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
      </v-card-text>

      <!-- <v-divider></v-divider> -->
      <v-card-actions>
        <v-spacer></v-spacer>
        <div class="pr-2">
          <v-btn color="indigo" @click="submit" dark>
            <span>{{$t("button.CONFIRM") }}</span>
          </v-btn>
        </div>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>


<script>
export default {
  name: "dfTopLock",
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