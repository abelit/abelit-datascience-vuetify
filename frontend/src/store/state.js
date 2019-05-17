const state = {
  count: 0,
  token: localStorage.getItem("token") || "",
  language: localStorage.getItem("language") || "zh_CN",
  themeColor: localStorage.getItem("theme_color") || "cyan",
  sidebarTheme: localStorage.getItem("sidebar_theme") || "light",
  buttonColor: localStorage.getItem("button_color") || "",
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
