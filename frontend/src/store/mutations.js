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
  SET_SIDEBAR_BUTTON_COLOR: (state, buttonColor) => {
    state.buttonColor = buttonColor;
    localStorage.setItem("sidebar_buttonColor", buttonColor);
  },
  SET_SIDEBAR_IMAGE: (state, image) => {
    state.image = image;
    localStorage.setItem("sidebar_image", image);
  },
  SET_SIDEBAR_COLOR: (state, color) => {
    state.color = color;
    localStorage.setItem("sidebar_color", color);
  },

  SET_TOOLBAR_COLOR: (state, toolbarColor) => {
    state.toolbarColor = toolbarColor;
    localStorage.setItem("toolbar_color", toolbarColor);
  },
  SET_MINI: (state, mini) => {
    state.mini = mini;
  },
  SET_DRAWER: (state, drawer) => {
    state.drawer = drawer;
  },
  SET_SMALLSCREEN: (state, isSmallScreen) => {
    state.isSmallScreen = isSmallScreen;
  },
  SET_WINDOWSIZE: (state, windowSize) => {
    state.windowSize = windowSize;
  },
  SET_FULLSCREEN: (state, isFullScreen) => {
    state.isFullScreen = isFullScreen;
  },
  SET_LOCK_PASSWORD: (state, lockPassword) => {
    state.lockPassword = lockPassword;
    localStorage.setItem("lock_password", lockPassword);
  },
  SET_LOCK: (state, isLock) => {
    state.isLock = isLock;
    localStorage.setItem("is_lock", isLock);
  },
  CLEAR_LOCK: state => {
    state.isLock = false;
    state.lockPassword = "";
    localStorage.removeItem("is_lock");
    localStorage.removeItem("lock_password");
  },
  SET_BROWSERHEADERTITLE: (state, browserHeaderTitle) => {
    state.browserHeaderTitle = browserHeaderTitle;
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