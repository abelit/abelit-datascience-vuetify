const state = {
    language: localStorage.getItem("language") || "zh_cn",
    lockPassword: localStorage.getItem("lockPassword") || "",
    appLoading: false,
    isFullscreen: false
};

export default state;
