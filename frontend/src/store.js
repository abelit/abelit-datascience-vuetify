import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

// // default store config
// export default new Vuex.Store({
//   state: {},
//   mutations: {},
//   actions: {}
// });

const state = {
  count: 0,
  token: localStorage.getItem("token") || ""
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
  }
};
const actions = {};

// const getters = {}

export default new Vuex.Store({
  state,
  mutations,
  actions
});
