const state = {
    language: localStorage.getItem("language") || "zh_cn",
    lockPassword: localStorage.getItem("lockPassword") || "",
};

export default state;
