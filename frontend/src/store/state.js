const state = {
    language: localStorage.getItem("language") || "zh_cn",
    lockPassword: localStorage.getItem("lockPassword") || "",
    appLoading: false,
    isFullscreen: false,
    isTag: localStorage.getItem("isTag") || true,
    isDark: localStorage.getItem("isDark") || false
};

export default state;
