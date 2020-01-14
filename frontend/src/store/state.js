const state = {
    language: localStorage.getItem("language") || "zh_cn",
    lockPassword: localStorage.getItem("lockPassword") || "",
    appLoading: false,
    isFullscreen: false,
    isTag: localStorage.getItem("isTag") || true,
    isDark: localStorage.getItem("isDark") || false,
    isFooter: localStorage.getItem("isFooter") || true,
};

export default state;
