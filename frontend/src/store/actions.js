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
    },
    setToken({ commit }, token) {
        commit("SET_TOKEN", token);
    },
    delToken({ commit }) {
        commit("DEL_TOKEN");
    },
    setSkin({ commit }, skin) {
        commit("SET_SKIN", skin);
    },
    setSidebarButtonColor({ commit }, buttonColor) {
        commit("SET_SIDEBAR_BUTTON_COLOR", buttonColor);
    },
    setSidebarImage({ commit }, image) {
        commit("SET_SIDEBAR_IMAGE", image);
    },
    setSidebarColor({ commit }, color) {
        commit("SET_SIDEBAR_COLOR", color);
    },
    setToolbarColor({ commit }, toolbarColor) {
        commit("SET_TOOLBAR_COLOR", toolbarColor);
    },
    setMini({ commit }, mini) {
        commit("SET_MINI", mini);
    },
    setDrawer({ commit }, drawer) {
        commit("SET_DRAWER", drawer);
    },
    setSmallScreen({ commit }, isSmallScreen) {
        commit("SET_SMALLSCREEN", isSmallScreen);
    },
    setWindowSize({ commit }, windowSize) {
        commit("SET_WINDOWSIZE", windowSize);
    },
    setFullScreen({ commit }, isFullScreen) {
        commit("SET_FULLSCREEN", isFullScreen);
    },
    setLockPassword({ commit }, lockPassword) {
        commit("SET_LOCK_PASSWORD", lockPassword);
    },
    setLock({ commit }, isLock) {
        commit("SET_LOCK", isLock);
    },
    clearLock({ commit }) {
        commit("CLEAR_LOCK");
    },
    logOut({ commit }) {
        commit("LOG_OUT");
    }
};

export default actions;