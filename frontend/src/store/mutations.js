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
  }
};

export default mutations;
