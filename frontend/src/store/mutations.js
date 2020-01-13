const mutations = {
  setLanguage: (state, value) => {
    state.language = value;
    localStorage.setItem("language", value);
  },
  setLockPassword: (state, value) => {
    state.lockPassword = value;
    localStorage.setItem("lockPassword", value);
  },
  logout: state => {
   state.token = "";
   localStorage.removeItem("token");
  },
  setFullscreen: (state, value) => {
    state.isFullscreen =  value;
  },
  setTag: (state, value) => {
    state.isTag = value;
    localStorage.setItem("isTag", value);
  },
  setDark: (state, value) => {
    state.isDark = value;
    localStorage.setItem("isDark", value);
  }
};

export default mutations;
