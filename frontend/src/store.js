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
  token: ''
}
const mutations = {
  increment: state => state.count++,
  decrement: state => state.count--,
  set_token(state, token) {
    state.token = token
    localStorage.token = token
  },
  del_token(state) {
    state.token = ''
    localStorage.removeItem('token')
  }
}
const actions = {}


export default new Vuex.Store({
  state,
  mutations,
  actions
});