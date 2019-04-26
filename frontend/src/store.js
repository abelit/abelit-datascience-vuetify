import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

const state = {
  count: 0,
  token: localStorage.getItem("token") || "",
  language: localStorage.getItem("language") || "zh_CN",
  skin: localStorage.getItem("skin") || "",
  btncolor: localStorage.getItem("sidebar_btncolor") || "",
  color: localStorage.getItem("sidebar_color") || "",
  tbcolor: localStorage.getItem("toobar_color") || "grey darken-3",
  image:
    localStorage.getItem("sidebar_image") ||
    "https://demos.creative-tim.com/vue-material-dashboard/img/sidebar-2.32103624.jpg",
  drawer: false,
  mini: false,
  isSmallScreen: false
};
const mutations = {
  increment: state => state.count++,
  decrement: state => state.count--,

  SET_TOKEN(state, token) {
    state.token = token;
    // localStorage.token = JSON.stringify(token)
    localStorage.setItem("token", JSON.stringify(token));
  },
  DEL_TOKEN(state) {
    state.token = "";
    localStorage.removeItem("token");
  },
  // 中英文切换
  SET_LANGUAGE: (state, language) => {
    state.language = language;
    localStorage.setItem("language", language);
  },
  SET_SKIN: (state, skin) => {
    state.skin = skin;
    localStorage.setItem("skin", JSON.stringify(skin));
  },
  SET_SIDEBAR_BUTTON_COLOR: (state, btncolor) => {
    state.btncolor = btncolor;
    localStorage.setItem("sidebar_btncolor", btncolor);
  },
  SET_SIDEBAR_IMAGE: (state, image) => {
    state.image = image;
    localStorage.setItem("sidebar_image", image);
  },
  SET_SIDEBAR_COLOR: (state, color) => {
    state.color = color;
    localStorage.setItem("sidebar_color", color);
  },

  SET_TOOLBAR_COLOR: (state, tbcolor) => {
    state.tbcolor = tbcolor;
    localStorage.setItem("toolbar_color", tbcolor);
  },
  SET_MINI: (state, mini) => {
    state.mini = mini;
  },
  SET_DRAWER: (state, drawer) => {
    state.drawer = drawer;
  },
  SET_SMALLSCREEN: (state, isSmallScreen) => {
    state.isSmallScreen = isSmallScreen;
  }
};
const actions = {
  aincrement(ctx) {
    ctx.commit("increment");
  },
  // 使用ES2015语法简化代码
  adecrement({ commit }) {
    commit("decrement");
  },

  setLanguage({ commit }, language) {
    commit("SET_LANGUAGE", language);
  },
  setToken({ commit }, token) {
    commit("SET_TOKEN", token);
  },
  delToken({ commit }) {
    commit("DEL_TOKEN");
  },
  setSkin({ commit }, skin) {
    commit("SET_SKIN", skin);
  },
  setSidebarButtonColor({ commit }, btncolor) {
    commit("SET_SIDEBAR_BUTTON_COLOR", btncolor);
  },
  setSidebarImage({ commit }, image) {
    commit("SET_SIDEBAR_IMAGE", image);
  },
  setSidebarColor({ commit }, color) {
    commit("SET_SIDEBAR_COLOR", color);
  },
  setToolbarColor({ commit }, tbcolor) {
    commit("SET_TOOLBAR_COLOR", tbcolor);
  },
  setMini({ commit }, mini) {
    commit("SET_MINI", mini);
  },
  setDrawer({ commit }, drawer) {
    commit("SET_DRAWER", drawer);
  },
  setSmallScreen({ commit }, isSmallScreen) {
    commit("SET_SMALLSCREEN", isSmallScreen);
  }
};

const getters = {
  skin: state => {
    return state.skin;
  }
};

export default new Vuex.Store({
  state,
  mutations,
  actions,
  getters
});
