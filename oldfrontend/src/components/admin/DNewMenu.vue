<template>
  <v-dialog v-model="dialog" max-width="500">
    <template v-slot:activator="{ on }">
      <div v-on="on">
        <v-tooltip bottom>
          <template v-slot:activator="{ on }">
            <v-btn color="primary" dark class="mb-2" v-on="on" icon flat>
                <v-icon>playlist_add</v-icon>
            </v-btn>
          </template>
          <span>{{ $t("admin.newMenu") }}</span>
        </v-tooltip>
      </div>
    </template>
    <v-flex xs-12 sm-6 md-4 lg-1>
      <v-toolbar dark color="primary">
        <v-toolbar-title>{{ $t("admin.newMenu") }}</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn icon dark @click="dialog = false">
          <v-icon>close</v-icon>
        </v-btn>
      </v-toolbar>
      <v-card class="px-3">
        <v-card-title class="headline lighten-2" color="blue-grey darken-2" primary-title></v-card-title>
        <v-card-text class="pa-0">
          <v-form class="pa-3">
            <v-layout row wrap align-center>
              <v-flex xs12 sm6>
                <v-text-field
                  v-model.trim="name"
                  prepend-inner-icon="menu"
                  color="deep-purple"
                  :label="$t('admin.name')"
                  type="name"
                  v-validate="'required|max:20|min:2'"
                  :error-messages="errors.collect('name')"
                  data-vv-name="name"
                  required
                  class="mx-1"
                ></v-text-field>
              </v-flex>
              <v-flex xs12 sm6>
                <v-text-field
                  v-model.trim="enname"
                  prepend-inner-icon="menu"
                  color="deep-purple"
                  :label="$t('admin.ENNAME')"
                  type="name"
                  v-validate="'required|max:20|min:2'"
                  :error-messages="errors.collect('enname')"
                  data-vv-name="enname"
                  required
                  class="mx-1"
                ></v-text-field>
              </v-flex>
            </v-layout>
            <v-layout row wrap align-center>
              <v-flex xs12 sm6>
                  <v-select
                  prepend-inner-icon="menu"
                  v-model="selected_pmenu"
                  v-validate="'required'"
                  :items="pmenus"
                  item-text="name"
                  item-value="id"
                  :label="$t('admin.parentMenu')"
                  class="mx-1"
                  data-vv-name="pmenu"
                ></v-select>
              </v-flex>
              <v-flex xs12 sm6>
                <v-text-field
                  v-model.trim="url"
                  prepend-inner-icon="http"
                  color="deep-purple"
                  :label="$t('admin.url')"
                  type="name"
                  v-validate="'required|max:20|min:2'"
                  :error-messages="errors.collect('url')"
                  data-vv-name="url"
                  required
                  class="mx-1"
                ></v-text-field>
              </v-flex>
            </v-layout>
           <v-layout row wrap align-center>
              <v-flex xs12 sm6>
                <v-text-field
                  v-model.trim="component"
                  prepend-inner-icon="extension"
                  color="deep-purple"
                  :label="$t('admin.component')"
                  type="name"
                  v-validate="'required|max:20|min:2'"
                  :error-messages="errors.collect('component')"
                  data-vv-name="component"
                  required
                  class="mx-1"
                ></v-text-field>
              </v-flex>
              <v-flex xs12 sm6>
                <v-text-field
                  v-model.trim="icon"
                  prepend-inner-icon="widgets"
                  color="deep-purple"
                  :label="$t('admin.icon')"
                  type="name"
                  v-validate="'required|max:20|min:2'"
                  :error-messages="errors.collect('icon')"
                  data-vv-name="icon"
                  required
                  class="mx-1"
                ></v-text-field>
              </v-flex>
            </v-layout>
            <v-layout row wrap align-center>
              <v-flex xs12 sm6>
                <v-text-field
                  v-model.trim="type"
                  prepend-inner-icon="class"
                  color="deep-purple"
                  :label="$t('admin.type')"
                  type="name"
                  v-validate="'required|max:20|min:2'"
                  :error-messages="errors.collect('type')"
                  data-vv-name="type"
                  required
                  class="mx-1"
                ></v-text-field>
              </v-flex>
              <v-flex xs12 sm6>
                <v-text-field
                  v-model.trim="order"
                  prepend-inner-icon="sort"
                  color="deep-purple"
                  :label="$t('admin.order')"
                  type="order"
                  data-vv-name="order"
                  class="mx-1"
                ></v-text-field>
              </v-flex>
            </v-layout>
            <v-layout row wrap align-center>
              <v-flex xs12 sm6>
                <v-checkbox
                  class="mx-1"
                  v-model="status"
                  :label="$t('button.ENABLE')"
                  value="1"
                  data-vv-name="status"
                ></v-checkbox>
              </v-flex>
            </v-layout>
          </v-form>
        </v-card-text>
        <!-- <v-divider></v-divider> -->
        <v-card-actions class="pb-3">
          <v-spacer></v-spacer>
          <v-btn color="primary" @click="dialog = false" dark>
            <span class="font-weight-bold">{{$t("button.CANCEL") }}</span>
          </v-btn>
          <v-btn color="primary" @click="handlePosition" dark>
            <span class="font-weight-bold">{{$t("button.CONFIRM") }}</span>
          </v-btn>
        </v-card-actions>
        <div class="loading-overlay" v-if="isButtonLoading">
          <v-progress-circular :size="50" color="primary" indeterminate></v-progress-circular>
          <span>{{loadingMessage}}</span>
        </div>
        <div class="loading-overlay" v-if="message">
          <span :class="[isActive ? 'activeClass' : 'errorClass']">{{message}}</span>
        </div>
      </v-card>
    </v-flex>
  </v-dialog>
</template>


<script>
export default {
  data: () => ({
    name: undefined,
    enname: undefined,
    pmenus: [],
    url: "",
    component: "",
    icon: "",
    order: "",
    type: "",
    selected_pmenu: 0,
    isButtonLoading: false,
    message: "",
    loadingMessage: "",
    isActive: false,
    status: 0,
    dialog: false
  }),
  methods: {
    // 等待完成表单输入验证后，然后显示登陆加载动画，这里在需要使用async与await关键字
    async handlePosition() {
      await this.$validator.validateAll();
      // 如果用户输入的所有内容没有错误信息，然后发起后台请求
      if (this.$validator.errors.all().length === 0) {
        this.isButtonLoading = true;
        this.loadingMessage = this.$t("message.LOADING");
        setTimeout(() => {
          this.isButtonLoading = false;
          this.$axios
            .post("/admin/menu/add", {
              name: this.name,
              enname: this.enname,
              fid: this.selected_pmenu,
              url: this.url,
              component: this.component,
              icon: this.icon,
              order: this.order,
              type: this.type,
              status: this.status
            })
            .then(() => {
              this.isActive = true;
              this.message = this.$t("message.SUCCESS_REGISTER");
              setTimeout(() => {
                this.message = "";
                // 跳转上一请求页面或主页
                this.dialog = false;
              }, 1000);
            })
            .catch(() => {
              this.isActive = false;
              this.message = this.$t("message.ERROR_REGISTER");
              setTimeout(() => {
                this.message = "";
              }, 1000);
            });
        }, 1000);
      }
    },
    getMenus() {
      this.$axios
        .get("/api/menu")
        .then(res => {
          // console.log(res.data)
          for (var i = 0; i < res.data.length; i++) {
            this.pmenus.push({
              id: res.data[i].id,
              name: res.data[i].name
            });
          }
        })
        .catch(error => {
          console.log(error);
        });
    },
    clear() {
      this.name = "";
      this.status = 0;
      this.$validator.reset();
    }
  },
  mounted() {
    this.getMenus();
  },
  computed: {}
};
</script>

<style lang="css" scoped>
#register {
  height: 50%;
  width: 100%;
  position: absolute;
  top: 0;
  left: 0;
  content: "";
  z-index: 0;
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