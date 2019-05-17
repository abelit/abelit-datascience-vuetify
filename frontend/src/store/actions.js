const actions = {
  setLanguage({ commit }, language) {
    commit("SET_LANGUAGE", language);
  },
  setToken({ commit }, token) {
    commit("SET_TOKEN", token);
  },
  delToken({ commit }) {
    commit("DEL_TOKEN");
  },
  setThemeColor({ commit }, color) {
    commit("SET_THEME_COLOR", color);
  },
  setSidebarTheme({ commit }, color) {
    commit("SET_SIDEBAR_THEME", color);
  },
  setButtonColor({ commit }, color) {
    commit("SET_BUTTON_COLOR", color);
  },
  setSidebarColor({ commit }, color) {
    commit("SET_SIDEBAR_COLOR", color);
  },
  setToolbarColor({ commit }, color) {
    commit("SET_TOOLBAR_COLOR", color);
  },
  setMini({ commit }, mini) {
    commit("SET_MINI", mini);
  },
  setDrawer({ commit }, drawer) {
    commit("SET_DRAWER", drawer);
  },
  setSmallScreen({ commit }, payload) {
    commit("SET_SMALLSCREEN", payload);
  },
  setWindowSize({ commit }, size) {
    commit("SET_WINDOWSIZE", size);
  },
  setFullScreen({ commit }, payload) {
    commit("SET_FULLSCREEN", payload);
  },
  setLockPassword({ commit }, password) {
    commit("SET_LOCK_PASSWORD", password);
  },
  setLock({ commit }, payload) {
    commit("SET_LOCK", payload);
  },
  clearLock({ commit }) {
    commit("CLEAR_LOCK");
  },
  logOut({ commit }) {
    commit("LOG_OUT");
  }
};

export default actions;
