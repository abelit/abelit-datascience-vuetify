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
  count: 0
}
const mutations = {
  increment: state => state.count++,
  decrement: state => state.count--
}
const actions = {}


export default new Vuex.Store({
  state,
  mutations,
  actions
});