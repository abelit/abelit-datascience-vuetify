<template>
  <div class="login-container container-fluid">
    <v-card class="mx-auto" style="max-width: 500px; margin-top:15%;" color="#eaeaeaa1">
      <v-toolbar color="#01074ccf !important" cards dark flat>
        <v-card-title
          class="title font-weight-regular"
          style="margin: 0 auto;"
        >{{$t('admin.GROUP_ADD')}}</v-card-title>
      </v-toolbar>
      <v-form ref="form" v-model="form" class="pa-3 pt-4" :disabled="!form">
        <v-text-field
          v-model="name"
          box
          color="deep-purple"
          :label="$t('admin.GROUP_CNNAME')"
          type="name"
          v-validate="'required'"
          :error-messages="errors.collect('name') + groupMessage"
          data-vv-name="name"
          required
          class="df-input"
        ></v-text-field>

        <v-text-field
          v-model="enname"
          box
          color="deep-purple"
          :label="$t('admin.GROUP_ENNAME')"
          type="enname"
          v-validate="'required'"
          :error-messages="errors.collect('enname')"
          data-vv-name="enname"
          required
          class="df-input"
          @focus="checkGroup"
          @blur="checkGroup"
        ></v-text-field>

        <v-textarea
          v-model="description"
          auto-grow
          box
          color="deep-purple"
          :label="$t('admin.GROUP_DESCRIPTION')"
          rows="5"
        ></v-textarea>

        <v-checkbox
          v-model="status"
          value="1"
          :label="$t('button.ENABLE')"
          data-vv-name="status"
          type="checkbox"
        ></v-checkbox>
      </v-form>
      <v-divider></v-divider>

      <v-card-actions>
        <v-btn flat class="title font-weight-regular">{{$t('button.CLOSE')}}</v-btn>
        <v-spacer></v-spacer>
        <v-spacer></v-spacer>
        <v-btn
          class="title font-weight-regular"
          color="#01074ccf"
          depressed
          @click="submit"
        >{{$t('button.ADD')}}</v-btn>
      </v-card-actions>
      <div class="loading-overlay" v-if="isButtonLoading">
        <v-progress-circular :size="50" color="primary" indeterminate></v-progress-circular>
        <span v-if="loadingMessage">{{loadingMessage}}</span>
      </div>

      <div class="loading-overlay" v-if="message">
        <span v-bind:class="[isActive?'activeClass':'errorClass']">{{message}}</span>
      </div>
    </v-card>
  </div>
</template>

<script>
export default {
  data: () => ({
    name: undefined,
    enname: undefined,
    status: 0,
    description: undefined,
    form: false,
    isButtonLoading: false,
    loadingMessage: "",
    groupMessage: "",
    message: "",
    isActive: false
  }),
  methods: {
    // 等待完成表单输入验证后，然后显示登陆加载动画，这里在需要使用async与await关键字
    async submit() {
      await this.$validator.validateAll();
      if (this.$validator.errors.all().length === 0) {
        this.isButtonLoading = true;
        this.loadingMessage = this.$t("message.LOADING");
        setTimeout(() => {
          this.isButtonLoading = false;
          this.$axios
            .post("/admin/group/add", {
              name: this.name,
              enname: this.enname,
              status: this.status,
              description: this.description
            })
            .then(res => {
              this.isActive = true;
              this.message = this.$t("message.SUCCESS_ADD");
              setTimeout(() => {
                this.message = "";
              }, 2000);
            })
            .catch(error => {
              console.log(error);
              this.isActive = false;
              this.message = this.$t("message.ERROR_ADD");
              setTimeout(() => {
                this.message = "";
              }, 2000);
            });
        }, 2000);
      }
    },
    checkGroup() {
      this.$axios
        .get("/api/checkgroup", {
          params: {
            name: this.name
          }
        })
        .then(res => {
          this.groupMessage = "";
        })
        .catch(error => {
          this.groupMessage = this.$t("api.GROUP_EXIST");
        });
    }
  }
};
</script>

<style lang="css">
.login-container {
  width: 100%;
  height: 100%;
  background-repeat: no-repeat;
  background-size: 100% 100%;
  -moz-background-size: 100% 100%;
}
.df-icon {
  position: relative;
  padding: 10px;
  background: #01074ccf;
  min-width: 50px;
  text-align: center;
}
.df-input {
  padding: 10px;
}
.loading-overlay {
  z-index: 10;
  top: 0;
  left: 0;
  right: 0;
  position: absolute;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.9);
  display: flex;
  align-items: center;
  justify-content: center;
}
.activeClass {
  color: green;
  font-size: 18px;
}
.errorClass {
  color: red;
  font-size: 18px;
}
</style>