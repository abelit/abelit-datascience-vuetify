<template>
  <div class="test">
    <h1> {{ msg }} </h1>
    <ol>
      <li>
      <router-link to="/books"><a>All Books</a></router-link>
    </li>
    <li>
    <router-link to="/ping"><a>Ping</a></router-link>
  </li>
    </ol>
  </div>
</template>

<script>

export default {
  name: 'TestVue',
  data () {
    return {
      msg: 'Hi ChenYing! Welcome to Your Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
