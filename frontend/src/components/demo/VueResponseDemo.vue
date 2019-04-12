<template>
  <div>
    <div>{{ message }}</div>
    <button @click="updateMessage">Update Message</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: "hey!"
    };
  },
  methods: {
    updateMessage: async function() {
      this.message = "hi!";
      console.log(this.$el.textContent); // => '未更新'
      await this.$nextTick();
      console.log(this.$el.textContent); // => '已更新'
    }
  }
};
</script>