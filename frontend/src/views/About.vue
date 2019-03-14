<template>
  <div class="about">
    <h1>This is an about page</h1>
    <input
      v-model="message"
      placeholder="edit me"
      :class="bcss"
      v-validate="'required'"
      name="myinput"
    >
    <span>{{ errors.first('myinput') }}</span>
    <p>Message is: {{ message }}</p>
    <button class="btn-primary" @click="logout">退出</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      p_name: "hello",
      m_name: "abelit",
      message: "",
      bcss: "form-control",
      mypath: process.env.BASE_URL,
      loginUser: ''
    };
  },
  methods: {
    logout() {
      this.$store.commit("delToken");
      this.$router.push("/user/login");
    },
    getUser() {
      this.$axios.get("/protected")
      .then
    }
  }
};
</script>

<style media="screen">
</style>
