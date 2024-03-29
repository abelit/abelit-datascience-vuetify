module.exports = {
  root: true,
  env: {
    node: true
  },
  extends: ["plugin:vue/essential", "@vue/prettier"],
  rules: {
    "no-console": process.env.NODE_ENV === "production" ? "error" : "off",
    "no-debugger": process.env.NODE_ENV === "production" ? "error" : "off",
    "semi": ["error", "always"],
    "quotes": ["error", "double"]
  },
  parserOptions: {
    parser: "babel-eslint",
    ecmaVersion: 6,
    esversion: 6
  },
};

