const state = {
    count: 0,
    token: localStorage.getItem("token") || "",
    language: localStorage.getItem("language") || "zh_CN",
    skin: localStorage.getItem("skin") || "",
    buttonColor: localStorage.getItem("button_color") || "",
    color: localStorage.getItem("sidebar_color") || "",
    toolbarColor: localStorage.getItem("toolbar_color") || "",
    image: localStorage.getItem("sidebar_image") || "./static/theme/sidebar001",
    drawer: false,
    mini: false,
    isSmallScreen: false,
    windowSize: "",
    isFullScreen: false,
    isLock: localStorage.getItem("is_lock") || false,
    lockPassword: localStorage.getItem("lock_password") || "",
    browserHeaderTitle: "DataAV"
};

export default state;