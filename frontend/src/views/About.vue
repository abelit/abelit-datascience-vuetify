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
    <p>{{mypath}}</p>
    <img :src="mypath+'static/cn.png'" alt>
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
      mypath: process.env.BASE_URL
    };
  },
  methods: {
    logout() {
      this.$store.commit("del_token");
      this.$router.push("/user/login");
    }
  }
};
</script>

<style media="screen">
</style>
