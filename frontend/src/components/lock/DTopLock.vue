<template>
  <v-dialog v-model="dialog" max-width="500">
    <template v-slot:activator="{ on: dialog }">
      <v-tooltip bottom>
        <template v-slot:activator="{ on: tooltip }">
          <v-btn icon v-on="{...tooltip, ...dialog}">
            <v-icon>lock</v-icon>
          </v-btn>
        </template>
        <span>{{ $vuetify.lang.t("$vuetify.tooltip.lockPassword") }}</span>
      </v-tooltip>
    </template>
    <v-card>
      <v-card-title class="primary" primary-title>
        {{ $vuetify.lang.t("$vuetify.tooltip.lockPassword") }}
      </v-card-title>
      <v-card-text>
        <v-form>
          <v-container>
            <v-row>
              <v-col cols="12" sm="12">
                <v-text-field v-model="title" :rules="rules" counter="25" :label="$vuetify.lang.t('$vuetify.form.password')" outlined></v-text-field>
              </v-col>
            </v-row>
          </v-container>
           <small>*indicates required field</small>
        </v-form>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="primary" @click="dialog=false">
          <span class="font-weight-bold">{{ $vuetify.lang.t("$vuetify.button.cancel") }}</span>
        </v-btn>
        <v-btn color="primary" @click="handLock">
          <span class="font-weight-bold">{{ $vuetify.lang.t("$vuetify.button.confirm") }}</span>
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>


<script>
import { mapState } from "vuex";
export default {
  data: () => ({
    dialog: false,
    passwordDisplay: false,
    password: undefined,
     rules: [v => v.length <= 25 || 'Max 25 characters'],
  }),
  methods: {
    async handLock() {
      await this.$validator.validateAll();
      if (this.$validator.errors.all().length === 0) {
        this.$store.commit("SET_LOCK_PASSWORD", this.password);
        this.$store.commit("SET_LOCK", true);
        setTimeout(() => {
          this.$router.push({ path: "/lock" });
        }, 100);
      }
    }
  },
  computed: {
    ...mapState(["toolbarColor"])
  }
};
</script>