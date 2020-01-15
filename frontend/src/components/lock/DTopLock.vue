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
      <v-card-text class="pb-0">
        <v-form :lazy-validation="lazy" ref="form" v-model="valid">
          <v-container>
            <v-row>
              <v-col cols="12" sm="12">
                <v-text-field
                  v-model="password"
                  :rules="rules('password',20)"
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
      <v-card-actions class="mx-6">
        <v-spacer></v-spacer>
        <v-btn class="primary" @click="dialog=false">
          <span>{{ $vuetify.lang.t("$vuetify.button.cancel") }}</span>
        </v-btn>
        <v-btn class="primary" @click="handLock">
          <span>{{ $vuetify.lang.t("$vuetify.button.confirm") }}</span>
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
    password: null,
    lazy: false,
    valid: true
  }),
  methods: {
    async handLock() {
      await this.$refs.form.validate();
      if (this.$refs.form.validate()) {
        // 使用md5加密密码
        this.password = this.$md5(this.password);
        // Vuex同步方式，实际调用的是mutations中的方法
        this.$store.commit("setLockPassword", this.password);
        console.log("dtoplock: " + this.password);
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
    resetValidation() {
      this.$refs.form.resetValidation();
    },
    reset() {
      this.$refs.form.reset();
    }
  },
  watch: {
    // 如果dialog发生变化且dialog为false，就重置表单验证
    dialog: function() {
      if (!this.dialog) {
        this.resetValidation();
        this.reset();
      }
    }
  }
};
</script>