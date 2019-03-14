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
    <p v-if="loginUser">UserInfo is: {{loginUser}}</p>
    <button class="btn-primary" @click="getUser">点击此通过token获取用户名</button> ||
    <button class="btn-primary" @click="logout">退出</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      p_name: "hello",
      m_name: "abelit",
      message: "test",
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
      // let token = JSON.parse(localStorage.token).access_token
      let token = JSON.parse(localStorage.getItem('token')).access_token

      this.$axios.get("/protected",{ headers: { Authorization: 'Bearer ' + token} })
      .then(res => {
        // 通过token获取用户名称
        console.log(res.data);
        this.loginUser = res.data.logged_in_as;
      })
      .catch(error => {
        console.log('error abelit');
        console.log(error);
      })
    }
  }
};
</script>

<style media="screen">
</style>
