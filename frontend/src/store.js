import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);
// // default store config
// export default new Vuex.Store({
//   state: {},
//   mutations: {},
//   actions: {}
// });


export default new Vuex.Store({
  state: {
    count: 0
  },
  mutations: {
    increment: state => state.count++,
    decrement: state => state.count--
  },
  action: {}
});

