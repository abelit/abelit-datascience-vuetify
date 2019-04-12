import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

const state = {
  count: 0,
  token: localStorage.getItem("token") || "",
  language: localStorage.getItem("language") || "zh_CN"
};
const mutations = {
  increment: state => state.count++,
  decrement: state => state.count--,

  setToken(state, token) {
    state.token = token;
    // localStorage.token = JSON.stringify(token)
    localStorage.setItem("token", JSON.stringify(token));
  },
  delToken(state) {
    state.token = "";
    localStorage.removeItem("token");
  },
  // 中英文切换
  SET_LANGUAGE: (state, language) => {
    state.language = language;
    localStorage.setItem("language", language);
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
  }
};

// const getters = {}

export default new Vuex.Store({
  state,
  mutations,
  actions
});
