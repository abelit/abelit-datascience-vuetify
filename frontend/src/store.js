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
  accessToken: ''
}
const mutations = {
  increment: state => state.count++,
  decrement: state => state.count--,
  setToken(state, accessToken) {
    state.accessToken = accessToken
    localStorage.accessToken = accessToken
  },
  delToken(state) {
    state.accessToken = ''
    localStorage.removeItem('accessToken')
  }
}
const actions = {}


export default new Vuex.Store({
  state,
  mutations,
  actions
});