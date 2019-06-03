const mutations = {
  SET_TOKEN(state, token) {
    state.token = token;
    // localStorage.token = JSON.stringify(token)
    localStorage.setItem("token", JSON.stringify(token));
  },
  DEL_TOKEN(state) {
    state.token = "";
    localStorage.removeItem("token");
  },
  SET_LANGUAGE: (state, language) => {
    state.language = language;
    localStorage.setItem("language", language);
  },
  SET_THEME_COLOR: (state, color) => {
    state.themeColor = color;
    localStorage.setItem("theme_color", color);
  },
  SET_SIDEBAR_THEME: (state, theme) => {
    state.sidebarTheme = theme;
    localStorage.setItem("sidebar_theme", theme);
  },
  SET_BUTTON_COLOR: (state, color) => {
    state.buttonColor = color;
    localStorage.setItem("button_color", color);
  },
  SET_TOOLBAR_COLOR: (state, color) => {
    state.toolbarColor = color;
    localStorage.setItem("toolbar_color", color);
  },
  SET_MINI: (state, mini) => {
    state.mini = mini;
  },
  SET_DRAWER: (state, drawer) => {
    state.drawer = drawer;
  },
  SET_SMALLSCREEN: (state, payload) => {
    state.isSmallScreen = payload;
  },
  SET_WINDOWSIZE: (state, size) => {
    state.windowSize = size;
  },
  SET_FULLSCREEN: (state, payload) => {
    state.isFullScreen = payload;
  },
  SET_PAGEFULLSCREEN: (state, payload) => {
    state.isPageFullScreen = payload;
  },
  SET_LOCK_PASSWORD: (state, password) => {
    state.lockPassword = password;
    localStorage.setItem("lock_password", password);
  },
  SET_LOCK: (state, payload) => {
    state.isLock = payload;
    localStorage.setItem("is_lock", payload);
  },
  CLEAR_LOCK: state => {
    state.isLock = false;
    state.lockPassword = "";
    localStorage.removeItem("is_lock");
    localStorage.removeItem("lock_password");
  },
  SET_BROWSERHEADERTITLE: (state, title) => {
    state.browserHeaderTitle = title;
  },
  LOG_OUT: state => {
    state.token = "";
    state.lockPassword = "";
    state.isLock = false;
    localStorage.removeItem("token");
    localStorage.removeItem("lock_password");
    localStorage.removeItem("is_lock");
  }
};

export default mutations;
