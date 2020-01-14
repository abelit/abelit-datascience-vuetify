const actions = {
  setLanguage({ commit }, value) {
    commit("setLanguage", value);
  },
  setLockPassword({ commit }, value) {
    commit("setLockPassword", value);
  },
  logout({commit}) {
    commit("logout");
  },
  setFullscreen({commit}) {
    commit("setFullscreen");
  },
  setTag({ commit }, value) {
    commit("setTag", value);
  },
  setDark({ commit }, value) {
    commit("setDark", value);
  },
  setFooter({ commit }, value) {
    commit("setFooter", value);
  }
};

export default actions;
