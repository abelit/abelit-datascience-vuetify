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
      <v-card-title
        class="primary"
        primary-title
      >{{ $vuetify.lang.t("$vuetify.tooltip.lockPassword") }}</v-card-title>
      <v-card-text>
        <v-form :lazy-validation="lazy" ref="form" v-model="valid">
          <v-container>
            <v-row>
              <v-col cols="12" sm="12">
                <v-text-field
                  v-model="title"
                  :rules="rules('title',20)"
                  :label="$vuetify.lang.t('$vuetify.form.password')"
                  :append-icon="passwordVisable ? 'visibility' : 'visibility_off'"
                  @click:append="passwordVisable = !passwordVisable"
                  :type="passwordVisable ? 'text' : 'password'"
                  prepend-inner-icon="lock"
                  outlined
                  required
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
          <small>*{{ $vuetify.lang.t('$vuetify.form.indicatesRequiredField') }}</small>
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
    passwordVisable: false,
    password: undefined
  }),
  methods: {
    async handLock() {
      await this.$refs.form.validate();
      if (this.$refs.form.validate()) {
        this.$store.commit("SET_LOCK_PASSWORD", this.password);
        this.$store.commit("SET_LOCK", true);
        setTimeout(() => {
          this.$router.push({ path: "/lock" });
        }, 100);
      }
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
    },
    resetValidation () {
      this.$refs.form.resetValidation();
    },
    reset () {
      this.$refs.form.reset()
    },
  },
  computed: {
    ...mapState(["toolbarColor"])
  },
  watch: {
    // 如果dialog发生变化且dialog为false，就重置表单验证
    dialog: function () {
      if (!this.dialog) {
        this.resetValidation();
        this.reset();
      }
    }
  }
};
</script>