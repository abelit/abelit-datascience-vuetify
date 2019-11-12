const state = {
    language: localStorage.getItem("language") || "zh_cn",
    lockPassword: localStorage.getItem("lockPassword") || "",
    appLoading: false
};

export default state;
