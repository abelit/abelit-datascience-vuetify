<template>
  <div class="login-container container-fluid">
    <v-card class="mx-auto" style="max-width: 500px; margin-top:15%;" color="#eaeaeaa1">
      <v-toolbar color="#01074ccf !important" cards dark flat>
        <v-card-title
          class="title font-weight-regular"
          style="margin: 0 auto;"
        >{{$t('admin.addPositionPage')}}</v-card-title>
      </v-toolbar>
      <v-form ref="form" v-model="form" class="pa-3 pt-4" :disabled="!form">
        <v-text-field
          v-model="name"
          box
          color="deep-purple"
          :label="$t('admin.positionCNName')"
          type="name"
          v-validate="'required'"
          :error-messages="errors.collect('name')"
          data-vv-name="name"
          required
          class="df-input"
        ></v-text-field>

      <v-text-field
          v-model="enname"
          box
          color="deep-purple"
          :label="$t('admin.positionENName')"
          type="enname"
          v-validate="'required'"
          :error-messages="errors.collect('enname')"
          data-vv-name="enname"
          required
          class="df-input"
        ></v-text-field>

       <v-textarea
        v-model="description"
        auto-grow
        box
        color="deep-purple"
        :label="$t('admin.positionDescription')"
        rows="5"
      ></v-textarea>

        <v-checkbox
          v-model="status"
          value="1"
          :label="$t('admin.enableName')"
          data-vv-name="status"
          type="checkbox"
        ></v-checkbox>
      </v-form>
      <v-divider></v-divider>

      <v-card-actions>
        <v-btn flat class="title font-weight-regular">
          <router-link to="/user/register">{{$t('button.closeButton')}}?</router-link>
        </v-btn>
        <v-spacer></v-spacer>
        <v-spacer></v-spacer>
        <v-btn
          class="title font-weight-regular"
          color="#01074ccf"
          depressed
          @click="submit"
        >{{$t('button.addButton')}}</v-btn>
      </v-card-actions>
      <div class="loading-overlay" v-if="isBtnLoading">
        <v-progress-circular :size="50" color="primary" indeterminate></v-progress-circular>
        <span>{{btnLoadingText}}</span>
      </div>

      <div class="loading-overlay" v-if="loginError">
        <span style="color:red;font-size:18px;">{{loginError}}</span>
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
    isBtnLoading: false
  }),
  methods: {
    // 等待完成表单输入验证后，然后显示登陆加载动画，这里在需要使用async与await关键字
    async submit() {
      await this.$validator.validateAll();
      if (this.$validator.errors.all().length === 0) {
        this.isBtnLoading = true;
        setTimeout(() => {
          this.isBtnLoading = false;
          this.$axios
            .post("/admin/position/add", {
              name: this.name,
              enname: this.enname,
              status: this.status,
              description: this.description

            })
            .then(res => {
              // console.log(res.data);
              if (res.data === 500) {
                this.loginError = this.$t("auth.loginError500");
                setTimeout(() => {
                  this.loginError = false;
                }, 2000);
                return;
              }

              // 跳转上一请求页面或主页
              // this.$router.push(this.$router.currentRoute.query.url || "/");
            })
            .catch(error => {
              console.log(error);
              this.loginError = this.$t("auth.loginError");
              setTimeout(() => {
                this.loginError = false;
              }, 2000);
            });
        }, 2000);
      }
    },
    // 清除输入款内容和错误提示信息
    clear() {
      this.name = "";
      this.email = "";
      this.select = null;
      this.checkbox = null;
      this.$validator.reset();
    }
  },
  computed: {
    // function to add loading text form submit button 登录加载时显示信息
    btnLoadingText() {
      if (this.isBtnLoading) {
        return this.$t("auth.loginLoadingText");
      } else {
        return "";
      }
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
</style>