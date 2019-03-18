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
    <p>Old Token: {{oldtoken}}</p>
    <button class="btn-primary" @click="getUser">点击此通过token获取用户名</button> ||
    <button class="btn-primary" @click="logout">退出</button>
    <div>
      <h1>用户可访问的菜单</h1>
      <!-- <ul>
        <li v-for="(k,v) in menulst">
          <router-link :to="k">{{v}}</router-link>
        </li>
      </ul> -->
      <!-- {{getMenu()}} -->
    </div>
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
      loginUser: '',
      oldtoken: JSON.parse(localStorage.getItem('token')).access_token || '',
      menulst: {}
    };
  },
  methods: {
    logout() {
      this.$store.commit("delToken");
      this.$router.push("/user/login");
    },
    getUser() {
      // let token = JSON.parse(localStorage.token).access_token
      let token = JSON.parse(localStorage.getItem('token')).access_token;
      
      this.$axios.get("/protected",{ headers: { Authorization: 'Bearer ' + token} })
      .then(res => {
        // 通过token获取用户名称
        console.log('nnnnnnnnnnnnnnnnnnnn');
        console.log(res);
        this.loginUser = res.data.logged_in_as;
        this.oldtoken =  token;
      })
      .catch(error => {
        console.log(error);
      });

      // this.$axios.post("/refresh",{},{ headers: { Authorization: 'Bearer ' + rtoken} })
      // .then(res => {
      //   console.log('mmmmmmmmmmmmmmmmm');
      //   console.log(res);
      //   this.newtoken = res.data.access_token;
      //   this.$store.commit("setToken", {access_token: res.data.access_token,refresh_token:rtoken});
      // })
      // .catch(error => {
      //   console.log(error);
      // });

      // console.log('chenying');
      // console.log(localStorage.getItem('token'));
    },
    getMenu() {
      let token = JSON.parse(localStorage.getItem('token')).access_token;
      this.$axios.get("/menu",{headers: {Authorization: 'Bearer ' + token}})
      .then(res => {
        console.log(res.data);
      })
      .catch(error => {
        console.log(error);
      });
    }
  }
};
</script>

<style media="screen">
</style>
