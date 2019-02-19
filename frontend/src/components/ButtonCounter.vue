<template>
  <button v-on:click="mcount++">You clicked me {{ mcount }} times.</button>
</template>

<script>
export default {
  name: "ButtonCounter",
  data() {
    return {
      mcount: 0
    };
  }
};
</script>